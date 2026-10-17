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
AGE_RULE = {"field": "age_years", "op": "lte", "value": 10}
TODAY = date(2026, 10, 15)


def run(profile: dict, **kwargs: object) -> dict:
    return match.run(profile, PROGRAMS, TODAY, **kwargs)


def doors(profile: dict, **kwargs: object) -> dict[str, dict]:
    return {door["id"]: door for door in run(profile, **kwargs)["doors"]}


# --- single rules ---------------------------------------------------------


def test_absent_field_is_unknown() -> None:
    result = match.evaluate_rule(AGE_RULE, {})
    assert result.status == "unknown"
    assert result.label == "at most 10 years old"
    assert result.question == "How old is the company, in years?"


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
    rule = {"field": "stage", "op": "in", "value": ["idea", "pre_seed"]}
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
    assert result.label == "revenue at most 10 MSEK, or balance sheet at most 10 MSEK"
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
    assert "revenue at most 10 MSEK, or balance sheet at most 10 MSEK" in [u["label"] for u in door["unknown"]]
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
    assert door["unknown"][0]["label"] == "in Sweden"
    assert "country" in door["unknown"][0]["question"].lower()


def test_blocked_hidden_without_all_flag() -> None:
    profile = {"country": "SE", "legal_form": "company", "age_years": 12, "need": ["money"]}
    assert "test-se-grant" not in doors(profile)
    blocked = doors(profile, include_all=True)["test-se-grant"]
    assert blocked["status"] == "blocked"
    assert "at most 10 years old" in blocked["failed"]


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
            "●  a company",
            "○  project lead employed past the allocation",
            "○  VAT number",
            "○  email on your own domain",
            "○  workload defined: code, one system, GPU hours",
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
    assert "×  at most 10 years old" in blocked["glyph"]


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


# --- availability -----------------------------------------------------------


def test_closed_door_ranks_last_even_when_eligible() -> None:
    closed = dict(CREDIT, availability="closed")
    out = match.run({"country": "SE", "legal_form": "company", "stack": ["anthropic"]}, [closed, EU_COMPUTE], TODAY)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute"]
    assert [door["id"] for door in out["more"]] == ["test-global-credit"]
    every = match.run({"country": "SE", "legal_form": "company", "stack": ["anthropic"]}, [closed, EU_COMPUTE], TODAY, top=0)
    assert [door["id"] for door in every["doors"]] == ["test-eu-compute", "test-global-credit"]
    assert every["doors"][1]["availability"] == "closed"


def test_closed_glyph_names_the_date_and_points_at_the_page() -> None:
    closed = dict(CREDIT, availability="closed")
    out = match.run({"country": "SE", "legal_form": "company", "stack": ["anthropic"], "funding_raised_usd": 0}, [closed], TODAY, top=0)
    glyph = out["doors"][0]["glyph"]
    assert glyph.startswith("●  Test global credit")
    assert "→  Closed when verified 2026-07-01; read the status page for the next round" in glyph


def test_availability_defaults_to_unknown() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["compute"]})["test-eu-compute"]
    assert door["availability"] == "unknown"
    assert "Closed when verified" not in door["glyph"]


# --- review fix pass --------------------------------------------------------


def test_eu_door_without_country_asks_for_country_first() -> None:
    profile = {"legal_form": "company", "has_employment": True, "has_vat": True, "has_work_email": True, "workload_defined": True}
    door = doors(profile)["test-eu-compute"]
    assert door["status"] == "unknown"
    assert door["unknown"][0]["label"] == "in the EU or an associated country"
    assert "country" in door["unknown"][0]["question"].lower()


def test_global_door_without_country_is_not_asked_for_country() -> None:
    door = doors({"legal_form": "company", "stack": ["anthropic"], "funding_raised_usd": 0})["test-global-credit"]
    assert door["status"] == "eligible"


def test_country_name_is_mapped_or_dropped_with_warning() -> None:
    assert match.normalize_profile({"country": "Sweden"})[0]["country"] == "SE"
    assert match.normalize_profile({"country": "norge"})[0]["country"] == "NO"
    profile, warnings = match.normalize_profile({"country": "Atlantis"})
    assert "country" not in profile
    assert any("country" in warning for warning in warnings)


def test_stage_variants_normalized_or_warned() -> None:
    assert match.normalize_profile({"stage": "Series A"})[0]["stage"] == "series_a"
    assert match.normalize_profile({"stage": "pre-seed"})[0]["stage"] == "pre_seed"
    assert match.normalize_profile({"stage": "Series B"})[0]["stage"] == "later"
    profile, warnings = match.normalize_profile({"stage": "unicorn"})
    assert "stage" not in profile
    assert any("stage" in warning for warning in warnings)


def test_legal_form_with_parenthetical_abbreviation_or_warned() -> None:
    assert match.normalize_profile({"legal_form": "Aktiebolag (AB)"})[0]["legal_form"] == "company"
    assert match.normalize_profile({"legal_form": "ideell förening"})[0]["legal_form"] == "nonprofit"
    profile, warnings = match.normalize_profile({"legal_form": "kommanditbolag"})
    assert "legal_form" not in profile
    assert any("legal_form" in warning for warning in warnings)


def test_unknown_need_words_dropped_with_warning() -> None:
    profile, warnings = match.normalize_profile({"need": ["funding", "cloud credits", "foo"]})
    assert profile["need"] == ["money", "credits"]
    assert any("foo" in warning for warning in warnings)


def test_comma_separated_stack_string_is_split_and_aliased() -> None:
    assert match.normalize_profile({"stack": "aws, Anthropic, Google Cloud"})[0]["stack"] == ["aws", "anthropic", "gcp"]


def test_none_inside_list_is_skipped() -> None:
    assert match.normalize_profile({"stack": [None, "aws"]})[0]["stack"] == ["aws"]


def test_sector_aliases_normalized() -> None:
    assert match.normalize_profile({"sector": ["Deep Tech", "climate tech"]})[0]["sector"] == ["deeptech", "climate"]


def test_integer_booleans_coerced() -> None:
    profile, warnings = match.normalize_profile({"has_vat": 1, "has_website": 0})
    assert profile["has_vat"] is True
    assert profile["has_website"] is False
    assert warnings == []


# --- deferred minors from the 2026-10-15 review ----------------------------


def test_non_finite_number_is_unknown_with_warning() -> None:
    assert match.to_number("nan") is None
    assert match.to_number("inf") is None
    assert match.to_number("-Infinity") is None
    assert match.to_number(float("nan")) is None
    assert match.to_number("1e999") is None
    profile, warnings = match.normalize_profile({"revenue_msek": "nan", "employees": "inf"})
    assert "revenue_msek" not in profile
    assert "employees" not in profile
    assert any("revenue_msek" in warning for warning in warnings)
    assert any("employees" in warning for warning in warnings)


def test_cli_missing_programs_file_exits_two_with_one_line(capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    missing = tmp_path / "nowhere.json"
    code = match.main(["--programs", str(missing)], stdin=io.StringIO("{}"))
    assert code == 2
    err = capsys.readouterr().err
    assert "nowhere.json" in err
    assert "Traceback" not in err
    assert len(err.strip().splitlines()) == 1


def test_cli_programs_file_not_json_exits_two_with_one_line(capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    broken = tmp_path / "broken.json"
    broken.write_text("{not json", encoding="utf-8")
    code = match.main(["--programs", str(broken)], stdin=io.StringIO("{}"))
    assert code == 2
    err = capsys.readouterr().err
    assert "broken.json" in err
    assert len(err.strip().splitlines()) == 1


def test_cli_malformed_record_exits_two_naming_the_record(capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"programs": [{"id": "half-a-record", "name": "Half"}]}), encoding="utf-8")
    code = match.main(["--programs", str(bad)], stdin=io.StringIO('{"country": "SE"}'))
    assert code == 2
    err = capsys.readouterr().err
    assert "half-a-record" in err
    assert "Traceback" not in err
    assert len(err.strip().splitlines()) == 1


def test_cli_programs_document_without_list_exits_two(capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    bad = tmp_path / "list.json"
    bad.write_text(json.dumps([1, 2, 3]), encoding="utf-8")
    code = match.main(["--programs", str(bad)], stdin=io.StringIO("{}"))
    assert code == 2
    assert "programs" in capsys.readouterr().err


# --- UX fixes: checklist, unlocks, residence, grouping, top -----------------


def test_before_apply_lists_open_questions_then_apply_requirements() -> None:
    door = doors({"country": "SE", "legal_form": "company", "need": ["compute"]})["test-eu-compute"]
    assert door["apply_requirements"] == ["Account on the portal; registration has a captcha", "Application written in English"]
    assert door["unclear"] == ["The hours table is an image and could not be read"]
    assert door["before_apply"][: len(door["unknown"])] == [item["label"] for item in door["unknown"]]
    assert door["before_apply"][-2:] == door["apply_requirements"]


def test_eligible_door_still_carries_its_apply_checklist() -> None:
    full = {"country": "SE", "legal_form": "company", "has_employment": True, "has_vat": True, "has_work_email": True, "workload_defined": True, "need": ["compute"]}
    door = doors(full)["test-eu-compute"]
    assert door["status"] == "eligible"
    assert door["before_apply"] == door["apply_requirements"]


def test_labels_follow_the_profile_language() -> None:
    sv = doors({"country": "SE", "legal_form": "company", "need": ["compute"], "lang": "sv"})["test-eu-compute"]
    assert sv["glyph"].split("\n")[1] == "●  ett bolag"
    assert "?  Är projektledaren anställd" in sv["glyph"]
    fi = doors({"country": "SE", "legal_form": "company", "need": ["compute"], "lang": "fi"})["test-eu-compute"]
    assert "○  ALV-rekisterissä" in fi["glyph"]


def test_unlocks_names_doors_blocked_only_by_legal_form() -> None:
    out = run({"country": "SE", "legal_form": "none", "age_years": 1, "revenue_msek": 0, "profit_distributed": False, "need": ["money"]})
    assert [e["name"] for e in out["unlocks"]["company"]] == ["Test SE grant"]
    assert "test-se-grant" not in {door["id"] for door in out["doors"]}


def test_unlocks_empty_when_another_rule_also_fails_or_form_unknown() -> None:
    assert run({"country": "SE", "legal_form": "none", "age_years": 12, "need": ["money"]})["unlocks"] == {}
    assert run({"country": "SE", "need": ["money"]})["unlocks"] == {}


def test_residence_country_makes_that_countrys_doors_relevant() -> None:
    dk_program = dict(
        SE_GRANT,
        id="test-dk-accelerator",
        name="Test DK accelerator",
        country="DK",
        eligibility=[{"field": "residence_country", "op": "in", "value": ["DK", "SE"]}, {"field": "legal_form", "op": "eq", "value": "company"}],
    )
    out = match.run({"country": "SE", "residence_country": "DK", "legal_form": "company", "need": ["money"]}, [SE_GRANT, dk_program], TODAY, top=0)
    by_id = {door["id"]: door for door in out["doors"]}
    assert set(by_id) == {"test-se-grant", "test-dk-accelerator"}
    assert "●  founders based in Denmark or Sweden" in by_id["test-dk-accelerator"]["glyph"]
    assert not match.is_relevant(dk_program, {"country": "SE"})


def test_doors_in_a_group_with_the_same_questions_collapse() -> None:
    small = dict(EU_COMPUTE, group="tiers")
    big = dict(EU_COMPUTE, id="test-eu-compute-big", name="Test EU compute big", group="tiers", amount={"text": "Up to 50 000 GPU hours"})
    other = dict(EU_COMPUTE, id="test-eu-compute-other", name="Other group", group="other")
    out = match.run({"country": "SE", "legal_form": "company", "need": ["compute"]}, [small, big, other], TODAY, top=0)
    ids = [door["id"] for door in out["doors"]]
    assert ids == ["test-eu-compute", "test-eu-compute-other"]
    leader = out["doors"][0]
    assert leader["also"] == [{"id": "test-eu-compute-big", "name": "Test EU compute big", "amount": "Up to 50 000 GPU hours", "apply_url": EU_COMPUTE["apply_url"], "extra": []}]
    assert "→  Also: Test EU compute big (Up to 50 000 GPU hours)" in leader["glyph"]


def test_door_with_fewer_questions_leads_and_the_sibling_lists_its_extra_ones() -> None:
    small = dict(EU_COMPUTE, group="tiers")
    big = dict(EU_COMPUTE, id="test-eu-compute-big", name="Test EU compute big", group="tiers", eligibility=EU_COMPUTE["eligibility"][:2])
    out = match.run({"country": "SE", "legal_form": "company", "need": ["compute"]}, [small, big], TODAY, top=0)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute-big"]
    sibling = out["doors"][0]["also"][0]
    assert sibling["id"] == "test-eu-compute"
    assert sibling["extra"] == ["VAT number", "email on your own domain", "workload defined: code, one system, GPU hours"]


def test_doors_in_a_group_with_a_different_status_stay_apart() -> None:
    small = dict(EU_COMPUTE, group="tiers")
    closed = dict(EU_COMPUTE, id="test-eu-compute-closed", group="tiers", availability="closed")
    out = match.run({"country": "SE", "legal_form": "company", "need": ["compute"]}, [small, closed], TODAY, top=0)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute", "test-eu-compute-closed"]
    assert all(door["also"] == [] for door in out["doors"])


def test_top_limits_full_doors_and_lists_the_rest_under_more() -> None:
    out = run({"country": "SE", "legal_form": "company", "stack": ["anthropic"]}, top=1)
    assert [door["id"] for door in out["doors"]] == ["test-global-credit"]
    assert [door["id"] for door in out["more"]] == ["test-se-grant", "test-eu-compute"]
    assert set(out["more"][0]) == {"id", "name", "kind", "status", "availability", "amount", "open_questions", "foreign", "founder_cost", "stage_mismatch", "topic_mismatch", "undersized", "poor_fit", "status_url"}
    assert run({"country": "SE", "legal_form": "company", "stack": ["anthropic"]}, top=0)["more"] == []


def test_cli_top_flag(capsys: pytest.CaptureFixture[str]) -> None:
    stdin = io.StringIO(json.dumps({"country": "SE", "legal_form": "company", "stack": ["anthropic"]}))
    assert match.main(["--programs", str(FIXTURE_PATH), "--today", "2026-10-15", "--top", "2"], stdin=stdin) == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out["doors"]) == 2 and len(out["more"]) == 1


def test_confirmation_rule_stays_open_until_the_founder_confirms() -> None:
    kth = dict(SE_GRANT, id="test-kth", name="Test KTH", eligibility=[{"field": "country", "op": "eq", "value": "SE"}, {"field": "confirmed", "op": "contains", "value": "kth_affiliation"}])
    out = match.run({"country": "SE", "legal_form": "none", "need": ["money"]}, [kth], TODAY)
    door = out["doors"][0]
    assert door["status"] == "unknown"
    assert door["unknown"][0]["label"] == "a current KTH student, researcher or employee on the team"
    confirmed = match.run({"country": "SE", "legal_form": "none", "need": ["money"], "confirmed": ["kth_affiliation"]}, [kth], TODAY)
    assert confirmed["doors"][0]["status"] == "eligible"


def test_group_collapses_when_sibling_only_adds_questions() -> None:
    small = dict(EU_COMPUTE, group="tiers")
    fast = dict(EU_COMPUTE, id="test-fast", name="Test fast", group="tiers", amount={"text": "Up to 50 000 GPU hours"},
                eligibility=EU_COMPUTE["eligibility"] + [{"field": "confirmed", "op": "contains", "value": "hpc_experience"}])
    out = match.run({"country": "SE", "legal_form": "company", "need": ["compute"]}, [small, fast], TODAY, top=0)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute"]
    sibling = out["doors"][0]["also"][0]
    assert sibling["extra"] == ["the team already runs its code on an HPC system"]
    assert "also needs: the team already runs its code on an HPC system" in out["doors"][0]["glyph"]


def test_top_takes_the_best_door_of_each_need_in_turn() -> None:
    credit_a = dict(CREDIT, id="credit-a", name="Credit A", eligibility=[])
    credit_b = dict(CREDIT, id="credit-b", name="Credit B", eligibility=[])
    compute = dict(EU_COMPUTE, eligibility=[{"field": "legal_form", "op": "eq", "value": "company"}, {"field": "has_vat", "op": "eq", "value": True}])
    out = match.run({"country": "SE", "legal_form": "company", "need": ["compute", "credits"]}, [credit_a, credit_b, compute], TODAY, top=2)
    assert [door["id"] for door in out["doors"]] == ["test-eu-compute", "credit-a"]
    assert [door["id"] for door in out["more"]] == ["credit-b"]


def test_unlocks_only_for_founders_who_can_register_a_company() -> None:
    not_in = dict(SE_GRANT, id="test-consortium", name="Test consortium", eligibility=[{"field": "country", "op": "eq", "value": "SE"}, {"field": "legal_form", "op": "not_in", "value": ["none", "sole_trader"]}])
    out = match.run({"country": "SE", "legal_form": "none", "need": ["money"]}, [SE_GRANT, not_in], TODAY)
    assert [e["name"] for e in out["unlocks"]["company"]] == ["Test SE grant", "Test consortium"]
    assert match.run({"country": "SE", "legal_form": "company", "need": ["money"]}, [SE_GRANT, not_in], TODAY)["unlocks"] == {}
    academic = match.run({"country": "SE", "legal_form": "academia", "need": ["money"]}, [SE_GRANT], TODAY)
    assert academic["unlocks"] == {}


def test_door_run_from_another_country_ranks_after_domestic_doors() -> None:
    swedish_open_call = dict(EU_COMPUTE, id="test-se-open-call", name="Swedish open call", home_country="SE", eligibility=[])
    finnish = dict(SE_GRANT, id="test-fi-grant", name="Finnish grant", country="FI", eligibility=[{"field": "country", "op": "eq", "value": "FI"}, {"field": "has_vat", "op": "eq", "value": True}])
    out = match.run({"country": "FI", "need": ["compute", "money"]}, [swedish_open_call, finnish], TODAY, top=0)
    assert [door["id"] for door in out["doors"]] == ["test-fi-grant", "test-se-open-call"]
    assert out["doors"][1]["foreign"] is True
    home = match.run({"country": "SE", "need": ["compute"]}, [swedish_open_call], TODAY, top=0)
    assert home["doors"][0]["foreign"] is False


def test_cross_border_founder_hears_which_doors_a_local_company_would_open() -> None:
    dk_grant = dict(SE_GRANT, id="test-dk-grant", name="Test DK grant", country="DK", eligibility=[{"field": "country", "op": "eq", "value": "DK"}, {"field": "legal_form", "op": "eq", "value": "company"}])
    out = match.run({"country": "SE", "residence_country": "DK", "legal_form": "company", "need": ["money"]}, [dk_grant], TODAY)
    assert [e["name"] for e in out["unlocks"]["country:DK"]] == ["Test DK grant"]
    assert out["doors"] == []
    same = match.run({"country": "DK", "residence_country": "DK", "legal_form": "company", "need": ["money"]}, [dk_grant], TODAY)
    assert same["unlocks"] == {}


def test_unlocks_list_open_doors_before_closed_ones() -> None:
    closed = dict(SE_GRANT, id="test-closed", name="Closed grant", availability="closed")
    open_ = dict(SE_GRANT, id="test-open", name="Open grant", availability="open")
    out = match.run({"country": "SE", "legal_form": "none", "age_years": 1, "revenue_msek": 0, "profit_distributed": False, "need": ["money"]}, [closed, open_], TODAY)
    assert [(e["name"], e["availability"]) for e in out["unlocks"]["company"]] == [("Open grant", "open"), ("Closed grant", "closed")]


def test_support_need_keeps_no_cash_programs_out_of_a_money_answer() -> None:
    camp = dict(SE_GRANT, id="test-camp", name="Free camp", need=["support"], eligibility=[{"field": "country", "op": "eq", "value": "SE"}])
    money = run({"country": "SE", "legal_form": "company", "need": ["money"]})
    assert "test-camp" not in {d["id"] for d in money["doors"]}
    both = match.run({"country": "SE", "need": ["money", "support"]}, [camp], TODAY)
    assert [d["id"] for d in both["doors"]] == ["test-camp"]
    assert match.normalize_profile({"need": ["coaching"]})[0]["need"] == ["support"]


def test_money_the_founder_keeps_ranks_before_equity_and_fees() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    doors = [
        match.evaluate(dict(EU_COMPUTE, **base, id="fee", founder_cost="fee"), {"country": "SE"}, TODAY, "en"),
        match.evaluate(dict(EU_COMPUTE, **base, id="equity", founder_cost="equity"), {"country": "SE"}, TODAY, "en"),
        match.evaluate(dict(EU_COMPUTE, **base, id="loan", founder_cost="repay"), {"country": "SE"}, TODAY, "en"),
        match.evaluate(dict(EU_COMPUTE, **base, id="grant"), {"country": "SE"}, TODAY, "en"),
    ]
    assert [door.id for door in match.rank(doors)] == ["grant", "loan", "equity", "fee"]


def test_stage_mismatch_ranks_after_doors_that_fit_the_stage() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    profile = {"country": "SE", "legal_form": "none"}
    doors = [
        match.evaluate(dict(EU_COMPUTE, **base, id="scaleup", stages=["seed", "series_a"]), profile, TODAY, "en"),
        match.evaluate(dict(EU_COMPUTE, **base, id="early", stages=["idea", "pre_seed"]), profile, TODAY, "en"),
    ]
    assert [door.id for door in match.rank(doors)] == ["early", "scaleup"]
    assert match.founder_stage({"legal_form": "none"}) == "idea"
    assert match.founder_stage({"legal_form": "company"}) is None


def test_open_doors_rank_before_doors_of_unknown_status() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    doors = [
        match.evaluate(dict(EU_COMPUTE, **base, id="maybe", availability="unknown"), {"country": "SE"}, TODAY, "en"),
        match.evaluate(dict(EU_COMPUTE, **base, id="open", availability="open"), {"country": "SE"}, TODAY, "en"),
    ]
    assert [door.id for door in match.rank(doors)] == ["open", "maybe"]


def test_topic_call_stays_out_unless_the_sector_matches() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    marine = dict(EU_COMPUTE, **base, id="marine", sectors=["marine"])
    general = dict(EU_COMPUTE, **base, id="general")
    out = match.run({"country": "SE", "legal_form": "company", "need": ["money"]}, [marine, general], TODAY)
    assert [door["id"] for door in out["doors"]] == ["general"]
    assert [door["id"] for door in out["more"]] == ["marine"]
    out = match.run({"country": "SE", "legal_form": "company", "need": ["money"], "sector": ["ocean"]}, [marine, general], TODAY)
    assert "marine" in [door["id"] for door in out["doors"]]


def test_door_paying_a_small_share_of_the_need_ranks_after_one_that_can_pay_it() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    group = dict(EU_COMPUTE, **base, id="group", amount={"text": "120 000 SEK", "max": 120000, "currency": "SEK"})
    project = dict(EU_COMPUTE, **base, id="project", amount={"text": "up to 2 MSEK", "max": 2000000, "currency": "SEK"})
    profile = {"country": "SE", "need_eur": 135000}
    doors = [match.evaluate(group, profile, TODAY, "en"), match.evaluate(project, profile, TODAY, "en")]
    assert [door.undersized for door in doors] == [True, False]
    assert [door.id for door in match.rank(doors)] == ["project", "group"]


def test_no_stated_need_or_no_maximum_is_never_undersized() -> None:
    base = {"country": "SE", "kind": "grant", "need": ["money"], "eligibility": []}
    small = dict(EU_COMPUTE, **base, id="small", amount={"text": "10 000 SEK", "max": 10000, "currency": "SEK"})
    open_ended = dict(EU_COMPUTE, **base, id="open-ended", amount={"text": "19 % of R&D costs"})
    assert not match.undersized(small, {"country": "SE"})
    assert not match.undersized(open_ended, {"country": "SE", "need_eur": 1000000})
    assert match.normalize_profile({"need_eur": "135 000"})[0]["need_eur"] == 135000.0
