# Benchmark, 16 October 2026

Does the skill make an AI assistant better at helping a founder find money,
GPU time or credits? We asked six founder questions twice: once to an assistant
with the skill, once to the same assistant with web search and no skill.
Independent graders then checked both answers against the programs' own pages
without knowing which answer came from where.

## Setup

- **Model:** Claude Opus 5.5 for every run and every grader.
- **Skill version:** commit `adbaa30`, frozen before the runs.
- **Without skill:** the same model with web search and page fetching, told not
  to read the skill.
- **Conversation:** two turns. The founder asks, then says "tell me more about
  the first one".
- **Grading:** one blind grader per question. It fetched the official pages of
  the program each answer detailed, listed every requirement that stops an
  application, and checked each answer against that list, plus facts, fit and
  length.
- **Size:** six questions, one run each. Treat the numbers as a strong signal,
  not a statistic.

Four of the questions were first run earlier the same day against commit
`a65d470`, and the skill lost two of them. Those losses led to fixes: Almi
Verifieringsmedel was missing, AWS Activate did not match a founder building on
Claude, and equity and fee programs ranked above grants. The new AWS and Almi
records were written with the requirements the first-round graders had listed,
which makes those two questions easier for the skill in the second round. The
answers without the skill for those four questions are the first-round answers,
reused because they do not depend on the skill. The two held-out questions,
Norway and Denmark, were written after the fixes and did not inform them, so
read their numbers first.

| Question | Language | Held out |
|---|---|---|
| Swedish AB, two years, four people, needs GPU to fine-tune | Swedish | no |
| Two founders, no company, a climate idea, any money? | Swedish | no |
| Helsinki Oy, founded 2025, no revenue, public money? | English | no |
| Pre-seed Swedish AB on Vercel, Supabase and Anthropic, which credits? | English | no |
| Bergen AS, one year, aquaculture software, which grants? | Norwegian | yes |
| Copenhagen ApS, seed VC, Google Cloud and OpenAI, which credits? | Danish | yes |

## Results

| | With skill | Without skill |
|---|---|---|
| Stoppers stated for the program the founder picked, held-out questions | 15 of 16 (94%) | 11 of 21 (52%) |
| Stoppers stated, the four questions that informed the fixes | 51 of 53 (96%) | 26 of 53 (49%) |
| Stoppers stated, all six | 66 of 69 (96%) | 37 of 74 (50%) |
| Picked the better first program | 1 question | 1 question |
| Same first program | 4 questions | 4 questions |
| Overall verdict from the grader | better in 5 (2 narrowly) | better in 1 (narrowly) |
| Words in the first answer | 138 to 213 | 253 to 551 |
| Time per two-turn conversation | 76 to 142 s | 65 to 84 s |
| Tokens per conversation | 114k to 119k | 99k to 108k |

Per question, stoppers stated on the detailed program:

| Question | With skill | Without skill | Grader's verdict |
|---|---|---|---|
| Swedish AB, GPU | 16 of 17 | 4 of 17 | skill, clearly |
| No company, idea | 10 of 10 | 5 of 10 | skill, narrowly |
| Finnish Oy, money | 12 of 12 | 11 of 12 | skill |
| Pre-seed, credits | 13 of 14 | 6 of 14 | skill, narrowly |
| Norwegian AS, grants (held out) | 12 of 13 | 5 of 13 | skill |
| Danish ApS, credits (held out) | 3 of 3 | 6 of 8 | without skill, narrowly |

In the Danish question the two answers detailed different programs, so the
lists differ in length.

## What the skill did better

- **It names what will stop the application before the founder opens the form.**
  Without the skill, the GPU answer missed the project lead's employment rule,
  the VAT number, the English-only form and the mandatory technical data.
- **Fewer wrong facts that change what a founder does.** Without the skill, the
  answers:
  - called Playground possibly closed while it was open
  - gave an old contact address
  - suggested spending an Almi grant on a prototype, which the grant excludes
  - gave the wrong age limit for Oppstartstilskudd
  - said Google credits could pay for Claude on Vertex, which Google's page rules out
  - misread Business Finland's test for a company in difficulty
- **Shorter first answer.** The verdict and the deciding question come first.

## What the skill did worse

- **It can still miss a program.** The plain assistant found two aquaculture
  calls for the Norwegian founder (Forskningsrådet's seafood innovation call
  and FHF) that the skill's data lacks and its one web search did not surface.
- **It can rank a long shot first.** For the Danish founder it led with OpenAI
  for Startups, which only pays through partner VCs. Google's Scale tier was the
  likelier win.
- **It asked two founders without a company for last year's revenue.** Fixed
  after the benchmark, in the commit after `adbaa30`.
- **It called an AWS FAQ answer broken** when the answer was there; the page
  renders it late.
- **It is not faster.** Reading every page it quotes costs time and tokens.
- **It states some rules a little stronger than the page.** The graders noted
  "Fast Lane requires code already running on HPC" where the page says
  HPC-ready, the 12-month funding rule placed on one AWS tier only, and "no
  credits without a partner VC" where OpenAI also hands out credits at events.

## Not measured

- **Other models.** Only Claude was tested. Codex could not run on the test
  machine and Grok was logged out.
- **A person using a search engine.** An agent cannot stand in for a human
  reading twenty tabs, so the README describes that column by what a search
  engine does, not by a score.

## Files

`answers/` holds all twelve answers verbatim. `with-skill` and `without-skill`
in the file name say which is which.
