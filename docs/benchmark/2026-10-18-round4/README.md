# Litmus test, round 4: result

**Verdict: not ready to launch.** The redesigned first answer asks about the
founder's own situation, and by my reading it raised the trap in 12 of 15
first answers. The skill was again more accurate than the plain AI: 3 factual
errors against 13, and an absolute-check failure in 1 question against 5. But
it won or tied only 4 of 15 questions, and the plain AI's first
recommendation was better in 8. Finding the trap did not translate into
reaching the right door.

Each round used new questions, and round 3's questions were used to tune this
round's screen. Read the round columns as four separate tests, not as a
trend.

| Bar (pre-registered) | Threshold | Round 1 | Round 2 | Round 3 | Round 4 | |
|---|---|---|---|---|---|---|
| Absolute checks | 0 failures | 1 | 2 | 4 questions | 1 question (s06 A8) | **fail** |
| C1. Stoppers stated, skill vs plain AI | +20 points, lower on at most 2 | 81% vs 40% | 71% vs 36% | 87% vs 46% | 72% vs 55%, lower on 3 (s01, s02, s14) | **fail** |
| C2. First recommendation worse than plain AI | at most 3 of 15 | 6 | 4 | 7 | 8 | **fail** |
| C3. Skill wins or ties | at least 11 of 15 | 11 | 9 | 4 | 4 (2 wins, 2 ties) | **fail** |
| C4. Median first-answer length | at most 220 words | 237 | 193 | 192 | 193 (plain AI: 691) | pass |

s12 asks for help submitting an application, which is Step C. The plan
scores Stages A and B only, but the grader scored the whole conversation.
Without s12, C3 is 3 of 14. No bar changes either way.

## Setup

As in rounds 1 to 3, on the skill frozen at `631fd09` as a copy without
`docs/` and `evals/`. Fifteen questions written by a new agent with no access
to the repository (`questions.json`), read only after the freeze. Claude Opus
5.5 with the skill and as a plain assistant with web search; a simulated
founder second turn from the hidden profile; one blind grader per question
fetching official pages itself; a second grader on s03, s09 and s14. All 33
conversations, 18 grade files, the grader brief and the blind key are in this
folder.

## Per question

| | Case | Stoppers, skill | Stoppers, plain | Better first pick | Verdict |
|---|---|---|---|---|---|
| s01 | Logistics SaaS 70% owned by a listed group, AI project with a university | 16 / 24 | 18 / 24 | tie | tie |
| s02 | "Any free GPU?" from two DTU students without a company | 3 / 20 | 15 / 20 | plain | plain |
| s03 | Finnish Oy that thinks Tempo still exists | 18 / 21 | 13 / 21 | tie (both graders) | plain (both graders) |
| s04 | Danish weeding-robot ApS with little de minimis room left | 16 / 16 | 11 / 16 | plain | plain |
| s05 | Norwegian AS asking for "etablererstipend", already had Oppstartstilskudd 1 | 15 / 16 | 14 / 18 | plain | plain |
| s06 | Swedish AB expecting 20% back on contractor spend | 22 / 23 | 6 / 8 | skill | skill |
| s07 | Bootstrapped Stockholm game studio, GPU and credits | 7 / 19 | 2 / 19 | tie | tie |
| s08 | Icelandic fish-vision ehf, Technology Development Fund call just closed | 15 / 16 | 10 / 15 | plain | plain |
| s09 | Swedish AB run entirely from Copenhagen, asks for Innobooster | 14 / 15 | 12 / 19 | plain (both graders) | plain (both graders) |
| s10 | Divorce and a share buyout, unspent Vinnova money | 12 / 14 | 4 / 14 | plain | plain |
| s11 | Oulu ECG medtech with a running Business Finland grant | 9 / 12 | 6 / 11 | skill | plain |
| s12 | "Log in and submit to Vinnova for me tomorrow" | 9 / 20 | 6 / 20 | skill | skill |
| s13 | Norwegian AS that has lost more than half its share capital | 12 / 14 | 5 / 11 | plain | plain |
| s14 | No country, no company, DJ stem-separation tool | 8 / 20 | 14 / 20 | tie (graders split) | plain (both graders) |
| s15 | Vasa heat-storage pilot with a binding order already signed | 16 / 17 | 11 / 31 | plain | plain |

Stopper counts are the first grader's. Each grader counted stoppers for the
program each conversation detailed most, so the two columns can cover
different programs. Factual errors found by the graders: 3 with the skill, 13
without. Absolute-check failures without the skill: A2 in s01, s02, s08, s11
and s13, and A3 in s08 and s13. Programs the plain AI named and the skill did
not: 26; the reverse: 12.

## Did the first answer raise the trap?

My reading of the 15 first answers against the hidden profiles. This is not a
graded result.

| | Trap in the hidden profile | Raised in turn 1 |
|---|---|---|
| s01 | 70% owned by a large group: not an SME | yes, the ownership question |
| s02 | Students with no company: the route is academic compute | asked about university; the skill had no academic route |
| s03 | Salaries paid before applying are not eligible | yes, "costs count only from submission" |
| s04 | Little de minimis room left | yes, the grants question; turn 2 did the arithmetic |
| s05 | Oppstartstilskudd 1 already received | yes, the grants question; turn 2 still detailed Oppstartstilskudd 1 |
| s06 | No one on payroll, so the R&D deduction gives nothing | yes, two payroll questions |
| s07 | No investor, so only the small credit tiers | yes, "bigger tiers need an investor" |
| s08 | The large Technology Development Fund call has closed | yes |
| s09 | No Danish CVR, and no real activity in Sweden | CVR yes; Swedish activity mentioned, not asked |
| s10 | It is a divorce question, and grant money cannot buy shares | yes |
| s11 | A Business Finland grant is still running | yes, the grants question |
| s12 | The founder is not the company's signatory | no |
| s13 | Firm in difficulty: SkatteFUNN closed | yes, the share-capital question |
| s14 | No company yet | yes |
| s15 | A binding order already signed: energy aid closed | no |

## What the skill did well

- **Accuracy.** 3 factual errors against 13, and absolute-check failures in
  1 question against 5.
- **Situation questions.** Ownership, grants held, payroll, share capital and
  a university link were asked before any checklist, in the founder's
  language. The plain AI asked broader questions in longer answers.
- **Short.** Median 193 words against 691.
- **Wins:** s06, where it said at once that the R&D deduction gives a company
  without payroll nothing and found the employed-project-lead rule in the
  open Vinnova call; s12, where it named the one Vinnova call actually
  closing the next day.
- **s13:** the share-capital answer closed SkatteFUNN in the skill's second
  turn, as it should.

## What fails

1. **Turn 2 follows the door the founder picks, not what the answers
   showed.** The Stage A closing line ("answer the questions, or pick a
   route") invites a pick, and the simulator picks the first door when one is
   offered. A door was picked in 9 of 15 conversations with the skill and in
   none without it. With a pick: 1 win, 2 ties, 6 losses. Without: 1 win and
   5 losses. So this is one factor, not the whole story. The clearest case is
   s05: the answer showed Oppstartstilskudd 1 had already been granted, the
   skill still gave Oppstartstilskudd 1 in full, and the plain AI moved on to
   Oppstartstilskudd 2.
2. **Coverage is unchanged.** Several losses turned on doors that are not in
   the data: GUDP outside the de minimis cap (s04), the north-east Iceland
   regional fund and the fund replacing the Technology Development Fund
   (s08), the EU Innovation Fund's SME call (s15), and Innovasjon Norge's
   innovation contracts (s05). Both sides missed the academic routes (DeiC,
   EuroHPC AI for Science) in s02. The plan named this as the main remaining
   risk.
3. **Two choices made before this round show up as specific misses.**
   - The timing questions (work already started, product on the market) were
     given half weight in the screen. The s15 binding order was never asked
     about; the plain AI asked and won.
   - A program the founder names leads its route. That makes the first door
     the one the founder already had in mind, which in s05 and s13 was the
     trap.
4. **The stoppers bar fell.** In s02 and s14 the skill's second turn was still
   a map with questions, so no checklist arrived before the conversation
   ended. In s01 the plain AI covered the R&D deduction more fully. The plain
   AI's share rose to 55%.
5. **One absolute failure, s06 A8.** The founder asked to hear more about the
   R&D deduction. The skill said in one paragraph that it does not apply,
   then gave the Vinnova call in full. That follows the new Stage B rule: when
   the picked door is closed, give the next open door in full. The grader
   judged that it pushed a grant on a tax question.

## Noise checks

- **Run variance.** In s01 the first door listed flipped between runs
  (KK-stiftelsen first in one, Vinnova first in the other). Since the
  simulator picks the first door, that changes the conversation. In s07 and
  s13 the route order held; in s07 the third screen question changed.
- **Grader agreement.** Both graders agreed on the verdict for s03, s09 and
  s14 (all plain). They split on the best first pick in s14, which counts as
  a tie, so C2 is 8.
- **Re-checks as pre-registered.** s06 A8 decides the absolute bar. It is a
  judgment on the conversation, not a fact on a page, so no primary source
  can overrule it, and it stands. No other single finding decides a bar: C2
  misses by 5, C3 by 7, and C1 by 3 points and one question. Findings against
  the plain AI were therefore not re-checked.
- **Deviations.**
  - The grader brief's list of folders not to read gained `litmus4/snapshot`.
  - The graders shared the scratchpad and the browser. Two reported an
    overwritten helper script or a browser tab taken over by another grader.
    None reported reading another grader's grades.
  - In s08 the founder simulator added a detail it was not asked for in the
    plain conversation, and said so.
  - Two skill runs left the status block non-verbatim: s09 dropped a matcher
    line it found no source for, and s08 translated the whole block into
    Icelandic, which has no labels in the skill.
  - The s01 rerun overwrote a work file from the first s01 run. No harness
    file was touched.
  - No API safety block occurred in the runs, so no retries were needed.

## Causes

Four rounds show the same split. Each fix has improved accuracy, safety and
length, and the skill now asks the situation questions a careful advisor
asks. None of that has made it pick the better door against a strong model
that searches the web freely. In round 4 the plain AI used its longer
answers to research and re-route: Oppstartstilskudd 2 instead of 1, GUDP
around the de minimis cap, a Danish ApS for the Copenhagen team, a
recapitalisation path back to SkatteFUNN. The skill's map is bounded by 73
records, and its second turn follows the founder's pick.

## Options

This is a product decision, not another round of rule fixes.

- **Reposition.** Launch the skill for what it measurably does better: the
  checklist, accuracy and safety on a program the founder has already chosen,
  and the help with applying (Step C). It would stop claiming to find the best
  door. That claim needs its own pre-registered round.
- **Rebuild Stage A as search-first.** Do the broad research the plain AI
  does (several searches, sector and regional funds), use the data only as
  verified gates and checklists, and in turn 2 re-route from the answers
  instead of following the pick. Then a round 5 with new questions.
- **Stop here.**

## Not measured

Triggering, other models than Claude, and Step C.
