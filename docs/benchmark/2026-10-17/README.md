# Litmus test, 17 October 2026: result

**Verdict: not ready to launch.** The skill failed three of the bars set in
[`plan.md`](plan.md) before any run. It is clearly better than a plain AI at
telling a founder what will stop an application, and no better at picking the
right door first.

| Bar (pre-registered) | Threshold | Result | |
|---|---|---|---|
| Absolute checks | 0 failures | 1 failure (q08: Danish kroner written as "kr" next to Swedish amounts) | **fail** |
| C1. Stoppers stated, skill vs plain AI | at least +20 points, lower on at most 2 questions | 81% vs 40%, lower on 1 question | pass |
| C2. First recommendation worse than plain AI | at most 3 of 15 | 6 of 15 | **fail** |
| C3. Skill wins or ties | at least 11 of 15 | 11 of 15 (9 wins, 2 ties) | pass, at the line |
| C4. Median first-answer length | at most 220 words | 237 words | **fail**, narrowly |

Per the plan, the launch waits, PR Baltsar/startup-krediter#1 stays unmerged,
and the next round needs new questions.

## Setup

Fifteen founder questions, written by an agent with no access to the skill or
its data, used unedited (`questions.json`). Each ran twice on Claude Opus 5.5:
following the skill (frozen at `21c1109`), and as a plain assistant with web
search. A founder simulator answered each assistant's first reply from a hidden
profile, truthfully and only what was asked. One blind grader per question read
both conversations, fetched the official pages itself, and scored the
pre-registered checks. All 30 conversations, the 18 grade files and the blind
key are in this folder.

## Per question

| | Case | Stoppers, skill | Stoppers, plain | Better first pick | Verdict |
|---|---|---|---|---|---|
| q01 | Swedish AB, API credits | 11 / 11 | 7 / 13 | skill | skill |
| q02 | Finnish Oy, too old for startup grant | 29 / 30 | 12 / 30 | plain | skill |
| q03 | Norwegian AS, false premise | 20 / 23 | 8 / 23 | plain | tie (graders split) |
| q04 | Asks AI to submit with login | 13 / 18 | 9 / 18 | tie | skill |
| q05 | Icelandic ehf | 11 / 14 | 2 / 13 | skill | skill |
| q06 | No country given, GPU | 4 / 14 | 7 / 23 | skill | skill |
| q07 | Tax question dressed as grant | 13 / 17 | 9 / 17 | skill | skill |
| q08 | Lives in SE, company in DK | 17 / 18 | 8 / 15 | plain | plain |
| q09 | Vague one-liner, Finnish | 3 / 7 | 3 / 7 | plain | plain |
| q10 | Postdoc, no company | 4 / 4 | 3 / 3 | plain | plain |
| q11 | Norwegian association, compute | 9 / 12 | 8 / 12 | plain | plain |
| q12 | Danish sole trader, loan | 7 / 9 | 5 / 9 | tie | skill |
| q13 | NTNU students, no company | 12 / 13 | 1 / 13 | tie | skill |
| q14 | Swedish sole trader, ineligible | 19 / 22 | 8 / 22 | skill | skill |
| q15 | Funded Finnish Oy, credits | 10 / 12 | 3 / 14 | skill | tie |

Factual errors the graders found: 2 with the skill (one of them overruled below), 16 without.
Absolute-check failures without the skill: 6 (q01, q06, q07, q12, q13, q15),
mostly calling open programs closed or giving wrong amounts.

## What the skill did well

- **No submissions, no logins.** In q04 it refused both, said why, and found
  that the Friday deadline the founder believed in did not exist.
- **Ineligibility stated plainly.** In q14 it told a sole trader he cannot
  apply to Vinnova and corrected "up to a million" to 500 000 SEK.
- **False premises corrected** in q02, q03 and q07.
- **Asked for the country** instead of assuming it in q06 and q09.
- **Requirements before the form.** 81% of the stoppers across all questions,
  against 40% for a plain AI with search.

## What fails

- **Picking the door.** Six times out of fifteen the plain AI's first
  recommendation fit the founder better. The patterns:
  - Programs from the wrong country or with a fee in the top three: a Danish
    accelerator charging DKK 250 000 for a Finnish idea-stage founder (q09).
  - Long shots ahead of likely wins: a Vinnova call needing a partner the
    founder lacks, closing in twelve days, ahead of Innobooster (q08).
  - Missing programs. The plain AI named 20 relevant programs the skill did not,
    such as university verification money (q10), Uusyrityskeskus (q09), Google
    and Microsoft credits (q15) and regional Icelandic funds (q05).
- **Currency.** "200 000 kr till 5 Mkr" for a Danish program in a Swedish reply
  (q08). A founder reads that as Swedish kronor.
- **Internal notes leak to founders.** Lines such as "this program is missing
  from our list and should be added" appeared in six of fifteen replies (q05, q07, q09, q10, q12, q13).
- **Length.** The first answer is short for most questions but runs long when
  the founder names one program (q03: 847 words).

## Noise checks

- **Run variance:** the first recommendation stayed the same on q08 and q15 and
  changed on q01 (AWS Activate first in one run, NVIDIA Inception in the other).
  Single-run results should be read with that in mind.
- **Grader agreement:** a second blind grader agreed on q10 and q13 and
  disagreed on q03 (tie versus skill). Per the plan, q03 counts as a tie.
- **A grader overruled by a primary source:** the first q13 grader failed the
  skill for calling Eurostars closed. Eureka's own page shows Call 12 opening on
  17 December 2026, so the skill was right. The second grader agreed. This is
  recorded in `grades/q13.json` and `grades/q13-g2.json`.
- **Fairness:** only that finding, which went against the skill, was re-checked
  against a primary source. Findings against the plain AI were not re-checked.
  The verdict does not depend on it, because q08 blocks the launch either way.

## Causes, and what to fix before the next round

Three of the failures come from rules in `SKILL.md` itself:

- **Leaked internal notes.** Step 3 tells the assistant to "mention in one line
  at the end of the answer that the door is missing from the data". That rule
  produced every "should be added to our list" line. Delete it.
- **Long first answers.** The rule "if the founder named one specific program,
  skip Stage A" sent q02, q03, q04, q07 and q14 straight to the full checklist,
  at 517 to 847 words. Those five set the median. Give a short verdict first in
  that case too.
- **Filler doors.** "Top three doors" is read as "always three", which is how a
  Danish fee-charging accelerator and EIC Accelerator reached idea-stage
  founders (q09, q13). Say that one or two doors are fine when nothing else fits.

The rest needs data and ranking work:

1. Rank by realistic fit, not by rule match alone: open now, in the founder's
   country, without a fee or equity unless asked, ahead of everything else.
2. Keep foreign and fee programs out of the top three unless the founder asks.
3. Label every amount with its currency code.
4. Aim the web search step at what the data lacks for this founder's country
   and stage.
5. Write new questions for the next round, independently. These fifteen are
   spent.

## Not measured

Triggering, and other models than Claude. See `plan.md`.
