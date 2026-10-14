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
