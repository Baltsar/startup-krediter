# startup-krediter

**Ask your AI assistant which grants, GPU hours and startup credits your company can get. Get the doors that fit, everything each one will ask of you, and the next step.**

For founders in Sweden, Finland, Norway, Denmark and Iceland. Answers in Swedish, Finnish, Norwegian, Danish or English.

An open-source skill for Claude Code, Cursor and Codex, by [OpenSverige](https://opensverige.se).

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

> We're a Swedish AB, two years old, four people, building an AI product. We need GPU time to fine-tune a model. Do we have a chance at anything free?

The answer starts with a verdict and the one question that decides it:

> Yes. EuroHPC Playground is open to a Swedish AB and gives you 5,000 free GPU hours for fine-tuning. What decides it is your project lead's employment contract. Is the project lead employed until at least three months after the GPU allocation ends?

Then each door that fits, at most three, with a status block:

```
◐  EuroHPC AI Factories Playground Access
●  a company
○  project lead employed past the allocation
○  VAT number
○  email on your own domain
○  workload defined: code, one system, GPU hours
?  Is the project lead employed until at least three months after the allocation ends?
→  5 000 GPU hours fixed per application, 1 to 3 months, one system
```

`●` you meet it · `○` not known yet · `×` this rules you out · `?` the question that matters next

Under the block, what the application will ask of you and what the page leaves open:

> **Before you apply:**
> - Use the hours for training or fine-tuning. Only a small, justified share can go to inference, and running a live product is not allowed.
> - Register on access.eurohpc-ju.europa.eu with your company email. You solve the captcha yourself.
> - You need the company's VAT number, plus a PIC if you have one.
> - The form is online and in English. Every mandatory field must be filled in.
>
> **Unclear:**
> - The terms say you commit to publishing results. Sweden AI Factory says startups are exempt. Ask aif.access@eurohpc-ju.europa.eu what you must publish.
>
> **Next step:** create the portal account, open the Playground call, choose a system and fill in the form. You click submit yourself.

*Shortened from a real answer the skill gave on 16 October 2026. The full answer had a second door and six more requirements.*

Answer the question and the status updates. No forms, no starting over.

## How it works

- **It reads the live page before it quotes anything.** Deadlines, amounts and "is it open" come from the program's own site that day, not from memory. When a page cannot be read, it says so and gives you the link.
- **It carries each program's own conditions.** Every program has a checklist read from its application and conditions pages: logins, attachments, co-financing, partners, what you must report afterwards.
- **It says what it does not know.** When a page leaves out the amount or two pages disagree, you hear it, with the address to ask.
- **It asks instead of guessing.** Country, legal form and headcount close more doors than anything else, so it asks for them rather than assume.
- **It tells you what would open more doors.** No company yet? It names the programs a registered company would unlock. Living in Copenhagen with a Swedish AB? You see both countries.
- **It never applies for you.** The account, the signature and the submit button stay with you.
- **No scores, no promises.** Vinnova draws lots between equally strong applications. EuroHPC is first come, first served. You get the process, not a made-up percentage.

## What it covers

63 programs, each read from its own pages on 15 or 16 October 2026.

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
| 24 | 12 | 14 | 6 | 4 | 2 | 1 |

Founders in every Nordic country can use the EU-wide and global programs. The national lists for Finland, Norway, Denmark and Iceland are thin, and [adding a program](#add-a-program) is the most useful contribution you can make.

Programs open and close all the time. Treat the data as a map: the skill reads the page again before it tells you anything.

## Get started

You need Claude Code, Cursor or Codex, plus git and Python 3.10 or later.

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
