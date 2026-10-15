"""Tests for scripts/validate.py. No network, no real data file."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

import validate

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
FIXTURE = json.loads((Path(__file__).parent / "fixtures" / "programs_small.json").read_text(encoding="utf-8"))
TODAY = date(2026, 10, 15)


def errors(programs: dict) -> list[str]:
    return validate.validate(programs, SCHEMA, TODAY, references_dir=None)


def test_fixture_is_valid() -> None:
    assert errors(FIXTURE) == []


def test_rejects_missing_required_field() -> None:
    bad = copy.deepcopy(FIXTURE)
    del bad["programs"][0]["who"]
    found = errors(bad)
    assert len(found) == 1
    assert "test-se-grant" in found[0]
    assert "who" in found[0]


def test_rejects_unknown_top_level_key() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["colour"] = "blue"
    assert any("colour" in e for e in errors(bad))


def test_rejects_unknown_op() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][1]["eligibility"][0]["op"] = "between"
    assert any("between" in e for e in errors(bad))


def test_rejects_unknown_profile_field() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][1]["eligibility"][0]["field"] = "shoe_size"
    assert any("shoe_size" in e for e in errors(bad))


def test_rejects_group_with_one_member() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["eligibility"][3]["any"].pop()
    assert any("any" in e for e in errors(bad))


def test_rejects_duplicate_id() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][2]["id"] = bad["programs"][0]["id"]
    assert any("duplicate" in e.lower() for e in errors(bad))


def test_rejects_future_last_verified() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["last_verified"] = "2026-11-01"
    assert any("future" in e.lower() for e in errors(bad))


def test_rejects_malformed_date() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["last_verified"] = "2026-13-40"
    assert any("last_verified" in e for e in errors(bad))


def test_rejects_bad_reference_anchor() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["reference"] = "references/Nordic Grants.md"
    assert any("reference" in e for e in errors(bad))


def test_rejects_bad_country_code() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["country"] = "Sweden"
    assert any("country" in e for e in errors(bad))


def test_reference_anchor_must_exist_in_file(tmp_path: Path) -> None:
    refs = tmp_path / "references"
    refs.mkdir()
    (refs / "nordic-grants.md").write_text("## Test SE grant {#test-se-grant}\n", encoding="utf-8")
    found = validate.validate(FIXTURE, SCHEMA, TODAY, references_dir=refs)
    assert not any("test-se-grant" in e for e in found)
    assert any("compute.md" in e for e in found)
    assert any("ai-api-credits.md" in e for e in found)


def test_reference_anchor_missing_inside_existing_file(tmp_path: Path) -> None:
    refs = tmp_path / "references"
    refs.mkdir()
    for name in ("nordic-grants.md", "compute.md", "ai-api-credits.md"):
        (refs / name).write_text("## Something else {#something-else}\n", encoding="utf-8")
    found = validate.validate(FIXTURE, SCHEMA, TODAY, references_dir=refs)
    assert len(found) == 3
    assert all("anchor" in e for e in found)


def test_rejects_bad_availability() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["availability"] = "maybe"
    assert any("availability" in e for e in errors(bad))


def test_accepts_known_availability() -> None:
    good = copy.deepcopy(FIXTURE)
    good["programs"][0]["availability"] = "closed"
    assert errors(good) == []


# --- op, value and field compatibility --------------------------------------


def rule(field: str, op: str, value: object) -> dict:
    return {"field": field, "op": op, "value": value}


def with_rule(new_rule: dict) -> dict:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["eligibility"][0] = new_rule
    return bad


def test_in_needs_a_list_value() -> None:
    found = errors(with_rule(rule("country", "in", "SE")))
    assert any("'in'" in e and "list" in e for e in found)
    assert errors(with_rule(rule("country", "in", ["SE", "FI"]))) == []


def test_not_in_needs_a_list_value() -> None:
    assert any("'not_in'" in e for e in errors(with_rule(rule("stage", "not_in", "later"))))


def test_contains_needs_a_list_field() -> None:
    found = errors(with_rule(rule("country", "contains", "SE")))
    assert any("'contains'" in e and "stack" in e for e in found)
    assert errors(with_rule(rule("stack", "contains", "aws"))) == []


def test_contains_value_must_be_a_single_item() -> None:
    assert any("'contains'" in e for e in errors(with_rule(rule("stack", "contains", ["aws", "gcp"]))))


def test_numeric_ops_need_a_numeric_field() -> None:
    found = errors(with_rule(rule("country", "lte", 10)))
    assert any("'lte'" in e and "numeric" in e for e in found)


def test_numeric_ops_need_a_numeric_value() -> None:
    found = errors(with_rule(rule("age_years", "gte", "10")))
    assert any("'gte'" in e and "numeric" in e for e in found)
    assert any("'lt'" in e for e in errors(with_rule(rule("employees", "lt", True))))
    assert errors(with_rule(rule("employees", "gt", 2.5))) == []


def test_eq_on_boolean_field_needs_a_boolean_value() -> None:
    found = errors(with_rule(rule("has_vat", "eq", "yes")))
    assert any("has_vat" in e and "boolean" in e for e in found)
    assert any("'neq'" in e for e in errors(with_rule(rule("vc_backed", "neq", 1))))
    assert errors(with_rule(rule("has_vat", "eq", True))) == []


def test_boolean_value_needs_a_boolean_field() -> None:
    found = errors(with_rule(rule("country", "eq", True)))
    assert any("country" in e and "boolean" in e for e in found)


def test_compatibility_is_checked_inside_groups() -> None:
    bad = copy.deepcopy(FIXTURE)
    bad["programs"][0]["eligibility"][3]["any"][0] = rule("revenue_msek", "lte", "ten")
    found = errors(bad)
    assert any("any[0]" in e and "'lte'" in e for e in found)
