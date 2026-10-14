---
name: startup-krediter
description: >-
  Use when a founder in Sweden or the Nordics asks whether their startup can get
  funding, a grant, a loan, cloud credits, API credits or GPU hours, or asks which
  program fits them. Triggers on Vinnova, Almi, Energimyndigheten, Tillväxtverket,
  EIC Accelerator, Eurostars, EuroHPC, Playground, Fast Lane, Sweden AI Factory,
  Mimer, LUMI, Olivia, Sigma2, KI-fabrikken, NAISS, Berzelius, NVIDIA Inception,
  Claude Startups, Anthropic credits, OpenAI for Startups, AWS Activate, Google for
  Startups, Microsoft for Startups, Innovasjon Norge, Business Finland,
  Innovationsfonden, Rannís, STING, Norrsken, Antler, startup-krediter,
  startup-kreditter, startup-krediitit, GPU-timmar, "har vi en chans", "har vi en
  sjanse", "har vi en chance", and any question about startup money, compute or
  credits in Sweden, Finland, Norway, Denmark or Iceland. Also use when asked to
  add or update a program in this skill's data. Invoke as /startup-krediter.
---

# Startup-krediter

A founder asks whether they have a chance. This skill turns that into a profile,
checks the profile against a data file of programs, reads the live page for every
door it is about to name, and answers with what is met, what is missing, and the
exact next step. It never submits anything.

There are three kinds of door, and they do not substitute for each other:
**money** (grants, loans, accelerator investment), **compute** (GPU or HPC hours
on public machines), and **credits** (vendor cloud or API credits). GPU hours do
not pay an API invoice, a grant does not come with GPU time, and credits sit with
whichever vendor the founder already uses. Say which door you are talking about.

## Step 1: Build the profile from the chat

Read the facts already in the conversation before asking anything. A founder who
wrote "Swedish AB, two years, four people" has given country, legal form, age and
headcount. Asking again costs trust.

| field | values | notes |
|---|---|---|
| `country` | `SE`, `FI`, `NO`, `DK`, `IS`, any ISO-2 | **Ask for this first if it is missing.** The door depends on it. |
| `legal_form` | `company`, `nonprofit`, `academia`, `public`, `sole_trader`, `none` | AB, AS, Oy, ApS, ehf, Ltd all normalize to `company` |
| `age_years`, `employees` | numbers | |
| `revenue_msek`, `balance_msek` | numbers, MSEK | Swedish caps (Vinnova) |
| `revenue_meur`, `balance_meur` | numbers, MEUR | EU SME definition |
| `funding_raised_usd` | number | credit programs cap on this |
| `stage` | `idea`, `pre_seed`, `seed`, `series_a`, `later` | accelerators |
| `vc_backed`, `vc_partner` | bool, list of names | partner-locked credit tiers |
| `stack` | list: `aws`, `gcp`, `azure`, `cloudflare`, `vercel`, `supabase`, `neon`, `mongodb`, `anthropic`, `openai`, `mistral`, `together`, `modal`, `lambda`, `runpod`, `huggingface`, `replicate`, `nvidia` | decides the credit doors |
| `sector` | list: `ai`, `deeptech`, `energy`, `climate`, `health`, `fintech`, `saas`, `hardware` | |
| `has_vat`, `has_employment`, `has_work_email`, `has_website`, `has_developer`, `workload_defined`, `profit_distributed` | bool | EuroHPC and vendor gates |
| `need` | list of `money`, `compute`, `credits` | `gpu` is accepted as an alias of `compute` |
| `lang` | `sv`, `en`, `fi`, `no`, `da` | answer in this language |

Leave out what the chat does not say. The matcher treats an absent field as
unknown and produces the question to ask. A guessed value produces a confident
wrong answer, and the founder cannot tell the difference. The one field worth
asking for before running anything is `country`, because without it every
national door is a guess and the matcher will return all of them.

## Step 2: Run the matcher

```bash
python3 scripts/match.py --live <<'EOF'
{"country":"SE","legal_form":"company","age_years":2,"employees":4,"need":["compute","credits"],"stack":["anthropic","aws"],"lang":"sv"}
EOF
```

The script lives next to this file. Flags: `--live` asks the Vinnova API for the
current round and its closing date (only Vinnova has a usable API); `--all` also
returns blocked doors, for a founder who wants to see what they do not qualify
for; `--today YYYY-MM-DD` pins the date for reproducible runs.

The output is JSON. For each door: `status` is `eligible` (every rule met),
`unknown` (nothing failed, something not yet known) or `blocked` (a rule
failed); `met`, `failed` and `unknown` list the rule labels, each unknown with
the question to ask; `glyph` is the compact status block to show; `what`,
`amount`, `next_step`, `apply_url`, `status_url`, `reference` and `notes` carry
the program facts; `stale` is true when the record is older than 90 days; `live`
holds the Vinnova round when `--live` was used. Doors come sorted: eligible
first, then unknown with the fewest open questions, then blocked. Top-level
`warnings` names profile values that could not be read, and `stale` lists the
stale door ids.

## Step 3: Read the page before you quote it

The data file records what was true on `last_verified`. The page says what is
true today. Before you state a deadline, an amount, or that a round is open,
fetch the door's `status_url` and read it. Rounds close, cohorts fill, tiers get
renamed; a founder who misses a deadline because the skill quoted a stale date
has been harmed by the skill.

Fetch with WebFetch, or with curl using a browser User-Agent. Some sites refuse
automated clients (innovasjonnorge.no, innovationsfonden.dk, openai.com and the
EU Funding and Tenders portal are known cases); use the in-app browser for those.
If a page cannot be read at all, say so and give the founder the link instead of
a number.

Open the file named in `reference` (one of `references/*.md`) when the founder
asks how the process works or what the catch is. Each entry has who, what,
amount, requirements, how to apply, a quoted sentence from the page as evidence,
and gotchas that are too long for the data file.

When `stale` is true, say the record is old and lead with what the page says.
When the page and the data disagree, show both and say which is newer. Picking
one hides the disagreement the founder needs to resolve.

## Step 4: Answer

For each door you present, in the matcher's order:

1. The `glyph` block verbatim, in a code block.
2. Two to four sentences: what the door is, why it fits or what is missing, and
   what the page says today (open, closed, next round, amount).
3. The exact next step from `next_step` and the link.

The glyph symbols: `●` met, `×` failed, `○` unknown, `?` the one question to
ask next, `→` the amount, the live closing date, or a staleness note. The head
symbol is `●` eligible, `◐` unknown, `×` blocked.

Answer in the founder's language. Lead with eligible doors. When several credit
doors are unknown only because the stack is unknown, do not print them all: say
that credits depend on the stack, list the vendors in one line, and ask which
they use. When the founder asked for two kinds of door, group the answer by kind.

Never write a percentage or a promise. Vinnova draws lots among equally strong
applications; EuroHPC Playground is first come, first served; accelerators pick
by judgment. Say what the process is instead.

Worked example. Founder: "Svenskt AB, två år, fyra personer. Har vi en chans på
gratis GPU?" Profile: `{"country":"SE","legal_form":"company","age_years":2,
"employees":4,"need":["compute"],"lang":"sv"}`. The matcher returns EuroHPC
Playground as unknown with employment as the first question. The answer shows
the glyph, then: Playground är EU:s AI-fabrikers öppna GPU-dörr för företag, och
formen håller. Det som avgör är att projektledaren är anställd minst tre månader
efter att GPU-tiden tar slut, momsnummer, yrkesmejl, och att ni kan peka på kod,
ett system och ett antal timmar. Sidan säger idag att callen är öppen och först
till kvarn. Nästa steg: skapa konto på access.eurohpc-ju.europa.eu; ni löser
captchan och klickar själva. Then the link. Then one question: the employment one.

## Step 5: Follow up

The next message usually answers the question. Put the new value into the same
profile, run the matcher again, and show what changed. One `○` that became `●`
is the whole update; do not restart the explanation.

## Rules, and why they exist

- **Never say an application is sent, and never click submit, register, or
  solve a captcha.** The account, the legal declaration and the money belong to
  the founder. The skill drafts, fills what it can, and stops before the button.
  Every `next_step` in the data ends with who clicks.
- **Never state an amount or date that is not on the page you read today.** The
  data file is a map, not a source. If the page does not give a number, say the
  number is not published.
- **Never guess the country, the headcount, the revenue, or whether a dividend
  was paid.** These are exactly the fields that close doors. Ask.
- **Show both when sources disagree.** A slide deck and a web page that give
  different scoring rules are a real signal; the founder should see it.
- **Say when the record is stale** (`stale: true`, older than 90 days) and when
  a page could not be read.
- **Do not build a submission integration.** None of these programs has a submit
  API, and the last click must stay with the account owner.

## Maintenance

To add a program: append a record to `data/programs.json` (shape in
`data/schema.json`, examples in `tests/fixtures/programs_small.json`), add an
entry with the matching `{#id}` anchor to the right `references/*.md`, set
`last_verified` to the day you read the page, then run:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

Eligibility is data: a rule is `{"field","op","value","label","question"}`, a
group `{"any":[...],"label"}` holds when any member holds. Only hard requirements
become rules; preferences go in `notes`. To refresh a record, re-read its
`status_url`, update what changed, and set `last_verified` to today.

## Files

- `data/programs.json`, `data/schema.json`: the programs and their shape.
- `scripts/match.py`: the matcher. `scripts/validate.py`: schema and anchor
  check. `scripts/check_links.py`: probes every url. `scripts/vinnova_api.py`:
  the live Vinnova round.
- `references/nordic-grants.md`, `eu-grants.md`, `compute.md`, `cloud-credits.md`,
  `ai-api-credits.md`, `accelerators-se.md`: the prose per domain.
- `tests/`: pytest, no network.
