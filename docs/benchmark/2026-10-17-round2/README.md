# Litmus test, round 2: result

**Verdict: not ready to launch.** The fixes from round 1 worked on what they
targeted: short first answers, no leaked notes, currency codes, fewer filler
doors. The skill still failed three of the five bars in [`plan.md`](plan.md),
on 15 new questions it had never seen.

| Bar (pre-registered) | Threshold | Round 1 | Round 2 | |
|---|---|---|---|---|
| Absolute checks | 0 failures | 1 | 2 (r02 A3, r06 A2) | **fail** |
| C1. Stoppers stated, skill vs plain AI | at least +20 points, lower on at most 2 | 81% vs 40%, lower on 1 | 71% vs 36%, lower on 2 (r01, r10) | pass, at the line |
| C2. First recommendation worse than plain AI | at most 3 of 15 | 6 | 4 (r02, r06, r08, r13) | **fail** |
| C3. Skill wins or ties | at least 11 of 15 | 11 | 9 (8 wins, 1 tie) | **fail** |
| C4. Median first-answer length | at most 220 words | 237 | 193 (plain AI: 492) | pass |

Without r07, which overlaps a round-1 question (see `plan.md`), C3 is 8 of 14
and C2 is 4 of 14. The verdict does not change.

## Setup

As in round 1. Fifteen questions written by an agent with no access to the
repository (`questions.json`), used unedited. Each ran on Claude Opus 5.5 with
the skill frozen at `870589b`, and as a plain assistant with web search. A
founder simulator answered each first reply from a hidden profile. One blind
grader per question fetched the official pages itself; a second grader scored
r03, r09 and r14. All 33 conversations, 18 grade files, the grader brief and
the blind key are in this folder.

## Per question

| | Case | Stoppers, skill | Stoppers, plain | Better first pick | Verdict |
|---|---|---|---|---|---|
| r01 | Swedish AB, salary grant, parental leave | 5 / 16 | 8 / 16 | tie | plain |
| r02 | Finnish Oy, rejected by BF last spring | 14 / 16 | 4 / 12 | plain | plain |
| r03 | Norwegian ENK, wrong program name | 12 / 13 | 7 / 13 | tie | skill (both graders) |
| r04 | Danish game studio, GPU, NIMBI | 14 / 15 | 6 / 13 | skill | skill |
| r05 | Icelandic repeat founder, Sproti | 12 / 15 | 4 / 15 | tie | skill |
| r06 | US C-corp opening a Swedish AB | 11 / 16 | 8 / 16 | plain | plain |
| r07 | Lives in Malmö, company is a Danish ApS | 15 / 17 | 5 / 17 | tie | skill |
| r08 | Norwegian student, no company | 4 / 10 | 1 / 10 | plain | plain |
| r09 | Aalto postdoc asks AI to submit | 15 / 16 | 7 / 16 | skill | skill (both graders) |
| r10 | "Ltd", no country, Azure credits | 4 / 15 | 3 / 4 | skill | skill |
| r11 | Father's money into a sole trader: tax | n/a | n/a | tie | tie |
| r12 | Danish volunteer association, AI credits | 9 / 9 | 1 / 6 | skill | skill |
| r13 | Norwegian defence startup, team in Sweden | 6 / 8 | 3 / 8 | plain | plain |
| r14 | Farmers' cooperative in Jämtland | 11 / 11 | 6 / 18 | tie | plain (both graders) |
| r15 | Moving from Berlin, register where? | 11 / 25 | 5 / 25 | skill | skill |

When the two conversations detailed different programs, the stopper lists
differ in length. Factual errors the graders found: 5 with the skill (one
overruled below), 11 without. Absolute-check failures without the skill: 5
(r05 A3; A2 in r07, r08, r10 and r15).

## What the skill did well

- **No submitting.** In r09 it declined to submit to Business Finland and
  offered to draft instead. It also found that the R2B call had closed on 16
  September, which the plain AI missed.
- **Stoppers before the form.** On the program the founder ends up discussing,
  it named 71% of what stops an application, against 36%. Clear cases: r04
  (14 of 15 for NIMBI, including the AI risk assessment), r07 (15 of 17 for
  Vinnova), r12 (9 of 9 for Microsoft's nonprofit grant).
- **Tax answered as tax.** In r11 it did not push grants and explained gift,
  loan and ownership.
- **Shorter.** Median 193 words in the first answer, against 492.

## What fails

1. **Wrong eligibility.** The skill made two of the mistakes it exists to
   prevent:
   - r06: it said Vinnova counts the whole group's employees, so 11 US staff
     rule the founder out. Vinnova's page applies the group rule only to
     listing, turnover and balance sheet. The data never said otherwise; the
     model inferred it.
   - r02: it told a Finnish founder Sprint "fits on what we know". The founder
     had a Tempo grant in 2023, which bars Sprint. The founder had said they
     applied to Business Finland before, and the skill did not ask about
     earlier funding.
2. **Too slow to arrive.** In r01 the country was evident (Uppsala, "bolag",
   Vinnova), yet the skill asked for it, then asked for the company's age, and
   never gave the checklist in two turns. The plain AI meanwhile caught that
   the project lead must be employed, which stops this founder. r10 is
   different: there the country was truly unknown, asking was required (A4),
   and the skill was right to ask. In a two-turn test any needed question
   means the checklist never appears, which is part of why r10 is low on C1.
3. **The small door instead of the real one.** In r14 the skill detailed the
   EIP group grant (80 000 to 120 000 SEK) when the founders need about
   1.5 MSEK, which only the EIP project grant pays. In r13 it led with
   SkatteFUNN, which the founder already has, and missed the defence money the
   founder asked for.
4. **Missing programs.** The plain AI named 23 relevant programs the skill did
   not, and the skill named 21 the plain AI did not. The skill's largest gaps: defence funding (NATO DIANA, EDF and EUDIS, LINC,
   Brave-Norway, Vinnova civil-military) in r13, university idea grants for
   students without a company (UiB idé and others) in r08, and the R&D
   employer-contribution reduction in Sweden in r10.

## Noise checks

- **Run variance.** r07: the same three doors in the same order both times.
  r01: the first run asked only for the country; the second gave three doors
  with Vinnova first. r13: Sigma2 first in one run, SkatteFUNN first in the
  other. Single-run results should be read with that in mind.
- **Grader agreement.** The second grader agreed with the first on r03
  (skill), r09 (skill) and r14 (plain).
- **Overruled findings.**
  - r10, against the skill, **overruled**. The grader failed the skill (A2)
    for giving Vinnova Avancerad digitalisering, AI as 1 to 10 MSEK, citing an
    older AI call that closed in January 2026. Vinnova's page for
    "Cybersäkerhet, AI och resiliens", fetched 17 October 2026, says "1-10
    miljoner kronor" and "Stänger den 19 januari 2027 kl 14:00". r10 counts as
    a pass on A2 for the skill.
  - r06, against the skill, **upheld**. Vinnova's page for Innovativa Startups
    2026 says the group must meet "kraven gällande börsnotering och storlek,
    se krav 3 och 4", and separately "Sökande företag får ha högst 10
    anställda". The skill's claim is wrong.
  - r02 (A3) is a judgment on the hidden profile, not a fact a page can
    settle, so it stands.
- **Fairness.** Only findings against the skill were re-checked against a
  primary source. Findings against the plain AI were not. Neither changes the
  verdict: C2 and C3 fail either way.
- **Blind key.** A script error lost the key for r01 to r06 before grading.
  It was rebuilt by matching each blind file to its source answer, and it
  agrees with every entry that had been saved.

## Causes, and what to fix

- **State the group rule per requirement in the data.** Add to the Vinnova
  Innovativa Startups record that the 10-employee cap applies to the applying
  company only. More generally: the skill must not extend a rule beyond what
  the page says.
- **Ask about earlier funding before saying "fits".** When a door excludes
  earlier grants from the same funder, and the founder has mentioned that
  funder, the deciding question is about earlier funding.
- **Answer first when the message settles the profile.** When the country is
  stated or strongly evident, Stage A should give the doors and ask the
  deciding question alongside them. When the country is unknown, asking stays
  correct.
- **Use the call's own name.** In r10 the skill shortened "Cybersäkerhet, AI
  och resiliens" to "Avancerad digitalisering: AI", the name of a different,
  closed call. A founder searching for it would land on the wrong page.
- **Match the size of the need.** When the founder names an amount, a door
  that pays a fraction of it goes below the one that can pay it. In r14 that
  means detailing the EIP project grant, with the group grant as step one.
- **Data coverage.** Add defence programs (DIANA, EUDIS, LINC, Vinnova
  civil-military), Norwegian university idea grants, and the Swedish R&D
  employer-contribution reduction. Fix Almi Verifieringsmedel: the page now
  allows a simple MVP.
- **New questions again.** These 15 are spent.

## Not measured

Triggering, and other models than Claude. See `plan.md`.
