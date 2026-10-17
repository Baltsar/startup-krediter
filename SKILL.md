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
| `age_years`, `employees` | numbers | `employees` counts the people working in the company, founders included, as the EU SME definition does |
| `revenue_msek`, `balance_msek` | numbers, MSEK | Swedish caps (Vinnova) |
| `revenue_meur`, `balance_meur` | numbers, MEUR | EU SME definition |
| `funding_raised_usd` | number | credit programs cap on this |
| `stage` | `idea`, `pre_seed`, `seed`, `series_a`, `later` | accelerators and credit tiers |
| `vc_backed`, `vc_partner` | bool, list of names | partner-locked credit tiers |
| `stack` | `aws`, `gcp`, `azure`, `cloudflare`, `vercel`, `supabase`, `neon`, `mongodb`, `anthropic`, `openai`, `mistral`, `together`, `modal`, `lambda`, `runpod`, `huggingface`, `replicate`, `nvidia` | decides the credit doors |
| `sector` | `ai`, `deeptech`, `energy`, `climate`, `health`, `fintech`, `saas`, `hardware`, `agriculture`, `defence`, `marine`, `transport`, `semiconductors` | calls tied to a topic stay out of the first answer unless the sector matches |
| `has_vat`, `has_employment`, `has_work_email`, `has_website`, `has_developer`, `workload_defined`, `profit_distributed` | bool | EuroHPC and vendor gates |
| `confirmed` | list of keys | requirements the founder confirms in words: `kth_affiliation`, `research_background`, `hpc_experience`, `region_skane`, `region_vgr`, `consortium_partner`, `need_owner` |
| `need` | list of `money`, `compute`, `credits`, `support` | `gpu` is an alias of `compute`; `support` is free coaching or programs without cash. A founder asking for money does not get no-cash programs unless they ask for support too |
| `need_eur` | number, EUR | how much money the founder says they need, converted to EUR; only when they name an amount. Doors that pay a small fraction of it rank lower |
| `lang` | `sv`, `en`, `fi`, `no`, `da` | the founder's language; labels and questions come back in it |

Leave out what the chat does not say. An absent field is unknown and becomes a
question; a guessed value becomes a confident wrong answer the founder cannot
tell from a right one. The one field worth asking before running anything is
`country`, and only when the chat does not settle it. A city ("pilotskolor i
Uppsala"), a national legal form (AB, AS, Oy, ApS, ehf) or a national funder
the founder names ("Vinnova känns svårt") settles it: set the country, run the
matcher, and name the assumption in the verdict ("för ett svenskt AB"). A
founder who wrote in Swedish about Uppsala and gets only "which country?" back
has lost a turn. Ask when the clues are missing or point to different
countries ("Ltd", euros, no city). If the founder lives in another country than the company is
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
- `unlocks`: doors that open on legal form alone, keyed by the form (`company`,
  `sole_trader`), and for a founder living abroad, doors that open on the
  registration country alone, keyed `country:XX`.
- `warnings`, `stale`, `lang`.

Per door: `status` is `eligible`, `unknown` or `blocked`; `met`, `failed`,
`unknown` hold labels in the founder's language, each unknown with its question;
`apply_requirements` is the checklist of what stops you inside the application
(`before_apply` repeats the open questions in front of it); `unclear`; `also`
lists collapsed sibling doors (Fast Lane and Large Scale under Playground) with
any extra question they add; `glyph` is the status block; `what`, `amount`,
`next_step`, `apply_url`, `status_url`, `reference`, `notes`, `availability`,
`last_verified`, `stale`, `live` carry the facts. `undersized` is true when
the founder gave `need_eur` and the door's maximum is under a fifth of it.

Labels are generated from each rule's field, operator and value, never written
by hand, so a label cannot claim more than the rule checks. "i Sverige" means
the country matched; it does not mean a company exists.

## Step 3: Look beyond the data, once

The data file is a map with edges. A program that is not in it cannot be
matched, and a general web search sometimes finds the better door: a grant for
founders without a company, or a way to spend credits on the vendor the founder
already pays. After the matcher runs, do one web search for programs that fit
this profile and are missing from the matcher's output, phrased like the
founder's need ("bidrag privatperson idé utan bolag Sverige", "use AWS credits
for Anthropic Claude"). Read the official page of anything you find before you
name it.

Aim the search at what the matcher cannot know:

- **No company yet, or a student:** the founder's university or city
  innovation office often has small idea grants that need no company
  ("UiB idé", "KTH Innovation", "Aalto Startup Center"). Search for the
  university or city the founder named.
- **A sector with its own money** (farming, fisheries, defence, culture,
  media): the sector agency usually runs it ("Jordbruksverket innovation",
  "defence innovation startup Norway").
- **A tax rule rather than a grant** (R&D relief on salaries, gifts, owner
  loans): answer it from the tax agency's page.

If you find a door that fits better than the matcher's first door, show it in
Stage A like any other door and give its amount and what decides it; in Stage B
give the checklist you read on its own pages. Keep it to one search and at most
one extra door, so the answer stays short.

The founder never hears about this skill's machinery. Do not write about "our
data", "our list", the matcher, records, or what should be added or maintained.
A founder reading "this program is missing from our list" learns nothing they
can act on and starts to doubt the rest of the answer.

## Step 4: Read the page before you quote it

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

For each door you show in full, also open the general-conditions page or FAQ
the program page links to ("General obstacles to granting funding", "Ofte
stilte spørsmål", "Allmänna villkor", terms). Rules that stop an application
often live there, not on the call page: register entries, filed accounts,
share capital not used up, market acceptance. Add anything the checklist lacks,
and drop an unclear line the linked page answers. Give financial conditions in
full: a minimum amount and any "also enough to cover other costs" clause.

Open the file in `reference` when the founder asks how the process works. Each
entry has who, what, amount, requirements, "Before you apply", "Unclear", how
to apply, a quoted sentence from the page, and gotchas.

## Step 5: Answer

The answer has two stages. The first answer is short so a founder on a phone
can see the options and choose. The full checklist comes when they choose a
door. Nothing is hidden: the first answer says how many requirements each door
carries, so no one walks to a site thinking it is simple.

### Stage A: the first answer (verdict and top three)

1. **Verdict**, one sentence: which door fits best and what decides it.
2. **The question** that moves them forward, one sentence (rule below).
3. **Up to three doors**, one line each, in this shape:

   `◐ EuroHPC Playground: 5 000 GPU-timmar gratis. Avgör: projektledarens anställning. 11 krav i ansökan, 2 oklarheter.`

   Head symbol from the glyph (`●` eligible, `◐` unknown, `×` blocked), the
   name, the amount in the founder's language, the one thing that decides it
   (the first `?` or the hardest stopper in `apply_requirements`), and the
   counts of `apply_requirements` and `unclear`. Mark a closed door as closed.
   Say what the money costs when `founder_cost` is not `none`: "lån",
   "investering mot ägarandel", "avgift". A founder who asked for money must
   not mistake an equity deal or a paid program for a grant.

   Show only doors that are realistic for this founder now. One or two doors
   is a good answer when nothing else fits; filler costs the founder time and
   trust. Leave a door out of Stage A when any of these is true, unless the
   founder asked for it by name:
   - it is run from another country than the one the founder's company is in
     or would be in (`foreign: true`);
   - it charges a fee or takes equity and the founder asked for money, not
     investment;
   - it is closed and no next date is published;
   - its stage or size clearly does not match the founder (an EU
     scale-up grant for two people with an idea, an investor program for a
     company with no plans to raise);
   - its hardest stopper is something the founder has already said they lack.
   Such doors may go in the `more` line, marked for what they are.

   Match the size of the need. A door with `undersized: true` pays a small
   fraction of what the founder said they need. Do not lead with it. When it
   is the first step toward a larger door (a grant to form a group before the
   project grant), lead with the larger door and name the small one as its
   first step.
4. **One closing line**: "Vilken vill ni titta på? Då får ni hela listan över
   vad ansökan kräver." Add `more` and `unlocks` lines (below) only if they
   exist.

No glyph blocks, no checklists and no links in Stage A. Aim for under 150
words, never over 200.

Write every amount with its currency code: SEK, NOK, DKK, ISK, EUR, USD. Never
"kr" or "kronor" alone. A Danish grant written as "200 000 kr" in a Swedish
answer reads as Swedish kronor, and the difference is a third of the money.

Before you name an amount or say a door is open, read its `status_url`
(Step 4); in Stage A you do not need the linked conditions pages yet.

If the founder named one specific program ("har vi en chans på Vinnova?"),
answer about that program first, still in Stage A form: two sentences on
whether it fits and what decides it, then its one-line door, then at most one
alternative if it fits better. Correct a wrong premise in the first sentence.
Offer the full checklist instead of printing it. Stay under 200 words; the
founder asked one question and should get the answer before the paperwork.

### Stage B: when the founder picks a door

When the founder names a door, a number, or says "visa", give that door in full:

1. The `glyph` in a code block, verbatim except that the `→` lines are
   translated into the founder's language (amounts are English in the data).
   `●` met, `×` failed, `○` unknown, `?` the next question, `→` amount,
   siblings, live closing date, closed or stale note.
2. One sentence: what the door is and whether it fits.
3. **Before you apply**: every item in `apply_requirements`, short, translated,
   plus anything the linked conditions page adds (Step 4). The `○` lines in the
   glyph are already the open eligibility questions; do not repeat them. This
   list is what keeps the trip to the site from ending in a surprise. Do not
   drop items; do not pad.
4. **Unclear**: one line per item: what is unclear, and whom to ask.
5. The next step from `next_step`, and the link.
6. One line: "Vill ni se nästa dörr, eller svara på frågan ovan?"

If the founder asks for several doors in full, give them one after another in
this form. Shorten sentences, never the checklist or the glyph.

### Lines that apply to both stages

- When `doors` is empty, nothing in the data fits this founder well. Say so in
  one plain sentence, do the Step 3 search, and offer `more` only as weaker
  options. Doors in `more` with `poor_fit: true` are closed, foreign, in the
  wrong stage or sector, or charge a fee; never promote one into Stage A.
- `more`: "Fler dörrar: X, Y, Z." Mark a closed door as closed. Leave out doors
  with `foreign: true` unless the founder asked about other countries or lives
  in one, and leave out kinds the founder did not ask for.
- `unlocks`: "Registrerar ni ett AB öppnas dessutom: A, B, C." Each entry has
  `name` and `availability`, open doors first; name at most five, then "och N
  till", and mark closed ones as closed. A key such as `country:DK` lists doors
  a company registered in that country would open, for a founder who lives
  there: "Ett bolag registrerat i Danmark skulle öppna: A, B."

Order: keep the matcher's order, except that doors of the kind the founder
stressed most ("vi behöver GPU") come first.

The question is the first `?` of the best door of the kind the founder stressed
most. If that door has no open question, ask the question whose answer opens
the most doors in `unlocks` ("Tänker ni registrera ett aktiebolag nu?"); if
`unlocks` is empty, ask about the hardest stopper of the best door ("Har ni
50 000 euro i eget kapital i bolaget i dag?"). Never ask for something the
founder cannot have yet: no revenue or balance-sheet question to founders
without a company. One question, not a form.

If a checklist item carries a date or figure the page you read today does not
show, keep the item and say where the date comes from ("enligt portalens
call-lista: öppen till 31 december 2026"), or drop only the date.

Never call a door ready to apply for until the founder has seen its Stage B
checklist and unclear points. In Stage A say "passar på det vi vet", not "ni
kan söka". A door whose page could not be read today is not open; say so.

When two kinds of door were asked for, say in one line which door is for which.
When credit doors are unknown only because the stack is unknown, do not list
them: say credits depend on the stack and ask which vendors they use.

Never write a percentage or a promise. Vinnova draws lots among equally strong
applications; EuroHPC Playground is first come, first served; accelerators pick
by judgment. Say what the process is instead.

Worked example. Founder: "Svenskt AB, två år, fyra personer. Har vi en chans på
gratis GPU?" Profile: `{"country":"SE","legal_form":"company","age_years":2,
"employees":4,"need":["compute"],"lang":"sv"}`. Stage A:

> Ja, EuroHPC Playground passar ett svenskt AB på det vi vet och ger 5 000
> GPU-timmar gratis. Det som avgör är projektledarens anställning.
>
> Är projektledaren anställd minst tre månader efter att GPU-tiden tar slut?
>
> ◐ EuroHPC Playground: 5 000 GPU-timmar gratis, 1 till 3 månader. Avgör: anställningen. 11 krav i ansökan, 3 oklarheter.
> ● Sweden AI Factory: gratis hjälp att välja call och granska ansökan, inga egna timmar än. 4 krav, 4 oklarheter.
> ◐ EuroHPC Fast Lane: upp till 50 000 GPU-timmar. Kräver att koden redan körs på en HPC-maskin.
>
> Vilken vill ni titta på? Då får ni hela listan över vad ansökan kräver.

Founder: "Playground." Stage B: the Playground glyph with `→` lines in Swedish,
one sentence, the full checklist in Swedish (konto på portalen med er egen
e-postdomän och en captcha ni löser själva, momsnummer, formulär på engelska,
etisk självskattning, ett system, teknisk underbyggnad för koden, ingen annan
pågående EuroHPC-allokering, 2026-callen på /calls/60, och allt efter
tilldelningen), the unclear line about open science, next step and link.

## Step 6: Follow up

If the founder picks a door, answer in Stage B. If they answer the question,
put it into the same profile, rerun, and show what changed: one `○` that became
`●` is the whole update; do not restart. If the previous turn only asked for the
country and showed no doors, the next answer is a Stage A answer. When the founder
confirms something a `confirmed` key covers ("ja, vi är KTH-studenter"), add
the key and rerun.

## Rules, and why they exist

- **Never say an application is sent; never click submit, register, or solve a
  captcha.** The account, the declaration and the money belong to the founder.
- **Never state an amount or date that is not on the page you read today.** The
  data is a map, not a source. No number on the page means "not published".
- **Never stretch a rule beyond the page.** A rule applies to exactly what the
  page says it applies to. Vinnova counts the whole group for listing,
  turnover and balance sheet, but the 10-employee cap is the applying
  company's alone. Telling a founder they are ruled out by a rule the page
  does not have is the worst error this skill can make.
- **Ask about earlier funding before "passar".** When a door excludes companies
  that already got money from the same funder, and the founder has mentioned
  that funder ("vi sökte Business Finland i våras"), the question is whether
  they have received anything from it before, and which program. Ask it before
  you say the door fits.
- **Use the call's own name.** Write "Avancerad digitalisering: Cybersäkerhet,
  AI och resiliens", not a shortening that matches another call. A founder
  searching for the short name lands on the wrong page.
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
