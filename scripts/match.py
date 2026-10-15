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
import math
import re
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

NUMERIC_FIELDS = {"age_years", "employees", "revenue_msek", "balance_msek", "revenue_meur", "balance_meur", "funding_raised_usd"}
INTEGER_FIELDS = {"employees"}
BOOLEAN_FIELDS = {"vc_backed", "has_vat", "has_employment", "has_work_email", "has_website", "has_developer", "workload_defined", "profit_distributed"}
LIST_FIELDS = {"stack", "sector", "vc_partner", "need"}
TRUE_WORDS = {"true", "yes", "ja", "y", "1"}
FALSE_WORDS = {"false", "no", "nej", "n", "0"}
NEEDS = {"money", "compute", "credits"}
STAGES = {"idea", "pre_seed", "seed", "series_a", "later"}
LEGAL_FORMS = {"company", "nonprofit", "academia", "public", "sole_trader", "none"}
# Alias tables are keyed by slug(): lowercase, spaces and hyphens as underscores.
COUNTRY_ALIASES = {
    "sweden": "SE", "sverige": "SE", "finland": "FI", "suomi": "FI", "norway": "NO", "norge": "NO",
    "denmark": "DK", "danmark": "DK", "iceland": "IS", "island": "IS", "ísland": "IS",
}
STACK_ALIASES = {
    "claude": "anthropic", "chatgpt": "openai", "google": "gcp", "google_cloud": "gcp", "gcloud": "gcp",
    "microsoft": "azure", "hf": "huggingface", "hugging_face": "huggingface", "amazon": "aws",
}
SECTOR_ALIASES = {
    "deep_tech": "deeptech", "ml": "ai", "ai_ml": "ai", "cleantech": "climate", "climatetech": "climate",
    "climate_tech": "climate", "klimat": "climate", "healthtech": "health", "medtech": "health",
    "life_science": "health", "lifescience": "health", "hälsa": "health", "energi": "energy", "fin_tech": "fintech",
}
NEED_ALIASES = {
    "gpu": "compute", "hpc": "compute", "gpu_hours": "compute", "gpu_timmar": "compute", "compute_hours": "compute",
    "beräkning": "compute", "funding": "money", "grant": "money", "grants": "money", "loan": "money", "loans": "money",
    "bidrag": "money", "pengar": "money", "lån": "money", "investment": "money", "credit": "credits",
    "krediter": "credits", "cloud_credits": "credits", "api_credits": "credits",
}
STAGE_ALIASES = {
    "preseed": "pre_seed", "pre": "pre_seed", "angel": "pre_seed", "mvp": "pre_seed", "prototype": "pre_seed",
    "concept": "idea", "a": "series_a", "series_b": "later", "series_c": "later", "series_d": "later",
    "growth": "later", "scaleup": "later", "late": "later",
}
LEGAL_FORM_ALIASES = {
    "ab": "company", "as": "company", "oy": "company", "aps": "company", "a/s": "company", "ehf": "company",
    "ltd": "company", "gmbh": "company", "inc": "company", "llc": "company", "aktiebolag": "company",
    "bolag": "company", "startup": "company", "sme": "company", "osakeyhtiö": "company",
    "ideell_forening": "nonprofit", "ideell_förening": "nonprofit", "förening": "nonprofit", "forening": "nonprofit",
    "stiftelse": "nonprofit", "foundation": "nonprofit", "ngo": "nonprofit",
    "university": "academia", "universitet": "academia", "research": "academia", "academic": "academia", "institute": "academia",
    "public_sector": "public", "offentlig": "public", "municipality": "public", "kommun": "public",
    "enskild_firma": "sole_trader", "sole": "sole_trader", "enk": "sole_trader",
    "individual": "none", "person": "none", "no_company": "none",
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
    availability: str = "unknown"
    live: dict | None = None
    glyph: str = ""


def slug(value: object) -> str:
    """Lowercase, trimmed, spaces and hyphens as underscores: the key form every alias table uses."""
    return re.sub(r"[\s\-]+", "_", str(value).strip().lower())


def to_number(value: object) -> float | None:
    """A finite float, or None. 'nan', 'inf' and 1e999 parse as floats, but no cap can be checked against them."""
    if isinstance(value, bool):
        return None
    number: float | None = None
    if isinstance(value, (int, float)):
        number = float(value)
    elif isinstance(value, str):
        try:
            number = float(value.replace(",", ".").replace(" ", ""))
        except ValueError:
            return None
    if number is None or not math.isfinite(number):
        return None
    return number


def to_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        word = value.strip().lower()
        if word in TRUE_WORDS:
            return True
        if word in FALSE_WORDS:
            return False
    return None


def split_list(value: object) -> list[str]:
    """A list, or a string split on commas, semicolons and slashes; empty and None items dropped."""
    items = value if isinstance(value, list) else re.split(r"[,;/]", str(value))
    return [str(item).strip() for item in items if item is not None and str(item).strip()]


def normalize_legal_form(value: object) -> str | None:
    """Accept the enum, an alias, or an abbreviation in parentheses such as 'Aktiebolag (AB)'."""
    word = slug(value)
    inside = re.findall(r"\(([^)]*)\)", word)
    outside = re.sub(r"\([^)]*\)", "", word)
    for candidate in [word, *inside, *re.split(r"[_/]+", outside)]:
        candidate = candidate.strip("_")
        if candidate in LEGAL_FORMS:
            return candidate
        if candidate in LEGAL_FORM_ALIASES:
            return LEGAL_FORM_ALIASES[candidate]
    return None


def normalize_profile(raw: dict) -> tuple[dict, list[str]]:
    """Alias and coerce every field; drop what cannot be read and say so in warnings.

    A value that is dropped becomes unknown, which makes the matcher ask the
    founder. A value that is silently kept in the wrong shape would instead
    fail every rule and hide the door, so every drop carries a warning.
    """
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
        elif key == "need":
            words: list[str] = []
            for item in split_list(value):
                word = NEED_ALIASES.get(slug(item), slug(item))
                if word in NEEDS:
                    words.append(word)
                else:
                    warnings.append(f"need {item!r} is not money, compute or credits, ignored")
            if words:
                profile[key] = list(dict.fromkeys(words))
        elif key in LIST_FIELDS:
            words = [slug(item) for item in split_list(value)]
            if key == "stack":
                words = [STACK_ALIASES.get(word, word) for word in words]
            if key == "sector":
                words = [SECTOR_ALIASES.get(word, word) for word in words]
            profile[key] = list(dict.fromkeys(words))
        elif key == "country":
            code = str(value).strip()
            code = COUNTRY_ALIASES.get(code.lower(), code.upper())
            if re.fullmatch(r"[A-Z]{2}", code):
                profile[key] = code
            else:
                warnings.append(f"country {value!r} is not an ISO-2 code, treated as unknown")
        elif key == "legal_form":
            form = normalize_legal_form(value)
            if form is None:
                warnings.append(f"legal_form {value!r} is not recognised, treated as unknown")
            else:
                profile[key] = form
        elif key == "stage":
            word = STAGE_ALIASES.get(slug(value), slug(value))
            if word in STAGES:
                profile[key] = word
            else:
                warnings.append(f"stage {value!r} is not idea, pre_seed, seed, series_a or later, treated as unknown")
        elif key == "lang":
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


def mentions_country(program: dict) -> bool:
    for gate in program["eligibility"]:
        members = gate["any"] if "any" in gate else [gate]
        if any(member.get("field") == "country" for member in members):
            return True
    return False


def evaluate(program: dict, profile: dict, today: date) -> Door:
    results = [evaluate_rule(rule, profile) for rule in program["eligibility"]]
    if program["country"] != "global" and profile.get("country") is None and not mentions_country(program):
        # An EU door has no country rule because relevance handles the set; with no
        # country at all it must still ask rather than read as eligible.
        results.insert(0, RuleResult("unknown", "eligible country", "In which country is the company registered?"))
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
        availability=str(program.get("availability", "unknown")),
    )


def render_glyph(door: Door) -> str:
    """The compact status block the skill shows verbatim: head, met, failed, unknown, first question, amount, live date, closed note, staleness."""
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
    if door.availability == "closed":
        lines.append(f"→  Closed when verified {door.last_verified}; read the status page for the next round")
    if door.stale:
        lines.append(f"→  Last verified {door.last_verified}, read the status page before quoting")
    return "\n".join(lines)


def rank(doors: list[Door]) -> list[Door]:
    """Open doors first: eligible, then unknown with the fewest open questions, then blocked. Closed doors last. Ties keep data-file order."""
    return sorted(doors, key=lambda door: (door.availability == "closed", RANK[door.status], len(door.unknown)))


class MalformedRecord(ValueError):
    """A record the matcher cannot evaluate. The message names the record and what is wrong with it."""


def describe_malformed(program: object, index: int, exc: Exception) -> str:
    ident = program["id"] if isinstance(program, dict) and isinstance(program.get("id"), str) else f"programs[{index}]"
    if isinstance(exc, KeyError):
        return f"record {ident} has no field {exc.args[0]!r}"
    return f"record {ident} cannot be evaluated: {exc}"


def build_door(
    program: dict,
    profile: dict,
    today: date,
    include_all: bool,
    live_fetch: Callable[[str], dict | None] | None,
) -> Door | None:
    """The door for one record, or None when the record is irrelevant to the profile or blocked and hidden."""
    if not is_relevant(program, profile):
        return None
    door = evaluate(program, profile, today)
    if door.status == "blocked" and not include_all:
        return None
    live = program.get("live")
    if live_fetch is not None and live and live.get("source") == "vinnova":
        try:
            door.live = live_fetch(live["call_id"])
        except Exception as exc:  # the boundary: a dead API must not hide the other doors
            door.live = {"error": str(exc)}
    door.glyph = render_glyph(door)
    return door


def run(
    raw_profile: dict,
    programs: list[dict],
    today: date,
    include_all: bool = False,
    live_fetch: Callable[[str], dict | None] | None = None,
) -> dict:
    """Raises MalformedRecord when a record lacks a field or holds a value the rules cannot read."""
    profile, warnings = normalize_profile(raw_profile)
    doors: list[Door] = []
    for index, program in enumerate(programs):
        try:
            door = build_door(program, profile, today, include_all, live_fetch)
        except (KeyError, TypeError, ValueError) as exc:
            raise MalformedRecord(describe_malformed(program, index, exc)) from exc
        if door is not None:
            doors.append(door)
    ranked = rank(doors)
    return {
        "profile": profile,
        "warnings": warnings,
        "stale": [door.id for door in ranked if door.stale],
        "doors": [asdict(door) for door in ranked],
    }


def load_programs(path: Path) -> list[dict]:
    """The records of a programs file. Raises ValueError with the one-line reason main prints instead of a traceback."""
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read programs file {path}: {exc.strerror or exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"programs file {path} is not valid JSON: {exc}") from exc
    records = document.get("programs") if isinstance(document, dict) else None
    if not isinstance(records, list):
        raise ValueError(f"programs file {path} must be an object with a 'programs' list")
    return records


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
    live_fetch: Callable[[str], dict | None] | None = None
    if args.live:
        now = datetime.now(timezone.utc)

        def fetch_round(call_id: str) -> dict | None:
            found = vinnova_api.open_round(call_id, now)
            return found.to_dict() if found else None

        live_fetch = fetch_round
    try:
        programs = load_programs(args.programs)
        result = run(raw, programs, args.today or date.today(), include_all=args.all, live_fetch=live_fetch)
    except ValueError as exc:  # unreadable file, wrong shape, or a MalformedRecord: one line, no traceback
        print(str(exc), file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
