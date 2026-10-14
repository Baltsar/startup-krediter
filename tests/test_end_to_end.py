"""End-to-end checks against the real data file: the done criteria from the rebuild plan."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import match

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS = json.loads((ROOT / "data" / "programs.json").read_text(encoding="utf-8"))["programs"]
TODAY = date(2026, 10, 15)
SWEDISH_AB = {
    "country": "SE", "legal_form": "company", "age_years": 2, "employees": 4,
    "need": ["compute", "credits"], "stack": ["anthropic", "aws"], "lang": "sv",
}


def test_swedish_ab_wanting_gpu_and_credits_gets_at_least_five_doors() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    ids = [door["id"] for door in out["doors"]]
    assert len(ids) >= 5, ids
    for expected in ("eurohpc-playground", "claude-startups", "aws-activate", "nvidia-inception"):
        assert expected in ids


def test_playground_first_question_is_employment() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    door = {d["id"]: d for d in out["doors"]}["eurohpc-playground"]
    assert door["status"] == "unknown"
    assert door["unknown"][0]["label"] == "employment"
    assert "?  Is the project lead employed" in door["glyph"]


def test_default_run_hides_blocked_and_nothing_is_stale_or_warned() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    assert all(door["status"] != "blocked" for door in out["doors"])
    assert out["stale"] == []
    assert out["warnings"] == []


def test_every_record_was_verified_on_the_rebuild_day() -> None:
    assert {program["last_verified"] for program in PROGRAMS} == {"2026-10-15"}


def test_finnish_money_doors_exclude_vinnova_and_include_eu() -> None:
    out = match.run({"country": "FI", "legal_form": "company", "need": ["money"]}, PROGRAMS, TODAY)
    ids = [door["id"] for door in out["doors"]]
    assert "business-finland-sprint" in ids
    assert "eic-accelerator" in ids
    assert "vinnova-innovativa-startups" not in ids


def test_academia_sees_ai_for_science_and_naiss_not_playground() -> None:
    out = match.run({"country": "SE", "legal_form": "academia", "need": ["compute"]}, PROGRAMS, TODAY, include_all=True)
    by_id = {door["id"]: door for door in out["doors"]}
    assert by_id["eurohpc-ai-for-science"]["status"] != "blocked"
    assert by_id["naiss-allocations"]["status"] != "blocked"
    assert by_id["eurohpc-playground"]["status"] == "blocked"


def test_data_is_ordered_by_domain() -> None:
    order = ["nordic-grants", "eu-grants", "compute", "cloud-credits", "ai-api-credits", "accelerators-se"]
    ranks = [order.index(program["reference"].split("/")[1].split(".md")[0]) for program in PROGRAMS]
    assert ranks == sorted(ranks)


def test_every_country_specific_record_has_a_country_rule() -> None:
    for program in PROGRAMS:
        if program["country"] in ("EU", "global"):
            continue
        fields = {rule.get("field") for rule in program["eligibility"]}
        assert "country" in fields, program["id"]


def test_every_record_states_availability() -> None:
    assert all(program.get("availability") in ("open", "closed", "unknown") for program in PROGRAMS)


def test_claude_startups_is_closed_and_ranks_after_the_open_doors() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    ids = [door["id"] for door in out["doors"]]
    by_id = {door["id"]: door for door in out["doors"]}
    assert by_id["claude-startups"]["availability"] == "closed"
    assert ids.index("claude-startups") > ids.index("eurohpc-playground")
    assert "Closed when verified 2026-10-15" in by_id["claude-startups"]["glyph"]
