#!/usr/bin/env python3
"""Render the prompts for each turn of a litmus round, and assemble the conversations.

    python3 turns.py <round-dir> <work-dir> prompt-t1  <qid> <with|without>
    python3 turns.py <round-dir> <work-dir> prompt-sim <qid> <with|without>
    python3 turns.py <round-dir> <work-dir> prompt-t2  <qid> <with|without>
    python3 turns.py <round-dir> <work-dir> assemble

The prompts come from the briefs in <round-dir> with their {placeholders} filled, so
every agent in the round gets the same words. Each agent writes one reply file under
<work-dir>: t1/<qid>-<arm>.md (assistant, turn 1), f2/<qid>-<arm>.md (founder, turn 2)
and t2/<qid>-<arm>.md (assistant, turn 2). `assemble` joins them into
<round-dir>/conversations/<qid>-<arm>-skill.md. The work dir also holds the frozen
skill under snapshot/, outside the repository, so no agent can reach the round's files.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

TODAY_FILE = "today.txt"
ARMS = ("with", "without")


def brief(root: Path, name: str) -> str:
    """The text between the first pair of ``` fences in a brief, the part agents receive."""
    text = (root / name).read_text(encoding="utf-8")
    start = text.index("```\n") + 4
    return text[start : text.index("\n```", start)]


def question(root: Path, qid: str) -> dict[str, str]:
    for item in json.loads((root / "questions.json").read_text(encoding="utf-8")):
        if item["id"] == qid:
            return {key: str(value) for key, value in item.items()}
    raise SystemExit(f"no question {qid!r} in questions.json")


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"missing turn file {path}")
    return path.read_text(encoding="utf-8").strip()


def render(root: Path, work: Path, step: str, qid: str, arm: str) -> str:
    item = question(root, qid)
    today = read(work / TODAY_FILE)
    fields = {
        "snapshot": str(work / "snapshot"),
        "today": today,
        "question": item["question"],
        "hidden_profile": item["hidden_profile"],
        "material": item.get("material", ""),
    }
    if step == "prompt-t1":
        fields["out"] = str(work / "t1" / f"{qid}-{arm}.md")
        return brief(root, f"assistant-{arm}-skill.md").format(**fields) + "\n\n" + brief(root, "assistant-turn1.md").format(**fields)
    fields["reply1"] = read(work / "t1" / f"{qid}-{arm}.md")
    if step == "prompt-sim":
        fields["out"] = str(work / "f2" / f"{qid}-{arm}.md")
        return brief(root, "simulator-brief.md").format(**fields)
    fields["founder2"] = read(work / "f2" / f"{qid}-{arm}.md")
    fields["out"] = str(work / "t2" / f"{qid}-{arm}.md")
    return brief(root, f"assistant-{arm}-skill.md").format(**fields) + "\n\n" + brief(root, "assistant-turn2.md").format(**fields)


def assemble(root: Path, work: Path) -> None:
    out_dir = root / "conversations"
    out_dir.mkdir(exist_ok=True)
    for item in json.loads((root / "questions.json").read_text(encoding="utf-8")):
        qid = item["id"]
        for arm in ARMS:
            parts = [
                f"# {qid} {arm}-skill",
                "## Founder, turn 1\n" + item["question"].strip(),
                "## Assistant, turn 1\n" + read(work / "t1" / f"{qid}-{arm}.md"),
                "## Founder, turn 2\n" + read(work / "f2" / f"{qid}-{arm}.md"),
                "## Assistant, turn 2\n" + read(work / "t2" / f"{qid}-{arm}.md"),
            ]
            (out_dir / f"{qid}-{arm}-skill.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    root, work, step = Path(argv[1]), Path(argv[2]), argv[3]
    if step == "assemble":
        assemble(root, work)
        return 0
    if step not in ("prompt-t1", "prompt-sim", "prompt-t2") or len(argv) != 6 or argv[5] not in ARMS:
        print(__doc__, file=sys.stderr)
        return 2
    print(render(root, work, step, argv[4], argv[5]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
