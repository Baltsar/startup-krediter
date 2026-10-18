"""Round-3 regressions: the trap in each lost case must reach the first answer's screen.

Each profile holds only what the founder's first message says, which is all the
skill knows when it writes the first answer. With the hidden profile the doors
would simply be blocked, which would test nothing: the point is that the
question gets asked. Cases and traps: docs/benchmark/2026-10-17-round3.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import match
import pytest

PROGRAMS = json.loads((Path(__file__).resolve().parent.parent / "data" / "programs.json").read_text(encoding="utf-8"))["programs"]
TODAY = date(2026, 10, 18)

FIRST_MESSAGES: dict[str, tuple[dict, str]] = {
    # A listed group owns 62%: not an SME, so the EIC Accelerator is closed.
    "s13": ({"named": ["eic-accelerator", "energimyndigheten"], "country": "SE", "legal_form": "company", "age_years": 3, "employees": 11, "sector": ["energy"], "need": ["money"], "need_eur": 9000000, "lang": "en"}, "ownership"),
    # Holds a running Sproti grant from the same fund.
    "s07": ({"named": ["rannis"], "country": "IS", "legal_form": "company", "sector": ["ai"], "need": ["money", "compute"], "lang": "en"}, "grants"),
    # A full-time teacher with no company: starttiraha needs full-time entrepreneurship.
    "s04": ({"country": "FI", "legal_form": "none", "sector": ["ai"], "need": ["money"], "need_eur": 25000, "lang": "fi"}, "work"),
    # "Anonymized" CT scans from a hospital are usually pseudonymised.
    "s15": ({"country": "SE", "legal_form": "company", "age_years": 2, "employees": 5, "sector": ["radiology"], "need": ["credits", "compute"], "personal_data": "anonymized", "lang": "en"}, "data"),
    # Two unpaid founders expecting 20% back from the R&D deduction, which needs salaried R&D staff.
    "s06": ({"named": ["skatteverket"], "country": "SE", "legal_form": "company", "sector": ["ai", "fintech"], "need": ["money"], "need_eur": 32000, "lang": "sv"}, "staff"),
    # A KTH student asking about "any grant for an app".
    "s11": ({"need": ["money"], "lang": "sv"}, "affiliation"),
}


@pytest.mark.parametrize("case", sorted(FIRST_MESSAGES))
def test_round3_trap_reaches_the_screen(case: str) -> None:
    profile, topic = FIRST_MESSAGES[case]
    out = match.run(profile, PROGRAMS, TODAY)
    assert topic in [item["topic"] for item in out["screen"]], (case, out["screen"])


def test_starttiraha_is_not_green_for_a_founder_whose_job_is_unknown() -> None:
    profile, _ = FIRST_MESSAGES["s04"]
    out = match.run(profile, PROGRAMS, TODAY, top=0)
    starttiraha = next(door for door in out["doors"] if door["id"] == "starttiraha")
    assert starttiraha["status"] == "unknown"


def test_starttiraha_closes_for_a_founder_with_a_full_time_job() -> None:
    profile, _ = FIRST_MESSAGES["s04"]
    out = match.run(dict(profile, founder_employed_elsewhere=True), PROGRAMS, TODAY, door_id="starttiraha")
    assert out["doors"][0]["status"] == "blocked"


def test_eic_closes_for_a_company_majority_owned_by_a_large_group() -> None:
    profile, _ = FIRST_MESSAGES["s13"]
    answered = dict(profile, owner_company_share=62, denied=["group_within_sme_limits"])
    out = match.run(answered, PROGRAMS, TODAY, door_id="eic-accelerator")
    assert out["doors"][0]["status"] == "blocked"


def test_rd_deduction_is_a_tax_route_and_needs_paid_staff() -> None:
    profile = {"country": "SE", "legal_form": "company", "need": ["money"], "lang": "sv"}
    out = match.run(profile, PROGRAMS, TODAY, door_id="skatteverket-forskningsavdrag")
    door = out["doors"][0]
    assert door["route"] == "tax"
    assert "staff" in door["situation"]
    no_payroll = match.run(dict(profile, paid_staff=0), PROGRAMS, TODAY, door_id="skatteverket-forskningsavdrag")
    assert no_payroll["doors"][0]["status"] == "blocked"
