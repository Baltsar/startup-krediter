# startup-krediter

**Find the money, GPU time and free credits your startup can actually get. In one conversation.**

For founders in Sweden, Norway, Finland, Denmark and Iceland.

---

## The problem

You have heard there is free money out there. Grants. Free GPU hours. Thousands of dollars in cloud credits. So you start looking.

Three hours later you have twenty open tabs and no answer.

- **Every program has its own website, its own words and its own rules.** Vinnova, Almi, EuroHPC, AWS, Google. Nobody puts them side by side.
- **You cannot tell if you qualify until you have read everything.** The rule that rules you out is often on page four.
- **The blog post you found is out of date.** The round closed in August. The cohort is full. The amount changed.
- **You do not know what to search for.** You need GPU time, but the door is called "EuroHPC AI Factories Playground Access".
- **Money, compute and credits get mixed up.** Free GPU hours will not pay your OpenAI bill. A grant will not give you a GPU.
- **The surprise comes inside the application.** You decide you qualify, open the form, and only then meet the BankID login, the co-financing rule, the partner you needed to sign first, or the deadline that passed.

So most founders give up, or apply for the one program they happened to hear about.

## What this does

You describe your company in plain words. You get back the programs that fit you, and what to do next.

```
You:   We're a Swedish AB, two years old, four people. We need GPU
       time and we pay for Claude and AWS. Do we have a chance?
```

The answer shows each program that fits, with a clear status:

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

`●` you meet it. `○` not known yet. `×` this rules you out. `?` the one question that matters next.

The answer starts with two lines: which door fits best, and the one question that decides it. Then, for at most three programs:

- what the program is, in one sentence
- **what you need before you apply**: the login, the attachments, the co-financing, the partner, the deadline
- **what the page leaves unclear**, and whom to ask
- the exact next step, with the link

Everything is in your language: Swedish, Finnish, Norwegian, Danish or English. Answer the question and it updates. No forms. No starting over.

## What makes it different

- **It checks the live page first.** Before it tells you a deadline or an amount, it reads the program's own website today. If the page says the round is closed, you hear that.
- **It asks, it does not guess.** If it does not know your country or your headcount, it asks. A guess gives you a confident wrong answer.
- **It tells you what rules you out.** Not just "you might qualify". It names the exact requirement, like "the project lead must be employed for three months after the GPU time ends".
- **It tells you what the form will ask before you open it.** Every program carries a checklist read from its own application page, so the BankID login or the 50 percent co-financing is not a surprise on page three of the form.
- **It says what it does not know.** When a page leaves out the amount or two pages disagree on a date, you hear it, with the address to ask.
- **It works across borders.** Live in Copenhagen with a Swedish AB? You see both countries, and which Danish programs a Danish company would open.
- **It never applies for you.** It shows you the door and the next step. The account, the signature and the submit button stay with you.
- **No percentages, no promises.** Vinnova draws lots between equally strong applications. EuroHPC is first come, first served. You get told how the process works, not a made-up score.

## What it covers

63 programs, checked on 15 and 16 October 2026.

| You need | Examples |
|---|---|
| **Money** | Vinnova, Almi, Energimyndigheten, EIC Accelerator, Eurostars, Innovasjon Norge, SkatteFUNN, Business Finland, Finnvera, Innofounder, Innobooster, Rannís |
| **GPU and compute** | EuroHPC Playground, Fast Lane and Large Scale, Sweden AI Factory, LUMI, Sigma2 KI-fabrikken, NAISS, Berzelius |
| **Cloud credits** | AWS Activate, Google for Startups, Microsoft for Startups, Cloudflare, Vercel, Neon, MongoDB |
| **AI credits** | Claude Startups, OpenAI for Startups, Together AI, Modal, Runpod, Lambda, NVIDIA Inception |
| **Accelerators** | Sting, Norrsken Evolve, Antler, Accelerace, Kiuas, KTH Innovation, Chalmers Ventures, Minc |

Programs open and close. The skill reads each page again before it tells you anything, so the list above is a map, not a promise.

## How to use it

It runs inside an AI coding assistant: Claude Code, Cursor or Codex. If you already use one of those, it takes a minute to set up.

**1. Install it once.** Paste this into your terminal:

```bash
git clone https://github.com/Baltsar/startup-krediter.git
cd startup-krediter
sh bootstrap.sh
```

**2. Ask your assistant.** In Swedish, Finnish, Norwegian, Danish or English. For example:

- "Har vi en chans på gratis GPU? Svenskt AB, två år, fyra personer."
- "We're a Finnish Oy, pre-seed, building on OpenAI. What credits can we get?"
- "Which grants can a Norwegian AS under three years apply for?"
- Or type `/startup-krediter`.

That is it. You need Python 3.10 or later, which most computers already have.

Prefer reading to asking? The human version of the Swedish GPU map is here: https://opensverige.se/blogg/startup-krediter-gpu-sverige

---

## For contributors

Everything below is for people who want to add a program or improve the code.

**How it works.** `data/programs.json` holds one record per program, with its requirements written as data. `scripts/match.py` takes a company profile and returns the programs ranked: eligible first, then unknown with the fewest open questions, then ruled out. `SKILL.md` tells the assistant how to build the profile from the chat, when to read the live page, and how to answer. `references/*.md` hold the longer notes per area, each with a quoted sentence from the program's page as evidence.

```bash
echo '{"country":"SE","legal_form":"company","age_years":2,"employees":4,"need":["compute","credits"],"stack":["anthropic","aws"]}' \
  | python3 scripts/match.py --live
```

Records older than 90 days are flagged so the assistant reads the page again. Standard library only, no packages.

**Add a program.** Append a record to `data/programs.json` (shape in `data/schema.json`), add an entry with the matching `{#id}` anchor to the right file in `references/`, set `last_verified` to the day you read the page, and run:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

Only facts that appear on the program's own page go into a record. If the page does not state an amount, the record says so.

MIT. Copyright 2026 OpenSverige.
