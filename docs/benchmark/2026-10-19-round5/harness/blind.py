#!/usr/bin/env python3
"""Blind the conversations of a litmus round: A and B per question, seeded per question id.

    python3 blind.py <round-dir>

Reads <round-dir>/conversations/<qid>-with-skill.md and <qid>-without-skill.md for
every question in <round-dir>/questions.json, writes <round-dir>/blind/<qid>-A.md and
<qid>-B.md with the arm names removed, and the key to <round-dir>/grades/blind-key.json.
The seed is fixed in the plan, so anyone can rebuild the key from the question ids.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

SEED_PREFIX = "202610195"
ARMS = ("with", "without")


def assign(qid: str) -> dict[str, str]:
    """The arm behind A and B for one question."""
    arms = list(ARMS)
    random.Random(f"{SEED_PREFIX}-{qid}").shuffle(arms)
    return {"A": arms[0], "B": arms[1]}


def strip_arm(text: str, qid: str, arm: str) -> str:
    """The conversation without its heading, which names the arm."""
    lines = text.splitlines()
    if lines and lines[0].startswith(f"# {qid} {arm}"):
        lines = lines[1:]
    return "\n".join(lines).lstrip("\n") + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    root = Path(argv[1])
    questions = json.loads((root / "questions.json").read_text(encoding="utf-8"))
    (root / "blind").mkdir(exist_ok=True)
    (root / "grades").mkdir(exist_ok=True)
    key: dict[str, dict[str, str]] = {}
    for question in questions:
        qid = str(question["id"])
        key[qid] = assign(qid)
        for letter, arm in key[qid].items():
            source = root / "conversations" / f"{qid}-{arm}-skill.md"
            text = strip_arm(source.read_text(encoding="utf-8"), qid, f"{arm}-skill")
            (root / "blind" / f"{qid}-{letter}.md").write_text(f"# {qid} conversation {letter}\n\n{text}", encoding="utf-8")
    note = f'A and B per question; seeded per question id with random.Random("{SEED_PREFIX}-<qid>")'
    (root / "grades" / "blind-key.json").write_text(json.dumps({"note": note, "key": key}, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
