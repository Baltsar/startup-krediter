# r15 without-skill

## Founder, turn 1
Hi, can you help me write our Rannís application for Tækniþróunarsjóður Sproti? we want to submit asap. pasting what we have:

Company: Hafbók ehf. (Reykjavík) - AI tool that reads fishing vessel logbooks + sensor data and predicts catch quality / fuel use per trip
Stage: working prototype on 3 vessels, LOI from one fishing company
Ask: 24M ISK over 2 yrs (12M + 12M)
Budget yr1: salaries 9.5M (2 devs), cloud 0.8M, consultancy (marine biologist) 1.2M, travel 0.5M
Team: me (Sigrún, CEO, ex-Marel), Tómas (CTO), part-time data scientist

missing: market size, competitor list, milestones. can you write the innovation, market and project plan sections?

## Assistant, turn 1
Hi Sigrún,

I'll start with the timing problem. The autumn Sproti call closed on 15 September 2026 at 15:00, so there's nothing open to submit to right now. Under the current rules Sproti has two deadlines a year, 15 February and 15 September at 15:00. That makes **15 February 2027** the likely next deadline, but Rannís hasn't announced it yet. For the February 2026 deadline the form opened around 1 January. So "asap" really means having everything ready by late January. That gives you about three months to fill the gaps, and the evaluators score those gaps heavily.

Rannís reworked both the form and the rules for 2026, and they may change them again. When the call opens, check both again. Everything below follows the current rules (the H26 version).

---

## How Sproti works now (this changes how you write it)

- **There's no separate project description anymore.** You answer every question directly in the online form on Mínar síður Rannís. That's why I wrote the drafts below as standalone answers keyed to the scoring criteria. Paste them into whatever fields the form gives you.
- **There are two stages.** In the pre-stage, nine screening questions are each marked Yes, Unclear or No, and **a single No rejects the application**. Only applications graded A1 or A2 (the top 25%) are invited to the main stage.
- **You can write in English.** The title and the short public summary must be in both Icelandic and English.
- **You can add a video** of up to 5 minutes, as a link. It's optional.

**The nine screening questions** (the form is in Icelandic, these are glosses):
1. Is the project at the right maturity stage for Sproti?
2. Is a practical solution being developed?
3. Is the problem or need clear and real?
4. Is there a clear target group?
5. Is the solution clear and linked to the problem?
6. Are the revenue or value-creation assumptions credible?
7. Is the value proposition clear and convincing?
8. Does the project have an advantage competitors would find hard to build?
9. Does the project involve real development, with real uncertainty or challenge?

**Main-stage scoring:** each item is scored 0–5, and some items have minimum scores.

| Criterion | Weight |
|---|---|
| 1. Market need and value creation (problem 10, market potential 10, value for the Icelandic economy 5) | 25% |
| 2. Novelty and market advantage (novelty 10, competitive advantage 10, protecting your position 5) | 25% |
| 3. Execution (work/time/cost plan 15, **team 15**, market plan 5, funding strategy 5) | **40%** |
| 4. Social impact, sustainability and responsibility | 10% |

The project plan and team together are 30% of the score, more than "innovation" itself. Social impact is another 10%, so I've drafted that section too.

---

## Checks before you write anything

- **Company age.** Hafbók ehf. must be under 5 years old at the deadline, counted from its founding date. When was it founded?
- **Your ask.** 24M ISK (12M + 12M) is exactly the cap, so it fits, but there's no headroom. The board approves one year at a time. Payments come as 40% on signing, 40% after the progress report is approved, and 20% after the interim or final report.
- **De minimis.** Sproti is de minimis aid, capped at €300,000 per company over three years. You'll declare all public aid received this year and in the two previous fiscal years. If the total, including this grant, exceeds the cap, nothing is paid out.
- **One grant at a time.** You can generally hold only one active development grant as lead applicant. You can't hold Sproti and Vöxtur at the same time.

## Budget: fix these before you submit

- **Year 1 adds up to exactly 12.0M, the same as the grant.** Sproti requires no co-funding, so that's allowed, but it leaves no buffer. Booked costs must be at least as large as the grant. If any line is disallowed, you drop below it. You can add **overhead** of up to 25% of total cost minus purchased services. You currently have none.
- **Salaries:**
  - Salaries must be actual pay plus employer charges, by time spent on the project. Hourly consultancy rates aren't allowed.
  - Your budget says "2 devs", but the team is you, Tómas and a part-time data scientist. List each person with their role, % of time on the project and monthly cost. If the devs are new hires, say when and how you'll hire them.
  - 9.5M looks low for two full-time developers including employer charges. If they're part-time or the founders are on reduced pay, say so. The evaluators score how realistic the cost plan is.
- **Marine biologist (1.2M).** This counts as a purchased service. The supplier must be unrelated to Hafbók, meaning not owned or controlled by you or in the same group. Describe what you're buying, why, and the cost. Alternatively, you could bring in a university or research institute as a co-applicant. The board looks favourably on research collaboration. Hafbók must keep at least 60% of the grant each year.
- **Travel (0.5M).** Give the domestic and foreign totals and the purpose of each trip.
- **Market infrastructure is capped at 10% of total project cost.** Applications above that are **rejected without review**. This category covers market research, marketing plans, website and branding, trade-show travel and marketing consulting. Keep it small and make the plan mostly development.
- **Cloud (0.8M).** This is fine. Describe it in one line, e.g. "training compute and storage for N vessels".
- **Not fundable:** grant-writing costs, patents, equipment purchases (only depreciation of specialised equipment counts) and company formation.
- **Year 2 budget.** I need it, broken down the same way as Year 1.

---

## Drafts

Anything in [brackets] is a fact only you have. I haven't invented any numbers, so don't submit anything that's still in brackets. Please also check every claim about your product against what it actually does today.

### Title and public summary

**Title (EN):** Hafbók: per-trip prediction of catch quality and fuel use for fishing vessels
**Title (IS), suggestion, please check the wording:** Hafbók – spá um olíunotkun og gæði afla í hverri veiðiferð

**Public summary (EN), to be translated into Icelandic:**
Fuel and catch quality decide whether a fishing trip pays off. Today both are known only after the trip. Hafbók combines vessel logbooks with onboard sensor data and predicts a trip's fuel use and catch quality, so skippers and shore managers can plan better trips. A working prototype runs on three vessels, and [fishing company] has signed a letter of intent. Over two years we will extend the models to [N] vessels and validate them against landing data. We will turn the pilot into a paid product.

### 1. Market need and value creation (25%)

**Problem.** Fuel use and catch quality largely decide a trip's profit, and fishing companies plan trips with little foresight of either. Decisions on grounds, towing, speed and time at sea draw on skipper experience and last season's results. The data to do better already exists in electronic logbooks and onboard sensors ([list the sensors you use]). But it sits in separate systems and is reviewed after the fact, if at all. [Add one concrete number from your pilot vessels: fuel as a share of operating cost, or the price gap between quality grades for the same species.] [Add a one-sentence quote from the LOI company or a pilot skipper describing the problem.]

**Target group.** We'll start with Icelandic vessel operators whose trawlers and larger decked vessels already carry the sensors and electronic logbooks Hafbók uses. Statistics Iceland counted 1,531 Icelandic fishing vessels at the end of 2024: 37 trawlers, 675 decked vessels and 820 undecked boats. Our serviceable market in Iceland is [N] of these vessels, [explain how you picked them, e.g. trawlers plus decked vessels over X m with engine and sensor data].

**Market size (bottom-up).**
- Iceland: [N vessels] × [ISK per vessel per year] = [ISK per year]
- Next markets: [Norway / Faroe Islands / Greenland]: [N vessels, from each country's fisheries registry] × [price] = [ISK per year]
- Target 36 months after project start: [N] paying vessels, [ISK] annual recurring revenue

Context: Icelandic seafood exports were about ISK 359 billion in 2025, according to Radarinn. In an industry that size, small percentage gains in fuel cost or catch price are worth a lot. Don't use the export figure as your market size, though. The evaluators want the bottom-up number.

**Value for customers.** [Pilot results so far: fuel per trip or per kg caught versus baseline, and any quality result.] Hafbók turns data the vessel already collects into a forecast before the trip and advice during it.

**Revenue model.** We'll charge a subscription per vessel per year at [price], with onboarding priced at [price or "included"]. [Fishing company] has signed a letter of intent covering [what it covers: number of vessels, pilot, intent to buy]. Our goal is to convert this into a paid pilot by [month].

**Value for Iceland.** This is software built on Icelandic fisheries know-how and exportable to other North Atlantic fleets. It creates skilled jobs in Reykjavík and helps the fleet get more value from the same quota.

### 2. Innovation: novelty and competitive advantage (25%)

**What is new.** Hafbók predicts the outcome of each trip, both catch quality and fuel use, by combining logbook records with onboard sensor data from the same trip. Existing tools do something different. Some forecast where the fish are, some measure the catch once it's on board, and some log data for compliance and shore visibility. Based on their public descriptions, none of the tools below predicts both fuel and catch quality per trip from the vessel's own data. [Confirm this matches what your prototype actually does.]

**Real development and uncertainty.** This answers screening question 9, so it must be specific. We don't yet know whether we can:
- generalise models trained on 3 vessels to vessels with different gear, engines and sensor setups;
- build reliable ground truth for quality by linking trip data to quality measured at landing or processing ([source of the quality data]);
- separate the drivers of fuel use (weather, towing, speed, load) well enough to give useful advice rather than just a forecast;
- cope with gaps in the data, manual logbook entries and sensor drift.

Current status: [what the prototype predicts today, on how many trips, and accuracy against a simple baseline].

**Competitors and alternatives**

| Company | What it does | How Hafbók differs |
|---|---|---|
| GreenFish (Reykjavík) | AI forecasts of fishing grounds and catch from satellite and ocean data | Forecasts where to fish. Hafbók forecasts what a trip costs in fuel and yields in quality |
| Catchwise (Oslo) | AI search and route predictions from satellite AIS, historical catch and ocean data. Raised €1.25M pre-seed in March 2025. Claims up to 50% fuel savings | Same: search and routing. No per-trip catch-quality prediction [verify] |
| Maritech Eye | Hyperspectral camera that recognises species and size in whitefish catch on board. Installed on Útgerðarfélag Reykjavíkur vessels | Measures the catch once caught. Could be a data source or partner |
| Trackwell (Iceland) | Electronic logbook, VMS, electronic reporting and a shore portal | Handles reporting and visibility. Hafbók builds on logbook data, so Trackwell is a possible integration partner |
| Hefring Marine (IMAS) | AI guidance from onboard sensors on speed for sea conditions, fuel and machinery health. Users include rescue services, navies, passenger and tourism operators | Not fishing-specific and uses no catch data |
| Arctic Economy (CATCH) | Neural networks on towing data going back to 2000, used to forecast stock movements and support quota decisions | Works at stock and quota level, not on individual trips |
| Status quo | Skipper experience, spreadsheets, engine dashboards | [What the LOI company uses today] |

[Add any tool your LOI company or pilot skippers mentioned.]

**Protecting your position (5%).** Every vessel adds to a dataset that links trip data to outcomes, and the models are trained on it. A new entrant would need years of the same data. [Describe your data agreements with vessel owners and who owns the data.] [List the integrations you have or plan, e.g. logbook systems.]

### 3. Social impact (10%)

Every litre of fuel saved per kg of catch cuts CO2 directly. [Fishing fleet's share of Iceland's emissions, from the national emissions inventory.] [Cite the government's current target for fishing-fleet emissions from the climate action plan, and check the figure at the source.] Better catch quality means more value from each kg caught and less downgraded fish. Risks and how we handle them: [crew data privacy, e.g. no individual-level monitoring], [over-reliance on predictions: the skipper keeps the decision].

### 4. Project plan: work, time and cost (15%, within execution at 40%)

**Work packages (24 months)**

| WP | Content | Months | Lead | Share of cost |
|---|---|---|---|---|
| WP0 | Project management, reporting | 1–24 | Sigrún | [%] |
| WP1 | Data platform: ingest logbook and sensor data from 3 → [N] vessels, data quality checks, common schema | 1–9 | Tómas | [%] |
| WP2 | Fuel model: per-trip forecast plus drivers of fuel use | 3–15 | [data scientist] | [%] |
| WP3 | Catch-quality model, with the marine biologist: define quality measures, link to landing data | 3–18 | [name] + marine biologist | [%] |
| WP4 | Pilot with [LOI company] on [N] vessels: measure against baseline, convert to a paid contract | 6–24 | Sigrún | [%] |
| WP5 | Product: views for skipper and shore manager, onboarding for new vessels | 9–24 | Tómas | [%] |
| WP6 | Market infrastructure: pricing tests, market validation | 12–24 | Sigrún | **under 10% of total** |

**Milestones.** They're measurable and line up with the progress report and with year 2 approval.
- **M1 (month 3):** Data agreement signed with [LOI company]. Data flowing from [N] vessels.
- **M2 (month 6):** Fuel model v1 reaches [error metric ≤ X%] on held-out trips from [N] vessels.
- **M3 (month 12):** Quality model v1 validated against [landing or processing data] at [metric]. Pilot running on [N] vessels. *This is the year 1 decision point.*
- **M4 (month 18):** Pilot results show [X% lower fuel per kg] or [quality outcome] against baseline. Product v1 released.
- **M5 (month 24):** [N] paying vessels or a signed contract with [LOI company]. Ready for the next funding round.

**Main risks**

| Risk | Mitigation |
|---|---|
| Vessel owners won't share data | Written data agreement first (M1). Value shown on the 3 existing vessels |
| No reliable quality ground truth | Marine biologist defines measures in WP3. [Agreement with a processor or auction for landing data] |
| Models don't generalise to new vessels | Add vessels gradually, test on held-out vessels, per-vessel calibration |
| Hiring delays | [Named candidates, or how you'll hire] |
| Customer doesn't convert to paid | Pilot success criteria agreed with [LOI company] at the start |

### Team (15%) and funding strategy (5%)

You didn't ask for these, but they're scored, and team is worth as much as the work plan.
- **Team:** [Sigrún: what you did at Marel and why it matters here], [Tómas: technical background, what he built], [data scientist: background, % of time], [marine biologist: who, and what expertise].
- **Funding:** [How you'll cover costs above the grant], [when revenue starts], [next round or investors]. The rules name Vöxtur as the expected next step after Sproti.

---

## What I need from you to finish this

1. Hafbók's founding date (for the 5-year limit).
2. Prototype results: what it predicts, on how many trips, and accuracy against a baseline.
3. LOI details: which company, how many vessels, and what it commits to.
4. Your price per vessel, even as a hypothesis.
5. Who the "2 devs" are, with their time on the project and salaries, plus the Year 2 budget.
6. Any public grants or aid in 2024, 2025 and 2026, for the de minimis declaration.
7. Who owns the vessel data, and where the quality ground truth comes from.

Once I have these, I'll fill in the brackets and tighten everything to the form's fields when it opens. Rannís can answer questions about the call: taeknithrounarsjodur@rannis.is, +354 515 5800 (Mon–Thu 10–12). Ask them to confirm the February 2027 date. Also ask whether a prototype on three vessels with an LOI counts as "right stage" for Sproti, since that's screening question 1.

**Sources**
- [Sproti grant page (island.is, EN)](https://island.is/en/grants-plaza/grant/1-46) and [IS](https://island.is/styrkjatorg/styrkur/1-46)
- [Rules and guidance H26: Sproti, Vöxtur, Markaður (PDF)](https://assets.ctfassets.net/8k0h54kbe6bj/5ve9pGv87bP55hYSDMsxow/f5863e2c972592719afb9e2263e50f4a/TS_Reglur_SVM-H26.pdf)
- [Autumn 2026 call, deadline 15 Sept 2026](https://island.is/v/taeknithrounarsjodur/frett/opid-fyrir-umsoknir-i-taeknithrounarsjod)
- [Guidance and rules page](https://island.is/v/taeknithrounarsjodur/leidbeiningar-vegna-umsokna)
- [Evaluation and allocation](https://island.is/v/taeknithrounarsjodur/mat-og-uthlutun-taeknithrounarsjods)
- [Statistics Iceland: Icelandic fishing fleet in 2024](https://old.statice.is/publications/news-archive/fisheries/icelandic-fishing-fleet-in-2024/)
- [Icelandic seafood export value 2025 (Radarinn, via We Are Aquaculture)](https://weareaquaculture.com/markets/icelandic-seafood-exports-value-increased-by-around-4-in-2025)
- [Catchwise pre-seed (Silicon Canals)](https://siliconcanals.com/catchwise-bags-1-25m)
- [GreenFish (Global Seafood Alliance)](https://www.globalseafood.org/advocate/here-to-stay-and-evolving-fast-how-greenfishs-ai-powered-fish-forecasting-tech-is-modernizing-commercial-fisheries/)
- [Maritech Eye in Iceland (Fish Focus)](https://fishfocus.co.uk/new-maritech-eye-contract-in-iceland/)
- [Hefring Marine, Icelandic Innovation Award 2025 (Fish Focus)](https://fishfocus.co.uk/hefring-marine-receives-the-icelandic-innovation-award-2025/)
- [Arctic Economy CATCH (World Fishing)](https://www.worldfishing.net/fisheries/exclusive-ai-fisheries-forecasting-targets-quota-revolution/1509219.article)
- [Trackwell (World Fishing)](https://www.worldfishing.net/trackwell-g62/1469994.article)

## Founder, turn 2
ok thanks, answers:

1. registered 11 March 2024.
2. it predicts catch quality and fuel use per trip, running on the 3 vessels. number of trips and accuracy vs baseline - don't know.
3. LOI details (which company, how many vessels, what it commits to) - don't know.
4. price per vessel - don't know.
5. right now it's me and Tómas on salary since January 2026, 650,000 ISK/month each, plus the data scientist on contract at 40%. who the "2 devs" are and % time on the project - don't know. yr2 budget - don't know, we only have the 12M total.
6. Tækniþróunarsjóður Fræ in 2024, 2M ISK, finished 2025. de minimis: none recorded.
7. logbook and sensor data from the 3 vessels under agreements with the owners, plus public weather and ocean data. where the quality ground truth comes from - don't know.

and yes please fill it in. here's what else we have:

Revenue 2025: 3.2M ISK in pilot fees. We got a Fræ grant in 2024 for the first prototype. Target customers: Icelandic and Faroese fishing companies, later Norway. Tómas teaches a bit at Reykjavík University.

## Assistant, turn 2
Hi Sigrún,

Thanks, this helps a lot. Your 2025 pilot revenue is the strongest evidence in the application, and the company's age is fine. Your answers also turn up three corrections, plus five gaps someone on your team can probably close in an afternoon. First, I need to correct something I told you last time.

## Correction: February is only the first stage

Last time I said to have everything ready by late January. That overstated it. Under the H26 rules, the February deadline (likely 15 February 2027) is for the **first stage only**. Evaluators mark the nine screening questions Yes, Unclear or No. The cost checks are marked as main-stage only: market infrastructure under 10%, and Hafbók keeping at least 60% of the grant. The cost figures go into the second-stage application. The first-stage result is due within three months of the deadline. I couldn't find when the main-stage application is due, so ask Rannís.

For late January you need:
1. The title and public summary, in Icelandic and English.
2. Answers to the nine screening questions (drafts below).
3. Your 2025 annual accounts. The rules recommend attaching the latest ones, and they show the pilot revenue.
4. The LOI, if you can find it (see gap 3 below).

The rules don't say outright whether the first-stage form asks for any cost figures, so keep a budget ready anyway. The work plan and budget below also have to match what you claim in February.

## What your answers settle

- **Company age.** Registered 11 March 2024, so 2 years 11 months old at 15 February 2027. You stay eligible for deadlines up to February 2029.
- **No grant conflict.** Fræ finished in 2025, so you hold no active development grant.
- **Fræ helps you.** Sproti is the natural next step after Fræ. Say what the Fræ prototype delivered. Your Fræ final report may already contain the first test results.
- **Stage.** The rules use a 1–5 maturity scale, and Sproti generally expects levels 2–4. A prototype running on 3 vessels with paid pilots looks like level 4: tested in realistic conditions, but still needing development. The risk is that an evaluator reads paid pilots as level 5 ("ready for the next development or funding step") or as Vöxtur territory. A No on question 1 rejects the application. So the Q1 draft below leans on what is still unproven. I'd still ask Rannís to confirm the fit.

## Three corrections

**1. Fræ is de minimis aid, so declare it.** The Fræ grant page says the category falls under the de minimis rules, so "none recorded" isn't right. List the 2M ISK when you declare public aid. If the grant went to Hafbók ehf., not to you personally before the company existed, it counts. 2M + 24M = 26M ISK, about €180,000 at roughly 145 ISK per euro. That's well under the €300,000 cap.

**2. The salary line doesn't match your payroll.**
- You and Tómas each cost roughly 767,000 ISK a month. That's 650,000 salary plus about 18% employer charges: 6.35% tryggingagjald plus the usual 11.5% employer pension. Your payroll provider has the exact figure, so use theirs.
- That's about 9.2M ISK a year each at 100%, or 18.4M for both. Your two salaries alone are more than the 12M annual cap.
- Each 10% of one founder's time on the project adds about 0.92M ISK a year.
- So the 9.5M "2 devs" line covers about half of your two salaries. Is it you and Tómas at about 50% each, or someone else? Whoever wrote that line knows.
- A budget above 12M is allowed, and it helps. Booked costs must be at least as large as the grant, so the extra gives you a buffer. But then your funding-strategy answer has to explain how Hafbók pays the difference. Pilot revenue is the obvious source.
- Only costs incurred after the application deadline and within the contract period can be approved. Your 2026 salaries don't count.
- Reports need timesheets and a ledger extract, so use percentages you'll actually log. Tómas's share should leave room for his teaching at RU.

**3. The data scientist's contract.** Salaries must be actual pay plus employer charges. Billed or hourly rates aren't allowed. Purchased services must come from an unrelated legal entity. The rules don't say how they treat an individual on contract, so there are two options:
- **Payroll at 40%.** The cost is actual pay plus charges, and it counts toward the overhead base.
- **Purchased service, invoiced through the data scientist's own company.** This doesn't count toward the overhead base, because overhead is capped at 25% of total cost excluding purchased services.

Ask Rannís which they accept for a 40% contractor.

## Five gaps that can still sink the first stage

| Gap | Screening question at risk | Where the answer is |
|---|---|---|
| 1. Trips run so far, and accuracy against a simple baseline | Q2, Q9 | Tómas. Also check your Fræ final report |
| 2. Where the quality ground truth comes from | Q5, Q9 | Tómas. If the model predicts quality, it was checked against something |
| 3. LOI: which company, how many vessels, what it commits to | Q6, Q7 | The signed letter |
| 4. Price per vessel | Q6 | The invoices behind the 3.2M ISK: who paid, for which vessels, how many months, subscription or one-off fee |
| 5. Who the "2 devs" are | Main stage | Whoever wrote the 12M budget |

Two notes:
- **If there's no quality ground truth yet,** don't claim the prototype predicts quality accurately. Say it produces quality estimates that haven't been validated yet, and make validating them the core development task. That's honest, and it strengthens Q9 (real uncertainty).
- **If you can't find the LOI, or it was only verbal,** leave it out. Rannís can ask for it, and the rules encourage attaching letters of intent from partners.

---

## Drafts

Anything in [brackets] is a fact only you have. Don't submit anything still in brackets, and check every product claim against what the prototype does today.

### Title and public summary

**Title (EN):** Hafbók: per-trip prediction of catch quality and fuel use for fishing vessels
**Title (IS), a suggestion, please check the wording:** Hafbók – spá um olíunotkun og gæði afla í hverri veiðiferð

**Public summary (EN), to translate into Icelandic:**
Fuel and catch quality decide whether a fishing trip pays off. Today both are known only after the trip. Hafbók combines vessel logbooks, onboard sensor data and public weather and ocean data to predict each trip's fuel use and catch quality. A prototype, first built with a Fræ grant, runs on three vessels. Pilot customers paid ISK 3.2 million in pilot fees in 2025. Over two years we will validate the quality predictions against [landing or processing data] and extend the models to [N] vessels. We will turn the pilots into a paid product for Icelandic and Faroese fishing companies.

### First-stage answers, one per screening question

The rules point applicants to the Lean Canvas, so the form's fields may follow its boxes rather than these nine questions. Each answer stands alone, so you can move them around.

**Q1. Is the project at the right stage for Sproti?**
Hafbók has been tested in real conditions, and substantial development is still ahead. Our prototype, first built with a Fræ grant in 2024, runs on three fishing vessels in normal operation. It has produced predictions for [N] trips so far. Pilot customers paid ISK 3.2 million in pilot fees in 2025. This project addresses what is still unproven:
- whether the quality predictions hold against [landing or processing] data;
- whether the models work on vessels with different gear, engines and sensors;
- whether forecasts can become advice that skippers act on.

Sproti funds that step. A larger next step, such as Vöxtur, would follow only if the results justify it.

**Q2. Is a practical solution being developed?**
Yes. Hafbók is software for fishing companies. It reads the vessel's logbook and sensor data ([list the sensors: e.g. engine, fuel flow, GPS]) together with public weather and ocean data. It predicts each trip's fuel use and catch quality. Skippers and shore managers see [what the user sees today]. It runs on three vessels today, under data agreements with their owners.

**Q3. Is the problem clear and real?**
Fuel and catch quality largely decide a trip's profit. Yet fishing companies plan trips with little foresight of either. Choices about grounds, towing, speed and time at sea rest on skipper experience and last season's results. The data to do better already exists in electronic logbooks and onboard sensors. But it sits in separate systems and is reviewed after the trip, if at all. Pilot customers paid ISK 3.2 million in 2025 to test a solution, which shows the need is real. [One number from your pilots: fuel as a share of trip cost, or the price gap between quality grades.] [A one-sentence quote from a pilot customer.]

**Q4. Is there a clear target group?**
Our first customers are Icelandic fishing companies whose trawlers and larger decked vessels carry electronic logbooks and engine sensors. Statistics Iceland counted 37 trawlers, 675 decked vessels and 820 undecked boats at the end of 2024. Our Icelandic market is [N] of these vessels ([how you pick them, e.g. trawlers plus decked vessels over X m with engine data]). Faroese fishing companies come next, then Norway. The buyer is [owner or operations manager]. The users are skippers and shore managers.

*Market size, for the main stage ("market potential"):*
- Iceland: [N vessels] × [price per vessel per year] = [ISK per year]
- Faroe Islands: [N vessels, from the Faroese vessel register or Hagstova Føroya] × [price] = [ISK per year]
- Norway, later: [N vessels, from Fiskeridirektoratet's vessel register] × [price] = [ISK per year]
- Target 36 months after project start: [N] paying vessels, [ISK] annual recurring revenue

**Q5. Is the solution clear and linked to the problem?**
The problem is that fuel and quality outcomes are known only after the trip. Hafbók moves the forecast to before the trip, using data the vessel already collects. The fuel model shows what drives fuel use, such as speed, towing and weather, so the skipper can change it. The quality model links trip conditions ([e.g. time at sea, handling, temperature]) to quality measured at [landing or processing]. [Replace with what the prototype actually does today.]

**Q6. Are the revenue assumptions credible?**
Customers already pay. Pilot fees brought in ISK 3.2 million in 2025 from [N] customers on [N] vessels. We will sell an annual subscription per vessel at [price], with onboarding [priced at X / included]. [LOI company] has signed a letter of intent covering [N vessels, and what it commits to]. Our goal is to convert this into a paid contract by [month]. [If you can't find the LOI, delete the last two sentences.]

**Q7. Is the value proposition clear and convincing?**
Before a trip, Hafbók tells a fishing company what it will likely cost in fuel and what quality the catch is likely to reach. It uses data the vessel already collects, [with no new hardware: check]. [Pilot result: fuel per trip or per kg against baseline, or a quality result.]

**Q8. Does the project have an advantage competitors would find hard to build?**
Existing tools solve neighbouring problems. GreenFish and Catchwise forecast where to fish. Maritech Eye measures the catch once it's on board. Trackwell handles logbooks and reporting. Hefring Marine advises on speed and fuel, but not for fishing and without catch data. Based on their public descriptions, none predicts both fuel use and catch quality per trip from the vessel's own data. Each vessel we add grows a dataset that links trip data to outcomes, collected under agreements with vessel owners. [Who owns the data and the trained models under those agreements.] [What the team brings that others lack: Sigrún's Marel background, Tómas's expertise.]

For the main stage, use the full competitor table from my last message.

**Q9. Does the project involve real development, with real uncertainty?**
Yes. We don't yet know whether we can:
- validate quality predictions against an independent quality measure ([source]);
- generalise models trained on 3 vessels to vessels with different gear, engines and sensor setups;
- separate the drivers of fuel use (weather, towing, speed, load) well enough to give advice, not just a forecast;
- cope with data gaps, manual logbook entries and sensor drift.

Today the prototype [predicts X on N trips with error Y, against a baseline of Z].

### Main stage

**Work packages (24 months).** Add each WP's share of cost once the budget is set.

| WP | Content | Months | Lead |
|---|---|---|---|
| WP0 | Project management, reporting, timesheets | 1–24 | Sigrún |
| WP1 | Data platform: ingest data from 3 → [N] vessels, quality checks, common schema | 1–9 | Tómas |
| WP2 | Fuel model: per-trip forecast plus the drivers of fuel use | 3–15 | [data scientist] |
| WP3 | Quality model: define quality measures, build ground truth from [landing or processing data], validate | 3–18 | [data scientist] + [quality expert] |
| WP4 | Pilots with current customers and [LOI company]: measure against baseline, convert to paid contracts | 6–24 | Sigrún |
| WP5 | Product: views for skipper and shore manager, onboarding for new vessels | 9–24 | Tómas |
| WP6 | Market infrastructure: pricing tests, Faroese market validation | 12–24 | Sigrún, **under 10% of total cost** |

**Quality expertise (WP3).** This is your biggest open question, so two options are worth a call besides a freelance marine biologist:
- **Matís** has worked with the seafood industry on fish quality, handling and shelf life for decades. It could supply measurement methods or quality data as a purchased service.
- **Reykjavík University**, where Tómas teaches, could join as a research co-applicant. The board takes research collaboration into account. A university co-applicant must cover at least 20% of its own cost, and Hafbók must keep at least 60% of the grant each year.

**Milestones**
- **M1 (month 3):** Data agreement signed with [LOI company]. Data flowing from [N] vessels.
- **M2 (month 6):** Fuel model v1 reaches [error ≤ X%] on held-out trips.
- **M3 (month 12):** Quality model v1 validated against [source] at [metric]. Pilots running on [N] vessels. *This is the year 1 decision point.*
- **M4 (month 18):** Pilots show [X% lower fuel per kg] or [quality outcome] against baseline. Product v1 released.
- **M5 (month 24):** [N] paying vessels in Iceland, and [a first Faroese pilot or customer].

**Budget, Year 1 and Year 2.** Build each salary line like this:

| Person | Role | Monthly cost incl. charges | % on project | Year 1 | Year 2 |
|---|---|---|---|---|---|
| Sigrún | CEO: WP0, WP4, WP6 | ~767,000 (check with payroll) | [%] | [ ] | [ ] |
| Tómas | CTO: WP1, WP5 | ~767,000 (check with payroll) | [%] | [ ] | [ ] |
| [Data scientist] | WP2, WP3 | [pay + charges, if on payroll] | 40% | [ ] | [ ] |
| [New hire, if any] | [role] | [ ] | [%], from month [ ] | [ ] | [ ] |

Then add:
- **Cloud:** [Year 1: 0.8M; Year 2: ?], e.g. "training compute and storage for [N] vessels".
- **Quality expertise:** [supplier, what you're buying, cost]. This is a purchased service.
- **Travel:** [domestic and foreign totals, purpose of each trip]. Pilot visits to the Faroes go here. Trade-show trips count as market infrastructure.
- **Overhead:** up to 25% of total cost excluding purchased services. You have none today.

You wrote that you only have the 12M total. Does that mean a Year 1 budget only, or 12M across both years? You're asking for 24M, so you need a Year 2 budget too.

**Team (15%)**
- **Sigrún, CEO:** [your role at Marel, how many years, and why it matters for selling to fishing companies].
- **Tómas, CTO:** [technical background, what he built in Hafbók]. He also teaches [subject] at Reykjavík University.
- **[Data scientist], 40%:** [background].
- **[Quality expert]:** [who, and what expertise].

Both founders have been on Hafbók's payroll since January 2026. That shows commitment, so say it.

**Funding strategy (5%)**
- **Revenue:** ISK 3.2 million in pilot fees in 2025, [2026 to date]. This covers [the part of the budget above the grant].
- **Grants so far:** Fræ (2024, ISK 2 million, completed 2025). The rules name Vöxtur as the expected step after Sproti, if the results justify it.
- **Equity:** [founders' own funds, angels, a planned round and when].
- **R&D tax deduction:** if you claim Iceland's R&D tax deduction, public grants reduce it. Check with your accountant before counting on both.

**Social impact (10%):** keep the draft from my last message as it is.

---

## What I need next

1. From Tómas: trips run, accuracy against a baseline, and where the quality numbers come from.
2. The LOI itself.
3. The invoices behind the 3.2M ISK: who paid, for which vessels, for how long, and what kind of fee.
4. Your price per vessel, even as a hypothesis.
5. Who the "2 devs" are, each person's % on the project, and what "12M total" covers.
6. How the data scientist is engaged: on payroll, or through their own company.

Once I have these, I'll fill the brackets and cut each answer to the form's length when the call opens. Ask Rannís three things (taeknithrounarsjodur@rannis.is, +354 515 5800, Mon–Thu 10–12):
- the February deadline and the main-stage due date;
- whether a prototype on three vessels with paid pilots fits Sproti's stage;
- how they treat a 40% contractor.

**Sources**
- [Rules and guidance H26: Sproti, Vöxtur, Markaður (PDF)](https://assets.ctfassets.net/8k0h54kbe6bj/5ve9pGv87bP55hYSDMsxow/f5863e2c972592719afb9e2263e50f4a/TS_Reglur_SVM-H26.pdf): two stages, maturity scale, cost rules, de minimis, reporting
- [Sproti grant page (island.is)](https://island.is/styrkjatorg/styrkur/1-46): no co-funding requirement, cost figures go into the second stage
- [Fræ grant page (island.is)](https://island.is/styrkjatorg/styrkur/1-42): Fræ falls under de minimis rules
- [Evaluation and allocation](https://island.is/v/taeknithrounarsjodur/mat-og-uthlutun-taeknithrounarsjods): first-stage result within three months
- [Guidance and rules page](https://island.is/v/taeknithrounarsjodur/leidbeiningar-vegna-umsokna)
- [Skatturinn: tryggingagjald 6.35% in 2026](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald/)
- [SA submission to Alþingi on the 11.5% employer pension share (PDF)](https://www.althingi.is/altext/erindi/151/151-2659.pdf)
- [Skatturinn: R&D tax deduction and public grants](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/styrkir-til-nyskopunarfyrirtaekja/)
- [EUR/ISK exchange rate](https://www.poundsterlinglive.com/data/currencies/eur-pairs/EURISK-exchange-rate)
- [Statistics Iceland: Icelandic fishing fleet in 2024](https://old.statice.is/publications/news-archive/fisheries/icelandic-fishing-fleet-in-2024/)
- [Matís: overview of fish quality research](https://matis.is/en/skyrsla/overview-on-fish-quality-research-impact-of-fish-handling-processing-storage-and-logistics-on-fish-quality-deterioration/)
