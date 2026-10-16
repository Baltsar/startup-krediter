#!/usr/bin/env python3
"""Validate data/programs.json against data/schema.json. Standard library only.

Interprets the subset of JSON Schema 2020-12 that schema.json uses (type, enum,
pattern, minLength, minItems, uniqueItems, required, properties,
additionalProperties, items, $ref, oneOf), so the schema stays the single source
of truth for enums and required fields. Then adds the checks a schema cannot
express: unique ids, last_verified not in the future, the reference anchor
present in the reference file, and that each rule's op suits its field and value
(a mismatch makes the matcher fail the rule for every founder without a word).

Usage: python3 scripts/validate.py [path/to/programs.json]
Prints one line per problem to stderr and exits 1 when anything is wrong.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Callable
from datetime import date
from pathlib import Path

from match import BOOLEAN_FIELDS, LIST_FIELDS, NUMERIC_FIELDS

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "data" / "schema.json"
PROGRAMS_PATH = ROOT / "data" / "programs.json"
REFERENCES_DIR = ROOT / "references"

# need is matched by relevance, not by a rule, so the schema's field enum leaves it out.
CONTAINS_FIELDS = LIST_FIELDS - {"need"}
NUMERIC_OPS = {"lte", "gte", "lt", "gt"}
LIST_VALUE_OPS = {"in", "not_in"}
EQUALITY_OPS = {"eq", "neq"}

TYPE_CHECKS: dict[str, Callable[[object], bool]] = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}


def resolve(ref: str, root: dict) -> dict:
    """Follow a local JSON pointer such as #/$defs/rule."""
    node: dict = root
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node


def check(value: object, schema: dict, path: str, root: dict) -> list[str]:
    """Return the schema violations of value at path. Empty when valid."""
    if "$ref" in schema:
        return check(value, resolve(schema["$ref"], root), path, root)
    if "oneOf" in schema:
        results = [check(value, branch, path, root) for branch in schema["oneOf"]]
        passing = [r for r in results if not r]
        if len(passing) == 1:
            return []
        if len(passing) > 1:
            return [f"{path}: matches {len(passing)} oneOf branches, expected exactly one"]
        # Nothing matched: report the branch that came closest, so a bad rule
        # reads as "bad op" rather than "not a group".
        return min(results, key=len)
    if "enum" in schema and value not in schema["enum"]:
        return [f"{path}: {value!r} is not one of {schema['enum']}"]
    expected = schema.get("type")
    if expected is not None and not TYPE_CHECKS[expected](value):
        return [f"{path}: expected {expected}, got {type(value).__name__}"]
    out: list[str] = []
    if isinstance(value, str):
        pattern = schema.get("pattern")
        if pattern is not None and not re.search(pattern, value):
            out.append(f"{path}: {value!r} does not match {pattern}")
        if len(value) < schema.get("minLength", 0):
            out.append(f"{path}: shorter than {schema['minLength']} characters")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            out.append(f"{path}: fewer than {schema['minItems']} items")
        if schema.get("uniqueItems"):
            keys = {json.dumps(item, sort_keys=True) for item in value}
            if len(keys) != len(value):
                out.append(f"{path}: items are not unique")
        if "items" in schema:
            for index, item in enumerate(value):
                out.extend(check(item, schema["items"], f"{path}[{index}]", root))
    if isinstance(value, dict):
        props: dict = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                out.append(f"{path}: missing required field '{key}'")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    out.append(f"{path}: unknown field '{key}'")
        for key, sub in props.items():
            if key in value:
                out.extend(check(value[key], sub, f"{path}.{key}", root))
    return out


def is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def check_rule_compatibility(rule: dict, path: str) -> list[str]:
    """The op must suit the field and the value. The matcher's compare() answers False for any mismatch, which would block the door silently."""
    field, op, value = rule.get("field"), rule.get("op"), rule.get("value")
    if not isinstance(field, str) or not isinstance(op, str):
        return []
    if op in LIST_VALUE_OPS and not isinstance(value, list):
        return [f"{path}: op '{op}' needs a list value, got {type(value).__name__}"]
    if op == "contains":
        if field not in CONTAINS_FIELDS:
            return [f"{path}: op 'contains' needs a list field ({', '.join(sorted(CONTAINS_FIELDS))}), got '{field}'"]
        if isinstance(value, (list, dict)):
            return [f"{path}: op 'contains' needs a single item as value, got {type(value).__name__}"]
    if op in NUMERIC_OPS:
        if field not in NUMERIC_FIELDS:
            return [f"{path}: op '{op}' needs a numeric field, got '{field}'"]
        if not is_number(value):
            return [f"{path}: op '{op}' needs a numeric value, got {value!r}"]
    if op in EQUALITY_OPS:
        if isinstance(value, (list, dict)):
            return [f"{path}: op '{op}' needs a scalar value, got {type(value).__name__}"]
        if field in BOOLEAN_FIELDS and not isinstance(value, bool):
            return [f"{path}: op '{op}' on boolean field '{field}' needs a boolean value, got {value!r}"]
        if field not in BOOLEAN_FIELDS and isinstance(value, bool):
            return [f"{path}: op '{op}' with a boolean value needs a boolean field, got '{field}'"]
    return []


def check_gates(ident: str, gates: object) -> list[str]:
    """Compatibility of every rule, inside groups too. Shape errors are the schema's job and are skipped here."""
    if not isinstance(gates, list):
        return []
    out: list[str] = []
    for index, gate in enumerate(gates):
        if not isinstance(gate, dict):
            continue
        if isinstance(gate.get("any"), list):
            for member_index, member in enumerate(gate["any"]):
                if isinstance(member, dict):
                    out.extend(check_rule_compatibility(member, f"{ident}.eligibility[{index}].any[{member_index}]"))
        else:
            out.extend(check_rule_compatibility(gate, f"{ident}.eligibility[{index}]"))
    return out


def check_date(ident: str, raw: object, today: date) -> list[str]:
    if not isinstance(raw, str):
        return []
    try:
        verified = date.fromisoformat(raw)
    except ValueError:
        return [f"{ident}: last_verified {raw!r} is not a valid date"]
    if verified > today:
        return [f"{ident}: last_verified {raw} is in the future (today is {today.isoformat()})"]
    return []


def check_reference(ident: str, raw: object, references_dir: Path) -> list[str]:
    if not isinstance(raw, str) or "#" not in raw:
        return []
    rel, anchor = raw.split("#", 1)
    target = references_dir / Path(rel).name
    if not target.exists():
        return [f"{ident}: reference file {rel} does not exist"]
    text = target.read_text(encoding="utf-8")
    if f"{{#{anchor}}}" not in text:
        return [f"{ident}: anchor #{anchor} not found in {rel}"]
    return []


def validate(programs: object, schema: dict, today: date, references_dir: Path | None) -> list[str]:
    """Every problem in the programs document, one human-readable line each."""
    if not isinstance(programs, dict):
        return ["document: expected an object with a 'programs' list"]
    records = programs.get("programs")
    if not isinstance(records, list):
        return ["document: 'programs' must be a list"]
    out: list[str] = []
    for key in programs:
        if key != "programs":
            out.append(f"document: unknown field '{key}'")
    program_schema = resolve("#/$defs/program", schema)
    seen: set[str] = set()
    for index, record in enumerate(records):
        ident = record.get("id") if isinstance(record, dict) and isinstance(record.get("id"), str) else f"programs[{index}]"
        out.extend(check(record, program_schema, ident, schema))
        if not isinstance(record, dict):
            continue
        if ident in seen:
            out.append(f"{ident}: duplicate id '{ident}'")
        seen.add(ident)
        out.extend(check_gates(ident, record.get("eligibility")))
        out.extend(check_date(ident, record.get("last_verified"), today))
        if references_dir is not None:
            out.extend(check_reference(ident, record.get("reference"), references_dir))
    return out


def main(argv: list[str]) -> int:
    programs_path = Path(argv[1]) if len(argv) > 1 else PROGRAMS_PATH
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    programs = json.loads(programs_path.read_text(encoding="utf-8"))
    problems = validate(programs, schema, date.today(), REFERENCES_DIR)
    count = len(programs.get("programs", [])) if isinstance(programs, dict) else 0
    for line in problems:
        print(line, file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s) in {count} record(s)", file=sys.stderr)
        return 1
    print(f"ok: {count} record(s) valid in {programs_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
