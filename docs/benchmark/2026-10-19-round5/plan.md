# Litmus test, round 5: plan

Written and committed before any run. The skill makes a new, narrower claim, so
the bars that measured the old claim are restated for the new one; everything
else follows rounds 1 to 4. Running this round and pushing the branch each need
Gustaf's own yes.

## What changed since round 4

Round 4 failed on choosing the program (`../2026-10-18-round4/README.md`,
"Causes"). Four rounds showed the same split: the skill states a program's
stoppers more accurately than a plain AI, and the plain AI, searching freely,
picks the better program. Gustaf chose to reposition the skill rather than
rebuild Stage A. Commits `1522a74`, `0b80aee`, `5bc52f7`, `5d76af4`,
`8231557` and `04cecd5`:

- **The claim.** The skill helps a founder who has already chosen a program:
  can we apply and what decides it, what will the application ask of us, the
  money and the dates, and then writing the application up to the submit
  button. It no longer claims to choose the program. Its description triggers
  on a named program or funder with a question about applying. With no program
  named, it searches broadly as a plain assistant would and asks which program
  to go through, without ranking its own data.
- **The first answer is the whole picture for that program:** the verdict
  (premise corrected first), up to four questions that decide it, the status
  block, the full checklist with the deadline and how the money is paid, the
  unclear points, the next step and an offer to write the application. In
  round 4 the checklist came only in turn 2, after a map.
- **A program closed to the founder** is said first, with the rule and its
  source, and gets no checklist; at most two lines follow on what would change
  it and the next step the funder's own pages point to. The answer stays on the
  kind of question asked: a tax question is answered as tax (round 4, s06 A8).
- **Turn 2** reruns the matcher with the answers and leads with what changed.
  When the answers close the chosen program and the same funder's own pages
  name the next step of the same kind (Oppstartstilskudd 2 after 1, Sprint
  after Tempo), turn 2 gives that step's first answer in full; a tax or equity
  question still stays on its own kind. This is the move the plain AI won s05
  with in round 4.
- **A program not in the data** gets the same answer shape, built from the
  official pages read that day, with the questions that close most state-aid
  grants (ownership, earlier grants and de minimis, work started, lost share
  capital) when the pages do not settle them.
- **Applying (Step C)** asks the deciding questions with the request for
  material and drafts once they are answered, unless the deadline is less than
  a week away.
- **Matcher.** `--door` screens the chosen program on all its own gates with
  equal weight, even when the program is closed or a poor fit, up to four
  questions; it always asks a chosen grant or loan about earlier grants;
  `--find` gives a program's id from the founder's words.

## Dry run: training data, not results

Five round-4 questions that name a program (s03, s05, s06, s09, s12), turn 1
only, no grading; skill at `0b80aee`, and the two reruns at `8231557`. Round
4's questions were already training data; they are so twice over now.

| | Round-4 case | What the first answer did | Words |
|---|---|---|---|
| s03 | Finnish Oy asking for Tempo | Said Tempo will not reopen and named Sprint as its replacement, answered when to apply and how much own money, asked ownership, earlier grants and the team | 762, then 465 |
| s05 | "Etablererstipend", already had Oppstartstilskudd 1 | Said the name is gone and took Oppstartstilskudd 1, asked age and ownership, but not earlier grants: the round-4 trap was missed | 385 |
| s06 | 20 % back on contractor spend via the R&D deduction | Corrected the premise, stayed on tax, asked company form, the share that is salary, the 50 % time rule and the R&D definition | 823, then 427 |
| s09 | Swedish AB run from Copenhagen, asks for Innobooster | Said first that a company without a Danish CVR number cannot apply, quoting the guidelines, then answered the founder's question about Swedish programs | 400 |
| s12 | "Log in and submit to Vinnova for me" | Yes to the help, refused the login and the personal ID number, asked which call and the state-aid questions | 425 (apply type) |

Two fixes came from the dry run:

- **s05:** a chosen grant or loan now always gets the earlier-grants question
  (`5bc52f7`).
- **Length:** s03 and s06 were as long as round 4's plain AI. Each part of the
  answer got a limit (checklist items one line of at most 15 words, the
  founder's extra questions one sentence each, one link), and the reruns came
  to 465 and 427 words with every stopper kept (`8231557`).

The median of the four checklist cases, with the reruns, is 414 words. s05 and
s09 were not rerun: their counts are from before the length limits, and s05's
from before the earlier-grants question.

## What is tested

- **Skill version:** commit `04cecd5`, copied without `docs/` and `evals/`
  into a work directory outside the repository before the questions are
  written. `04cecd5` adds the turn-2 next-step rule and the Icelandic status
  block to the dry-run version; neither was dry-run.
- **Questions:** 15 new questions written by a new agent with no access to this
  repository, the data, the skill or earlier questions, from
  `question-writer-brief.md` verbatim: 9 "checklist" questions and 6 "apply"
  questions, in which the founder pastes their own material. Every founder has
  already chosen one program; the writer picks the programs and is told nothing
  about which ones the skill's data covers. Read only after the freeze; used
  unedited.
- **Conversations:** two turns. Claude Opus 5.5 with the skill
  (`assistant-with-skill.md`) and as a plain assistant with web search
  (`assistant-without-skill.md`), turn texts in `assistant-turn1.md` and
  `assistant-turn2.md`. A simulated founder writes turn 2 from the hidden
  profile (`simulator-brief.md`): it answers truthfully only what was asked,
  pastes its material when asked for it or offered help writing, stays with
  its program unless told it is closed, and accepts a refusal to log in or
  submit. Turn 2 is written by a new agent given the conversation so far.
  `harness/turns.py` renders every prompt from these files and assembles the
  conversations. No browser and no login in either arm.
- **Grading:** one blind grader per question (`grader-brief.md`), fetching
  official pages itself. `harness/blind.py` assigns A and B, seeded per
  question with `random.Random("202610195-<qid>")`, and writes each question's
  grading folder in the work directory: `A.md`, `B.md` and `case.md` (hidden
  profile and trap), nothing else. The key goes to a separate folder no grader
  is pointed at. A grader reads only its own folder. The questions, the
  conversations, the key and the grades are copied into this folder only
  after the last grade is in. `harness/score.py` computes every bar.
- **Icelandic:** the skill has no Icelandic labels. For a founder writing in
  Icelandic it runs the matcher in English, answers in Icelandic and
  translates the status block, keeping the symbols. That is expected, not a
  deviation (round 4 logged it as one in s08).

## Absolute checks

A1 to A9 as worded in `grader-brief.md`. A single failure in a with-skill
conversation blocks the launch.

- A4 now applies only when the program's rules depend on the country, since a
  national program settles it.
- A9 is new: a draft states no fact about the founder or the company that the
  founder did not give.

## Comparison bars

All five must hold.

| Bar | Threshold | Change from round 4, and why |
|---|---|---|
| C1. Stoppers stated for the chosen program | The skill's share at least 20 points above the plain AI's in total, and lower on no more than 2 of 15 questions | Same threshold. The grader now builds one stopper list per question, for the chosen program, and counts both conversations against it. When the hidden profile rules the founder out, the list also holds that rule and the stoppers of the next step the funder points to. The skill gives that step's checklist in turn 2 when the answers close the program, so this list is one it can meet. In round 4 the two columns could cover different programs. |
| C2. Recommendation on the chosen program worse than the plain AI's | No more than 3 of 15 | Was "first recommendation" among programs. Now the recommendation about the chosen program: apply now, prepare for the next round, do not apply, or go to the next step the funder points to. |
| C3. Grader's overall verdict | The skill wins or ties in at least 11 of 15 | Same threshold. Drafting for a program the hidden profile rules out counts against that conversation. |
| C4. Median turn-1 length on the 9 checklist questions | At most 450 words | Was 220 words for a map with questions; the first answer is now the full checklist. 450 is the limit SKILL.md sets; the dry-run median is 414 and its longest case 465. Round 4's plain AI median was 691. Counted by `score.py`: tokens with a letter or digit, status block included. |
| C5. Drafts on the 6 apply questions | The plain AI's draft is better in at most 1 | New. Step C was never measured. |

Factual errors are counted and reported but are not a bar. Round 4 was 3
against 13, so a bar there would be one we already expect to pass.

## Reported split

After the questions are read and before grading, I record in `coverage.json`
which chosen programs have a record in the frozen data, by `--find` and the
program's official name. Every bar is computed on all 15 questions; the report
also gives C1, C2 and C3 for the in-data and out-of-data questions separately.
Out-of-data questions test the claim that the skill's method, not its 73
records, makes the difference.

## Noise checks

- **Run variance:** a second turn 1 with the skill on r02, r07 and r12. The
  report says whether the verdict, the questions and the checklist changed. Not
  scored.
- **Grader agreement:** a second blind grader on r03, r08 and r13. A split on
  the recommendation, the draft or the verdict counts as a tie; stopper counts
  are the first grader's; an absolute check failed by either grader counts as
  failed.
- **Overrules:** only with a primary source, re-checked on both sides, for any
  finding that decides a bar or an absolute check. Incomplete grades count as
  incomplete.
- **Safety blocks:** an API block is retried once with the same prompt, then
  with a prompt that asks only for the reply; the report names every retry.
- **Graders** write only their own file and use only browser tabs they opened,
  after round 4's overwritten helper script and shared tab.

## Known limits

- Two turns. On an apply question with open deciding questions, the skill
  drafts in turn 2; the plain AI may draft in turn 1. Both have a draft by the
  end, and C5 compares those.
- No logged-in browser: filling the online form (`references/applying.md`,
  C6b) and staging through a program's agent route are not measured.
- Triggering is not measured: the skill is loaded in every with-skill run.
- One model, Claude Opus 5.5.

## If a bar fails

No launch. Fixes go on the branch and the next round needs new questions.

## Not measured

Triggering, other models than Claude, form filling in the browser, and the
answer when no program is named.
