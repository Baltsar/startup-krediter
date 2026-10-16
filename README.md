# startup-krediter

**Ask your AI assistant which grants, GPU hours and startup credits your company can get. Get the doors that fit, everything each one will ask of you, and the next step.**

For founders in Sweden, Finland, Norway, Denmark and Iceland. Answers in Swedish, Finnish, Norwegian, Danish or English.

An open-source skill for AI assistants, by [OpenSverige](https://opensverige.se). Tested with Claude Code; it also installs into Cursor and Codex.

---

## Why this exists

There is real money for early startups in the Nordics: grants, soft loans, free time on EU supercomputers, and tens of thousands of dollars in cloud and AI credits. Finding the part that fits you is the hard part.

- **Every program speaks its own language.** Vinnova, Almi, EuroHPC, Business Finland and AWS all describe eligibility differently, on different sites.
- **The rule that rules you out is buried.** It sits on a conditions page, in a PDF, or in the form itself.
- **Old advice looks current.** Rounds close, cohorts fill, amounts change. The blog post you found does not say so.
- **You do not know the names.** You need GPU time, and the door is called "EuroHPC AI Factories Playground Access".
- **The surprises come late.** You decide you qualify, start the application, and then meet the BankID login, the co-financing rule, the partner you needed first, or the deadline that passed.

This skill does that reading for you, before you open a single form.

## What you get

You describe your company in plain words, the way you would to a friend:

> we're pre-seed (just closed a 400k USD angel round, no VC), 3 people, Swedish AB, building an AI agent product on Vercel + Supabase + Anthropic. which credits can we actually get?

**The first answer is short.** A verdict, the one question that decides it, and the three doors that fit, one line each. Every line says how many requirements are waiting, so nothing looks simpler than it is:

> AWS Activate fits you best on what we know. What decides it is your angel round: the Founders tier is for self-funded startups, and the bigger Portfolio tier needs an Org ID from an Activate Provider.
>
> How old is the company, in years?
>
> ◐ AWS Activate Credits: Founders tier starts at 1 000 USD, and select startups may get up to 5 000 USD. Portfolio tier goes up to 200 000 USD with a provider Org ID. Decides: whether one of your angels is an Activate Provider. 9 requirements in the application, 3 unclear points.
> ◐ NVIDIA Inception: free membership with cloud credits from NVIDIA and partners, amounts not published. 8 requirements, 5 unclear points.
> ● Claude Startups (Anthropic): partner credits worth up to 45 000 USD. Closed right now because the cohort is full. 4 requirements, 3 unclear points.
>
> AWS credits can pay for Claude, but only when you call it through Amazon Bedrock, not Anthropic's own API.

**Pick a door and you get all of it.** The status block, everything the application will ask of you, what the page leaves unclear and whom to ask, and the next step:

```
◐  AWS Activate Credits
●  uses AWS, or uses Anthropic
●  stage: idea, pre-seed, seed or series A
○  at most 10 years old
○  new to AWS Activate credits, or asking for more than you received before
?  How old is the company, in years?
```

`●` you meet it · `○` not known yet · `×` this rules you out · `?` the question that matters next

> **Before you apply**
> - The Founders tier is for bootstrapped or self-funded startups. With outside funding, ask your angels whether any of them is an Activate Provider, and if so apply on the Portfolio tier.
> - For the Portfolio tier, the provider must answer AWS's verification email. If they don't, the application is declined.
> - AWS may ask you to verify your identity with an ID document. Saying no means rejection.
> - An application cannot be edited after you submit it.
>
> **Unclear**
> - Whether an angel-funded startup whose angels are not Activate Providers can still use the Founders tier. The credits page says self-funded, but the FAQ says the program is open to funded startups. Ask AWS Activate through the contact page.

*Shortened from real answers the skill gave on 16 October 2026. The full checklist had eleven items.*

Answer the question and the status updates. No forms, no starting over.

## How it compares

We asked six founder questions to the same AI model twice: with the skill, and with web search but no skill. Graders who did not know which answer was which checked both against the programs' own pages.

| | Search engine | AI without the skill | AI with the skill |
|---|---|---|---|
| Starts from your company | No. You read every page yourself | Yes | Yes |
| Checks whether you qualify | No | Partly, from what it finds | Rule by rule, from each program's own pages |
| Requirements that stop an application, named before you apply | You find them in the form | 50% (37 of 74) | 96% (66 of 69) |
| Wrong facts that would change what you do | Old pages rank high | 6 across six answers, such as a call called closed while open, or a grant spent on costs it excludes | 2 across six answers: a revenue question to founders with no company (since fixed), and an FAQ answer called broken when it was not |
| Words in the first answer | none | 253 to 551 | 138 to 213 |
| Picked the better first program | | better in 1 of 6 | better in 1 of 6; same pick in 4 |
| Time per conversation | hours | 65 to 84 seconds | 76 to 142 seconds |

The search engine column describes what a search engine does; it was not measured. Six questions, one run each, Claude Opus 5.5, 16 October 2026. The skill is not faster, and a plain AI search still sometimes finds a program our data lacks. Its edge is that you learn what will stop you before you start. Full method, per-question results and all twelve answers: [docs/benchmark/2026-10-16](docs/benchmark/2026-10-16/).

## How it works

- **It reads the live page before it quotes anything.** Deadlines, amounts and "is it open" come from the program's own site that day, not from memory. When a page cannot be read, it says so and gives you the link.
- **It carries each program's own conditions.** Every program has a checklist read from its application and conditions pages: logins, attachments, co-financing, partners, what you must report afterwards.
- **It says what it does not know.** When a page leaves out the amount or two pages disagree, you hear it, with the address to ask.
- **It asks instead of guessing.** Country, legal form and headcount close more doors than anything else, so it asks for them rather than assume.
- **It tells you what would open more doors.** No company yet? It names the programs a registered company would unlock. Living in Copenhagen with a Swedish AB? You see both countries.
- **It never applies for you.** The account, the signature and the submit button stay with you.
- **No scores, no promises.** Vinnova draws lots between equally strong applications. EuroHPC is first come, first served. You get the process, not a made-up percentage.

## What it covers

64 programs, each read from its own pages on 15 or 16 October 2026.

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
| 25 | 12 | 14 | 6 | 4 | 2 | 1 |

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

- "Har vi en chans på gratis GPU? Svenskt AB, två år, fyra personer."
- "Olemme suomalainen Oy, pre-seed, rakennamme OpenAI:n päälle. Mitä krediittejä voimme saada?"
- "Hvilke tilskudd kan et norsk AS under tre år søke?"
- "Two founders, no company yet, a climate idea. Is there any money for us?"

Or type `/startup-krediter`.

**Not using an AI assistant?** Read the human-written map of Swedish GPU and credit programs at [opensverige.se](https://opensverige.se/blogg/startup-krediter-gpu-sverige).

## Good to know

- This is not financial or legal advice. It points you at doors and reads their rules. The program decides.
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
- `scripts/match.py` takes a company profile as JSON and returns the doors ranked: fits first, then fewest open questions, then ruled out. Standard library only, no packages.
- `scripts/vinnova_api.py` reads the current Vinnova round from Vinnova's open data API.
- `references/*.md` hold the longer notes per area.
- Records older than 90 days are flagged so the assistant re-reads the page.

```bash
echo '{"country":"SE","legal_form":"company","age_years":2,"employees":4,"need":["compute"],"lang":"en"}' \
  | python3 scripts/match.py --live
```

</details>

---

MIT licensed. Made by [OpenSverige](https://opensverige.se), Sweden's open community for AI agents.
