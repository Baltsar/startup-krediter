# Litmus test, round 3: plan

Written and committed before any run. Same method and the same bars as rounds
1 and 2 (`../2026-10-17/plan.md`, `../2026-10-17-round2/plan.md`), on a new
set of questions.

## What changed since round 2

Commits `beb0514`, `9748995` and `d0aaabc`, after round 2 failed:

- `SKILL.md`: settle the country from a city, a national legal form or a
  funder the founder names; aim the one web search at student, sector and tax
  doors; never stretch a rule beyond the page; ask about earlier funding
  before saying a door fits; use a call's own name; lead with the door that
  can pay the stated need.
- Matcher: `need_eur` in the profile; doors paying under a fifth of it rank
  after doors that can pay it; a call tied to the founder's sector ranks
  before general calls.
- Data, 66 to 73 records: Jordbruksverket EIP project and group grants,
  Skatteverket forskningsavdrag, EUDIS Business Accelerator, EDF SME calls,
  Innovasjon Norge LINC, Vinnova civil-military acceleration. Fixes to Vinnova
  Innovativa Startups (employee cap, employed project lead), Almi
  Verifieringsmedel (simple MVP allowed) and Business Finland Sprint (earlier
  Business Finland funding as a gate).
- Not added: NATO DIANA, whose site sits behind a Cloudflare challenge.

## What is tested

- **Skill version:** commit `d0aaabc`, frozen as a copy before the runs.
- **Questions:** the 15 in `questions.json`, written by a new agent with no
  access to this repository, the data, the skill or earlier questions, and
  used unedited. The agent got only the list of case types, the language mix,
  and two extra asks: at least two founders name an amount, and at least one
  has earlier funding from the funder they ask about. The questions were read
  only after the skill was frozen at `d0aaabc`.
- **Overlap note:**
  - s05 (Danish ApS, founders in Malmö) is close to round-1 q08 and round-2
    r07.
  - s10 (a parent's money into the company: gift, loan or shares) is close to
    round-2 r11.
  - s06 (forskningsavdrag) tests a door added after round 2.

  The report gives the results with and without s05 and s10.
- **Everything else is as in rounds 1 and 2:** two configurations on Claude
  Opus 5.5, with the skill and as a plain assistant with web search; a
  simulated founder second turn from the hidden profile; one blind grader per
  question fetching official pages itself; the same grader brief.

## Absolute checks

Same eight checks, A1 to A8. A single failure in a with-skill conversation
blocks the launch. Questions built to trigger them:

| Check | Questions |
|---|---|
| A1, A6 (no submitting, no logins, help prepare instead) | s08 |
| A3 (no false eligibility) | s06, s13 |
| A4 (ask for the country) | s02 |
| A5 (correct a false premise) | s03, s06, s13 |
| A8 (tax or equity question answered as that) | s10 |
| A2, A7 | all |

## Comparison bars

Unchanged. All four must hold.

| Bar | Threshold |
|---|---|
| C1. Stoppers stated for the program discussed | The skill's share at least 20 points above the plain AI's in total, and lower on no more than 2 of 15 questions |
| C2. First recommendation worse than the plain AI's | No more than 3 of 15 |
| C3. Grader's overall verdict | The skill wins or ties in at least 11 of 15 |
| C4. Median length of the first answer | At most 220 words |

## Noise checks

- **Run variance:** the with-skill configuration runs a second first turn on
  s01, s07 and s13, the same positions as in round 2.
- **Grader agreement:** a second blind grader scores s03, s09 and s14, the same
  positions as in round 2. A split counts as a tie.
- **Overruling a grader:** only with a primary source. New in this round: any
  finding that decides a bar or an absolute check is re-checked against the
  primary source on both sides, not only findings against the skill. The
  report names every overruled finding.
- **Incomplete grades** count as incomplete, not as a win.
- **Known limit:** two turns. When a question is required (A4), the checklist
  cannot appear before turn 3, which lowers C1 for that question. The report
  says so where it happens.

## If a bar fails

No launch. Fixes go on the branch and the next round needs new questions.

## Not measured

Triggering, and other models than Claude.
