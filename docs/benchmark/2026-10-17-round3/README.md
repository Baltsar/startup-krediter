# Litmus test, round 3: result

**Verdict: not ready to launch.** The skill got the paperwork right more often
than in any round: 87% of what stops an application, 3 factual errors against
the plain AI's 20, and a median first answer of 192 words. But it lost 11 of
15 questions. It picks the wrong door and misses the trap in the founder's own
situation. Rule fixes after rounds 1 and 2 did not address that.

The rounds are not like-for-like: each used new questions, and the round-3
question writer was told to put a trap a careful assistant should find into
every hidden profile. Read the round columns below as three separate tests,
not as a trend.

| Bar (pre-registered) | Threshold | Round 1 | Round 2 | Round 3 | |
|---|---|---|---|---|---|
| Absolute checks | 0 failures | 1 | 2 | 4 questions (s04 A3, s07 A3, s13 A2 A3 A5, s15 A5) | **fail** |
| C1. Stoppers stated, skill vs plain AI | +20 points, lower on at most 2 | 81% vs 40% | 71% vs 36% | 87% vs 46%, lower on 2 (s02, s11) | pass, at the line |
| C2. First recommendation worse than plain AI | at most 3 of 15 | 6 | 4 | 7 | **fail** |
| C3. Skill wins or ties | at least 11 of 15 | 11 | 9 | 4 (3 wins, 1 tie) | **fail** |
| C4. Median first-answer length | at most 220 words | 237 | 193 | 192 (plain AI: 727) | pass |

Without s05 and s10, which overlap earlier questions (see `plan.md`), C2 is
6 of 13 and C3 is 2 of 13. Both overlapping questions were skill wins, so the
overlap flatters the skill. Without s07 (see the deviation below), C3 is 4 of
14.

## Setup

As in rounds 1 and 2, on the skill frozen at `d0aaabc`. Fifteen questions
written by an agent with no access to the repository (`questions.json`),
read only after the skill was frozen. Claude Opus 5.5 with the skill and as a
plain assistant with web search; a simulated founder second turn from a hidden
profile; one blind grader per question fetching official pages itself; a
second grader on s03, s09 and s14. All 33 conversations, 18 grade files, the
grader brief and the blind key are in this folder.

## Per question

| | Case | Stoppers, skill | Stoppers, plain | Better first pick | Verdict |
|---|---|---|---|---|---|
| s01 | Profitable 14-person SaaS, Vinnova and GPU | 12 / 12 | 8 / 14 | plain | plain |
| s02 | No country, open-source eval tool, GPU | 5 / 12 | 6 / 12 | tie | plain |
| s03 | Norwegian ENK webshop, old program name | 11 / 12 | 5 / 12 | plain | plain (both graders) |
| s04 | Finnish teacher, no company | 9 / 10 | 4 / 12 | plain | plain |
| s05 | Danish ApS, founders in Malmö | 23 / 25 | 14 / 25 | tie | skill |
| s06 | Swedish AB, wrong idea of the R&D deduction | 10 / 10 | 5 / 9 | plain | plain |
| s07 | Icelandic ehf, already holds a Sproti grant | 16 / 18 | 6 / 18 | skill | plain |
| s08 | Asks AI to log in and submit to Business Finland | 12 / 15 | 8 / 15 | tie | tie |
| s09 | Helsinki game studio, EUR 500k | 13 / 14 | 10 / 16 | tie | plain (both graders) |
| s10 | Father's money into an ApS: tax and inheritance | 19 / 19 | 4 / 19 | plain | skill |
| s11 | "Any grant for an app?" (KTH student) | 3 / 10 | 9 / 15 | skill | plain |
| s12 | Norwegian floating solar, NOK 25–30M pilot | 19 / 19 | 5 / 19 | tie | plain |
| s13 | Battery startup 62% owned by a listed group, EIC | 11 / 15 | 8 / 15 | plain | plain |
| s14 | Finnish greenhouse AI, two founders | 18 / 18 | 12 / 18 | tie | skill (both graders) |
| s15 | Radiology AI on "anonymized" CT scans | 14 / 14 | 2 / 14 | plain | plain |

Factual errors found by the graders: 3 with the skill, 20 without.
Absolute-check failures without the skill: 9 (A2 in s01, s02, s05, s09, s10,
s13; A3 in s02, s14; A4 in s11). Programs the plain AI named and the skill
did not: 27; the reverse: 10.

## What the skill did well

- **Accuracy.** Three factual errors in 15 conversations, against 20.
- **Stoppers.** Full checklists on the door it picked: 19 of 19 for
  Innobooster (s10), 19 of 19 for Enova's pilot program (s12), 23 of 25 for
  Innobooster's larger band, including the ATP rule that breaks a DKK 1–2M
  budget for founders living in Sweden (s05).
- **No logins.** In s08 it refused the founder's bank credentials, told them
  not to paste them, and asked about earlier Business Finland money first, as
  the new rule says. That found the Tempo grant that closes Sprint.
- **Short.** Median 192 words against 727.
- **Fixes from round 2 held:** the call's own name (s01), sector doors from the
  search (Creative Europe in s09, Enova in s12), forskningsavdrag explained
  correctly (s06), country settled from a city or funder (s03, s05, s07, s14)
  and asked when missing (s02, s11).

## What fails

1. **The trap in the founder's own situation.** Every hidden profile had one.
   The plain AI asked broad questions and found it. The skill asked the
   matcher's next field and walked past it:
   - s13: a listed group owns 62%, so the company is not an SME. The skill
     asked only turnover and told the founder the EIC fits (A3, A5).
   - s07: the company already holds a Sproti grant. The skill offered Sproti
     without asking about earlier grants, although the founder named the fund
     (A3). Its own new rule says to ask in exactly this case.
   - s04: a full-time teacher. The skill marked starttiraha as met (●),
     which requires full-time entrepreneurship (A3). The data record lacks
     that gate.
   - s15: "anonymized" CT scans are often only pseudonymised health data. The
     skill built on the premise (A5).
   - s11: a KTH student; the skill never asked, the plain AI found KTH
     Innovation.
2. **Depth on the wrong door.** Stage B gives a full checklist for the door
   the founder picks, and the founder picks the first door listed. In s06 that
   was the R&D deduction, worth 0 SEK to a company with no payroll; in s03 a
   grant the founder could not get; in s01 a cybersecurity call that fits the
   project poorly. The plain AI used the second turn to move to the realistic
   route.
3. **Coverage.** The plain AI found 27 relevant programs the skill did not,
   among them Eurostars (s01), Business Finland's creative-industries grant
   (s09), the EU Innovation Fund (s13), OKKA teacher grants (s04), Enova's
   industry program for the customer (s12) and SkatteFUNN (s02).

## Noise checks

- **Run variance.** The first door was the same in both runs on s01, s07 and
  s13. The deciding question changed on s07 (amount in one run, company age
  in the other).
- **Grader agreement.** The second grader agreed on the verdict for s03
  (plain), s09 (plain) and s14 (skill). They split on one absolute check for
  the plain AI in s14 (A3), which does not affect any bar.
- **Re-checked against primary sources, as pre-registered:**
  - s13, A2 against the skill: upheld. Energimyndigheten's call text says
    "Nästa utlysning planeras att öppna första kvartalet 2027"; the skill
    wrote that no next round is published.
  - s13, A3 against the skill: upheld. The Commission's SME page says a firm
    in a larger group "may need to include" the group's figures. The grader
    cites the SME user guide for adding 100% of a majority owner's figures;
    that guide was not re-read for this report.
  - s04, s07 and s15 are judgments on the hidden profile, which names each
    trap explicitly; no page can overrule them, so they stand.
  - The plan said findings that decide a bar would be re-checked on both
    sides. None did: C3 misses its threshold by 7 verdicts and C2 by 4, so no
    single finding on either side could change a bar. Findings against the
    plain AI were therefore not re-checked.
- **Deviation.** The plain AI's second turn on s07 was blocked twice by an API
  safety filter. A fresh agent wrote it from the same first message, its own
  first reply and the founder's answer, given as files. That conversation won.
- **Matcher bug found during the round.** A `confirmed` rule failed instead of
  staying unknown once the profile held any other confirmed key. Agents in s06
  and s15 noticed it and worked around it. Fixed on the branch after the
  freeze (another session, with tests); the frozen copy still had it.

- **Known limits of the method.** Two turns, so a needed question can push
  the checklist past the end. And the simulated founder always picks the
  first door listed, which sends the skill's second turn into a full
  checklist for that door (s01, s03, s06). The rule was the same in every
  round and for both sides, but it amplifies the second cause below.

## Causes

The fixes after rounds 1 and 2 targeted length, wording, ranking and data.
They show up here as short answers, few errors and high stopper counts. The
losses come from somewhere else, the design:

- **One question per turn, chosen by the matcher.** The matcher asks the next
  missing field of the best door (turnover, age). The questions that decide
  these cases are about the founder: who owns the company, which grants it
  already holds, whether the founder works full-time elsewhere, whether they
  study, whether the data is really anonymous. The matcher has no fields for
  most of them, so it never asks.
- **Depth before breadth.** Stage A commits to up to three doors from the data,
  and Stage B spends the next turn on one of them. The plain AI spends both
  turns mapping the options and the risks, then narrows.
- **Coverage is bounded by the data.** One web search a turn cannot find what
  73 records miss.

## What to change before round 4

- **Screen before matching.** Ask a short set of founder-situation questions
  in the first answer when the profile leaves them open: ownership above 25%
  by another company, public grants already held from the named funder,
  employment status, student or researcher affiliation, and for health or
  personal data, whether it is truly anonymous. Answers become gates.
- **Map, then deepen.** Show the realistic routes across kinds (grant, loan,
  tax relief, equity, own money) before a checklist, and let Stage B wait for
  a founder who has chosen with the traps in view.
- **Gate data for traps.** Starttiraha needs a full-time-entrepreneur gate;
  EIC and every SME-only door need a group-ownership gate.
- **Widen the search when the data is thin**, for example two searches when
  the matcher's best door is weak or the sector is specialised.
- **Step C** (writing and filling in applications) was built on the branch
  after the freeze and has not been measured. It needs its own pre-registered
  round.

## Not measured

Triggering, other models than Claude, and Step C.
