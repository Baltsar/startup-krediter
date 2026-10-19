#!/usr/bin/env python3
"""Score a litmus round against the bars pre-registered in plan.md.

    python3 score.py <round-dir>

Reads questions.json, grades/blind-key.json, grades/<qid>.json (first grader),
grades/<qid>-g2.json (second grader, where there is one) and the conversations.
Prints each bar with its value and pass or fail, then the per-question table.

Rules, as the plan states them:
- A split between two graders on best_recommendation, draft_better or verdict
  counts as a tie.
- Stopper counts are the first grader's.
- An absolute check failed by either grader counts as failed.
- Turn-1 words are counted here, not by the graders: tokens holding at least one
  letter or digit in the assistant's turn-1 text, status block included.
"""

from __future__ import annotations

import json
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path

ABSOLUTE = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9")
C1_MARGIN = 20.0
C1_MAX_LOWER = 2
C2_MAX_WORSE = 3
C3_MIN_WIN_OR_TIE = 11
C4_MAX_MEDIAN_WORDS = 450
C5_MAX_LOST = 1
WORD = re.compile(r"\S*[^\W_]\S*")


@dataclass
class Row:
    qid: str
    kind: str
    total: int
    stated_skill: int
    stated_plain: int
    recommendation: str
    draft: str
    verdict: str
    fails_skill: list[str]
    fails_plain: list[str]
    errors_skill: int
    errors_plain: int
    words_skill: int
    words_plain: int


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def to_arm(choice: str, key: dict[str, str]) -> str:
    """A grader's A, B or tie as skill, plain or tie."""
    if choice in ("A", "B"):
        return "skill" if key[choice] == "with" else "plain"
    return choice


def agreed(first: str, second: str | None) -> str:
    return first if second is None or first == second else "tie"


def turn1_words(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    start = text.index("## Assistant, turn 1")
    end = text.index("## Founder, turn 2", start)
    body = text[start + len("## Assistant, turn 1") : end]
    return len(WORD.findall(body))


def failed(grades: list[dict], letter: str) -> list[str]:
    return sorted({check for grade in grades for check in ABSOLUTE if grade["absolute"][letter].get(check) == "fail"})


def row(root: Path, item: dict, key: dict[str, str]) -> Row:
    qid = item["id"]
    first = load(root / "grades" / f"{qid}.json")
    second_path = root / "grades" / f"{qid}-g2.json"
    second = load(second_path) if second_path.exists() else None
    skill = "A" if key["A"] == "with" else "B"
    plain = "B" if skill == "A" else "A"
    grades = [first] + ([second] if second else [])

    def choice(field: str) -> str:
        return to_arm(agreed(first[field], second[field] if second else None), key)

    conversations = root / "conversations"
    return Row(
        qid=qid,
        kind=item["type"],
        total=int(first["stoppers_total"]),
        stated_skill=int(first["stoppers_stated"][skill]),
        stated_plain=int(first["stoppers_stated"][plain]),
        recommendation=choice("best_recommendation"),
        draft=choice("draft_better"),
        verdict=choice("verdict"),
        fails_skill=failed(grades, skill),
        fails_plain=failed(grades, plain),
        errors_skill=len(first["factual_errors"][skill]),
        errors_plain=len(first["factual_errors"][plain]),
        words_skill=turn1_words(conversations / f"{qid}-with-skill.md"),
        words_plain=turn1_words(conversations / f"{qid}-without-skill.md"),
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    root = Path(argv[1])
    questions = load(root / "questions.json")
    key = load(root / "grades" / "blind-key.json")["key"]
    rows = [row(root, item, key[item["id"]]) for item in questions]
    incomplete = [item["id"] for item in questions if load(root / "grades" / f"{item['id']}.json").get("incomplete")]

    absolute = [r.qid for r in rows if r.fails_skill]
    total = sum(r.total for r in rows) or 1
    share_skill = 100 * sum(r.stated_skill for r in rows) / total
    share_plain = 100 * sum(r.stated_plain for r in rows) / total
    lower = [r.qid for r in rows if r.stated_skill < r.stated_plain]
    worse = [r.qid for r in rows if r.recommendation == "plain"]
    win_or_tie = [r.qid for r in rows if r.verdict in ("skill", "tie")]
    checklist = [r for r in rows if r.kind == "checklist"]
    median_skill = statistics.median([r.words_skill for r in checklist]) if checklist else 0
    median_plain = statistics.median([r.words_plain for r in checklist]) if checklist else 0
    drafts = [r for r in rows if r.kind == "apply"]
    drafts_lost = [r.qid for r in drafts if r.draft == "plain"]

    bars = [
        ("Absolute checks (A1-A9), with skill", f"failures in {len(absolute)} questions {absolute}", not absolute),
        (
            "C1 stoppers, skill vs plain",
            f"{share_skill:.0f}% vs {share_plain:.0f}%, lower on {len(lower)} {lower}",
            share_skill - share_plain >= C1_MARGIN and len(lower) <= C1_MAX_LOWER,
        ),
        ("C2 recommendation worse than plain", f"{len(worse)} {worse}", len(worse) <= C2_MAX_WORSE),
        ("C3 skill wins or ties", f"{len(win_or_tie)} of {len(rows)}", len(win_or_tie) >= C3_MIN_WIN_OR_TIE),
        (
            "C4 median turn-1 words, checklist questions",
            f"{median_skill:.0f} (plain {median_plain:.0f})",
            median_skill <= C4_MAX_MEDIAN_WORDS,
        ),
        ("C5 drafts lost to plain, apply questions", f"{len(drafts_lost)} of {len(drafts)} {drafts_lost}", len(drafts_lost) <= C5_MAX_LOST),
    ]
    for name, value, ok in bars:
        print(f"{'pass' if ok else 'FAIL'}  {name}: {value}")
    print(f"Factual errors: skill {sum(r.errors_skill for r in rows)}, plain {sum(r.errors_plain for r in rows)} (reported, not a bar)")
    if incomplete:
        print(f"Incomplete grades: {incomplete}")
    print()
    print("qid  type       stoppers s/p/total  rec    draft  verdict  words s/p  fails skill / plain")
    for r in rows:
        print(
            f"{r.qid:<4} {r.kind:<10} {r.stated_skill:>3}/{r.stated_plain:>3}/{r.total:<5}  {r.recommendation:<6} {r.draft:<6} "
            f"{r.verdict:<8} {r.words_skill:>4}/{r.words_plain:<4}  {r.fails_skill} / {r.fails_plain}"
        )
    return 0 if all(ok for _, _, ok in bars) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
