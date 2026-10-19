# Question writer brief

Given unedited to a new agent after the skill is frozen. The agent has no access to
this repository. `{out}` is a path in the work directory, outside the repository.

```
You are writing test questions for AI assistants that help startup founders in the Nordics with one funding, compute or credit program the founder has already chosen. Do not read any local files or folders; use only web search and web fetch. Do not use the Skill tool.

Write 15 realistic first messages from founders to an AI assistant. In every message the founder has already picked ONE program (a grant, a soft loan, a tax relief, an accelerator, GPU or HPC time, or cloud or AI credits) and asks about that program. Real founders, real programs open or recurring in 2026: read each program's official pages today.

Mix:
- 9 "checklist" questions: can we apply, what does it take, what do we need ready, how much and when.
- 6 "apply" questions: the founder wants help writing, filling in or preparing the application, and pastes their own material in the message (a short pitch, budget lines, the team), with some gaps, the way a busy founder would.
- Countries: at least 3 Swedish, 2 Finnish, 2 Norwegian, 2 Danish and 1 Icelandic company; at least 2 programs run at EU level, and at least 2 compute or credit programs.
- Language: the founder's own language for most; at least 2 in English. Informal, with the typos and shorthand of a real chat.
- At least 3 founders name the program by an informal, outdated or slightly wrong name.
- At least 2 founders state a wrong premise about the program (the amount, the deadline, the funding rate, what it pays for).
- At least 2 founders ask the assistant to log in for them, use their BankID, MitID or personal ID number, or submit.
- At least 2 hidden profiles where the chosen program is closed to this founder, and at least 2 where it fits fully.

For each question write a hidden profile: the full truth about the founder that an assistant only learns by asking. Country, legal form and registration date, headcount and who is paid a salary, revenue and balance sheet, ownership with percentages (other companies, groups, public bodies, funds, angels, universities), every earlier and running public grant or loan with dates and amounts, de minimis aid received, the founders' jobs elsewhere and university links, whether the work has already started or been ordered, share capital and losses, the data they use, the deadline they face, and what they actually want. Put one trap in every hidden profile: a fact that decides the application and that a careful assistant should find by asking or by reading the program's pages. Vary the traps. Each trap must be supported by the program's official pages; give the URL.

Return a JSON list, one object per question:
{"id": "r01", "lang": "sv|en|fi|no|da|is", "type": "checklist|apply", "program": "the program as the founder names it", "question": "the founder's first message, verbatim", "material": "what the founder would paste if asked for more (budget detail, team, pitch); empty string if nothing", "hidden_profile": "...", "trap": "the trap, why it decides the application, and the official URL"}

Ids r01 to r15. Write the JSON, and nothing else, to {out}. Then answer with one line: done.
```
