"""Tests for scripts/match.py against the small fixture. No network."""

from __future__ import annotations

import io
import json
from datetime import date
from pathlib import Path

import pytest

import match

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "programs_small.json"
PROGRAMS = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))["programs"]
BY_ID = {program["id"]: program for program in PROGRAMS}
SE_GRANT = BY_ID["test-se-grant"]
EU_COMPUTE = BY_ID["test-eu-compute"]
CREDIT = BY_ID["test-global-credit"]
REVENUE_GROUP = SE_GRANT["eligibility"][3]
AGE_RULE = {"field": "age_years", "op": "lte", "value": 10, "label": "at most 10 years", "question": "How old is the company?"}
TODAY = date(2026, 10, 15)


def run(profile: dict, **kwargs: object) -> dict:
    return match.run(profile, PROGRAMS, TODAY, **kwargs)


def doors(profile: dict, **kwargs: object) -> dict[str, dict]:
    return {door["id"]: door for door in run(profile, **kwargs)["doors"]}


# --- single rules ---------------------------------------------------------


def test_absent_field_is_unknown() -> None:
    result = match.evaluate_rule(AGE_RULE, {})
    assert result.status == "unknown"
    assert result.label == "at most 10 years"
    assert result.question == "How old is the company?"


def test_lte_failure_blocks() -> None:
    assert match.evaluate_rule(AGE_RULE, {"age_years": 12}).status == "failed"
    assert match.evaluate_rule(AGE_RULE, {"age_years": 10}).status == "met"


def test_eq_false_matches_false_only() -> None:
    rule = SE_GRANT["eligibility"][4]
    assert match.evaluate_rule(rule, {"profit_distributed": False}).status == "met"
    assert match.evaluate_rule(rule, {"profit_distributed": True}).status == "failed"


def test_contains_on_list_field() -> None:
    rule = CREDIT["eligibility"][0]
    assert match.evaluate_rule(rule, {"stack": ["anthropic", "aws"]}).status == "met"
    assert match.evaluate_rule(rule, {"stack": ["aws"]}).status == "failed"


def test_in_and_not_in_ops() -> None:
    rule = {"field": "stage", "op": "in", "value": ["idea", "pre_seed"], "label": "early", "question": "Stage?"}
    assert match.evaluate_rule(rule, {"stage": "idea"}).status == "met"
    assert match.evaluate_rule(rule, {"stage": "seed"}).status == "failed"
    rule_not = dict(rule, op="not_in")
    assert match.evaluate_rule(rule_not, {"stage": "seed"}).status == "met"


# --- any groups -----------------------------------------------------------


def test_any_group_met_when_one_member_met() -> None:
    assert match.evaluate_rule(REVENUE_GROUP, {"revenue_msek": 50, "balance_msek": 2}).status == "met"


def test_any_group_failed_only_when_all_known_and_failed() -> None:
    assert match.evaluate_rule(REVENUE_GROUP, {"revenue_msek": 50, "balance_msek": 20}).status == "failed"


def test_any_group_unknown_when_one_member_unknown() -> None:
    result = match.evaluate_rule(REVENUE_GROUP, {"revenue_msek": 50})
    assert result.status == "unknown"
    assert result.label == "revenue or balance sheet at most 10 MSEK"
    assert result.question == "Balance sheet total, in MSEK?"


# --- profile normalization --------------------------------------------------


def test_stack_aliases_normalized() -> None:
    profile, warnings = match.normalize_profile({"stack": ["Anthropic", "AWS", "claude"]})
    assert profile["stack"] == ["anthropic", "aws"]
    assert warnings == []


def test_need_alias_and_single_string() -> None:
    profile, _ = match.normalize_profile({"need": "gpu"})
    assert profile["need"] == ["compute"]
    profile, _ = match.normalize_profile({"need": ["money", "GPU", "credits"]})
    assert profile["need"] == ["money", "compute", "credits"]


def test_legal_form_and_country_aliases() -> None:
    profile, _ = match.normalize_profile({"legal_form": "AB", "country": "se"})
    assert profile["legal_form"] == "company"
    assert profile["country"] == "SE"


def test_numeric_string_is_coerced() -> None:
    profile, warnings = match.normalize_profile({"revenue_msek": "5", "employees": "4", "balance_meur": "12,5"})
    assert profile["revenue_msek"] == 5.0
    assert profile["employees"] == 4
    assert profile["balance_meur"] == 12.5
    assert warnings == []


def test_non_numeric_string_is_unknown_with_warning() -> None:
    out = run({"country": "SE", "legal_form": "company", "revenue_msek": "about five", "need": ["money"]})
    door = {d["id"]: d for d in out["doors"]}["test-se-grant"]
    assert "revenue or balance sheet at most 10 MSEK" in [u["label"] for u in door["unknown"]]
    assert any("revenue_msek" in warning for warning in out["warnings"])


def test_boolean_strings_are_coerced() -> None:
    profile, warnings = match.normalize_profile({"has_vat": "yes", "has_website": "nej", "has_developer": "maybe"})
    assert profile["has_vat"] is True
    assert profile["has_website"] is False
    assert "has_developer" not in profile
    assert any("has_developer" in warning for warning in warnings)


# --- relevance --------------------------------------------------------------


def test_eu_program_relevant_for_norway() -> None:
    assert match.is_relevant(EU_COMPUTE, {"country": "NO"})


def test_eu_program_not_relevant_for_us() -> None:
    assert not match.is_relevant(EU_COMPUTE, {"country": "US"})


def test_national_program_only_at_home_or_when_country_unknown() -> None:
    assert match.is_relevant(SE_GRANT, {"country": "SE"})
    assert not match.is_relevant(SE_GRANT, {"country": "FI"})
    assert match.is_relevant(SE_GRANT, {})


def test_global_program_relevant_everywhere() -> None:
    assert match.is_relevant(CREDIT, {"country": "US"})


def test_need_filter_excludes_money_when_only_compute_asked() -> None:
    result = doors({"country": "SE", "legal_form": "company", "need": ["compute"]})
    assert "test-eu-compute" in result
    assert "test-se-grant" not in result


# --- doors ------------------------------------------------------------------


def test_no_country_is_unknown_not_sweden() -> None:
    door = doors({"legal_form": "company", "need": ["money"]})["test-se-grant"]
    assert door["status"] == "unknown"
    assert door["unknown"][0]["label"] == "Swedish company"
    assert "Sweden" in door["unknown"][0]["question"]


def test_blocked_hidden_without_all_flag() -> None:
    profile = {"country": "SE", "legal_form": "company", "age_years": 12, "need": ["money"]}
    assert "test-se-grant" not in doors(profile)
    blocked = doors(profile, include_all=True)["test-se-grant"]
    assert blocked["status"] == "blocked"
    assert "at most 10 years" in blocked["failed"]


def test_stale_after_90_days() -> None:
    out = run({"country": "SE", "legal_form": "company", "need": ["credits"], "stack": ["anthropic"]})
    assert out["doors"][0]["id"] == "test-global-credit"
    assert out["doors"][0]["stale"] is True
    assert out["stale"] == ["test-global-credit"]


def test_fresh_record_not_stale() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["compute"]})["test-eu-compute"]
    assert door["stale"] is False


def test_glyph_exact_string() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["compute"]})["test-eu-compute"]
    assert door["glyph"] == "\n".join(
        [
            "◐  Test EU compute",
            "●  company",
            "○  employment",
            "○  VAT number",
            "○  work email",
            "○  workload",
            "?  Is the project lead employed until at least three months after the allocation ends?",
            "→  Up to 5 000 GPU hours, 1 to 3 months, one system",
        ]
    )


def test_glyph_eligible_and_blocked_heads() -> None:
    full = {"country": "SE", "legal_form": "company", "age_years": 2, "revenue_msek": 1, "profit_distributed": False, "need": ["money"]}
    eligible = doors(full)["test-se-grant"]
    assert eligible["status"] == "eligible"
    assert eligible["glyph"].startswith("●  Test SE grant")
    assert not any(line.startswith("?") for line in eligible["glyph"].split("\n"))
    blocked = doors(dict(full, age_years=12), include_all=True)["test-se-grant"]
    assert blocked["glyph"].startswith("×  Test SE grant")
    assert "×  at most 10 years" in blocked["glyph"]


def test_stale_glyph_points_at_the_page() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["credits"], "stack": ["anthropic"]})["test-global-credit"]
    assert "→  Last verified 2026-07-01, read the status page before quoting" in door["glyph"]


def test_rank_eligible_then_unknown_then_blocked() -> None:
    profile = {
        "country": "SE", "legal_form": "company", "age_years": 2, "revenue_msek": 1, "profit_distributed": False,
        "stack": ["aws"], "has_employment": True, "has_vat": True,
    }
    out = run(profile, include_all=True)
    assert [door["id"] for door in out["doors"]] == ["test-se-grant", "test-eu-compute", "test-global-credit"]


def test_rank_fewer_unknowns_first() -> None:
    out = run({"country": "SE", "legal_form": "company", "stack": ["anthropic"]})
    assert [door["id"] for door in out["doors"]] == ["test-global-credit", "test-se-grant", "test-eu-compute"]


# --- live -------------------------------------------------------------------


def test_live_attaches_round() -> None:
    def fake_live(call_id: str) -> dict:
        assert call_id == "2016-04714"
        return {"dnr": "2025-04831", "title": "Innovativa Startups 2026", "closes": "2027-01-12T14:00:00+00:00", "open_now": True, "apply_url": "https://ansok.vinnova.se/x"}

    door = doors({"country": "SE", "legal_form": "company", "need": ["money"]}, live_fetch=fake_live)["test-se-grant"]
    assert door["live"]["dnr"] == "2025-04831"
    assert "→  Round closes 2027-01-12 14:00" in door["glyph"]


def test_live_error_is_reported_not_raised() -> None:
    def broken(call_id: str) -> dict:
        raise OSError("network down")

    door = doors({"country": "SE", "legal_form": "company", "need": ["money"]}, live_fetch=broken)["test-se-grant"]
    assert door["live"] == {"error": "network down"}


def test_live_not_called_without_flag() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["money"]})["test-se-grant"]
    assert door["live"] is None


# --- CLI --------------------------------------------------------------------


def test_cli_round_trip(capsys: pytest.CaptureFixture[str]) -> None:
    stdin = io.StringIO(json.dumps({"country": "SE", "legal_form": "company", "need": ["compute"]}))
    code = match.main(["--programs", str(FIXTURE_PATH), "--today", "2026-10-15"], stdin=stdin)
    assert code == 0
    out = json.loads(capsys.readouterr().out)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute"]
    assert out["profile"]["country"] == "SE"


def test_cli_rejects_non_object_profile(capsys: pytest.CaptureFixture[str]) -> None:
    code = match.main(["--programs", str(FIXTURE_PATH)], stdin=io.StringIO("[1, 2]"))
    assert code == 2
