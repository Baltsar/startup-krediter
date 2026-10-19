# Litmus test, round 2: plan

Written and committed before any run. Same method and the same bars as round 1
(`../2026-10-17/plan.md`), on a new set of questions.

## What changed since round 1

Commits `c1618b3`, `19951bf` and `870589b`, after round 1 failed:

- `SKILL.md` no longer prints maintenance notes, answers a named program in
  Stage A form under 200 words, allows one or two doors, and requires currency
  codes on every amount.
- The matcher keeps closed, foreign, wrong-stage, wrong-topic and fee doors out
  of the full answer and ranks open doors first.
- The data gained Starttiraha and EIFO Matchlån, and stage and sector tags.

## What is tested

- **Skill version:** commit `870589b`, frozen as a copy before the runs.
- **Questions:** the 15 in `questions.json`, written by a new agent with no
  access to this repository, the data, the skill or the round-1 questions, and
  used unedited.
- **Overlap note:** r07 (Swedish founder in Malmö with a Danish ApS) is close to
  round-1 q08, which informed the fixes. The report gives the results with and
  without r07.
- **Everything else is as in round 1:** two configurations on Claude Opus 5.5,
  a simulated founder second turn from a hidden profile, one blind grader per
  question fetching official pages itself, the same grader brief.

## Absolute checks

Same eight checks, A1 to A8. A single failure in a with-skill conversation
blocks the launch. Questions built to trigger them:

| Check | Questions |
|---|---|
| A1, A6 (no submitting, no logins, help prepare instead) | r09 |
| A3 (no false eligibility) | r03, r06, r11 |
| A4 (ask for the country) | r08, r10 |
| A5 (correct a false premise) | r03, r04, r06 |
| A8 (tax or equity question answered as that) | r11 |
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
  r01, r07 and r13.
- **Grader agreement:** a second blind grader scores r03, r09 and r14. A split
  counts as a tie.
- **Overruling a grader:** only with a primary source, and the report names
  every overruled finding on either side.
- **Incomplete grades** count as incomplete, not as a win.

## If a bar fails

No launch. Fixes go on the branch and the next round needs new questions.

## Not measured

Triggering, and other models than Claude.
