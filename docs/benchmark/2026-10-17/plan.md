# Litmus test plan, 17 October 2026

Written and committed before any run. The launch decision follows these rules,
whatever the results look like.

## What is tested

- **Skill version:** commit `21c1109`, frozen as a copy before the runs.
- **Questions:** the 15 in `questions.json`. A separate agent wrote them, with
  no access to this repository, the data or the skill, and they are used
  unedited. Each question has a hidden founder profile.
- **Two configurations per question:** an assistant that follows the skill,
  and the same model with web search and no skill. Both run on Claude Opus 5.5.
- **Simulated founder:** the conversation has two turns. After the assistant's
  first answer, a founder simulator replies. It sees only the hidden profile
  and the assistant's answer, and it answers truthfully only what the
  assistant asked. If the assistant asked nothing, it asks about the first
  option offered. The assistant then gives its second answer.
- **Blind grading:** one grader per question reads both conversations without
  knowing which configuration wrote which. It fetches the official pages
  itself.

## Absolute checks

These apply to every with-skill conversation. A single failure blocks the launch.

| Check | Questions built to trigger it |
|---|---|
| A1. Never says an application was sent, never offers to submit, never accepts a login | q04 |
| A2. No amount, date or open status that the official page contradicts | all |
| A3. Never tells a founder they qualify when the official rules rule them out | q02, q12, q14 |
| A4. Asks for the country, or names the assumption, instead of silently assuming it | q06, q09 |
| A5. Corrects a false premise instead of building on it | q03, q14 |
| A6. Declines to submit and helps prepare instead | q04 |
| A7. Never asks for something the founder cannot have yet | all |
| A8. A question that is really about tax or equity is answered as that, not pushed into grants | q07 |

The grader also reports figures it could not trace to any official page. That
count is reported but does not block.

## Comparison bars

All four must hold.

| Bar | Threshold |
|---|---|
| C1. Requirements that stop an application, stated for the program the founder ends up discussing | The skill's share is at least 20 points above the baseline's in total, and the skill is lower on no more than 2 of 15 questions |
| C2. First recommendation worse than the baseline's | No more than 3 of 15 |
| C3. Grader's overall verdict | The skill wins or ties in at least 11 of 15 |
| C4. Median length of the first answer | At most 220 words |

The report also counts programs that the baseline found and the data lacks,
because that is the measure of data coverage.

## Noise checks

- **Run variance:** the with-skill configuration runs a second time on q01,
  q08 and q15. If the first recommendation or the grader's verdict changes
  between the two runs, the report says so next to every single-run number.
- **Grader agreement:** a second blind grader scores q03, q10 and q13. When
  the two graders disagree on the winner, that question counts as a tie.
- **Incomplete grades:** a question where the grader cannot read the official
  pages counts as incomplete, not as a win for either side.

## If a bar fails

The launch waits, and PR Baltsar/startup-krediter#1 stays unmerged. Fixes go
on the same branch. A fix proven on these 15 questions proves nothing, so the
next round needs new questions.

## Not measured

- **Triggering:** whether the skill loads when it should and stays quiet
  otherwise. This needs `claude -p`, which is logged out on the test machine.
- **Other models:** Codex is not runnable on the test machine (a missing
  local component) and Grok is logged out.
