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
  when a founder asks for help writing, filling in or preparing an application to
  one of these programs ("hjälp oss söka", "skriv ansökan", "fyll i ansökan",
  "help us apply", "write the application"), and when asked to add or update a
  program in this skill's data. Invoke as /startup-krediter.
---

# Startup-krediter

A founder asks whether they have a chance. This skill turns that into a profile,
checks it against a data file of programs, reads the live page for every door it
names, and answers with what is met, what is missing, what they must have ready
before applying, and what the page leaves unclear. When the founder wants to
apply, it writes the application with them, puts the budget in the program's
template, reviews it as an assessor would, and fills the online form after they
have logged in, stopping before the submit button. Logging in, the declarations
and the submit click stay with the founder.

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
| `confirmed` | list of keys | requirements the founder confirms in words; the keys are those in `CONFIRMATIONS` in `scripts/i18n.py`: `aws_paid_plan`, `baltic_marine_monitoring`, `business_not_yet_fulltime`, `consortium_partner`, `dk_financial_foundation`, `each_founder_owns_12_5_percent`, `eic_running_grant_only_applying_blended`, `eip_competence_mix`, `equity_majority_eu_efta_uk`, `eur_200k_raised_or_revenue`, `fulltime_team_member`, `group_unlisted_within_10msek`, `group_within_small_enterprise_limits`, `group_within_sme_limits`, `hpc_experience`, `independent_investor_commits`, `kth_affiliation`, `need_owner`, `new_to_aws_activate`, `no_earlier_bf_funding_same_solution`, `no_third_country_control`, `owner_is_founders_own_holding`, `owners_all_natural_persons`, `project_lead_employed`, `region_skane`, `region_vgr`, `research_background`, `research_west_sweden_university`, `se_rd_staff_on_payroll`, `separate_from_owner_operations` |
| `denied` | list of keys | the same keys when the founder says no ("vi har ingen partner"). A key in neither list stays an open question |
| `need` | list of `money`, `compute`, `credits`, `support` | `gpu` is an alias of `compute`; `support` is free coaching or programs without cash. A founder asking for money does not get no-cash programs unless they ask for support too |
| `need_eur` | number, EUR | how much money the founder says they need, converted to EUR; only when they name an amount. Doors that pay a small fraction of it rank lower |
| `lang` | `sv`, `en`, `fi`, `no`, `da` | the founder's language; labels and questions come back in it |
| `named` | list of program ids or funder prefixes: `vinnova`, `almi`, `energimyndigheten`, `skatteverket`, `business-finland`, `starttiraha`, `innovasjon-norge`, `forskningsradet`, `innovationsfonden`, `eifo`, `rannis`, `eic-accelerator`, `eurostars` | programs or funders the founder named. Their doors lead their route and their traps lead the `screen` |

The founder's own situation decides more doors than any company fact, and no
search for programs reveals it. Set these only from what the founder says; the
matcher's `screen` asks for the rest.

| field | values | notes |
|---|---|---|
| `owner_company_share` | number, % | the largest share held by another company with its group, or by public bodies together. Venture funds, business angels and universities count only above 50%. Exactly 25% already counts |
| `prior_grants`, `active_grants` | list of program ids, or short keys such as `rannis-sproti` | `prior_grants`: every public grant the company has had, running ones included; `active_grants`: the ones still running. "Inga" is `[]`, an answer |
| `founder_employed_elsewhere`, `fulltime_in_company` | bool | plans, not today: the founder will keep a full-time job outside the company while building it; the founder works full-time in the company, or will once the funded work starts |
| `paid_staff` | number | people the company pays a salary to; founders without salary do not count |
| `affiliation` | `student`, `researcher`, `staff`, `none` | the founder's link to a university now |
| `personal_data` | `none`, `anonymous`, `pseudonymised`, `identifiable` | set only from the answer to the screen question. "Anonymised" is the founder's word, not a fact: data the source can link back is pseudonymised |
| `lost_half_capital`, `work_started`, `on_market`, `de_minimis_eur` | bool, bool, bool, EUR | firm in difficulty, project already started, product already sold, de minimis aid in three years |

Leave out what the chat does not say. An absent field is unknown and becomes a
question; a guessed value becomes a confident wrong answer the founder cannot
tell from a right one. The one field worth asking before running anything is
`country`, and only when the chat does not settle it. A city ("pilotskolor i
Uppsala"), a national legal form (AB, AS, Oy, ApS, ehf) or a national funder
the founder names ("Vinnova känns svårt") settles it: set the country, run the
matcher, and name the assumption in the verdict ("för ett svenskt AB"). A
founder who wrote in Swedish about Uppsala and gets only "which country?" back
has lost a turn. Ask when the clues are missing or point to different
countries ("Ltd", euros, no city). Then run the matcher without a country
anyway and ask, with the country, its `basics` and university or data
questions from `screen`: at most three questions, no doors yet. "Finns det
bidrag för en app?" from a student is answered by the university question,
and a turn spent on the country alone delays it. If the founder lives in another country than the company is
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
full (default 3, `0` for all); `--today YYYY-MM-DD` pins the date; `--door
<id>` returns one program in full with its `application` block, for Stage C.

The JSON has:

- `doors`: the best doors in full, three by default. When two kinds were asked
  for, the best door of each kind is taken in turn.
- `more`: the rest, by name, kind, status and amount.
- `screen`: up to three questions, the ones that decide the most of the best
  doors. The first may be `basics` (legal form or company age, when the best
  doors need it); the rest are about the founder's own situation. Each has
  `question`, `why` (one short sentence) and `decides` (the doors it settles;
  empty for a trap no rule in the data covers, such as patient data or a
  university's IP rules).
- `routes`: the realistic routes (grants, tax relief, loans, compute, credits,
  equity, support) in rank order, each with its `label` in the founder's
  language, a `count` and its best doors.
- `unlocks`: doors that open on legal form alone, keyed by the form (`company`,
  `sole_trader`), and for a founder living abroad, doors that open on the
  registration country alone, keyed `country:XX`.
- `warnings`, `stale`, `lang`. A warning about the founder's own words
  ("anonymised") is a question to ask, not a note to drop.

Per door: `status` is `eligible`, `unknown` or `blocked`; `met`, `failed`,
`unknown` hold labels in the founder's language, each unknown with its question
and, when the founder's situation decides it, its `situation` topic; `route`;
`apply_requirements` is the checklist of what stops you inside the application
(`before_apply` repeats the open questions in front of it); `unclear`; `also`
lists collapsed sibling doors (Fast Lane and Large Scale under Playground) with
any extra question they add; `glyph` is the status block; `what`, `amount`,
`next_step`, `apply_url`, `status_url`, `reference`, `notes`, `availability`,
`last_verified`, `stale`, `live` carry the facts; `application`, when the
record has one, describes the form itself (Stage C). `undersized` is true when
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

### Stage A: the first answer (map, then the questions that decide it)

Map the routes and ask what decides between them before going deep on any
door. A full checklist for a door the founder cannot get is the most expensive
answer this skill can give: in the last test it lost most of its cases that
way, on a company owned by a listed group, a grant the company already held, a
founder with a full-time job, and "anonymised" patient data.

1. **Verdict**, one or two sentences: which route looks most realistic and
   what decides it. Correct a wrong premise first ("FoU-avdraget sänker
   arbetsgivaravgiften på löner, det betalar inte ut pengar").
2. **Routes**, one line each, at most four, from `routes` in its order:

   `Bidrag: ◐ Vinnova Innovativa startups, 300 000 SEK; ◐ Almi Verifieringsmedel, upp till 100 000 SEK.`

   The route label, then its best one or two doors with the head symbol from
   the glyph (`●` eligible, `◐` unknown, `×` blocked), the name and the amount
   in the founder's language. The label already says what the money costs
   (Lån, Ägarkapital); add "avgift" for a paid program. Mark a closed door as
   closed. Leave out a route the founder cannot use now (below), and kinds they
   did not ask for.
3. **Before the details**, the `screen` questions, numbered, in its order. Say
   each in at most 15 words in the founder's language, keeping its facts (25 %,
   50 %, tio år), then its `why` in a few words. When `decides` is not empty,
   name at most two of its programs by a short name, then "och N till":

   `1. Äger ett annat bolag eller en koncern 25 % eller mer av er? Då kan SME-statusen falla (EIC, Eurostars).`

   When `screen` is empty, ask the one question from the rule under "Lines
   that apply to all stages". Never more than three questions.
4. **One closing line**: "Svara på frågorna, eller välj en väg, så går jag
   igenom vad ansökan kräver." Add `more` and `unlocks` lines (below) only if
   they exist.

Show only routes and doors that are realistic for this founder now. One route
is a good answer when nothing else fits; filler costs the founder time and
trust. Leave a door out of Stage A when any of these is true, unless the
founder asked for it by name:
- it is run from another country than the one the founder's company is in
  or would be in (`foreign: true`);
- it charges a fee or takes equity and the founder asked for money, not
  investment;
- it is closed and no next date is published;
- its stage or size clearly does not match the founder (an EU scale-up grant
  for two people with an idea, an investor program for a company with no plans
  to raise);
- its hardest stopper is something the founder has already said they lack.
Such doors may go in the `more` line, marked for what they are.

Match the size of the need. A door with `undersized: true` pays a small
fraction of what the founder said they need. Do not lead with it. When it is
the first step toward a larger door (a grant to form a group before the
project grant), lead with the larger door and name the small one as its first
step.

No glyph blocks, no checklists and no links in Stage A. Aim for under 170
words, never over 200: four route lines and three questions are the ceiling,
not the target.

Write every amount with its currency code: SEK, NOK, DKK, ISK, EUR, USD. Never
"kr" or "kronor" alone. A Danish grant written as "200 000 kr" in a Swedish
answer reads as Swedish kronor, and the difference is a third of the money.

Before you name an amount or say a door is open, read its `status_url`
(Step 4); in Stage A you do not need the linked conditions pages yet.

If the founder named one specific program ("har vi en chans på Vinnova?"),
answer about that program first, still in Stage A form: two sentences on
whether it fits and what decides it, then its one-line door, then at most one
alternative route if it fits better, then the `screen` questions. Correct a
wrong premise in the first sentence. Offer the full checklist instead of
printing it. Stay under 200 words; the founder asked one question and should
get the answer before the paperwork.
If they asked for help applying to it, not whether they have a chance, go
straight to Stage C.

### Stage B: when the founder picks a door

First put every answer from the founder's reply into the profile and rerun the
matcher. Then:

- If the door they picked is now blocked, say so in one sentence with the
  line that closes it ("EIC kräver SME-status, och med 62 % ägt av en
  börsnoterad koncern är ni inte ett SME"), and give the best open door of the
  same route in full instead, or of the next route when the route is empty.
- If a `screen` question that decides the picked door is still unanswered,
  ask it in the first line, then give the door in full with that line first
  among the `○` lines and marked as deciding.
- If they answered the questions without picking, give the best door of the
  first route in full and say in one line which doors the answers closed.

Give the door in full:

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

### Stage C: when the founder wants help applying

When the founder asks for help with the application itself ("hjälp oss söka",
"kan du skriva ansökan", "fyll i den åt oss", "write the application"), the
answer starts with yes: "Ja, jag skriver ansökan med er och fyller i formuläret
fram till skicka-knappen." The second sentence says, once, what stays with
them: they log in with their own BankID, MitID or account, tick the
declarations and press submit. If they offer a login or password, decline in
that sentence and move on. A founder who asked for help and gets a checklist
back has been refused, whatever the checklist says.

Read `references/applying.md` before you draft; it has each step in detail.
In short:

1. **Check fit and timing** in one line each: run the matcher with `--door
   <id>`; ask its `screen` questions first if the founder has not answered
   them (ownership, grants already held, full-time work, data); say if the
   round is closed and offer to prepare for the next one; do not draft for a
   door the program will reject.
2. **Material:** take the form's sections, limits, criteria and budget rules
   from the door's `application` block, or from the program's guide and
   templates when the block is missing. Ask once for the deck, the budget and
   the facts the sections need, and read every file they share.
3. **Draft section by section** in the form's order, language and limits,
   each criterion easy to find. Only the founder's facts; mark gaps
   `[FYLL I: ...]`; never invent customers, numbers or letters.
4. **Budget in the program's template,** with the funding rate, caps and
   excluded costs applied and the arithmetic shown.
5. **Review as the assessor:** score each criterion on the program's scale,
   check every `apply_requirements` item and the conditions page, and name
   the three changes that would help most. No probabilities.
6. **Deliver** as files in the founder's folder when you can write files,
   otherwise ready to paste, field by field.
7. **Hand it over for submission.** If the program has an official agent
   route (`application.agent_path`, as AWS Activate does), stage the
   application there after the founder has seen what you will send, and give
   them the link to submit. Otherwise, if this session has a browser, the
   founder logs in, you fill the fields and upload their files, save a draft,
   and stop before anything that submits, signs or declares. Tell them what is
   left and which button submits. If the program wants AI use disclosed
   (`application.ai_disclosure`), the draft says so.

### Lines that apply to all stages

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

The questions are the `screen` items, in its order: they decide the most doors
and are the ones a careful advisor asks first. When `screen` is empty, ask one
question: the first `?` of the best door of the kind the founder stressed most;
if that door has no open question, the question whose answer opens the most
doors in `unlocks` ("Tänker ni registrera ett aktiebolag nu?"); if `unlocks` is
empty, the hardest stopper of the best door ("Har ni 50 000 euro i eget kapital
i bolaget i dag?"). Never ask for something the founder cannot have yet: no
revenue or balance-sheet question to founders without a company. Three
questions at most, never a form.

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
"employees":4,"need":["compute"],"lang":"sv"}`. `screen` is empty, so the one
question is Playground's first `?`. Stage A:

> Ja, gratis GPU-tid finns för ett svenskt AB på det vi vet. Vägen går via
> EuroHPC, och det som avgör är projektledarens anställning.
>
> Beräkningskraft: ● Sweden AI Factory, gratis hjälp att välja call och granska ansökan; ◐ EuroHPC Playground, 5 000 GPU-timmar gratis i 1 till 3 månader.
>
> Innan detaljerna: Är projektledaren anställd minst tre månader efter att GPU-tiden tar slut?
>
> Svara på frågan, eller välj en väg, så går jag igenom vad ansökan kräver.

Founder: "Ja, hon är fast anställd. Playground." Stage B: rerun with
`has_employment: true`, then the Playground glyph with `→` lines in Swedish,
one sentence, the full checklist in Swedish (konto på portalen med er egen
e-postdomän och en captcha ni löser själva, momsnummer, formulär på engelska,
etisk självskattning, ett system, teknisk underbyggnad för koden, ingen annan
pågående EuroHPC-allokering, 2026-callen på /calls/60, och allt efter
tilldelningen), the unclear line about open science, next step and link.

Second example. Founder: "Vi har ett AB och funderar på Vinnova. Finns det
bidrag för oss?" Profile: `{"named":["vinnova"],"country":"SE",
"legal_form":"company","need":["money"],"lang":"sv"}`. `screen` asks the
company's age, ownership and the share capital. Stage A gives the verdict, the
Bidrag line with the Vinnova door first, the Lån and Skattelättnad lines, then:

> 1. Hur gammalt är bolaget, i år? Vinnova Innovativa Startups kräver högst tio år.
> 2. Äger något annat bolag, en koncern eller en offentlig aktör 25 % eller mer av ert? Då kan SME-statusen falla.
> 3. Har bolaget förbrukat mer än hälften av aktiekapitalet? Vinnova kräver att det inte har det.

## Step 6: Follow up

If the founder picks a door or answers the `screen`, answer in Stage B. If they
ask for help applying, or say yes to it after Stage B, go to Stage C. If they
answer a single question after Stage B, put it into the same profile, rerun,
and show what changed: one `○` that became `●` is the whole update; do not
restart. If the previous turn only asked for the
country and showed no doors, the next answer is a Stage A answer. When the founder
confirms something a `confirmed` key covers ("ja, vi är KTH-studenter"), add
the key and rerun.

## Rules, and why they exist

- **Help with everything up to the button, and never press it.** Write the
  application, fill the budget, review it, fill the form in the founder's own
  logged-in browser. Never log in for them, type a password, personal identity
  number or code, solve a captcha, create an account, tick a declaration, sign,
  or click submit; never say an application is sent. The account, the
  declarations and the money belong to the founder, and BankID or MitID is
  their legal signature. Say this once, as the second sentence, and get on
  with the help.
- **Never state an amount or date that is not on the page you read today.** The
  data is a map, not a source. No number on the page means "not published".
- **Never stretch a rule beyond the page.** A rule applies to exactly what the
  page says it applies to. Vinnova counts the whole group for listing,
  turnover and balance sheet, but the 10-employee cap is the applying
  company's alone. Telling a founder they are ruled out by a rule the page
  does not have is the worst error this skill can make.
- **Ask about the founder's situation before "passar".** Ownership by another
  company, grants already held or running, a full-time job elsewhere, a
  university affiliation and whether the data is really anonymous each close
  doors the company facts leave open. The `screen` asks them; when the founder
  has named a funder ("vi sökte Business Finland i våras"), ask what they got
  from it before you say any of its doors fits.
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
- **Do not build a submission integration.** No program has a submit API,
  and the last click stays with the account owner. Filling the founder's open
  form is help; submitting it is not.

## Maintenance

To add a program, append a record to `data/programs.json` (shape in
`data/schema.json`, examples in `tests/fixtures/programs_small.json`). Rules
are `{"field","op","value"}` with no label; `scripts/i18n.py` generates the
text in five languages. A requirement no company fact expresses (affiliation,
region, research origin, partner) is `{"field":"confirmed","op":"contains",
"value":"<key>"}`; a new key needs its five labels and questions in
`CONFIRMATIONS` in `scripts/i18n.py`. A rule on the founder's situation uses
the situation fields: an SME-only door gets
`{"any":[{"field":"owner_company_share","op":"lt","value":25},{"field":"confirmed","op":"contains","value":"group_within_sme_limits"}]}`,
and "no earlier or running grant from this fund" is `prior_grants` or
`active_grants` with `excludes` and a list of keys, each named in `GRANT_NAMES`
in `scripts/i18n.py`. Set `route` only when kind and cost do not say it (`tax`
for a deduction claimed in a return). Fill `apply_requirements` (3 to 8 items
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
- `references/*.md`: prose per domain; `references/applying.md`: Stage C step by
  step. `tests/`: pytest, no network.
