# startup-krediter

**You have picked a grant, a GPU program or a credits program. Before you open the form, ask your AI assistant whether you can apply, what the application will ask of you, and when. Then let it write the application with you.**

For founders in Sweden, Finland, Norway, Denmark and Iceland. Answers in Swedish, Finnish, Norwegian, Danish or English.

An open-source skill for AI assistants, by [OpenSverige](https://opensverige.se). Tested with Claude Code; it also installs into Cursor and Codex.

> **Status, 19 October 2026: not released, and we want your feedback.** We tested the skill in five pre-registered rounds against the same AI model with web search and no skill, with blind graders checking both against the programs' own pages. It did not pass any of them. In the latest round, on a program the founder had already chosen, the skill named more of what stops an application (89% against 77%) with fewer factual errors (5 against 8) and a shorter answer. It won only 9 of 15 questions, because the plain model asked about the founder's own situation more often. The full report, every conversation and the grades are in [docs/benchmark/2026-10-19-round5](docs/benchmark/2026-10-19-round5/README.md). Tell us what you think in an [issue](https://github.com/Baltsar/startup-krediter/issues/new): what would make this worth using, and what you would test differently.

---

## Why this exists

There is real money for early startups in the Nordics: grants, soft loans, free time on EU supercomputers, and cloud and AI credits. Once you know which program you want, the hard part is everything between deciding and submitting.

- **The rule that rules you out is buried.** It sits on a conditions page, in a PDF, or in the form itself.
- **Your own situation decides more than your company facts.** Another company owning 25 %, a grant you already had, a full-time job you keep, work you already started: each can close a program that looks open.
- **Old advice looks current.** Rounds close, programs are renamed, amounts change. The blog post you found does not say so.
- **The surprises come late.** You decide you qualify, start the application, and then meet the login you cannot use, the co-financing rule, the attachment you do not have, or the deadline that passed.

This skill does that reading for you, for the program you chose, before you open the form.

## What it does not do

It does not pick the program for you. In four tests against the same AI model without the skill, the model searching the web on its own found the better program more often. The skill was more accurate about the rules of the program in front of it. So use your assistant, or any search, to choose; use the skill once you have chosen. If you ask it to choose, it searches broadly like a careful assistant would and asks which program to go through.

## What you get

Name the program and describe your company in plain words:

> We're applying to Vinnova's Innovativa startups in January. Swedish AB, two years old, four people. What do we need to have ready?

**One answer with the whole picture.** Whether it fits on what you have said, the questions that decide it, the status rule by rule, everything the application will ask of you, what the page leaves unclear, and the next step:

> Innovativa startups fits you on what we know. Four things decide it:
>
> 1. Does another company, a group or a public body own 25 % or more of yours? Then SME status can end.
> 2. Which public grants or loans has the company had, and is any still running?
> 3. Has the company lost more than half its share capital?
> 4. How many people does the company pay a salary to?

```
◐  Vinnova Innovativa Startups 2026
●  in Sweden
●  a company
●  at most 10 years old
●  at most 10 employees
○  revenue at most 10 MSEK, or balance sheet at most 10 MSEK
○  no dividend last year
○  the project lead employed by the company
○  not lost more than half the share capital
?  Net revenue last fiscal year, in MSEK?
→  Up to 500 000 SEK
```

`●` you meet it · `○` not known yet · `×` this rules you out · `?` the question that matters next

> **Before you apply**
> - The project lead must be employed by the company, and an unpaid founder's time is not an eligible cost.
> - Name a signatory and a project lead in the form; the grant is paid only to a bankgiro or plusgiro in the company's name.
> - Mark the application complete before 12 January 2027 at 14:00, according to the page today. An application not marked complete is not registered.
>
> **Unclear**
> - Whether starting a salary for a founder who has been unpaid counts as an unexplained salary increase. Ask startups@vinnova.se before you budget it.

*Shortened from the skill's output on 19 October 2026. The full checklist has twelve items.*

When a program is closed to you, it says so first, with the rule and the page, and does not hand you a checklist for something you cannot get.

**Then the application.** Say "help us apply" and it drafts the application section by section in the form's own order and limits, puts your budget in the program's template with its funding rate and excluded costs, reviews the draft the way an assessor would, and fills the online form after you have logged in. It stops before the submit button. It never invents a customer, a number or a letter of intent; it marks the gap for you to fill.

## How it compares

*These are the first, informal results, from 16 October 2026 on an earlier version. The five pre-registered rounds that followed are in [docs/benchmark](docs/benchmark/); none of them passed.*

We asked six founder questions to the same AI model twice: with the skill, and with web search but no skill. Graders who did not know which answer was which checked both against the programs' own pages.

| | Search engine | AI without the skill | AI with the skill |
|---|---|---|---|
| Starts from your company | No | Yes | Yes |
| Checks whether you qualify | No | Partly, from what it finds | Rule by rule, from each program's own pages |
| Requirements that stop an application, named before you apply: **two questions the skill was not tuned on** | not measured | 11 of 21 (52%) | 15 of 16 (94%) |
| Same, all six questions | not measured | 37 of 74 (50%) | 66 of 69 (96%) |
| Words in the first answer | not measured | 253 to 551 | 138 to 213 |
| Picked the better first program | not measured | better in 1 of 6 | better in 1 of 6; same pick in 4 |
| Time per conversation | not measured | 65 to 84 seconds | 76 to 142 seconds |

Examples of wrong facts the graders found. Without the skill: a GPU call described as possibly closed while it was open, a grant budgeted for a prototype the grant excludes, the wrong age limit for a Norwegian grant, Google credits said to pay for Claude when Google's page says they do not. With the skill: a revenue question put to founders with no company (since fixed), an AWS FAQ answer called broken when it was not, and requirements stated a little stronger than the page states them.

The search engine column describes what a search engine does; nothing in it was measured. Six questions, one run each, Claude Opus 5.5, 16 October 2026. Four of the questions shaped fixes made earlier that day, so the first row counts only the two that did not. The skill is not faster, and a plain AI search still sometimes finds a program our data lacks. Its edge is that you learn what will stop you before you start. Full method, per-question results and all twelve answers: [docs/benchmark/2026-10-16](docs/benchmark/2026-10-16/).

## How it works

- **It reads the live page before it quotes anything.** Deadlines, amounts and "is it open" come from the program's own site that day, not from memory. When a page cannot be read, it says so and gives you the link.
- **It carries each program's own conditions.** 73 programs have a checklist read from their application and conditions pages: logins, attachments, co-financing, partners, what you must report afterwards. For a program outside that list it reads the official pages and builds the same checklist from them, citing each page.
- **It asks about your situation, not just your company.** Ownership, grants already held, full-time work, work already started, lost share capital: the questions that close a program the company facts leave open.
- **It says what it does not know.** When a page leaves out the amount or two pages disagree, you hear it, with the address to ask.
- **It never applies for you.** The login, the declarations and the submit button stay with you.
- **No scores, no promises.** Vinnova draws lots between equally strong applications. EuroHPC is first come, first served. You get the process, not a made-up percentage.

## What it covers

73 programs, each read from its own pages between 15 and 18 October 2026.

| You need | Programs include |
|---|---|
| **Grants and loans** | Vinnova, Almi, Energimyndigheten, EIC Accelerator, Eurostars, Eureka Innowwide, Innovasjon Norge, SkatteFUNN, Business Finland, Finnvera, InnoFounder, Innobooster, Rannís |
| **GPU and compute** | EuroHPC Playground, Fast Lane and Large Scale, Sweden AI Factory, LUMI, Sigma2 KI-fabrikken, NAISS, Berzelius |
| **Cloud credits** | AWS Activate, Google for Startups, Microsoft for Startups, Cloudflare, Vercel, Neon, MongoDB |
| **AI credits** | Claude Startups, OpenAI for Startups, Together AI, Modal, Runpod, Lambda, NVIDIA Inception |
| **Accelerators** | Sting, Norrsken Evolve, Antler, Accelerace, Kiuas, KTH Innovation, Chalmers Ventures, Minc |

Coverage is deepest in Sweden. Here is the honest count by where a program is run:

| Sweden | EU-wide | Global vendors | Finland | Norway | Denmark | Iceland |
|---|---|---|---|---|---|---|
| 29 | 14 | 14 | 7 | 5 | 3 | 1 |

Founders in every Nordic country can use the EU-wide and global programs. The national lists for Finland, Norway, Denmark and Iceland are thin, and [adding a program](#add-a-program) is the most useful contribution you can make.

Programs open and close all the time. Treat the data as a map: the skill reads the page again before it tells you anything.

## Get started

You need an AI coding assistant, plus git and Python 3.10 or later. The skill is tested with Claude Code. It also installs into Cursor and Codex, but those have not been tested yet.

**1. Install once.** In a terminal:

```bash
git clone https://github.com/Baltsar/startup-krediter.git
cd startup-krediter
sh bootstrap.sh
```

The script links the folder into each assistant it finds on your machine. Keep the folder where it is, because the links point to it. Run `git pull` in it to get new programs.

**2. Ask your assistant**, in any of the five languages:

- "Vi vill söka EuroHPC Playground för gratis GPU. Svenskt AB, två år, fyra personer. Vad krävs?"
- "Haemme Business Finlandin rahoitusta, mitä hakemukseen tarvitaan? Suomalainen Oy, pre-seed."
- "Kan vi søke Oppstartstilskudd 1? Norsk AS, ett år gammelt."
- "Help us apply for AWS Activate credits. Swedish AB, angel-funded, building on Bedrock."

Or type `/startup-krediter`.

**Not using an AI assistant?** Read the human-written map of Swedish GPU and credit programs at [opensverige.se](https://opensverige.se/blogg/startup-krediter-gpu-sverige).

## Good to know

- This is not financial or legal advice. It reads the rules of the program you chose. The program decides.
- The data was correct on the date shown for each program. Rules change, so the skill checks the live page, and you should read it too before you apply.
- Some sites block automated readers. When that happens the skill says so instead of guessing.

## Add a program

**Not a developer?** [Open an issue](https://github.com/Baltsar/startup-krediter/issues/new) with the program's name, its link, and the country. That is enough for someone to add it.

**Developer?** Each program is one record in `data/programs.json`. Its eligibility rules are data, so you add a program without writing any code.

1. Append a record. The shape is in `data/schema.json` and examples are in `tests/fixtures/programs_small.json`.
2. Add an entry with the matching `{#id}` anchor to the right file in `references/`, with a quoted sentence from the program's page as evidence.
3. Set `last_verified` to the day you read the page.
4. Run the checks:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

Only facts that appear on the program's own pages go into a record. If a page does not state an amount, the record says so.

<details>
<summary>How the pieces fit</summary>

- `SKILL.md` tells the assistant how to build a profile from the chat, when to read the live page, and how to answer.
- `scripts/match.py` finds a program by name (`--find`) and checks one program against a company profile (`--door`): every rule met, open or failed, the questions that decide it, and the checklist. Standard library only, no packages.
- `scripts/vinnova_api.py` reads the current Vinnova round from Vinnova's open data API.
- `references/*.md` hold the longer notes per area.
- Records older than 90 days are flagged so the assistant re-reads the page.

```bash
python3 scripts/match.py --find "innovativa startups"
echo '{"country":"SE","legal_form":"company","age_years":2,"employees":4,"lang":"en"}' \
  | python3 scripts/match.py --door vinnova-innovativa-startups --live
```

</details>

---

MIT licensed. Made by [OpenSverige](https://opensverige.se), Sweden's open community for AI agents.
