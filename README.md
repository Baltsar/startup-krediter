# startup-krediter

A skill for Claude Code, Cursor and Codex that tells a startup founder in Sweden
or the Nordics which funding, compute and credit doors they can apply to, what is
met, what is missing, and the exact next step. It reads the live program page
before quoting a date or an amount. It never submits an application.

Three kinds of door, kept apart because they do not substitute for each other:
**money** (Vinnova, Almi, Energimyndigheten, Tillväxtverket, EIC Accelerator,
Eurostars, Innovasjon Norge, Business Finland, Innovationsfonden, Rannís, Swedish
accelerators), **compute** (EuroHPC Playground, Fast Lane, Large Scale, AI for
Science, LUMI, Olivia, Sweden AI Factory, NAISS), and **credits** (AWS, Google
Cloud, Microsoft, Cloudflare, Vercel, Supabase, Neon, MongoDB, Anthropic, OpenAI,
Mistral, Together, Modal, Lambda, RunPod, Hugging Face, Replicate, NVIDIA
Inception).

## Install

```bash
git clone https://github.com/Baltsar/startup-krediter.git
cd startup-krediter
sh bootstrap.sh
```

That links the directory into `~/.claude/skills`, `~/.cursor/skills`,
`~/.codex/skills` and `~/.agents/skills`. Python 3.10 or later, standard
library only. Then ask your agent: "Svenskt AB, två år, fyra personer. Har vi en
chans på gratis GPU?" or invoke `/startup-krediter`.

## How it works

`data/programs.json` holds one record per program with its eligibility rules as
data. `scripts/match.py` reads a founder profile as JSON on stdin and prints the
doors ranked: eligible first, then unknown with the fewest open questions, then
blocked. `SKILL.md` tells the agent how to build the profile from the chat, when
to re-read the live page, and how to answer. `references/*.md` hold the prose
per domain with a quoted sentence from each page as evidence.

```bash
echo '{"country":"SE","legal_form":"company","age_years":2,"employees":4,"need":["compute","credits"],"stack":["anthropic","aws"]}' \
  | python3 scripts/match.py --live
```

Each door comes with a glyph block: `●` met, `×` failed, `○` unknown, `?` the
next question, `→` the amount or the live closing date. Records older than 90
days are flagged `stale` so the agent re-reads the page.

## Contribute a program

Append a record to `data/programs.json` (shape in `data/schema.json`), add an
entry with the matching `{#id}` anchor to the right `references/*.md`, set
`last_verified` to the day you read the page, and run:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

Only facts that appear on the program's own page go into a record. If the page
does not state an amount, the record says so.

A human map of the Swedish GPU landscape: https://opensverige.se/blogg/startup-krediter-gpu-sverige

MIT. Copyright 2026 OpenSverige.
