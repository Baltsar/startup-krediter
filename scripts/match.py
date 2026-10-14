#!/usr/bin/env python3
"""Match a founder profile against data/programs.json. Standard library only.

    python3 scripts/match.py [--all] [--live] [--programs PATH] [--today YYYY-MM-DD] < profile.json

A door is eligible when every rule is met, blocked when any rule failed, and
unknown otherwise. A field that is absent from the profile is unknown, never
defaulted: the skill asks the founder instead of guessing, because a guessed
country or headcount produces a confident wrong answer. Blocked doors are
hidden unless --all is given. Records whose last_verified is older than
STALE_DAYS are flagged so the skill re-reads the page before quoting them.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import TextIO

import vinnova_api

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS_PATH = ROOT / "data" / "programs.json"
STALE_DAYS = 90

EU_MEMBERS = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE",
    "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",
}
# EEA members, EuroHPC participating states and Horizon Europe associated countries.
# EuroHPC and EIC calls accept applicants from this wider set, not EU27 alone.
EU_ASSOCIATED = EU_MEMBERS | {
    "NO", "IS", "LI", "CH", "GB", "UA", "TR", "RS", "ME", "MK", "AL", "BA", "MD",
    "GE", "AM", "IL", "TN", "FO", "NZ",
}

NUMERIC_FIELDS = {"age_years", "employees", "revenue_msek", "balance_msek", "revenue_meur", "funding_raised_usd"}
INTEGER_FIELDS = {"employees"}
BOOLEAN_FIELDS = {"vc_backed", "has_vat", "has_employment", "has_work_email", "has_website", "has_developer", "workload_defined", "profit_distributed"}
LIST_FIELDS = {"stack", "sector", "vc_partner", "need"}
TRUE_WORDS = {"true", "yes", "ja", "y", "1"}
FALSE_WORDS = {"false", "no", "nej", "n", "0"}
STACK_ALIASES = {
    "claude": "anthropic", "chatgpt": "openai", "google": "gcp", "google cloud": "gcp", "gcloud": "gcp",
    "microsoft": "azure", "hf": "huggingface", "hugging face": "huggingface", "amazon": "aws",
}
NEED_ALIASES = {
    "gpu": "compute", "hpc": "compute", "gpu-timmar": "compute", "pengar": "money", "grant": "money",
    "bidrag": "money", "krediter": "credits", "credit": "credits",
}
LEGAL_FORM_ALIASES = {
    "ab": "company", "as": "company", "oy": "company", "aps": "company", "a/s": "company", "ehf": "company",
    "ltd": "company", "gmbh": "company", "inc": "company", "llc": "company", "aktiebolag": "company",
    "bolag": "company", "startup": "company", "sme": "company",
    "ideell_forening": "nonprofit", "ideell förening": "nonprofit", "förening": "nonprofit", "forening": "nonprofit",
    "stiftelse": "nonprofit", "university": "academia", "universitet": "academia", "research": "academia",
    "academic": "academia", "public_sector": "public", "offentlig": "public",
    "enskild_firma": "sole_trader", "sole trader": "sole_trader",
}
HEAD = {"eligible": "●", "unknown": "◐", "blocked": "×"}
RANK = {"eligible": 0, "unknown": 1, "blocked": 2}


@dataclass(frozen=True)
class RuleResult:
    status: str
    label: str
    question: str | None


@dataclass
class Door:
    id: str
    name: str
    kind: str
    country: str
    status: str
    met: list[str]
    failed: list[str]
    unknown: list[dict]
    what: str
    amount: dict
    next_step: str
    apply_url: str
    status_url: str
    reference: str
    last_verified: str
    stale: bool
    notes: str
    live: dict | None = None
    glyph: str = ""


def to_number(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.replace(",", ".").replace(" ", ""))
        except ValueError:
            return None
    return None


def to_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        word = value.strip().lower()
        if word in TRUE_WORDS:
            return True
        if word in FALSE_WORDS:
            return False
    return None


def normalize_profile(raw: dict) -> tuple[dict, list[str]]:
    """Lowercase and alias the free-text fields; coerce numbers and booleans; drop what cannot be read."""
    profile: dict = {}
    warnings: list[str] = []
    for key, value in raw.items():
        if value is None:
            continue
        if key in NUMERIC_FIELDS:
            number = to_number(value)
            if number is None:
                warnings.append(f"{key} is not a number, treated as unknown")
                continue
            profile[key] = int(number) if key in INTEGER_FIELDS and number == int(number) else number
        elif key in BOOLEAN_FIELDS:
            flag = to_bool(value)
            if flag is None:
                warnings.append(f"{key} is not yes or no, treated as unknown")
                continue
            profile[key] = flag
        elif key in LIST_FIELDS:
            items = value if isinstance(value, list) else [value]
            words = [str(item).strip().lower() for item in items if str(item).strip()]
            if key == "stack":
                words = [STACK_ALIASES.get(word, word) for word in words]
            if key == "need":
                words = [NEED_ALIASES.get(word, word) for word in words]
            profile[key] = list(dict.fromkeys(words))
        elif key == "country":
            profile[key] = str(value).strip().upper()
        elif key == "legal_form":
            word = str(value).strip().lower()
            profile[key] = LEGAL_FORM_ALIASES.get(word, word)
        elif key in ("stage", "lang"):
            profile[key] = str(value).strip().lower()
        else:
            profile[key] = value
    return profile, warnings


def compare(op: str, actual: object, expected: object) -> bool:
    if isinstance(actual, bool) or isinstance(expected, bool):
        return op in ("eq", "neq") and ((actual == expected) == (op == "eq"))
    if op == "eq":
        return actual == expected
    if op == "neq":
        return actual != expected
    if op == "in":
        return isinstance(expected, list) and actual in expected
    if op == "not_in":
        return isinstance(expected, list) and actual not in expected
    if op == "contains":
        return isinstance(actual, list) and expected in actual
    if not isinstance(actual, (int, float)) or not isinstance(expected, (int, float)):
        return False
    if op == "lte":
        return actual <= expected
    if op == "gte":
        return actual >= expected
    if op == "lt":
        return actual < expected
    if op == "gt":
        return actual > expected
    raise ValueError(f"unknown op {op}")


def evaluate_rule(rule: dict, profile: dict) -> RuleResult:
    """A rule is met, failed or unknown. A group is met if any member is met, failed only when every member is known and failed."""
    if "any" in rule:
        results = [evaluate_rule(member, profile) for member in rule["any"]]
        if any(result.status == "met" for result in results):
            return RuleResult("met", rule["label"], None)
        if all(result.status == "failed" for result in results):
            return RuleResult("failed", rule["label"], None)
        question = next((result.question for result in results if result.status == "unknown"), None)
        return RuleResult("unknown", rule["label"], question)
    actual = profile.get(rule["field"])
    if actual is None:
        return RuleResult("unknown", rule["label"], rule["question"])
    status = "met" if compare(rule["op"], actual, rule["value"]) else "failed"
    return RuleResult(status, rule["label"], None)


def is_relevant(program: dict, profile: dict) -> bool:
    """Need must overlap when given. Country must match when given: ISO-2 exactly, EU by the associated set, global always."""
    need = profile.get("need")
    if need and not set(need) & set(program["need"]):
        return False
    country = profile.get("country")
    scope = program["country"]
    if not country or scope == "global":
        return True
    if scope == "EU":
        return country in EU_ASSOCIATED
    return scope == country


def evaluate(program: dict, profile: dict, today: date) -> Door:
    results = [evaluate_rule(rule, profile) for rule in program["eligibility"]]
    met = [result.label for result in results if result.status == "met"]
    failed = [result.label for result in results if result.status == "failed"]
    unknown = [{"label": result.label, "question": result.question} for result in results if result.status == "unknown"]
    status = "blocked" if failed else "eligible" if not unknown else "unknown"
    verified = date.fromisoformat(program["last_verified"])
    return Door(
        id=program["id"],
        name=program["name"],
        kind=program["kind"],
        country=program["country"],
        status=status,
        met=met,
        failed=failed,
        unknown=unknown,
        what=program["what"],
        amount=program["amount"],
        next_step=program["next_step"],
        apply_url=program["apply_url"],
        status_url=program["status_url"],
        reference=program["reference"],
        last_verified=program["last_verified"],
        stale=(today - verified).days > STALE_DAYS,
        notes=program.get("notes", ""),
    )


def render_glyph(door: Door) -> str:
    """The compact status block the skill shows verbatim: head, met, failed, unknown, first question, amount, live date, staleness."""
    lines = [f"{HEAD[door.status]}  {door.name}"]
    lines += [f"●  {label}" for label in door.met]
    lines += [f"×  {label}" for label in door.failed]
    lines += [f"○  {item['label']}" for item in door.unknown]
    first_question = next((item["question"] for item in door.unknown if item.get("question")), None)
    if first_question:
        lines.append(f"?  {first_question}")
    lines.append(f"→  {door.amount['text']}")
    if door.live and door.live.get("closes"):
        lines.append(f"→  Round closes {str(door.live['closes'])[:16].replace('T', ' ')}")
    if door.stale:
        lines.append(f"→  Last verified {door.last_verified}, read the status page before quoting")
    return "\n".join(lines)


def rank(doors: list[Door]) -> list[Door]:
    """Eligible first, then unknown with the fewest open questions, then blocked. Ties keep data-file order."""
    return sorted(doors, key=lambda door: (RANK[door.status], len(door.unknown)))


def run(
    raw_profile: dict,
    programs: list[dict],
    today: date,
    include_all: bool = False,
    live_fetch: Callable[[str], dict | None] | None = None,
) -> dict:
    profile, warnings = normalize_profile(raw_profile)
    doors: list[Door] = []
    for program in programs:
        if not is_relevant(program, profile):
            continue
        door = evaluate(program, profile, today)
        if door.status == "blocked" and not include_all:
            continue
        live = program.get("live")
        if live_fetch is not None and live and live.get("source") == "vinnova":
            try:
                door.live = live_fetch(live["call_id"])
            except Exception as exc:  # the boundary: a dead API must not hide the other doors
                door.live = {"error": str(exc)}
        door.glyph = render_glyph(door)
        doors.append(door)
    ranked = rank(doors)
    return {
        "profile": profile,
        "warnings": warnings,
        "stale": [door.id for door in ranked if door.stale],
        "doors": [asdict(door) for door in ranked],
    }


def main(argv: list[str] | None = None, stdin: TextIO | None = None) -> int:
    parser = argparse.ArgumentParser(description="Match a founder profile (JSON on stdin) against the program data.")
    parser.add_argument("--all", action="store_true", help="include blocked doors")
    parser.add_argument("--live", action="store_true", help="ask live sources (the Vinnova API) for round dates")
    parser.add_argument("--programs", type=Path, default=PROGRAMS_PATH, help="path to programs.json")
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="override today's date, YYYY-MM-DD")
    args = parser.parse_args(argv)
    source = stdin if stdin is not None else sys.stdin
    try:
        raw = json.load(source)
    except json.JSONDecodeError as exc:
        print(f"profile is not valid JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(raw, dict):
        print("profile must be a JSON object", file=sys.stderr)
        return 2
    programs = json.loads(args.programs.read_text(encoding="utf-8"))["programs"]
    live_fetch: Callable[[str], dict | None] | None = None
    if args.live:
        now = datetime.now(timezone.utc)

        def fetch_round(call_id: str) -> dict | None:
            found = vinnova_api.open_round(call_id, now)
            return found.to_dict() if found else None

        live_fetch = fetch_round
    result = run(raw, programs, args.today or date.today(), include_all=args.all, live_fetch=live_fetch)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
