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


def all_ids(out: dict) -> list[str]:
    """Doors shown in full, then the ones summarised under more, then collapsed siblings."""
    ids = [door["id"] for door in out["doors"]] + [door["id"] for door in out["more"]]
    for door in out["doors"]:
        ids += [sibling["id"] for sibling in door["also"]]
    return ids


def test_swedish_ab_wanting_gpu_and_credits_gets_at_least_five_doors() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    ids = all_ids(out)
    assert len(ids) >= 5, ids
    for expected in ("eurohpc-playground", "claude-startups", "aws-activate", "nvidia-inception"):
        assert expected in ids


def test_default_answer_shows_at_most_three_doors_in_full() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY)
    assert len(out["doors"]) <= 3
    assert out["more"], "the remaining doors must be listed under more, not dropped"


def test_eurohpc_tiers_collapse_into_one_door_for_a_swedish_ab() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY, top=0)
    by_id = {d["id"]: d for d in out["doors"]}
    assert "eurohpc-playground" in by_id
    assert "eurohpc-fast-lane" not in by_id and "eurohpc-large-scale" not in by_id
    siblings = {s["id"] for s in by_id["eurohpc-playground"]["also"]}
    assert siblings == {"eurohpc-fast-lane", "eurohpc-large-scale"}
    assert "→  Även:" in by_id["eurohpc-playground"]["glyph"]


def test_playground_first_question_is_employment_in_swedish() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY, top=0)
    door = {d["id"]: d for d in out["doors"]}["eurohpc-playground"]
    assert door["status"] == "unknown"
    assert door["unknown"][0]["label"] == "anställd projektledare efter allokeringen"
    assert "?  Är projektledaren anställd" in door["glyph"]
    assert not any(word in door["glyph"] for word in ("company", "employment", "VAT number", "work email")), door["glyph"]


def test_idea_stage_founder_without_company_gets_no_false_green_marks() -> None:
    """Regression for the Sting case: a founder with no company and an idea saw a green 'early research spinout'."""
    out = match.run({"country": "SE", "legal_form": "none", "stage": "idea", "sector": ["climate"], "need": ["money"], "lang": "sv"}, PROGRAMS, TODAY, top=0)
    for door in out["doors"]:
        for label in door["met"]:
            assert not any(word in label.lower() for word in ("research", "spinout", "forsk")), (door["id"], label)
            # "ett bolag, eller inget bolag än" (EIC) is honest; a bare "ett bolag" for a founder with none is not.
            assert label != "ett bolag", door["id"]


def test_idea_stage_founder_hears_what_a_company_unlocks() -> None:
    out = match.run({"country": "SE", "legal_form": "none", "stage": "idea", "need": ["money"]}, PROGRAMS, TODAY)
    unlocked = [entry["name"] for entry in out["unlocks"].get("company", [])]
    for expected in ("Vinnova Innovativa Startups 2026", "Almi Innovationslån"):
        assert expected in unlocked, out["unlocks"]


def test_almi_innovationslan_needs_a_business() -> None:
    out = match.run({"country": "SE", "legal_form": "none", "need": ["money"]}, PROGRAMS, TODAY, include_all=True, top=0)
    door = {d["id"]: d for d in out["doors"]}["almi-innovationslan"]
    assert door["status"] == "blocked"


def test_no_rule_in_the_data_carries_free_text() -> None:
    for program in PROGRAMS:
        for gate in program["eligibility"]:
            members = gate["any"] if "any" in gate else [gate]
            assert "label" not in gate and "question" not in gate, program["id"]
            for member in members:
                assert set(member) == {"field", "op", "value"}, (program["id"], member)


def test_swedish_company_with_founders_in_denmark_sees_both_countries() -> None:
    out = match.run({"country": "SE", "residence_country": "DK", "legal_form": "company", "need": ["money"]}, PROGRAMS, TODAY, include_all=True, top=0)
    countries = {door["country"] for door in out["doors"]}
    assert {"SE", "DK"} <= countries, countries
    by_id = {d["id"]: d for d in out["doors"]}
    # A Danish door with a registration rule says the company is not registered in Denmark; it does not pretend to fit.
    assert "×  in Denmark" in by_id["innovationsfonden-innofounder"]["glyph"]


def test_default_run_hides_blocked_and_nothing_is_stale_or_warned() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY, top=0)
    assert all(door["status"] != "blocked" for door in out["doors"])
    assert out["stale"] == []
    assert out["warnings"] == []


def test_every_record_verified_between_the_rebuild_day_and_today() -> None:
    rebuild_day = date(2026, 10, 15)
    for program in PROGRAMS:
        verified = date.fromisoformat(program["last_verified"])
        assert rebuild_day <= verified <= date.today(), program["id"]


def test_finnish_money_doors_exclude_vinnova_and_include_eu() -> None:
    out = match.run({"country": "FI", "legal_form": "company", "need": ["money"]}, PROGRAMS, TODAY, top=0)
    ids = [door["id"] for door in out["doors"]]
    assert "business-finland-sprint" in ids
    assert "eic-accelerator" in ids
    assert "vinnova-innovativa-startups" not in ids


def test_academia_sees_ai_for_science_and_naiss_not_playground() -> None:
    out = match.run({"country": "SE", "legal_form": "academia", "need": ["compute"]}, PROGRAMS, TODAY, include_all=True, top=0)
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
        fields: set[str] = set()
        for gate in program["eligibility"]:
            fields |= match.rule_fields(gate)
        assert fields & {"country", "residence_country"}, program["id"]


def test_every_record_states_availability() -> None:
    assert all(program.get("availability") in ("open", "closed", "unknown") for program in PROGRAMS)


def test_claude_startups_is_closed_and_ranks_after_the_open_doors() -> None:
    out = match.run(SWEDISH_AB, PROGRAMS, TODAY, top=0)
    ids = [door["id"] for door in out["doors"]]
    by_id = {door["id"]: door for door in out["doors"]}
    assert by_id["claude-startups"]["availability"] == "closed"
    assert ids.index("claude-startups") > ids.index("eurohpc-playground")
    assert "Stängd vid kontroll 2026-10-15" in by_id["claude-startups"]["glyph"]


def test_finnish_founder_does_not_get_a_swedish_call_first() -> None:
    """Regression from the 2026-10-16 evaluation: FFI ASP led a Finnish answer."""
    out = match.run({"country": "FI", "legal_form": "company", "age_years": 1, "employees": 2, "need": ["money"], "lang": "en"}, PROGRAMS, TODAY, top=0)
    ids = [door["id"] for door in out["doors"]]
    first_foreign = next((i for i, d in enumerate(out["doors"]) if d["foreign"]), len(ids))
    assert all(not d["foreign"] for d in out["doors"][:first_foreign])
    assert ids[0] != "vinnova-ffi-asp-accelerated-startup-partnership", ids
    assert out["doors"][0]["country"] in ("FI", "EU"), ids[:3]


def test_aws_activate_matches_a_founder_who_builds_on_claude() -> None:
    out = match.run({"country": "SE", "legal_form": "company", "age_years": 1, "stage": "pre_seed", "need": ["credits"], "stack": ["anthropic", "vercel"]}, PROGRAMS, TODAY)
    assert "aws-activate" in all_ids(out)


def test_idea_stage_money_puts_a_grant_before_equity_and_fees() -> None:
    out = match.run({"country": "SE", "legal_form": "none", "stage": "idea", "need": ["money"], "lang": "sv"}, PROGRAMS, TODAY)
    first = out["doors"][0]
    assert first["id"] == "almi-verifieringsmedel"
    costs = [door["founder_cost"] for door in out["doors"]]
    assert costs == sorted(costs, key=lambda cost: {"none": 0, "repay": 1, "equity": 2, "fee": 3}[cost])
