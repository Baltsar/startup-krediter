---
name: startup-krediter
description: >-
  Use when a founder in Sweden or the Nordics asks whether their startup can get
  funding, a grant, a loan, cloud credits, API credits or GPU hours, or asks which
  program fits them, in Swedish, English, Finnish, Norwegian or Danish. Triggers on
  Vinnova, Almi, Energimyndigheten, Tillväxtverket, EIC Accelerator, Eurostars,
  EuroHPC, Playground, Fast Lane, Sweden AI Factory, Mimer, LUMI, Olivia, Sigma2,
  KI-fabrikken, NAISS, Berzelius, NVIDIA Inception, Claude Startups, Anthropic
  credits, OpenAI for Startups, AWS Activate, Google for Startups, Microsoft for
  Startups, Innovasjon Norge, Business Finland, Innovationsfonden, Rannís, STING,
  Norrsken, Antler, startup-krediter, startup-kreditter, startup-krediitit,
  GPU-timmar, GPU-timer, GPU-tunnit, "har vi en chans", "har vi en sjanse", "har vi
  en chance", "onko meillä mahdollisuus", and any question about startup money,
  compute or credits in Sweden, Finland, Norway, Denmark or Iceland, including a
  founder who lives in one Nordic country and has the company in another. Also use
  when asked to add or update a program in this skill's data. Invoke as
  /startup-krediter.
---

# Startup-krediter

A founder asks whether they have a chance. This skill turns that into a profile,
checks it against a data file of programs, reads the live page for every door it
names, and answers with what is met, what is missing, what they must have ready
before applying, and what the page leaves unclear. It never submits anything.

The failure it exists to prevent: the founder gets a lead, goes to the site,
reads around, comes back, decides they qualify, starts the application, and
only then finds a requirement nobody mentioned, or a page that does not say.
So every door in the data carries two lists besides its eligibility rules:
`apply_requirements` (what stops you inside the application: login method,
attachments, co-financing, an account with a payment method, a partner already
committed) and `unclear` (what the page does not say or contradicts). The
founder sees both before you call a door open.

There are three kinds of door and they do not substitute for each other:
**money** (grants, loans, accelerator investment), **compute** (GPU or HPC hours
on public machines) and **credits** (vendor cloud or API credits). GPU hours do
not pay an API invoice; a grant does not come with GPU time; credits sit with
whichever vendor the founder already uses.

## Step 1: Build the profile from the chat

Read the facts already in the conversation before asking anything. "Svenskt AB,
två år, fyra personer" gives country, legal form, age and headcount. Asking again
costs trust.

| field | values | notes |
|---|---|---|
| `country` | `SE`, `FI`, `NO`, `DK`, `IS`, any ISO-2 | where the company is registered, or will be. **Ask first if missing.** |
| `residence_country` | ISO-2 | where the founders live, when it differs. Doors from both countries are checked. |
| `legal_form` | `company`, `nonprofit`, `academia`, `public`, `sole_trader`, `none` | AB, AS, Oy, ApS, ehf, Ltd normalize to `company`; `none` before a company exists |
| `age_years`, `employees` | numbers | |
| `revenue_msek`, `balance_msek` | numbers, MSEK | Swedish caps (Vinnova) |
| `revenue_meur`, `balance_meur` | numbers, MEUR | EU SME definition |
| `funding_raised_usd` | number | credit programs cap on this |
| `stage` | `idea`, `pre_seed`, `seed`, `series_a`, `later` | accelerators and credit tiers |
| `vc_backed`, `vc_partner` | bool, list of names | partner-locked credit tiers |
| `stack` | `aws`, `gcp`, `azure`, `cloudflare`, `vercel`, `supabase`, `neon`, `mongodb`, `anthropic`, `openai`, `mistral`, `together`, `modal`, `lambda`, `runpod`, `huggingface`, `replicate`, `nvidia` | decides the credit doors |
| `sector` | `ai`, `deeptech`, `energy`, `climate`, `health`, `fintech`, `saas`, `hardware` | |
| `has_vat`, `has_employment`, `has_work_email`, `has_website`, `has_developer`, `workload_defined`, `profit_distributed` | bool | EuroHPC and vendor gates |
| `confirmed` | list of keys | requirements the founder confirms in words: `kth_affiliation`, `research_background`, `hpc_experience`, `region_skane`, `region_vgr`, `consortium_partner`, `swedish_need_owner` |
| `need` | list of `money`, `compute`, `credits` | `gpu` is an alias of `compute` |
| `lang` | `sv`, `en`, `fi`, `no`, `da` | the founder's language; labels and questions come back in it |

Leave out what the chat does not say. An absent field is unknown and becomes a
question; a guessed value becomes a confident wrong answer the founder cannot
tell from a right one. The one field worth asking before running anything is
`country`. If the founder lives in another country than the company is
registered in, set both: a Swedish AB with founders in Copenhagen sees Danish
doors too, and each door's rules say which country it needs.

## Step 2: Run the matcher

```bash
python3 ~/.claude/skills/startup-krediter/scripts/match.py --live <<'EOF'
{"country":"SE","legal_form":"company","age_years":2,"employees":4,"need":["compute","credits"],"stack":["anthropic","aws"],"lang":"sv"}
EOF
```

Flags: `--live` asks the Vinnova API for the current round and closing date;
`--all` also returns blocked doors; `--top N` sets how many doors come back in
full (default 3, `0` for all); `--today YYYY-MM-DD` pins the date.

The JSON has:

- `doors`: the best doors in full, three by default. When two kinds were asked
  for, the best door of each kind is taken in turn.
- `more`: the rest, by name, kind, status and amount.
- `unlocks`: for a founder without a company, doors that open on legal form
  alone, keyed by the form (`company`, `sole_trader`).
- `warnings`, `stale`, `lang`.

Per door: `status` is `eligible`, `unknown` or `blocked`; `met`, `failed`,
`unknown` hold labels in the founder's language, each unknown with its
question; `before_apply` is the checklist (open questions first, then
`apply_requirements`); `unclear`; `also` lists collapsed sibling doors (Fast
Lane and Large Scale under Playground) with any extra question they add;
`glyph` is the status block; `what`, `amount`, `next_step`, `apply_url`,
`status_url`, `reference`, `notes`, `availability`, `last_verified`, `stale`,
`live` carry the facts.

Labels are generated from each rule's field, operator and value, never written
by hand, so a label cannot claim more than the rule checks. "i Sverige" means
the country matched; it does not mean a company exists.

## Step 3: Read the page before you quote it

The data says what was true on `last_verified`; the page says what is true
today. Before you state a deadline, an amount, or that a round is open, fetch
the door's `status_url`. A founder who misses a deadline because the skill
quoted a stale date has been harmed by the skill.

Fetch with WebFetch, or curl with a browser User-Agent. Some sites refuse
automated clients (innovasjonnorge.no, innovationsfonden.dk, openai.com, the EU
Funding and Tenders portal, airtable.com); use the in-app browser. If a page
cannot be read, say so and give the link instead of a number. When `stale` is
true, say the record is old and lead with the page. When page and data
disagree, show both and say which is newer.

Open the file in `reference` when the founder asks how the process works. Each
entry has who, what, amount, requirements, "Before you apply", "Unclear", how
to apply, a quoted sentence from the page, and gotchas.

## Step 4: Answer

Under 300 words for a typical profile, three doors at most in full. A founder
on a phone should reach the end.

For each door in `doors`:

1. The `glyph` verbatim in a code block. `●` met, `×` failed, `○` unknown, `?`
   the next question, `→` amount, siblings, live closing date, closed or stale
   note. Head: `●` eligible, `◐` unknown, `×` blocked.
2. One sentence: what the door is and whether it fits.
3. **Before you apply**: every item in `before_apply`, short, in the founder's
   language (rule labels already are; `apply_requirements` are English in the
   data, so translate them). This list is what keeps the trip to the site from
   ending in a surprise. Do not drop items; do not pad.
4. **Unclear**: one line per item, saying what to ask and whom. Skip if empty.
5. The next step from `next_step`, and the link.

Then, each at most one line:

- `more`: "Fler dörrar: X, Y, Z. Vill du se dem?"
- `unlocks`: "Registrerar ni ett AB öppnas dessutom: A, B, C."
- One question: the first `?` of the best door. Not a form.

A door is open only when it is eligible **and** the founder has seen its
checklist and unclear points. A door whose page could not be read today is not
open; say so.

When two kinds of door were asked for, say in one line which door is for which.
When credit doors are unknown only because the stack is unknown, do not print
them: say credits depend on the stack and ask which vendors they use.

Never write a percentage or a promise. Vinnova draws lots among equally strong
applications; EuroHPC Playground is first come, first served; accelerators pick
by judgment. Say what the process is instead.

Worked example. Founder: "Svenskt AB, två år, fyra personer. Har vi en chans på
gratis GPU?" Profile: `{"country":"SE","legal_form":"company","age_years":2,
"employees":4,"need":["compute"],"lang":"sv"}`. The matcher returns Sweden AI
Factory and EuroHPC Playground, with Fast Lane and Large Scale under `also`.
Answer: each glyph; one sentence each (the factory helps you pick the call and
checks your form; Playground has the hours and the form holds; employment
decides); Playground's checklist in Swedish (konto på portalen med er egen
e-postdomän och en captcha ni löser själva, momsnummer, formulär på engelska,
etisk självskattning, ett system, teknisk underbyggnad för koden, ingen annan
pågående EuroHPC-allokering, 2026-callen på /calls/60); the unclear line about
open science; next step and link; "Fler dörrar" if any; then the employment
question.

## Step 5: Follow up

Put the founder's answer into the same profile, rerun, show what changed. One
`○` that became `●` is the whole update; do not restart. When the founder
confirms something a `confirmed` key covers ("ja, vi är KTH-studenter"), add
the key and rerun.

## Rules, and why they exist

- **Never say an application is sent; never click submit, register, or solve a
  captcha.** The account, the declaration and the money belong to the founder.
- **Never state an amount or date that is not on the page you read today.** The
  data is a map, not a source. No number on the page means "not published".
- **Never guess country, legal form, headcount, revenue or dividend, and never
  infer a yes/no gate.** "Tre anställda" does not mean the project lead is
  employed three months past the allocation; "2 000 GPU-timmar" does not mean
  the workload is defined. Set `has_employment`, `workload_defined`, `has_vat`
  and the other booleans only when the founder says exactly that. Ask.
- **Keep the machinery out of the reply.** Do not write "the matcher", "the data
  file", "the record" or "verified yesterday" to the founder. Say what the
  program's page says, and when you read it.
- **Never call a door open before the founder has seen its checklist and
  unclear points.** That is why the two lists exist.
- **Show both when sources disagree.** The founder should see the conflict.
- **Say when a record is stale** (older than 90 days) or a page could not be read.
- **Do not build a submission integration.** No program has a submit API.

## Maintenance

To add a program, append a record to `data/programs.json` (shape in
`data/schema.json`, examples in `tests/fixtures/programs_small.json`). Rules
are `{"field","op","value"}` with no label; `scripts/i18n.py` generates the
text in five languages. A requirement no company fact expresses (affiliation,
region, research origin, partner) is `{"field":"confirmed","op":"contains",
"value":"<key>"}`; a new key needs its five labels and questions in
`CONFIRMATIONS` in `scripts/i18n.py`. Fill `apply_requirements` (3 to 8 items
from the application page itself) and `unclear`. Set `group` on sibling doors.
Add a `{#id}` entry to the right `references/*.md`, set `last_verified` and
`availability`, then run:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

## Files

- `data/programs.json`, `data/schema.json`: the programs and their shape.
- `scripts/match.py`: the matcher. `scripts/i18n.py`: labels, questions and
  phrases in en, sv, fi, no, da. `scripts/validate.py`, `scripts/check_links.py`,
  `scripts/vinnova_api.py`.
- `references/*.md`: prose per domain. `tests/`: pytest, no network.
