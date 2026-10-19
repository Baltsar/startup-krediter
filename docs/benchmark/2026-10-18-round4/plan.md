# Litmus test, round 4: plan

Written and committed before any run. Same method and the same bars as rounds
1 to 3 (`../2026-10-17/plan.md`, `../2026-10-17-round2/plan.md`,
`../2026-10-17-round3/plan.md`), on a new set of questions.

## What changed since round 3

Round 3 failed on the founder's own situation and on depth before breadth
(`../2026-10-17-round3/README.md`, "Causes"). Commits `cdf1d5d`, `a32bc49`,
`e9b2e58`, `e04dad5` and `631fd09`:

- **Screen before matching.** The matcher takes the founder's situation:
  ownership by another company or a public body, grants held and still
  running, a full-time job kept elsewhere or full-time work in the company,
  paid staff, a university affiliation, personal data, lost share capital,
  work already started, a product already sold, de minimis aid, and the
  programs the founder named. Its output has a `screen`: up to three
  questions that decide the most of the best doors, with one slot for a basic
  fact (legal form or company age) and two questions no rule covers (a
  university link for an early founder, and whether data is really anonymous
  in health). "Anonymised" in the founder's words is not accepted as a fact.
- **Map, then deepen.** The output has `routes` (grants, tax relief, loans,
  compute, credits, equity, support) in the order of the founder's needs, a
  named program first in its route. Stage A shows at most four route lines and
  the screen questions instead of three door lines and one question. Stage B
  reruns the matcher with the answers; a door the answers close is named as
  closed and the best open door of the route is given in full. When the
  country is missing, the screen's basic and university questions are asked
  with it.
- **Gates for traps, from official pages.** 38 records gained situation gates
  read on 2026-10-18: the EU SME ownership test (under 25 %, or the group
  within the limits, public bodies included) and its small-enterprise variant,
  Vinnova's own group and share-capital rules, work not started before the
  application, earlier or running grants (Business Finland under five years,
  Innowwide by year, EIC concurrent projects, Rannís one active grant,
  InnoFounder once), full-time founders (starttiraha, InnoFounder, Sprint),
  paid staff for the Swedish R&D deduction, de minimis room and firms in
  difficulty. Fixes found on the way: starttiraha no longer requires "no
  company yet", EIFO Matchlån matches business angels, Rannís Fræ allows five
  years, Chalmers Startup Camp needs research from western Sweden.
- **Not changed: coverage.** The data still has 73 records and one web search
  a turn. Round 3's plain AI named 27 relevant programs the skill did not.
  This is the main remaining risk to C2 and C3.

## Round 3 is training data now

The screen weights, the basic-fact slot, the named-program weight and the
regression tests (`tests/test_round3_screen.py`) were tuned on round-3 first
messages. A turn-1 dry run on six of them (s03, s06, s07, s11, s13, s15,
no grading) gave a median of 187 words (44 to 202). The trap's question
appeared in five of six; s11 asked only for the country, which the last fix
addresses. Round-3 questions must not be reused.

## What is tested

- **Skill version:** commit `631fd09`, frozen as a copy without `docs/` and
  `evals/` before the runs.
- **Questions:** 15 new questions in `questions.json`, written by a new agent
  with no access to this repository, the data, the skill or earlier questions,
  and used unedited. Same case types and language mix as round 3, the same two
  extra asks (at least two founders name an amount; at least one has earlier
  funding from the funder they ask about), and the same instruction to put a
  trap a careful assistant should find into every hidden profile. The
  question writer gets no list of the traps the skill now screens for. Read
  only after the skill is frozen.
- **Step C is not measured.** A question that asks for help writing or filling
  in an application is answered, but the bars score Stage A and Stage B only.
  Step C needs its own pre-registered round.
- **Everything else is as in rounds 1 to 3:** Claude Opus 5.5 with the skill and
  as a plain assistant with web search; a simulated founder second turn from
  the hidden profile that answers truthfully only what the assistant asked and
  otherwise asks about the first option offered; one blind grader per question
  fetching official pages itself; the same grader brief.

## Absolute checks

Same eight checks, A1 to A8. A single failure in a with-skill conversation
blocks the launch.

## Comparison bars

Unchanged. All four must hold.

| Bar | Threshold |
|---|---|
| C1. Stoppers stated for the program discussed | The skill's share at least 20 points above the plain AI's in total, and lower on no more than 2 of 15 questions |
| C2. First recommendation worse than the plain AI's | No more than 3 of 15 |
| C3. Grader's overall verdict | The skill wins or ties in at least 11 of 15 |
| C4. Median length of the first answer | At most 220 words |

## Noise checks

As in round 3: a second first turn on s01, s07 and s13; a second blind grader
on s03, s09 and s14; overrule only with a primary source, re-checked on both
sides for any finding that decides a bar or an absolute check; incomplete
grades count as incomplete. An API safety block is retried once with the same
prompt, then with a prompt that asks only for the reply; the report names
every retry.

**Known limits:** two turns. The screen asks its questions in turn 1 and the
answers arrive in turn 2, so the full checklist for the right door comes in
turn 2 at the earliest, and later when the country must be asked first (A4).
C1 counts stoppers stated for the program discussed, so a turn spent on the
screen can lower it.

## If a bar fails

No launch. Fixes go on the branch and the next round needs new questions.

## Not measured

Triggering, other models than Claude, and Step C.
