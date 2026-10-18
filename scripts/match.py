#!/usr/bin/env python3
"""Match a founder profile against data/programs.json. Standard library only.

    python3 scripts/match.py [--all] [--live] [--top N] [--programs PATH] [--today YYYY-MM-DD] < profile.json

A door is eligible when every rule is met, blocked when any rule failed, and
unknown otherwise. A field that is absent from the profile is unknown, never
defaulted: the skill asks the founder instead of guessing, because a guessed
country or headcount produces a confident wrong answer. Blocked doors are
hidden unless --all is given. Records whose last_verified is older than
STALE_DAYS are flagged so the skill re-reads the page before quoting them.

Labels and questions are generated from each rule's field, op and value in the
founder's language (profile.lang: en, sv, fi, no, da), so the glyph says exactly
what was checked. Doors that share a group and the same open questions collapse
into one door with the siblings listed under "also". The first --top doors are
returned in full; the rest are listed under "more" by name, so the founder is
not buried. Doors blocked only by legal form are reported under "unlocks", so a
founder without a company hears what registering one would open.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Callable
from dataclasses import asdict, dataclass, field as dc_field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import TextIO

import i18n
import vinnova_api

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS_PATH = ROOT / "data" / "programs.json"
STALE_DAYS = 90
DEFAULT_TOP = 3

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

NUMERIC_FIELDS = {
    "age_years", "employees", "revenue_msek", "balance_msek", "revenue_meur", "balance_meur", "funding_raised_usd", "need_eur",
    "owner_company_share", "paid_staff", "de_minimis_eur",
}
INTEGER_FIELDS = {"employees", "paid_staff"}
BOOLEAN_FIELDS = {
    "vc_backed", "has_vat", "has_employment", "has_work_email", "has_website", "has_developer", "workload_defined", "profit_distributed",
    "fulltime_in_company", "founder_employed_elsewhere", "lost_half_capital", "work_started", "on_market",
}
GRANT_FIELDS = {"prior_grants", "active_grants"}
# Program ids or funder prefixes ("vinnova", "rannis") the founder named; hyphenated like grant keys.
KEY_FIELDS = GRANT_FIELDS | {"named"}
LIST_FIELDS = {"stack", "sector", "vc_partner", "need", "confirmed", "denied"} | KEY_FIELDS
# Words a founder uses for "none" when asked which grants they hold: an empty list, which is an answer.
NO_GRANT_WORDS = {"none", "no", "nej", "inga", "ingen", "ei", "nei", "ingen_tidligere", "-"}
# Fields with a fixed set of values, keyed by the words founders use for them.
ENUM_FIELDS: dict[str, dict[str, str]] = {
    "affiliation": {
        "student": "student", "studerande": "student", "studerende": "student", "opiskelija": "student", "student_at_university": "student",
        "researcher": "researcher", "forskare": "researcher", "forsker": "researcher", "tutkija": "researcher",
        "postdoc": "researcher", "phd": "researcher", "doktorand": "researcher", "phd_student": "researcher",
        "staff": "staff", "university_staff": "staff", "none": "none", "ingen": "none", "no": "none", "nej": "none",
    },
    # "Anonymised" is deliberately missing: it is what founders call data the source can
    # still re-link (round 3, s15). Only the answer to the screen question sets this field.
    "personal_data": {
        "none": "none", "no": "none", "ingen": "none", "no_personal_data": "none",
        "anonymous": "anonymous", "truly_anonymous": "anonymous", "irreversibly_anonymous": "anonymous",
        "pseudonymised": "pseudonymised", "pseudonymized": "pseudonymised", "pseudonymiserad": "pseudonymised", "coded": "pseudonymised",
        "identifiable": "identifiable", "personal": "identifiable", "personal_data": "identifiable",
    },
}
CLAIMED_ANONYMOUS = {"anonymised", "anonymized", "anonymiserad", "anonymiseret", "anonymisert", "anonymisoitu"}
# Facts about the founder's own situation, grouped into the topics the first answer asks
# about. Each round-3 loss turned on one of them, and no search for programs reveals
# them: who owns the company, which grants it holds, whether the founder works
# elsewhere, studies, or trains on data that is really anonymous.
SITUATION_TOPICS: dict[str, tuple[str, ...]] = {
    "ownership": ("owner_company_share",),
    "grants": ("prior_grants", "active_grants", "de_minimis_eur"),
    "work": ("founder_employed_elsewhere", "fulltime_in_company"),
    "affiliation": ("affiliation",),
    "data": ("personal_data",),
    "finances": ("lost_half_capital",),
    "timing": ("work_started", "on_market"),
    "staff": ("paid_staff",),
}
# Ties in the screen go to the trap that cost most in round 3.
SITUATION_ORDER = tuple(SITUATION_TOPICS)
FIELD_TOPIC: dict[str, str] = {field: topic for topic, fields in SITUATION_TOPICS.items() for field in fields}
# Confirmations that follow up a situation answer: a firm more than 25% owned by another
# company can still be an SME if the group's figures are within the limits.
CONFIRMATION_TOPIC: dict[str, str] = {
    "group_within_sme_limits": "ownership", "group_within_small_enterprise_limits": "ownership",
    "group_unlisted_within_10msek": "ownership", "owners_all_natural_persons": "ownership",
    "owner_is_founders_own_holding": "ownership", "separate_from_owner_operations": "ownership",
    "each_founder_owns_12_5_percent": "ownership", "equity_majority_eu_efta_uk": "ownership",
    "eic_running_grant_only_applying_blended": "grants", "no_earlier_bf_funding_same_solution": "grants",
    "business_not_yet_fulltime": "work", "fulltime_team_member": "work", "project_lead_employed": "staff",
}
SITUATION_FIELDS = set(FIELD_TOPIC)
SCREEN_MAX = 3
SCREEN_DOORS = 8
# Routes the first answer maps before going deep on one door. A record may set its own
# route (tax relief is paid as a grant-like deduction, not applied for as one).
ROUTES = ("grant", "tax", "loan", "compute", "credits", "equity", "support")
KIND_ROUTE: dict[str, str] = {
    "grant": "grant", "loan": "loan", "compute": "compute", "cloud_credit": "credits", "ai_api_credit": "credits",
    "perks": "credits", "accelerator": "support",
}
ROUTE_DOORS = 3
# The order routes appear in: the founder's needs in the order they gave them, the money
# routes from what the founder keeps to what it costs. Ordering by the best door's rank put
# a payroll-tax deduction first for a webshop with no payroll, and the founder picks the
# first door listed.
NEED_ROUTES: dict[str, tuple[str, ...]] = {
    "money": ("grant", "tax", "loan", "equity"), "compute": ("compute",), "credits": ("credits",), "support": ("support",),
}
# A project can usually be defined to start after the application, so "already started"
# closes fewer doors than it gates; it should not crowd out ownership or grants held.
# Losing half the share capital closes doors too, but it is a formality the application checks,
# not a fact about the founder that changes which route to take.
TOPIC_WEIGHT: dict[str, float] = {"timing": 0.5, "finances": 0.5}
# A door the founder named weighs as two best doors: "can we get Innobooster?" should screen
# for Innobooster's traps before anything else.
NAMED_WEIGHT = 2
# Basic company facts the first answer may need before any trap: one slot at most.
BASIC_FIELDS = ("legal_form", "age_years")
COUNTRY_FIELDS = {"country", "residence_country"}
TRUE_WORDS = {"true", "yes", "ja", "y", "1", "kyllä", "joo"}
FALSE_WORDS = {"false", "no", "nej", "n", "0", "nei", "ei"}
NEEDS = {"money", "compute", "credits", "support"}
STAGES = {"idea", "pre_seed", "seed", "series_a", "later"}
LEGAL_FORMS = {"company", "nonprofit", "academia", "public", "sole_trader", "none"}
# Alias tables are keyed by slug(): lowercase, spaces and hyphens as underscores.
COUNTRY_ALIASES = {
    "sweden": "SE", "sverige": "SE", "ruotsi": "SE", "finland": "FI", "suomi": "FI", "norway": "NO", "norge": "NO",
    "norja": "NO", "denmark": "DK", "danmark": "DK", "tanska": "DK", "iceland": "IS", "island": "IS", "ísland": "IS",
    "islanti": "IS",
}
STACK_ALIASES = {
    "claude": "anthropic", "chatgpt": "openai", "google": "gcp", "google_cloud": "gcp", "gcloud": "gcp",
    "microsoft": "azure", "hf": "huggingface", "hugging_face": "huggingface", "amazon": "aws",
}
SECTOR_ALIASES = {
    "deep_tech": "deeptech", "ml": "ai", "ai_ml": "ai", "ki": "ai", "tekoäly": "ai", "cleantech": "climate",
    "climatetech": "climate", "climate_tech": "climate", "klimat": "climate", "klima": "climate", "ilmasto": "climate",
    "healthtech": "health", "medtech": "health", "life_science": "health", "lifescience": "health", "hälsa": "health",
    "healthcare": "health", "medical": "health", "medicine": "health", "radiology": "health", "medical_imaging": "health",
    "diagnostics": "health", "digital_health": "health", "e_health": "health", "vård": "health", "sjukvård": "health",
    "medicin": "health", "terveysteknologia": "health", "sundhedsteknologi": "health", "helseteknologi": "health",
    "helse": "health", "sundhed": "health", "terveys": "health", "energi": "energy", "energia": "energy", "fin_tech": "fintech",
    "logistics": "transport", "logistik": "transport", "logistikk": "transport", "logistiikka": "transport",
    "trucking": "transport", "road_transport": "transport", "mobility": "transport", "chips": "semiconductors",
    "semiconductor": "semiconductors", "halvledare": "semiconductors", "ocean": "marine", "maritime": "marine",
    "hav": "marine", "aquaculture": "marine", "havbruk": "marine", "fiskeoppdrett": "marine",
    "agritech": "agriculture", "agtech": "agriculture", "agri": "agriculture", "farming": "agriculture",
    "jordbruk": "agriculture", "lantbruk": "agriculture", "trädgård": "agriculture", "rennäring": "agriculture",
    "landbruk": "agriculture", "landbrug": "agriculture", "maatalous": "agriculture",
    "defense": "defence", "försvar": "defence", "forsvar": "defence", "puolustus": "defence", "military": "defence",
    "dual_use": "defence",
}
NEED_ALIASES = {
    "gpu": "compute", "hpc": "compute", "gpu_hours": "compute", "gpu_timmar": "compute", "gpu_timer": "compute",
    "gpu_tunnit": "compute", "compute_hours": "compute", "beräkning": "compute", "funding": "money", "grant": "money",
    "grants": "money", "loan": "money", "loans": "money", "bidrag": "money", "pengar": "money", "penger": "money",
    "penge": "money", "rahaa": "money", "rahoitus": "money", "tilskudd": "money", "tilskud": "money", "lån": "money",
    "laina": "money", "investment": "money", "credit": "credits", "krediter": "credits", "kreditter": "credits",
    "krediitit": "credits", "cloud_credits": "credits", "api_credits": "credits",
    "coaching": "support", "mentoring": "support", "stöd": "support", "incubator": "support", "inkubator": "support",
    "accelerator": "support", "accelerator_program": "support",
}
STAGE_ALIASES = {
    "preseed": "pre_seed", "pre": "pre_seed", "angel": "pre_seed", "mvp": "pre_seed", "prototype": "pre_seed",
    "concept": "idea", "idé": "idea", "a": "series_a", "series_b": "later", "series_c": "later", "series_d": "later",
    "growth": "later", "scaleup": "later", "late": "later",
}
LEGAL_FORM_ALIASES = {
    "ab": "company", "as": "company", "oy": "company", "aps": "company", "a/s": "company", "ehf": "company",
    "ltd": "company", "gmbh": "company", "inc": "company", "llc": "company", "aktiebolag": "company",
    "aksjeselskap": "company", "osakeyhtiö": "company", "anpartsselskab": "company", "aktieselskab": "company",
    "bolag": "company", "selskap": "company", "selskab": "company", "yhtiö": "company", "startup": "company", "sme": "company",
    "ideell_forening": "nonprofit", "ideell_förening": "nonprofit", "förening": "nonprofit", "forening": "nonprofit",
    "stiftelse": "nonprofit", "foundation": "nonprofit", "ngo": "nonprofit", "yhdistys": "nonprofit",
    "university": "academia", "universitet": "academia", "yliopisto": "academia", "research": "academia",
    "academic": "academia", "institute": "academia",
    "public_sector": "public", "offentlig": "public", "municipality": "public", "kommun": "public", "kommune": "public",
    "kunta": "public",
    "ekonomisk_förening": "company", "cooperative": "company", "kooperativ": "company", "osuuskunta": "company",
    "andelslag": "company", "samvirkelag": "company", "andelsselskab": "company",
    "enskild_firma": "sole_trader", "sole": "sole_trader", "enk": "sole_trader", "enkeltpersonforetak": "sole_trader",
    "toiminimi": "sole_trader", "enkeltmandsvirksomhed": "sole_trader",
    "individual": "none", "person": "none", "no_company": "none", "inget_bolag": "none", "ei_yhtiötä": "none",
}
HEAD = {"eligible": "●", "unknown": "◐", "blocked": "×"}
RANK = {"eligible": 0, "unknown": 1, "blocked": 2}


@dataclass(frozen=True)
class RuleResult:
    status: str
    label: str
    question: str | None
    field: str | None = None


@dataclass
class Door:
    id: str
    name: str
    kind: str
    need: list[str]
    country: str
    status: str
    met: list[str]
    failed: list[str]
    unknown: list[dict]
    apply_requirements: list[str]
    unclear: list[str]
    before_apply: list[str]
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
    group: str | None = None
    home_country: str | None = None
    foreign: bool = False
    founder_cost: str = "none"
    stage_mismatch: bool = False
    topic_mismatch: bool = False
    topic_match: bool = False
    undersized: bool = False
    also: list[dict] = dc_field(default_factory=list)
    situation: list[str] = dc_field(default_factory=list)
    route: str = "grant"
    application: dict | None = None
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


def normalize_country(value: object) -> str | None:
    code = str(value).strip()
    code = COUNTRY_ALIASES.get(code.lower(), code.upper())
    return code if re.fullmatch(r"[A-Z]{2}", code) else None


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
                    warnings.append(f"need {item!r} is not money, compute, credits or support, ignored")
            if words:
                profile[key] = list(dict.fromkeys(words))
        elif key in KEY_FIELDS:
            # Grant keys are program ids, which use hyphens; slug() would turn them into underscores.
            keys = [re.sub(r"[\s_]+", "-", item.lower()) for item in split_list(value)]
            profile[key] = list(dict.fromkeys(grant for grant in keys if slug(grant) not in NO_GRANT_WORDS))
        elif key in LIST_FIELDS:
            words = [slug(item) for item in split_list(value)]
            if key == "stack":
                words = [STACK_ALIASES.get(word, word) for word in words]
            if key == "sector":
                words = [SECTOR_ALIASES.get(word, word) for word in words]
            profile[key] = list(dict.fromkeys(words))
        elif key in COUNTRY_FIELDS:
            code = normalize_country(value)
            if code is None:
                warnings.append(f"{key} {value!r} is not an ISO-2 code, treated as unknown")
            else:
                profile[key] = code
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
        elif key in ENUM_FIELDS:
            enum_value = ENUM_FIELDS[key].get(slug(value))
            if key == "personal_data" and slug(value) in CLAIMED_ANONYMOUS:
                profile["personal_data_claim"] = slug(value)
                warnings.append(
                    "personal_data 'anonymised' is the founder's word, not a fact: ask whether anyone, the data source "
                    "included, can link a record to a person, then record anonymous, pseudonymised or identifiable"
                )
                continue
            if enum_value is None:
                warnings.append(f"{key} {value!r} is not one of {sorted(set(ENUM_FIELDS[key].values()))}, treated as unknown")
            else:
                profile[key] = enum_value
        elif key == "lang":
            profile[key] = i18n.pick_lang(value)
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
    if op == "excludes":
        # A list the founder gave, possibly empty, holding none of the values: "no earlier Sprint or Tempo".
        return isinstance(actual, list) and isinstance(expected, list) and not set(actual) & set(expected)
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


def evaluate_rule(rule: dict, profile: dict, lang: str = i18n.DEFAULT_LANG) -> RuleResult:
    """A rule is met, failed or unknown. A group is met if any member is met, failed only when every member is known and failed.

    The label and question come from the rule itself, in the founder's language,
    never from free text in the data file.
    """
    if "any" in rule:
        results = [evaluate_rule(member, profile, lang) for member in rule["any"]]
        label = i18n.group_label(rule["any"], lang)
        if any(result.status == "met" for result in results):
            return RuleResult("met", label, None)
        if all(result.status == "failed" for result in results):
            return RuleResult("failed", label, None)
        question = next((result.question for result in results if result.status == "unknown"), None)
        return RuleResult("unknown", label, question)
    label = i18n.rule_label(rule, lang)
    if rule["field"] == "confirmed" and rule["op"] == "contains":
        # A founder confirms a requirement in words or says no to it. Not mentioning
        # it is neither: confirming one key must not fail every other confirmation.
        if rule["value"] in (profile.get("denied") or []):
            return RuleResult("failed", label, None, "confirmed")
        if rule["value"] in (profile.get("confirmed") or []):
            return RuleResult("met", label, None, "confirmed")
        return RuleResult("unknown", label, i18n.rule_question(rule, lang), "confirmed")
    actual = profile.get(rule["field"])
    if actual is None:
        return RuleResult("unknown", label, i18n.rule_question(rule, lang), rule["field"])
    status = "met" if compare(rule["op"], actual, rule["value"]) else "failed"
    return RuleResult(status, label, None, rule["field"])


def profile_countries(profile: dict) -> set[str]:
    return {profile[key] for key in COUNTRY_FIELDS if profile.get(key)}


def is_relevant(program: dict, profile: dict) -> bool:
    """Need must overlap when given. Country must match when given, by registration or by residence: ISO-2 exactly, EU by the associated set, global always.

    A founder who lives in Denmark with a Swedish company sees both countries'
    doors; the rules then say which one each door needs.
    """
    need = profile.get("need")
    if need and not set(need) & set(program["need"]):
        return False
    countries = profile_countries(profile)
    scope = program["country"]
    if not countries or scope == "global":
        return True
    if scope == "EU":
        return bool(countries & EU_ASSOCIATED)
    return scope in countries


def mentions_country(program: dict) -> bool:
    for gate in program["eligibility"]:
        members = gate["any"] if "any" in gate else [gate]
        if any(member.get("field") in COUNTRY_FIELDS for member in members):
            return True
    return False


def rule_fields(gate: dict) -> set[str]:
    members = gate["any"] if "any" in gate else [gate]
    return {member["field"] for member in members}


def member_topic(member: dict, profile: dict) -> str | None:
    """The situation topic of one rule the profile leaves open, or None."""
    field = member["field"]
    if field == "confirmed":
        key = member["value"]
        answered = key in (profile.get("confirmed") or []) or key in (profile.get("denied") or [])
        return None if answered else CONFIRMATION_TOPIC.get(key)
    return FIELD_TOPIC.get(field) if profile.get(field) is None else None


def gate_topic(gate: dict, profile: dict) -> str | None:
    """The situation topic that keeps an open gate open, if any: the first member the founder's situation answers."""
    members = gate.get("any", [gate])
    return next((topic for topic in (member_topic(member, profile) for member in members) if topic), None)


def program_route(program: dict) -> str:
    """The route a door belongs to on the map: the record's own, else derived from kind and what it costs the founder."""
    if program.get("route"):
        return str(program["route"])
    if program.get("founder_cost") == "equity":
        return "equity"
    return KIND_ROUTE.get(program["kind"], "support")


def evaluate(program: dict, profile: dict, today: date, lang: str) -> Door:
    results = [evaluate_rule(rule, profile, lang) for rule in program["eligibility"]]
    if program["country"] != "global" and not profile_countries(profile) and not mentions_country(program):
        # An EU door has no country rule because relevance handles the set; with no
        # country at all it must still ask rather than read as eligible.
        country_rule = {"field": "country", "op": "eq", "value": program["country"]}
        results.insert(0, RuleResult("unknown", i18n.rule_label(country_rule, lang), i18n.rule_question(country_rule, lang), "country"))
    topics: list[str | None] = [gate_topic(rule, profile) for rule in program["eligibility"]]
    if len(results) > len(topics):
        topics.insert(0, None)
    met = [result.label for result in results if result.status == "met"]
    failed = [result.label for result in results if result.status == "failed"]
    unknown = [
        {"label": result.label, "question": result.question, "situation": topic, "field": result.field}
        for result, topic in zip(results, topics)
        if result.status == "unknown"
    ]
    status = "blocked" if failed else "eligible" if not unknown else "unknown"
    verified = date.fromisoformat(program["last_verified"])
    apply_requirements = list(program.get("apply_requirements") or [])
    return Door(
        id=program["id"],
        name=program["name"],
        kind=program["kind"],
        need=list(program["need"]),
        country=program["country"],
        status=status,
        met=met,
        failed=failed,
        unknown=unknown,
        apply_requirements=apply_requirements,
        unclear=list(program.get("unclear") or []),
        before_apply=[item["label"] for item in unknown] + apply_requirements,
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
        group=program.get("group"),
        home_country=program.get("home_country"),
        founder_cost=str(program.get("founder_cost", "none")),
        stage_mismatch=stage_mismatch(program, profile),
        topic_mismatch=topic_mismatch(program, profile),
        topic_match=bool(set(program.get("sectors") or []) & set(profile.get("sector") or [])),
        undersized=undersized(program, profile),
        situation=list(dict.fromkeys(item["situation"] for item in unknown if item["situation"])),
        route=program_route(program),
        foreign=bool(program.get("home_country")) and bool(profile_countries(profile)) and program.get("home_country") not in profile_countries(profile),
        application=program.get("application"),
    )


def render_glyph(door: Door, lang: str) -> str:
    """The compact status block the skill shows verbatim: head, met, failed, unknown, first question, amount, siblings, live date, closed note, staleness."""
    lines = [f"{HEAD[door.status]}  {door.name}"]
    lines += [f"●  {label}" for label in door.met]
    lines += [f"×  {label}" for label in door.failed]
    lines += [f"○  {item['label']}" for item in door.unknown]
    # The screen asks the situation questions for all doors at once; the door's own line asks the rest first.
    asked = sorted(door.unknown, key=lambda item: bool(item.get("situation")))
    first_question = next((item["question"] for item in asked if item.get("question")), None)
    if first_question:
        lines.append(f"?  {first_question}")
    lines.append(f"→  {door.amount['text']}")
    if door.also:
        parts = []
        for sib in door.also:
            extra = f"; {i18n.phrase('also_needs', lang)} {', '.join(sib['extra'])}" if sib.get("extra") else ""
            parts.append(f"{sib['name']} ({sib['amount']}{extra})")
        lines.append("→  " + i18n.phrase("also", lang, list="; ".join(parts)))
    if door.live and door.live.get("closes"):
        lines.append("→  " + i18n.phrase("round_closes", lang, date=str(door.live["closes"])[:16].replace("T", " ")))
    if door.availability == "closed":
        lines.append("→  " + i18n.phrase("closed_when_verified", lang, date=door.last_verified))
    if door.stale:
        lines.append("→  " + i18n.phrase("stale", lang, date=door.last_verified))
    return "\n".join(lines)


# What taking the money costs the founder. A grant ranks before a loan, a loan
# before an equity investment, and anything with a fee last: two founders who
# ask "is there money for us" should see the money they keep first.
COST_RANK: dict[str, int] = {"none": 0, "repay": 1, "equity": 2, "fee": 3}


def founder_stage(profile: dict) -> str | None:
    """The founder's stage, or idea when they have no company and gave no stage."""
    stage = profile.get("stage")
    if stage in STAGES:
        return str(stage)
    if profile.get("legal_form") == "none":
        return "idea"
    return None


def stage_mismatch(program: dict, profile: dict) -> bool:
    """True when the program lists the stages it serves and the founder's known stage is not one of them.

    An EU scale-up grant is formally open to two people with an idea, but
    leading their answer with it sends them to the wrong door.
    """
    stages = program.get("stages")
    stage = founder_stage(profile)
    return bool(stages) and stage is not None and stage not in stages


def topic_mismatch(program: dict, profile: dict) -> bool:
    """True for a call tied to sectors the founder has not said they work in.

    A Vinnova challenge on Baltic marine monitoring is open to any Swedish
    company, but it should not lead an answer to a logistics founder, or to a
    founder whose sector is unknown.
    """
    sectors = program.get("sectors")
    if not sectors:
        return False
    return not set(sectors) & set(profile.get("sector") or [])


# Rough EUR value of one unit of each currency in the data. Used only to order
# doors by how much of the founder's stated need they can pay, never shown.
EUR_PER_UNIT: dict[str, float] = {"EUR": 1.0, "SEK": 0.09, "NOK": 0.085, "DKK": 0.134, "ISK": 0.0072, "USD": 0.92}
UNDERSIZED_SHARE = 0.2


def undersized(program: dict, profile: dict) -> bool:
    """True when the founder named how much they need and the door's maximum is under a fifth of it.

    Farmers who need 1.5 MSEK should hear about the project grant before the
    120 000 SEK grant for forming the group, even though both fit.
    """
    need = profile.get("need_eur")
    amount = program.get("amount") or {}
    rate = EUR_PER_UNIT.get(str(amount.get("currency")))
    if not need or rate is None or not isinstance(amount.get("max"), (int, float)):
        return False
    return amount["max"] * rate < UNDERSIZED_SHARE * need


def poor_fit(door: Door) -> bool:
    """Doors that stay out of the full answer and go to `more`: closed, run from another country, wrong stage, wrong sector, or charging a fee."""
    return (
        door.availability == "closed"
        or door.foreign
        or door.stage_mismatch
        or door.topic_mismatch
        or door.founder_cost == "fee"
    )


def core_open(door: Door) -> int:
    """Open questions that are not about the founder's situation."""
    return sum(1 for item in door.unknown if not item.get("situation"))


def core_status(door: Door) -> str:
    """The status as if every situation question were answered in the door's favour.

    The screen asks those questions for every door at once. Ranking on them
    would sink a carefully gated record below one nobody has researched yet.
    """
    if door.status == "blocked":
        return "blocked"
    return "unknown" if core_open(door) else "eligible"


def rank(doors: list[Door]) -> list[Door]:
    """Open doors first: eligible, then unknown with the fewest open questions, then blocked. Doors run from another country than the founder's come after domestic ones, doors that pay a small fraction of the stated need after doors that can pay it, a call tied to the founder's own sector before general calls, closed doors last. Ties keep data-file order.

    A Swedish call that admits foreign startups is technically open to a Finnish
    founder, but leading a Finnish answer with it buries the Finnish doors.
    """
    return sorted(
        doors,
        key=lambda door: (
            door.availability == "closed",
            door.foreign,
            door.stage_mismatch or door.topic_mismatch,
            door.undersized,
            not door.topic_match,
            COST_RANK.get(door.founder_cost, 0),
            door.availability != "open",
            RANK[core_status(door)],
            core_open(door),
        ),
    )


def collapse_groups(doors: list[Door]) -> list[Door]:
    """Doors that share a group and a status, where the leader's open questions are a subset of the sibling's, become one door.

    Playground, Fast Lane and Large Scale ask a Swedish AB the same four
    questions, and Fast Lane adds one about HPC experience. Three blocks that
    differ in the hour count and one question read as noise; one block with
    the tiers on a line, each with its extra question, reads as a choice.
    """
    kept: list[Door] = []
    leaders: dict[tuple, Door] = {}
    for door in doors:
        if not door.group:
            kept.append(door)
            continue
        key = (door.group, door.status, door.availability)
        leader = leaders.get(key)
        own = {item["label"] for item in door.unknown}
        if leader is not None and {item["label"] for item in leader.unknown} <= own:
            extra = [item["label"] for item in door.unknown if item["label"] not in {it["label"] for it in leader.unknown}]
            leader.also.append({"id": door.id, "name": door.name, "amount": door.amount["text"], "apply_url": door.apply_url, "extra": extra})
        else:
            leaders.setdefault(key, door)
            kept.append(door)
    return kept


# A founder without a company can register one; nobody becomes a university by filing a form.
UNLOCKABLE_FROM = {"none", "sole_trader"}
UNLOCK_TARGETS = ("company", "sole_trader")


def unlock_entry(program: dict) -> dict:
    return {"id": program["id"], "name": program["name"], "availability": str(program.get("availability", "unknown"))}


def open_first(entries: list[dict]) -> list[dict]:
    """Open doors first, closed last; data-file order inside each."""
    return sorted(entries, key=lambda entry: entry["availability"] == "closed")


def legal_form_unlocks(programs: list[dict], profile: dict, today: date, lang: str) -> dict[str, list[str]]:
    """Doors the profile fails only on legal form, keyed by the form that would pass.

    A founder with an idea and no company is blocked from most grants by the
    form alone. Hiding those doors hides the most useful sentence in the
    answer: register a company and these open.
    """
    unlocks: dict[str, list[str]] = {}
    current = profile.get("legal_form")
    if current not in UNLOCKABLE_FROM:
        return unlocks
    for program in programs:
        if not is_relevant(program, profile):
            continue
        failing = [gate for gate in program["eligibility"] if evaluate_rule(gate, profile, lang).status == "failed"]
        if not failing or any(rule_fields(gate) != {"legal_form"} for gate in failing):
            continue
        for form in UNLOCK_TARGETS:
            if form == current:
                continue
            trial = dict(profile, legal_form=form)
            if all(evaluate_rule(gate, trial, lang).status == "met" for gate in failing):
                unlocks.setdefault(form, []).append(unlock_entry(program))
    return {form: open_first(entries) for form, entries in unlocks.items()}


def country_unlocks(programs: list[dict], profile: dict, lang: str) -> dict[str, list[str]]:
    """For a founder who lives in another country than the company is registered in: doors blocked only by
    the registration country that a company registered where the founder lives would pass.

    A Swede in Copenhagen with a Swedish AB fails every Danish grant on one line,
    the registration. Saying so is the useful answer; hiding the doors is not.
    """
    home, residence = profile.get("country"), profile.get("residence_country")
    if not home or not residence or home == residence:
        return {}
    trial = dict(profile, country=residence)
    found: list[str] = []
    for program in programs:
        if not is_relevant(program, profile):
            continue
        failing = [gate for gate in program["eligibility"] if evaluate_rule(gate, profile, lang).status == "failed"]
        if not failing or any(rule_fields(gate) != {"country"} for gate in failing):
            continue
        if all(evaluate_rule(gate, trial, lang).status == "met" for gate in failing):
            found.append(unlock_entry(program))
    return {f"country:{residence}": open_first(found)} if found else {}


def pick_top(doors: list[Door], needs: list[str] | None, top: int) -> tuple[list[Door], list[Door]]:
    """The doors shown in full, then the rest.

    With several needs asked, the best remaining door of each need is taken in
    turn, so a founder who asked for GPU and credits does not get three credit
    doors and the GPU door under "more".
    """
    if top <= 0:
        return doors, []
    good = [door for door in doors if not poor_fit(door)]
    poor = [door for door in doors if poor_fit(door)]
    if not needs or len(needs) < 2:
        return good[:top], good[top:] + poor
    shown: list[Door] = []
    remaining = list(good)
    while len(shown) < top and remaining:
        progressed = False
        for need in needs:
            candidate = next((door for door in remaining if need in door.need), None)
            if candidate is None:
                continue
            shown.append(candidate)
            remaining.remove(candidate)
            progressed = True
            if len(shown) == top:
                break
        if not progressed:
            shown.append(remaining.pop(0))
    return shown, remaining + poor


def context_topics(profile: dict) -> list[str]:
    """Situation topics worth asking even when no door in the data gates on them.

    A student's university runs its own startup support and may own part of the
    idea; trained-on patient data is personal data unless nobody, the hospital
    included, can link it back. Neither shows up as a failed rule anywhere.
    """
    topics: list[str] = []
    if profile.get("affiliation") is None and (
        profile.get("legal_form") in (None, "none") or founder_stage(profile) in ("idea", "pre_seed")
    ):
        topics.append("affiliation")
    if profile.get("personal_data") is None and ("health" in (profile.get("sector") or []) or profile.get("personal_data_claim")):
        topics.append("data")
    return topics


def screen(doors: list[Door], profile: dict, lang: str) -> list[dict]:
    """The founder-situation questions for the first answer, at most SCREEN_MAX.

    A topic weighs more the more of the best doors it decides and the higher
    those doors rank. A door the founder named, and a context topic, weigh as
    two best doors. One slot goes first to a basic fact the best doors need.
    Asking these before going deep on any door is what the plain assistant did
    in round 3 and the skill did not.
    """
    weight: dict[str, float] = {}
    decides: dict[str, list[str]] = {}
    open_doors = [door for door in doors if door.status != "blocked"]
    named = [door for door in open_doors if is_named(door, profile)]
    best = named + [door for door in open_doors if not poor_fit(door) and door not in named][: SCREEN_DOORS - len(named)]
    for position, door in enumerate(best):
        door_weight = SCREEN_DOORS * NAMED_WEIGHT if door in named else SCREEN_DOORS - position
        for topic in door.situation:
            weight[topic] = weight.get(topic, 0) + door_weight * TOPIC_WEIGHT.get(topic, 1.0)
            decides.setdefault(topic, []).append(door.name)
    for topic in context_topics(profile):
        # A student's university support, or patient data, changes the route whatever the doors say.
        weight[topic] = weight.get(topic, 0) + SCREEN_DOORS * NAMED_WEIGHT
        decides.setdefault(topic, [])
    order = sorted(weight, key=lambda topic: (-weight[topic], SITUATION_ORDER.index(topic)))
    basics = basic_question(best, lang)
    items = [basics] if basics else []
    items += [
        {
            "topic": topic,
            "fields": [field for field in SITUATION_TOPICS[topic] if profile.get(field) is None],
            "question": i18n.screen_question(topic, lang),
            "why": i18n.screen_why(topic, lang),
            "decides": decides[topic],
        }
        for topic in order[: SCREEN_MAX - len(items)]
    ]
    return items


def is_named(door: Door, profile: dict) -> bool:
    """True when the founder named this program, by its id or by the funder's prefix ("vinnova", "rannis")."""
    return any(door.id == key or door.id.startswith(f"{key}-") for key in profile.get("named") or [])


def basic_question(best: list[Door], lang: str) -> dict | None:
    """The best door's open basic fact (legal form, then company age), with the doors it decides.

    Without it a webshop owner who never said whether it is an AS or an ENK
    gets three questions about ownership and grants and none about the form
    that decides the grant.
    """
    for field in BASIC_FIELDS:
        deciding = [door for door in best if any(item.get("field") == field for item in door.unknown)]
        if deciding:
            item = next(item for item in deciding[0].unknown if item.get("field") == field)
            return {
                "topic": "basics",
                "fields": [field],
                "question": item["question"],
                "why": i18n.screen_why("basics", lang),
                "decides": [door.name for door in deciding],
            }
    return None


def route_order(profile: dict) -> list[str]:
    """Routes for the founder's needs first, in the order they gave them, then the rest."""
    order: list[str] = []
    for need in profile.get("need") or []:
        order.extend(NEED_ROUTES.get(need, ()))
    return list(dict.fromkeys([*order, *ROUTES]))


def routes(doors: list[Door], profile: dict, lang: str) -> list[dict]:
    """The realistic routes, each with its best doors in rank order, the routes in `route_order`.

    The founder chooses a route with the traps in view before any door gets a
    full checklist. Closed, foreign, wrong-stage and blocked doors are not routes.
    """
    found: dict[str, list[Door]] = {}
    # A program the founder named leads its route, so the line they read first answers their question.
    for door in sorted(doors, key=lambda door: not is_named(door, profile)):
        if poor_fit(door) or door.status == "blocked":
            continue
        found.setdefault(door.route, []).append(door)
    order = route_order(profile)
    ranked = sorted(found.items(), key=lambda item: order.index(item[0]) if item[0] in order else len(order))
    return [
        {
            "route": route,
            "label": i18n.route_name(route, lang),
            "count": len(members),
            "doors": [
                {"id": door.id, "name": door.name, "status": door.status, "amount": door.amount["text"]}
                for door in members[:ROUTE_DOORS]
            ],
        }
        for route, members in ranked
    ]


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
    lang: str,
    picked: bool = False,
) -> Door | None:
    """The door for one record, or None when the record is irrelevant to the profile or blocked and hidden. A picked door is always returned."""
    if not picked and not is_relevant(program, profile):
        return None
    door = evaluate(program, profile, today, lang)
    if door.status == "blocked" and not include_all:
        return None
    live = program.get("live")
    if live_fetch is not None and live and live.get("source") == "vinnova":
        try:
            door.live = live_fetch(live["call_id"])
        except Exception as exc:  # the boundary: a dead API must not hide the other doors
            door.live = {"error": str(exc)}
    return door


def summary(door: Door) -> dict:
    return {
        "id": door.id,
        "name": door.name,
        "kind": door.kind,
        "route": door.route,
        "status": door.status,
        "availability": door.availability,
        "amount": door.amount["text"],
        "open_questions": len(door.unknown),
        "foreign": door.foreign,
        "founder_cost": door.founder_cost,
        "stage_mismatch": door.stage_mismatch,
        "topic_mismatch": door.topic_mismatch,
        "undersized": door.undersized,
        "poor_fit": poor_fit(door),
        "status_url": door.status_url,
    }


def run(
    raw_profile: dict,
    programs: list[dict],
    today: date,
    include_all: bool = False,
    live_fetch: Callable[[str], dict | None] | None = None,
    top: int = DEFAULT_TOP,
    door_id: str | None = None,
) -> dict:
    """Raises MalformedRecord when a record lacks a field or holds a value the rules cannot read. top=0 returns every door in full.

    door_id returns that one program in full, blocked or not and whatever the
    founder asked for, with its application block: the founder has picked it
    and wants help applying, so relevance filters no longer apply.
    """
    if door_id is not None:
        chosen = [program for program in programs if isinstance(program, dict) and program.get("id") == door_id]
        if not chosen:
            known = sorted(str(program.get("id")) for program in programs if isinstance(program, dict))
            close = [ident for ident in known if door_id.split("-")[0] in ident][:8]
            raise ValueError(f"no program with id {door_id!r}" + (f"; did you mean one of: {', '.join(close)}" if close else ""))
        programs = chosen
        raw_profile = {key: value for key, value in raw_profile.items() if key != "need"}
        include_all, top = True, 0
    profile, warnings = normalize_profile(raw_profile)
    lang = profile.get("lang", i18n.DEFAULT_LANG)
    doors: list[Door] = []
    for index, program in enumerate(programs):
        try:
            door = build_door(program, profile, today, include_all, live_fetch, lang, picked=door_id is not None)
        except (KeyError, TypeError, ValueError) as exc:
            raise MalformedRecord(describe_malformed(program, index, exc)) from exc
        if door is not None:
            doors.append(door)
    ranked = collapse_groups(rank(doors))
    for door in ranked:
        door.glyph = render_glyph(door, lang)
    try:
        unlocks = legal_form_unlocks(programs, profile, today, lang) | country_unlocks(programs, profile, lang)
    except (KeyError, TypeError, ValueError) as exc:
        raise MalformedRecord(f"cannot compute unlocks: {exc}") from exc
    shown, rest = pick_top(ranked, profile.get("need"), top)
    return {
        "profile": profile,
        "lang": lang,
        "warnings": warnings,
        "stale": [door.id for door in ranked if door.stale],
        "screen": screen(ranked, profile, lang),
        "routes": routes(ranked, profile, lang),
        "unlocks": unlocks,
        "doors": [asdict(door) for door in shown],
        "more": [summary(door) for door in rest],
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
    parser.add_argument("--top", type=int, default=DEFAULT_TOP, help=f"doors returned in full, the rest under 'more' (default {DEFAULT_TOP}, 0 for all)")
    parser.add_argument("--programs", type=Path, default=PROGRAMS_PATH, help="path to programs.json")
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="override today's date, YYYY-MM-DD")
    parser.add_argument("--door", default=None, help="return this one program in full, with its application block, for helping the founder apply")
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
        result = run(raw, programs, args.today or date.today(), include_all=args.all, live_fetch=live_fetch, top=args.top, door_id=args.door)
    except ValueError as exc:  # unreadable file, wrong shape, or a MalformedRecord: one line, no traceback
        print(str(exc), file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
