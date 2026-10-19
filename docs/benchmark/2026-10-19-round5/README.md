# Litmus test, round 5: result

**Verdict: not ready to launch.** The repositioned skill works only on a
program the founder has already chosen. On that program it was more complete
and more accurate than the plain AI, though not by the margin the plan
required:

- stoppers stated: 89% against 77%;
- factual errors: 5 against 8;
- first answer: 416 words against 626.

But it won only 9 of 15 questions. Its recommendation was worse in 7, it lost
2 of 6 drafts, and it failed an absolute check in 3 questions. Its stopper
lead was 12 points, short of the 20 the plan required, so even the claim the
repositioning kept did not hold.

In four of the six losses, the plain AI asked about or flagged the one fact
the case turned on: the project budget (r04), a founder's degree (r13), a
municipal owner (r11), a parent group (r08). The skill's questions come only
from the rules in its data, and none of those four facts was among them.

| Bar (pre-registered) | Threshold | Round 5 | |
|---|---|---|---|
| Absolute checks A1 to A9 | 0 failures | 3 questions: r08 (A3, A5), r11 (A3), r15 (A9) | **fail** |
| C1. Stoppers stated for the chosen program | +20 points, lower on at most 2 | 89% vs 77% (+12), lower on 1 (r02) | **fail** |
| C2. Recommendation worse than plain AI | at most 3 of 15 | 7 | **fail** |
| C3. Skill wins or ties | at least 11 of 15 | 9 (9 wins, 0 ties) | **fail** |
| C4. Median turn-1 length, 9 checklist questions | at most 450 words | 416 (plain AI: 626) | pass |
| C5. Drafts lost to plain AI, 6 apply questions | at most 1 | 2 (r02, r10) | **fail** |

Round 5 measured a narrower claim than rounds 1 to 4, so its numbers are not
comparable with theirs. For reference, round 4 had 4 wins or ties of 15 and
8 worse first recommendations.

## Setup

As pre-registered in `plan.md`, on the skill frozen at `04cecd5` and copied
outside the repository without `docs/` and `evals/`.

- **Questions:** 15, written by a new agent with no access to the repository
  (`questions.json`), and read only after the freeze. 9 were checklist
  questions and 6 asked for help applying.
- **Data coverage:** 14 of the 15 chosen programs have a record in the frozen
  data, three of them under an old name (SNIC, Tempo, etablerertilskudd). Only
  Rannís Sproti (r15) is missing (`coverage.json`).
- **Conversations:** Claude Opus 5.5, with the skill and as a plain assistant
  with web search. Two turns, with a simulated founder writing turn 2 from the
  hidden profile.
- **Grading:** one blind grader per question, plus a second grader on r03,
  r08 and r13. `harness/score.py` computed every bar.

All 30 conversations, the three turn-1 reruns, the 18 grades with their full
reports and the blind key are in this folder.

## Per question

| | Case | Type | Stoppers skill / plain / total | Better recommendation | Better draft | Verdict |
|---|---|---|---|---|---|---|
| r01 | Forskningsavdrag; the CEO spends 20 % on R&D | checklist | 11 / 9 / 11 | skill | | skill |
| r02 | Vinnova Innovativa Startups; consultancy already ordered | apply | 15 / 20 / 23 | tie | plain | skill |
| r03 | "SNIC" for a company; NAISS is academic only | checklist | 17 / 14 / 20 | plain (both graders) | | skill (both) |
| r04 | Almi innovationslån, 500k on an 800k project | checklist | 17 / 14 / 18 | plain | | plain |
| r05 | EIC Accelerator; the applicant is a Delaware Inc. | apply | 14 / 9 / 16 | skill | skill | skill |
| r06 | Business Finland "Tempo"; replaced by Sprint | checklist | 22 / 18 / 22 | tie | | skill |
| r07 | Starttiraha; full-time business already started | apply | 10 / 9 / 12 | tie | skill | skill |
| r08 | LUMI AI Factory; 100 % owned by a 2,400-person group | checklist | 15 / 11 / 16 | plain (both) | | plain (both) |
| r09 | SkatteFUNN; older than three years, half the equity lost | checklist | 12 / 11 / 13 | skill | | skill |
| r10 | "Etablerertilskudd" for an ENK | apply | 17 / 14 / 20 | plain | plain | plain |
| r11 | AWS Activate; 66 % owned by a municipal energy group | checklist | 12 / 11 / 13 | plain | | plain |
| r12 | Innobooster; no financial foundation | apply | 17 / 17 / 17 | plain | skill | plain |
| r13 | InnoFounder; one founder has 90 ECTS | checklist | 12 / 12 / 13 | plain (both) | | plain (both) |
| r14 | Eurostars; one participant holds 78 % of the budget | checklist | 21 / 16 / 25 | skill | | skill |
| r15 | Rannís Sproti (not in the data); window closed | apply | 20 / 18 / 23 | tie | skill | skill |

Stopper counts are the first grader's. On checklist questions where the
founder accepted the offer to write, the graders also judged the draft. Those
judgments are not part of C5.

## In the data or not, as pre-registered

| | Questions | C1 stoppers, skill vs plain | C2 worse | C3 wins or ties |
|---|---|---|---|---|
| Program has a record in the frozen data | 14 | 89% vs 77% | 7 | 8 |
| Program has no record (r15, Rannís Sproti) | 1 | 87% vs 78% | 0 | 1 |

The question writer chose programs the data mostly covers, so the split has
a single out-of-data question. One question cannot show that the skill's
method, rather than its 73 records, makes the difference. r15 is also one of
the three absolute failures (A9).

## What the skill did well

- **Completeness and accuracy.** It stated more stoppers in 12 of 15
  questions, as many in 2 and fewer in 1. It made 5 factual errors to the plain AI's 8,
  and its first answer was a third shorter.
- **Wrong premises about the program.** It corrected the ones the founders
  stated: Tempo replaced by Sprint, SNIC by NAISS, etablerertilskudd by
  Oppstartstilskudd 1, Innobooster's 35 % against the founder's half, AWS's
  100k against the real tiers. The premise it missed was about the founder
  (r08, below).
- **Logins and submitting.** Where founders offered a login or an ID number
  (r07, r12), it declined. No conversation with the skill failed A1 or A6.
- **Programs outside the data.** The one such program, Rannís Sproti (r15),
  was built from the official pages and won on the verdict. Its draft failed
  A9 (below).
- **Cases it won:**
  - r01: the CEO's R&D share is too small for the deduction.
  - r05: the Delaware Inc. cannot apply.
  - r09: SkatteFUNN is closed to a firm in difficulty.
  - r14: one participant holds too much of the Eurostars budget.

## What fails

1. **The questions follow the data's rules, not the program.** The skill asks
   what the matcher's `screen` returns, and the screen asks only about the
   record's eligibility rules. In four losses the deciding fact was not among
   them:
   - In r04 and r13 the fact was in the record's checklist, but not in its
     rules.
   - In r08 and r11 it was in neither.

   Each time the skill did not ask about it, and the plain AI did, or at
   least flagged it.
   - **r08:** the LUMI AI Factory record checks headcount but not group
     ownership, so the skill asked about legal form and a university link. It then told a wholly owned subsidiary
     of a 2,400-person group that it met the conditions for free access.
     Failed A3 and A5.
   - **r11:** AWS Activate's record has no rule for government-owned
     companies, which its terms exclude. The skill asked about company age, a
     university link and an Activate Provider, never about the owners. It
     then recommended Founders and drafted the application. Failed A3.
   - **r13:** the 120 ECTS requirement is in the record's checklist, not its
     rules, and the skill never asked each founder's education. The plain AI
     asked in its first reply and found that one founder has 90 ECTS.
   - **r04:** Almi's 50 % rule is in the record's checklist, but no rule asks
     the project's total cost, and the skill never did. It built the draft on
     500k against a project of at least 1 MSEK. The plain AI asked, and found
     that 400k is the most the founders can get.
2. **Drafting before eligibility is settled, and refusing to draft when it
   can be fixed.**
   - **r12:** the skill wrote the full Innobooster application while the
     financial-foundation rule was still open. Under the hidden profile it
     fails that rule.
   - **r10:** the opposite. The skill followed "never draft for a program
     the answers close" and wrote no application for an ENK, though the
     founder asked twice. The plain AI drafted for the AS she has to found
     first, and the grader judged that the useful answer.
3. **Recommendations without the founder's own goal.** In r03 the plain AI
   fitted its advice to when the founder needs compute (January), and in r04
   to the project's real size. The skill's recommendation followed the
   program's rules alone.
4. **One invented fact in a draft (r15, A9).** The Sproti draft claims a
   catch-quality outcome dataset the founder never mentioned. The plain AI's
   drafts failed A9 in three questions (r02, r05, r10), so drafting from
   partial material is a risk for both. But the skill's bar is zero.

## Noise checks

- **Run variance.** The reruns of turn 1 on r02, r07 and r12 opened the same
  way and asked mostly the same deciding questions. Two of them differed in
  what came next:
  - **r02:** the rerun drafted at once (1 253 words) where the first run
    asked first and drafted later (482 words).
  - **r07:** the rerun asked two questions and listed eight things to send,
    where the first run asked four questions.
- **Grader agreement.** The second graders on r03, r08 and r13 agreed with
  the first on the recommendation, the draft and the verdict in all three.
  - Stopper totals differed by up to 6 (r13: 13 against 19).
  - On r08 the second grader also scored A2 as a fail for the skill. The
    first grader had A5 instead. Both failed A3.
- **Re-checks.**
  - **Absolute checks:** they fail in three separate questions, so no single
    finding decides that bar. The failures in r08 and r11 rest on the hidden
    profile and on rules the grader cites from official pages: the SME group
    test and AWS's government-entity clause.
  - **C1, C2 and C3:** these miss by 8 points, 4 questions and 2 questions,
    so no single finding decides them either.
  - **C5:** this misses by one. It turns on one judgment about a draft (r02
    or r10), and no primary source can overrule a judgment, so it stands,
    as s06 A8 did in round 4.

  No re-check was run, and findings against the plain AI were not
  re-checked.
- **Deviations.**
  - Each agent got a one-line pointer to its prompt file rendered by
    `harness/turns.py`, instead of the text inline. The file holds the
    rendered prompt word for word.
  - The subagents had an advisor tool in both arms. It was often
    rate-limited.
  - Graders started per question once both arms of that question were done.
    They used the harness's own functions to build each question's grading
    folder. Afterwards, `turns.py assemble` and `blind.py` on a copy rebuilt
    the same conversations, grading folders and key, byte for byte.
  - Work files outside the reply files:
    - r15 turn 1 with the skill saved three web downloads to a shared `web/`
      folder in the work directory. It listed the folder's other file names
      without opening them.
    - r12 turn 1 and r02 turn 2 with the skill wrote scratch files outside
      the reply folders.
  - r12 turn 2 without the skill used Bash (curl and pdftotext) to read a web
    PDF. Its brief allowed only web search and fetch.
  - No API safety block occurred, so no run was retried.

## Causes

Repositioning did not hold even the claim it kept. The skill still names more
of what stops the founder, with fewer errors, in a shorter first answer. But
the margin is 12 points against the 20 required, smaller than round 4's 17
(72% vs 55%). Given a single program, the plain AI reads the same pages and
closes most of the gap.

What remains is the same weakness as in round 4, moved inside one program.
The plain AI asks the founder about the fact the case turns on: budget, degree,
owner, timing. The skill asks the questions its 73 records know to ask. Where
a record is thin, the skill is confident and wrong (r08, r11). That is worse
than the plain AI's "you probably qualify, check SME status".

## Options

This is a product decision.

- **Fix the questions, then round 6.** For a chosen program, ask from the
  program's own pages, not only from the record. That means asking:
  - who owns the company, every time;
  - what the founder needs, how much and by when, against the project's size;
  - every personal requirement the page names, such as a degree, residence
    or full-time work;
  - and dropping the university question unless the page makes it matter.

  Draft only once the deciding questions are answered. When the founder can
  fix the block, as with founding an AS, draft for the fixed state. This is a
  narrow change to SKILL.md and the matcher's chosen-program screen, but it
  is the fifth round of fixes to how the skill asks.

  Better questions target C2, C3 and A3. Nothing in this round shows they
  would add the 8 points C1 lacks.
- **Ship the checklist alone.** Release only a checklist and drafting help,
  with no verdict on eligibility. No bar measured that, and C1, the closest
  bar, failed.
- **Stop.**

## Not measured

Triggering, models other than Claude, filling the form in a browser, staging
through a program's agent route, and the answer when no program is named.
