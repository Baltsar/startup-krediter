---
name: startup-krediter
description: >-
  Use when a founder in Sweden or the Nordics has picked a funding, compute or
  credit program and asks whether they can apply, what the application
  requires, or for help writing, filling in or preparing it, in Swedish,
  English, Finnish, Norwegian or Danish. Triggers on a named program or funder
  with such a question: Vinnova, Almi, Energimyndigheten, forskningsavdrag,
  Business Finland, starttiraha, Innovasjon Norge, SkatteFUNN,
  Innovationsfonden, Innobooster, InnoFounder, EIFO, Rannís, EIC Accelerator,
  Eurostars, EuroHPC, LUMI, NAISS, AWS Activate, Google for Startups,
  Microsoft for Startups, NVIDIA Inception, Claude Startups; "kan vi söka",
  "vad krävs för att söka", "hjälp oss söka", "skriv ansökan", "can we
  apply", "help us apply". Also to add or update a program in this skill's
  data. Not for choosing among programs. Invoke as /startup-krediter.
---

# Startup-krediter

The founder has picked a program. Before they open the form, this skill tells
them three things about it: whether they can apply and what decides it, what
the application will ask of them, and the money and the dates. If they want, it
then writes the application with them, puts the budget in the program's
template, reviews it as an assessor would, and fills the online form after
they have logged in, stopping before the submit button. Logging in, the
declarations and the submit click stay with the founder.

It does not choose the program. In four pre-registered tests a general
assistant searching the web freely found the better program more often, while
this skill was more accurate about the rules of the program in front of it (3
factual errors against 13 in the last test). So it starts where the founder
has already chosen, and spends its words on that one program.

The failure it exists to prevent: the founder decides they qualify, starts the
application, and only then finds a requirement nobody mentioned, or a page
that does not say. Every program in the data carries two lists besides its
eligibility rules: `apply_requirements` (what stops you inside the
application: login method, attachments, co-financing, an account with a
payment method, a partner already committed) and `unclear` (what the page does
not say or contradicts). The founder sees both in the first answer.

Money (grants, loans, accelerator investment), compute (GPU or HPC hours on
public machines) and credits (vendor cloud or API credits) do not substitute
for each other: GPU hours do not pay an API invoice, and credits sit with
whichever vendor the founder already uses.

## Step 1: Find the program

```bash
python3 ~/.claude/skills/startup-krediter/scripts/match.py --find "innobooster"
```

lists the programs whose id or name holds the words, with id, country, kind
and availability. Then:

- **One match:** use its id.
- **A funder with several calls** ("Vinnova", "Business Finland", "Innovasjon
  Norge"): take the call that fits what the founder described (a startup grant
  for a young company, a loan for a later one), name it in the first sentence,
  and ask only when two fit equally.
- **An old or wrong name** ("Tempo", a call closed for good): say so in the
  first sentence and work on the program that replaced it, when the funder's
  own page names one.
- **Not in the data:** work from the program's official pages (Step 4). The
  answer has the same shape; every stopper, amount and date comes from a page
  you read today.
- **No program named** ("vilka bidrag finns för oss?"): this skill does not
  choose. Answer as a careful assistant would without it: search the web
  broadly for the founder's country, stage, sector and region, name the two or
  three most realistic programs with their official links and what decides
  each, and ask which one to go through. Do not rank programs from the data
  file; it covers 73 programs and misses most sector and regional funds. When
  the founder picks one, continue at Step 2.

## Step 2: Build the profile from the chat

Read the facts already in the conversation before asking anything. "Svenskt AB,
två år, fyra personer" gives country, legal form, age and headcount. Asking
again costs trust.

| field | values | notes |
|---|---|---|
| `country` | `SE`, `FI`, `NO`, `DK`, `IS`, any ISO-2 | where the company is registered, or will be. A national program settles it (Vinnova is Swedish); ask only when the program's rules depend on it and the chat does not say |
| `residence_country` | ISO-2 | where the founders live, when it differs |
| `legal_form` | `company`, `nonprofit`, `academia`, `public`, `sole_trader`, `none` | AB, AS, Oy, ApS, ehf, Ltd normalize to `company`; `none` before a company exists |
| `age_years`, `employees` | numbers | `employees` counts the people working in the company, founders included, as the EU SME definition does |
| `revenue_msek`, `balance_msek` | numbers, MSEK | Swedish caps (Vinnova) |
| `revenue_meur`, `balance_meur` | numbers, MEUR | EU SME definition |
| `funding_raised_usd` | number | credit programs cap on this |
| `stage` | `idea`, `pre_seed`, `seed`, `series_a`, `later` | accelerators and credit tiers |
| `vc_backed`, `vc_partner` | bool, list of names | partner-locked credit tiers |
| `stack` | `aws`, `gcp`, `azure`, `cloudflare`, `vercel`, `supabase`, `neon`, `mongodb`, `anthropic`, `openai`, `mistral`, `together`, `modal`, `lambda`, `runpod`, `huggingface`, `replicate`, `nvidia` | credit programs |
| `sector` | `ai`, `deeptech`, `energy`, `climate`, `health`, `fintech`, `saas`, `hardware`, `agriculture`, `defence`, `marine`, `transport`, `semiconductors` | `health` adds the personal-data question |
| `has_vat`, `has_employment`, `has_work_email`, `has_website`, `has_developer`, `workload_defined`, `profit_distributed` | bool | EuroHPC and vendor gates |
| `confirmed` | list of keys | requirements the founder confirms in words; the keys are those in `CONFIRMATIONS` in `scripts/i18n.py`: `aws_paid_plan`, `baltic_marine_monitoring`, `business_not_yet_fulltime`, `consortium_partner`, `dk_financial_foundation`, `each_founder_owns_12_5_percent`, `eic_running_grant_only_applying_blended`, `eip_competence_mix`, `equity_majority_eu_efta_uk`, `eur_200k_raised_or_revenue`, `fulltime_team_member`, `group_unlisted_within_10msek`, `group_within_small_enterprise_limits`, `group_within_sme_limits`, `hpc_experience`, `independent_investor_commits`, `kth_affiliation`, `need_owner`, `new_to_aws_activate`, `no_earlier_bf_funding_same_solution`, `no_third_country_control`, `owner_is_founders_own_holding`, `owners_all_natural_persons`, `project_lead_employed`, `region_skane`, `region_vgr`, `research_background`, `research_west_sweden_university`, `se_rd_staff_on_payroll`, `separate_from_owner_operations` |
| `denied` | list of keys | the same keys when the founder says no ("vi har ingen partner"). A key in neither list stays an open question |
| `lang` | `sv`, `en`, `fi`, `no`, `da` | the founder's language; labels and questions come back in it |

The founder's own situation decides more applications than any company fact,
and no program page reveals it. Set these only from what the founder says; the
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
tell from a right one.

## Step 3: Run the matcher on that program

```bash
python3 ~/.claude/skills/startup-krediter/scripts/match.py --door vinnova-innovativa-startups --live <<'EOF'
{"country":"SE","legal_form":"company","age_years":2,"employees":4,"lang":"sv"}
EOF
```

`--live` asks the Vinnova API for the current round and closing date; `--today
YYYY-MM-DD` pins the date. The JSON has:

- `doors[0]`: the program in full, whatever its status.
- `screen`: up to four questions that decide this program. The first may be
  `basics` (legal form or company age); then the founder's own situation
  (ownership, grants held or running, full-time work, share capital, work
  already started, payroll); then a university link for an early founder or
  personal data in health. Each has `question`, `why` (one short sentence) and
  `decides`.
- `warnings`, `stale`, `lang`. A warning about the founder's own words
  ("anonymised") is a question to ask, not a note to drop.

The program's `status` is `eligible`, `unknown` or `blocked`; `met`, `failed`,
`unknown` hold labels in the founder's language, each unknown with its
question; `apply_requirements` is the checklist of what stops you inside the
application; `unclear`; `also` lists sibling calls (Fast Lane and Large Scale
under Playground) with any extra question they add; `glyph` is the status
block; `what`, `amount`, `next_step`, `apply_url`, `status_url`, `reference`,
`notes`, `availability`, `last_verified`, `stale`, `live` carry the facts;
`application`, when the record has one, describes the form itself.

Labels are generated from each rule's field, operator and value, never written
by hand, so a label cannot claim more than the rule checks. "i Sverige" means
the country matched; it does not mean a company exists. The output also has
`routes`, `unlocks` and `more`; they are for comparing programs, which this
skill leaves to the founder.

## Step 4: Read the page before you quote it

The data says what was true on `last_verified`; the page says what is true
today. Before you state a deadline, an amount, or that a round is open, fetch
the program's `status_url`. A founder who misses a deadline because the skill
quoted a stale date has been harmed by the skill.

Fetch with WebFetch, or curl with a browser User-Agent. Some sites refuse
automated clients (innovasjonnorge.no, innovationsfonden.dk, openai.com, the EU
Funding and Tenders portal, airtable.com); use the in-app browser. If a page
cannot be read, say so and give the link instead of a number. When `stale` is
true, say the record is old and lead with the page. When page and data
disagree, show both and say which is newer.

Also open the general-conditions page or FAQ the program page links to
("General obstacles to granting funding", "Ofte stilte spørsmål", "Allmänna
villkor", terms). Rules that stop an application often live there, not on the
call page: register entries, filed accounts, share capital not used up, market
acceptance, one grant per company. Add anything the checklist lacks, and drop
an unclear line the linked page answers. Give financial conditions in full: a
minimum amount, the funding rate, what is paid when, and any "also enough to
cover other costs" clause.

**A program not in the data.** This step is then the whole source. Read the
call page, the conditions or terms, the FAQ and the application guide, and
build the verdict, the checklist and the unclear points from them, citing the
page for each stopper. Search once for the program's name with "closed",
"replaced" or the year when the page looks old. For a grant, ask the questions
that close most state-aid grants unless the pages settle them: does another
company or a public body own 25 % or more; what public grants or de minimis
aid has the company had in three years, and is any still running; has the work
already started or been ordered; has the company lost half its share capital.

Open the file in `reference` when the founder asks how the process works. Each
entry has who, what, amount, requirements, "Before you apply", "Unclear", how
to apply, a quoted sentence from the page, and gotchas.

## Step 5: Answer

### The first answer

The founder chose this program, so the first answer gives the whole picture
for it at once, in this order:

1. **Verdict**, one or two sentences: it fits on what we know, it does not, or
   it depends on the questions below. Correct a wrong premise first
   ("FoU-avdraget sänker arbetsgivaravgiften på löner, det betalar inte ut
   pengar"). Name the call if the founder named only the funder.
2. **What decides it**: the `screen` questions, numbered, in its order. Each in
   at most 20 words in the founder's language, keeping its facts (25 %, 50 %,
   tio år), then its `why` in a few words. Leave out a question the chat
   already answers.
3. **Status**: the `glyph` in a code block, verbatim except that the `→` lines
   are translated into the founder's language (amounts are English in the
   data). `●` met, `×` failed, `○` unknown, `?` the next question, `→` amount,
   siblings, live closing date, closed or stale note.
4. **Before you apply**: every item in `apply_requirements`, short and
   translated, plus what the conditions page adds (Step 4). Merge two items
   that say the same thing; drop nothing else and add no padding. The deadline
   and how the money is paid are in this list, each with where it comes from
   ("enligt sidan i dag: klarmarkera senast 12 januari 2027 kl 14:00").
5. **Unclear**: one line per item: what is unclear, and whom to ask.
6. **Next step**: from `next_step`, the link, and one line offering to write
   the application with them.

No other programs in the first answer, except as the next section says. Keep
sentences short; never shorten the checklist or the glyph. Aim for under 400
words.

If the founder asked for help applying rather than whether they can, go to
Stage C instead.

### When the program is closed to them

When the glyph's head is `×`, or the founder's own words close the program,
say so in the first sentence with the rule and where it comes from ("EIC
kräver SME-status, och med 62 % ägt av en börsnoterad koncern är ni inte ett
SME"). No checklist. Then at most two lines:

- what would change it, if anything: a new round, a company of the right form,
  the group's figures within the limits, salaried R&D staff;
- the next step the same funder's pages point to, when they point to one (a
  later stage of the same ladder, the program that replaced it), by name and
  one line on what it is, offered and not given in full.

Stay on the kind of question asked. A question about a tax rule gets a tax
answer; a question about equity gets an equity answer. Do not turn a closed
door into a pitch for a grant the founder did not ask about. Give another
program in full only when the founder asks for it.

When the round is closed but the program runs again, say when the next round
opens (from the page) or that no date is published, then give the first
answer in full so they can prepare.

### After the founder answers

Put every answer into the profile and rerun with `--door`. Lead with what
changed: one sentence per answer that settled something ("Inga tidigare
bidrag: den punkten är klar."). If the program is now closed to them, answer
as the section above says. If it is still open, list the `○` lines still open
and anything the answers added to the checklist, then offer to write the
application. Do not repeat the full checklist; one `○` that became `●` is the
whole update. When the founder confirms something a `confirmed` key covers
("ja, vi är KTH-studenter"), add the key and rerun.

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
   <id>`; say if the round is closed and offer to prepare for the next one.
   When `screen` has questions the chat has not answered, ask them with the
   request for material and draft once they are answered. When the deadline
   is less than a week away, draft now and put the questions first, saying
   which answer would stop the application. Never draft for a program the
   founder's answers close: say why, as above.
2. **Material:** take the form's sections, limits, criteria and budget rules
   from the program's `application` block, or from its guide and templates
   when the block is missing. Ask once for the deck, the budget and the facts
   the sections need, and read every file they share.
3. **Draft section by section** in the form's order, language and limits,
   each criterion easy to find. Only the founder's facts; mark gaps
   `[FYLL I: ...]`; never invent customers, numbers, letters or team members.
4. **Budget in the program's template,** with the funding rate, caps and
   excluded costs applied and the arithmetic shown. Flag each cost the rules
   exclude, such as costs before submission or an unpaid founder's time.
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

### Lines that apply to every answer

Write every amount with its currency code: SEK, NOK, DKK, ISK, EUR, USD. Never
"kr" or "kronor" alone. A Danish grant written as "200 000 kr" in a Swedish
answer reads as Swedish kronor, and the difference is a third of the money.

If a checklist item carries a date or figure the page you read today does not
show, keep the item and say where the date comes from ("enligt portalens
call-lista: öppen till 31 december 2026"), or drop only the date. A program
whose page could not be read today is not open; say so.

Never write a percentage or a promise. Vinnova draws lots among equally strong
applications; EuroHPC Playground is first come, first served; accelerators pick
by judgment. Say what the process is instead.

Never ask for something the founder cannot have yet: no revenue or
balance-sheet question to founders without a company.

Worked example. Founder: "Vi ska söka Vinnovas Innovativa startups i januari.
Svenskt AB, två år, fyra anställda. Vad behöver vi ha klart?" `--find
"innovativa startups"` gives `vinnova-innovativa-startups`. Profile:
`{"country":"SE","legal_form":"company","age_years":2,"employees":4,"lang":"sv"}`.
`screen` asks ownership, grants held, share capital and payroll. The answer:
"Innovativa startups passar er på det vi vet; fyra saker avgör det", the four
questions, the glyph, the checklist (konto i Vinnovas e-tjänst, firmatecknare
och projektledare i formuläret, de tre bedömningskriterierna, budget i hela
kronor upp till 500 000 SEK, projektledaren anställd, ingen olönad grundares
tid som lönekostnad, bidraget till bankgiro i bolagets namn, klarmarkera
senast 12 januari 2027 kl 14:00 enligt sidan i dag), the unclear lines (hur man
loggar in, var gränsen för lottningen går, om en ny lön för en grundare räknas
som oförklarad löneökning), and the offer to write the application.

Second example. Founder: "Vi räknar med 20 % tillbaka på konsultfakturorna via
forskningsavdraget. Ingen av oss tar lön än." Profile with `paid_staff: 0`;
the glyph's head is `×`. The answer: "Forskningsavdraget ger er inget i dag:
det är 20 % av lön som bolaget betalar till personer som arbetar med FoU,
avräknat mot arbetsgivaravgiften, och konsultfakturor och olönade grundare
räknas inte." Then what would change it: "Avdraget börjar den månad bolaget
betalar lön till någon som lägger minst halva arbetstiden och 15 timmar i
månaden på FoU." Nothing about grants.

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
  company, grants already held or running, a full-time job elsewhere, work
  already started, a university affiliation and whether the data is really
  anonymous each close programs the company facts leave open. When the
  founder mentions the funder before ("vi sökte Business Finland i våras"),
  ask what they got from it before you say the program fits.
- **Use the call's own name.** Write "Avancerad digitalisering: Cybersäkerhet,
  AI och resiliens", not a shortening that matches another call. A founder
  searching for the short name lands on the wrong page.
- **Never guess country, legal form, headcount, revenue or dividend, and never
  infer a yes/no gate.** "Tre anställda" does not mean the project lead is
  employed three months past the allocation; "2 000 GPU-timmar" does not mean
  the workload is defined. Set `has_employment`, `workload_defined`, `has_vat`
  and the other booleans only when the founder says exactly that. Ask.
- **Keep the machinery out of the reply.** Do not write "the matcher", "the data
  file", "the record", "our list" or "verified yesterday" to the founder. Say
  what the program's page says, and when you read it.
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
the situation fields: an SME-only program gets
`{"any":[{"field":"owner_company_share","op":"lt","value":25},{"field":"confirmed","op":"contains","value":"group_within_sme_limits"}]}`,
and "no earlier or running grant from this fund" is `prior_grants` or
`active_grants` with `excludes` and a list of keys, each named in `GRANT_NAMES`
in `scripts/i18n.py`. Set `route` only when kind and cost do not say it (`tax`
for a deduction claimed in a return). Fill `apply_requirements` (3 to 8 items
from the application page itself) and `unclear`. Set `group` on sibling calls.
An `application` block (portal, login, sections with limits, criteria, budget
rules, attachments, `ai_disclosure`) makes Stage C faster; add one when you
read the form. Add a `{#id}` entry to the right `references/*.md`, set
`last_verified` and `availability`, then run:

```bash
python3 scripts/validate.py && python3 scripts/check_links.py && uv run --with pytest pytest tests/ -q
```

## Files

- `data/programs.json`, `data/schema.json`: the programs and their shape.
- `scripts/match.py`: the matcher (`--find`, `--door`). `scripts/i18n.py`:
  labels, questions and phrases in en, sv, fi, no, da. `scripts/validate.py`,
  `scripts/check_links.py`, `scripts/vinnova_api.py`.
- `references/*.md`: prose per domain; `references/applying.md`: Stage C step by
  step. `tests/`: pytest, no network.
