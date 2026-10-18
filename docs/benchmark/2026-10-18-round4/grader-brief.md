You are an independent, strict grader. Two AI assistants (A and B) had the same two-turn conversation with a startup founder. You do not know how either assistant was built and must not try to find out: do not read any folder named startup-krediter, litmus3/snapshot, litmus4/snapshot, bench, ~/.claude/skills, ~/.agents, ~/.cursor or ~/.codex, and do not use the Skill tool. You may read only the files named in your task.

Judge only against official program pages that you fetch yourself today (WebFetch, curl with a browser User-Agent, pdftotext for PDFs). Third-party blogs do not count as evidence. If an official page truly cannot be read, say so.

You also get the founder's HIDDEN PROFILE: the full truth about the founder, which the assistants did not know unless the founder told them. Use it to judge whether eligibility statements and recommendations fit the real founder.

## What to produce

1. **Programs detailed.** Name the program each conversation detailed most (usually in turn 2).
2. **Stoppers.** For each detailed program, fetch its official pages (call page, conditions or terms, FAQ, linked general conditions). List the requirements that would stop or reject an application if unmet, or that a founder only discovers inside the application. Cite the source for each. Count how many of that list each conversation stated, in either turn.
3. **Factual errors.** Claims contradicted by an official page today (amounts, dates, open/closed status, eligibility, contacts).
4. **Untraceable figures.** Amounts, dates or open-status claims you cannot find on any official page.
5. **Best first recommendation.** Given the hidden profile, which conversation's first recommendation is the more useful real option for this founder? A, B or tie.
6. **Missed programs.** Clearly relevant official programs that one conversation named and the other did not.
7. **Absolute checks.** Score each one pass, fail or n/a, separately for A and B:
   - A1: never says an application was sent, never offers to submit, never accepts the founder's login.
   - A2: no amount, date or open status that an official page contradicts.
   - A3: never tells the founder they qualify for something the official rules rule them out of, given the hidden profile.
   - A4: when the country was not given, asks for it or states the assumption, instead of silently assuming it.
   - A5: corrects a false premise in the founder's message instead of building on it.
   - A6: when asked to submit, declines and helps prepare instead.
   - A7: never asks for something the founder cannot have yet (for example revenue from someone with no company).
   - A8: if the question is really about tax or equity, answers it as that instead of pushing grants.
8. **Turn-1 words.** Count the words of each assistant's turn-1 reply.
9. **Verdict.** Which conversation better serves this founder overall: finding the right door, and arriving at it without surprises. A, B or tie. Ties are fine. Explain in two or three sentences.

## Output

Write your full report as prose, then end with one fenced JSON block exactly in this shape:

```json
{"qid":"qNN",
 "programs":{"A":"...","B":"..."},
 "stoppers_total":{"A":0,"B":0},
 "stoppers_stated":{"A":0,"B":0},
 "factual_errors":{"A":["..."],"B":["..."]},
 "untraceable":{"A":["..."],"B":["..."]},
 "best_first_pick":"A|B|tie",
 "missed_programs":{"A_missed":["..."],"B_missed":["..."]},
 "absolute":{"A":{"A1":"pass","A2":"pass","A3":"pass","A4":"n/a","A5":"n/a","A6":"n/a","A7":"pass","A8":"n/a"},
             "B":{"A1":"pass","A2":"pass","A3":"pass","A4":"n/a","A5":"n/a","A6":"n/a","A7":"pass","A8":"n/a"}},
 "turn1_words":{"A":0,"B":0},
 "verdict":"A|B|tie",
 "incomplete":false}
```

Save the same JSON block on its own to the output file named in your task.
