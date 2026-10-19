# r05 without-skill

## Founder, turn 1
Hi! we got a GO on our EIC short proposal last month (basically the old SME instrument phase 2) and now need to write the full application for the Nov 4 cutoff. can you help draft the impact + implementation parts? here's our stuff:

Fjordline Robotics - autonomous hull inspection drones for ships, replaces divers and drydock inspections
TRL 6, sea trials w a ferry operator + Port of Gothenburg
Ask: 2.4M EUR grant + 6M EUR equity
Budget 24 mo: personnel 1.9M, subcontracting (class society certification) 450k, equipment 380k, other 200k, total ~3.4M
Team: Elin (CEO, ex-defence industry), Marco (CTO, PhD robotics KTH), Jonas (COO), 11 employees in Gothenburg
Revenue 2025: ~0.8M EUR (inspection-as-a-service pilots)

we dont have market sizing or a risk table yet. deadline is tight so pls be quick

## Assistant, turn 1
Hi, and congrats on the GO.

Below you'll find five things to fix first, a draft of Impact, a draft of Implementation with a risk table, and a list of what I need from you. Everything in [brackets] is a number or fact only you have. I haven't made up any of your data, and the evaluators would catch it if I had.

One note on framing: this isn't quite SME Instrument phase 2 anymore. The grant is a 70% lump sum, it's blended with EIC Fund equity, and a technology expert, a panel and then a jury judge it. Write for investors as much as for evaluators.

---

## 1. Fix these before writing

**a) The budget doesn't add up, and the grant ask may be over the cap.**
Your lines add up to €2.93M, not €3.4M (1.9 + 0.45 + 0.38 + 0.2). The grant covers 70% of eligible costs, so:
- If eligible costs really are €3.4M, the maximum grant is €2.38M. Your €2.4M is about €20k too high.
- If the missing €0.47M is meant to be indirect costs: Horizon Europe normally adds 25% on direct costs except subcontracting. That's 0.25 × €2.48M = €0.62M, a total of €3.55M and a 70% cap of about €2.485M. In that case €2.4M fits, and you could ask for up to about €2.48M (the ceiling is €2.5M).

Check three things in the lump-sum budget template:
1. How indirect costs are calculated.
2. Whether the €380k of equipment counts at full cost or only as depreciation during the project. If it's depreciation only, that line could shrink a lot.
3. Whether the class-society fees count as "subcontracting" or "purchase of services". That decides whether the 25% applies to them.

Vinnova is the Swedish NCP for EIC, and a 30-minute call with them can sanity-check this. Also show where your 30% own share (about €1.0–1.1M) comes from: revenue, current investors or the equity round.

**b) 16 days left, and the pack is much more than two sections.**
The 4 Nov submission (17:00 Brussels time) needs all of this:
- the Part B questionnaire (max 20 pages)
- a pitch deck
- a video (max 3 minutes)
- the lump-sum budget table
- an implementation plan (max 10 pages)
- the "financial plan and equity needed" sheet
- freedom-to-operate results (or a note of up to 2 pages)
- letters of intent

About 3–4 weeks after the cut-off, a technology expert interviews you remotely, so roughly 25 Nov – 2 Dec. Marco should block that time now.

**c) Decide by about 26 Oct whether 4 Nov is realistic.**
The EIC FAQ says a GO under the 2025 or 2026 work programme lets you submit in 2026 or 2027. The 2027 dates aren't set yet, and the 2027 call is expected to open in November. A rejected full proposal counts toward the three unsuccessful applications you're allowed under Horizon Europe.

On 26 Oct, check whether you have:
- a budget that adds up
- at least two signed letters of intent
- pilot numbers for the market model
- a freedom-to-operate note

If any of these is missing, I'd target the first 2027 cut-off instead of rushing. Confirm the 2027 rule with EIC or Vinnova, because work programmes change.

**d) Don't overclaim "replaces drydock".**
Class still requires drydocking at the five-year renewal survey. An in-water survey can usually replace only the intermediate docking, and only for eligible ships (age, coating, class notation). The technology expert will test this. Write "replaces divers and, for eligible ships, the intermediate drydock bottom survey" unless your class society confirms more.

**e) Claim the defence angle only if you can prove it.**
The 2026 call accepts dual-use, but it gives no scoring advantage. It also needs a credible business case with evidence of defence demand, not just "navies could use it too". Sales to coast guard, police or civil protection don't count on their own. Evaluators may ask because of Elin's background. If you have real navy interest, declare it with evidence. Otherwise keep the proposal strictly civil. Don't include classified information.

---

## 2. Draft: Impact

I couldn't open the exact text of the 2026 Part B questions. Map these blocks onto the template's Impact questions (market, commercialisation, broader impact, scale-up), and keep the whole Part B within 20 pages.

### 2.1 Problem and value

> Every seagoing merchant ship must have its underwater hull, propeller, rudder and sea chests inspected regularly. Classification requires bottom surveys in every five-year class cycle. IMO's 2023 Biofouling Guidelines recommend in-water inspections at least every 12–18 months, and IMO has agreed to develop a binding framework. Inspections are also needed after groundings and contacts, and before charter or sale.
>
> Today this means either commercial divers or taking the ship out of service in drydock. Diver inspections depend on weather and visibility, put people into one of the most hazardous jobs in a port, and produce video that is hard to compare between inspections. A drydock inspection costs [€X] and [N] off-hire days for a vessel like [launch customer]'s [ferry type] [source: customer data].
>
> Not inspecting is becoming more expensive. Fouling raises fuel consumption: DNV reports up to 20% for light slime and up to 85% for heavy calcareous fouling. Since 2024, ships calling EU ports have paid for the extra CO2 under the EU ETS.
>
> Fjordline Robotics sells autonomous hull inspection as a service. [One operator] launches a drone from the quay or the ship. It maps the full underwater hull in [X hours] and produces a [geo-referenced, repeatable] report [accepted by / designed for acceptance by] the class surveyor. Compared with a diver inspection this cuts [time] by [X%] and [cost] by [Y%], with no diver in the water. For eligible ships it can replace the intermediate drydock bottom survey.

### 2.2 Market size, bottom-up (fill in)

Don't use a top-down "global underwater robotics market $Xbn" figure as your main number, because evaluators discount it. Build the number from inspections × price, and use one top-down figure only as a cross-check.

| Step | Calculation | Source | Value |
|---|---|---|---|
| A. Fleet | World merchant fleet, about 112,500 ships (1 Jan 2025) | UNCTAD Review of Maritime Transport 2025 | 112,500 |
| B. Inspections per ship per year | Biofouling (every 12–18 months ≈ 0.7–1.0/yr) + class in-water bottom survey (≈ 1 per 5-year cycle for eligible ships ≈ 0.2/yr) + damage, charter and insurance surveys [your pilot data] | IMO guidelines, class rules, your pilots | [x] |
| C. Price per inspection | Your average pilot price (2025 revenue ÷ number of inspections) | Your invoices | [€] |
| **TAM** | A × B × C | | [€] |
| **SAM** | Ships you can serve 2027–2031: [segments, e.g. ferries, ro-pax and short-sea ships calling Nordic and North European ports] × B × C | [fleet database, Port of Gothenburg port-call data] | [€] |
| **SOM (year 5)** | Drones in service × inspections per drone per year × price; then check it as a % of SAM | Your operations plan | [€] |

Add one line on value per inspection for the customer (avoided off-hire days and diver costs, earlier cleaning). It shows how much room you have on price.

### 2.3 Traction and business model

> Our inspection-as-a-service pilots generated about €0.8M in revenue in 2025 from [N] customers and [N] inspections. Sea trials with [ferry operator] and the Port of Gothenburg validated the system in real operations (TRL 6): [hull coverage %, defects found compared with a diver, hours saved]. [Ferry operator] has signed a letter of intent to [use the service on N vessels from 2027 / spend €X per year]. The Port of Gothenburg intends to [offer the service in the port / host a service hub].
>
> We charge per inspection (€[X]) or by annual subscription per vessel (€[Y] per vessel per year for [n] inspections plus fouling trend reports). Our beachhead is Nordic ferry and ro-pax operators: fixed routes, frequent port calls and a very high cost per day off hire. Next come short-sea and [tanker/cruise] fleets calling North European ports, served from hubs in [ports]. Our channels are service-supplier approval with the class societies, port authorities, and [partnerships with hull-cleaning and coatings companies that need inspection data before and after cleaning].

### 2.4 Competition (fill in)

Name 3–5 real alternatives and say why you win against each:
- diving contractors (the incumbents)
- ROV makers and operators (a tool, not a service)
- hull-cleaning robots (an adjacent market, maybe partners)
- other autonomous inspection startups

Base the comparison on time per inspection, cost, class acceptance and the data you deliver. An honest comparison scores better than "no direct competitors".

### 2.5 Scale-up and ambition

> The EIC grant takes us to TRL 8 and class approval by [M24]. The EIC investment, together with [co-investors], funds [N] service hubs, a fleet of [N] drones and a sales team. Revenue grows from €0.8M (2025) to €[X]M (2028) and €[Y]M (2031), and the team from 11 to [N] people. Our long-term goal is to become the standard for in-water inspection of [the EU-calling fleet]. A second business line is condition history for every hull, which owners, insurers and cleaning companies pay for.

### 2.6 Broader impact

> - **Climate:** earlier fouling detection leads to earlier cleaning and lower fuel use. [Ferry operator data: X% fuel / Y t CO2 per vessel per year]
> - **Biodiversity:** inspection supports biofouling management, which IMO ties to the spread of invasive species.
> - **Safety:** fewer diver hours in port waters, around propellers and in poor visibility.
> - **Economy:** fewer unnecessary drydock visits and less off-hire; [N] skilled jobs in Gothenburg by 2031; a European supplier in maritime robotics.

---

## 3. Draft: Implementation, risk and need for EU support

The work packages belong in the implementation plan (max 10 pages). Part B covers the team, risks and need for EU support.

### 3.1 Team

> **Elin [surname], CEO:** [N] years in the defence industry delivering [complex hardware programmes] to demanding, regulated customers. Leads sales, investors and partnerships.
> **Marco [surname], CTO:** PhD in robotics from KTH ([thesis topic]). Architect of our autonomy and navigation.
> **Jonas [surname], COO:** [background]. Runs field operations, certification and the service organisation.
> 11 employees in Gothenburg working on [hardware / software / field operations].
> **Gaps we fill with this funding:** [Head of Sales with a shipowner network], [quality and certification manager, ideally an ex-class surveyor], [field operations lead]. Advisory board: [name, ex-class society / ferry industry].

Evaluators look for gaps. Name them yourselves and say how you fill them.

### 3.2 Work plan (grant-funded, TRL 6 → 8, 24 months)

The cost split is my suggestion, and it adds up to your lines. Adjust it to how your team actually works.

| WP | Title | Lead | Months | Key deliverables | Indicative cost |
|---|---|---|---|---|---|
| WP1 | Production-grade drone and reliability | Marco | M1–M15 | D1.1 Design freeze (M6); D1.2 [n] production units qualified (M15) | Personnel €0.60M, equipment €0.28M |
| WP2 | Autonomy, hull mapping and class-compliant reporting | Marco | M1–M20 | D2.1 Automated hull-coverage and defect/fouling report validated against diver/drydock findings on [n] vessels | Personnel €0.55M |
| WP3 | Class approval and certification | Jonas | M3–M22 | D3.1 Test programme approved by [class society] (M9); D3.2 Witnessed in-water surveys; D3.3 Approval as service supplier [and/or type approval] (M20) | Subcontracting €0.45M, personnel €0.20M |
| WP4 | Operational demonstration with launch customers (TRL 8) | Jonas/Elin | M6–M24 | D4.1 [n] surveys accepted by an attending class surveyor; D4.2 Demonstration report with customer savings data | Personnel €0.45M, equipment €0.10M, other €0.20M |
| WP5 | Coordination, IP, quality and safety | Elin | M1–M24 | D5.1 Operations and safety manual; D5.2 Updated IP and FTO | Personnel €0.10M |

**Equity-funded, outside the grant:** WP6 commercial scale-up (sales team, hubs in [ports], drone fleet) and [WP7 manufacturing / next generation]. The EIC wants the grant to cover TRL 6–8 work and the equity to cover scale-up, so keep them separate.

Each work package needs at least one deliverable, and each task at most one.

**Milestones:**
- M6: design freeze
- M9: test programme approved by the class society
- M15: first drone survey witnessed and accepted by class
- M20: approval obtained
- M24: TRL 8, with [n] paying customers in [n] ports

In WP3, say exactly what the €450k buys: service-supplier approval for Fjordline (IACS UR Z17), type approval of the drone, or both.

### 3.3 Risk table

Likelihood and impact (L/I: L = low, M = medium, H = high) are my starting point; adjust them. Evaluators want commercial and financial risks too, not just technical ones, each with an owner and a link to a work package.

| # | Risk | Type | L | I | Mitigation | Owner/WP |
|---|---|---|---|---|---|---|
| 1 | Class approval takes longer or requires design changes | Regulatory | M | H | Involve [class society] from M1; test programme approved by M9; certification budget ring-fenced; sell biofouling and damage inspections (no class approval needed) in the meantime | Jonas / WP3 |
| 2 | Inspection quality doesn't match diver/drydock in poor visibility, currents or complex stern areas | Technical | M | H | Validation against diver/drydock findings on [n] vessels (D2.1); [your sensor approach]; defined operating limits, with a diver as fallback outside them | Marco / WP2 |
| 3 | Shipowners are slow to switch from divers | Commercial | M | H | Reference customers ([ferry operator], Port of Gothenburg); price at or below diver cost; return-on-investment data from WP4; class acceptance removes the main objection | Elin / WP4 |
| 4 | Rules for underwater drone operations differ by port | Regulatory/operational | M | M | Permit checklist per port; start in ports where we have partners; Port of Gothenburg as reference | Jonas / WP4 |
| 5 | Safety incident near propellers or thrusters | Operational | L | H | Lockout procedure with the crew; operations manual (D5.1); insurance | Jonas / WP5 |
| 6 | Long lead times for components of production units | Supply chain | M | M | Two suppliers for critical parts; long-lead items ordered in M1–M3 | Marco / WP1 |
| 7 | Key hires in Gothenburg take longer than planned | Organisational | M | M | Recruit from M1; KTH and Chalmers networks; employee stock options | Elin / WP5 |
| 8 | Equity round or the 30% own share doesn't close in time | Financial | M | H | Start talking to co-investors now; revenue covers part of the 30%; WP4 can be phased | Elin |
| 9 | A competitor gets class approval first | Market | M | M | Class approval is the critical path in the plan; patents/FTO on [what]; data advantage from inspection history | Elin / WP5 |

### 3.4 Need for EU support

> The next step combines three things that private investors in Europe rarely fund together before revenue scales: hardware industrialisation, a 12–24-month class certification with an uncertain outcome, and long sales cycles with conservative shipowners. [Current investors / named VCs] have said they will invest once class approval is in place [letters or meeting notes].
>
> The EIC grant (€[2.4]M) de-risks certification and the TRL 8 demonstration. The EIC investment (€6M), together with [co-investors, €X], funds commercial scale-up: [n] hubs, [n] drones and a sales team. Without EIC support, [certification is delayed by about two years / we remain a Nordic pilot business / the technology gets licensed to a player outside the EU].

Only claim what you can back with a letter or a named conversation.

---

## 4. What I need from you (by Wednesday if you're aiming for 4 Nov)

1. What the €3.4M is made of, so the gap against the €2.93M of lines can be explained.
2. Pilot data: number of inspections in 2025, average price, time per inspection compared with a diver, and the ferry operator's estimate of what they save.
3. Which class society you're working with, what the €450k covers and how far approval has come.
4. Letters of intent: who has signed, and who can sign within a week.
5. Investors: who you've talked to about co-investing, and what the €6M will fund.
6. Whether there is real interest from any navy (yes/no, with evidence).
7. IP status and whether you have an FTO analysis.
8. The surnames and a few lines of background for Elin, Marco and Jonas.

Send what you have, and I'll fill in the numbers and cut everything to fit the page limits.

---

**Sources**
- [EIC Accelerator, official page (cut-offs, contents of the full proposal, the technology expert's interview, grant and investment amounts)](https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en)
- [EIC FAQ, Accelerator (20 pages, annexes, GO validity, three unsuccessful applications, dual-use, work packages)](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-eic-accelerator_en)
- [EIC FAQ, lump-sum budget and financial annexes](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-lump-sum-budgets-and-financial-annexes_en)
- [EIC Accelerator 2026, 70% funding rate and €1–10M investment (Cyprus funding portal)](https://www.fundingprogrammesportal.gov.cy/en/call/eic-accelerator-2026-short-application-en-2025/)
- [Access2EIC, annotated template for the 2026 full proposal](https://access2eic.eu/the-new-2026-annotated-template-for-the-eic-accelerator-full-proposal/)
- [EIC Accelerator call page with the note about the 2027 call (third-party site)](https://www.euacc.ai/calls/HORIZON-EIC-2026-ACCELERATOR-01)
- [IMO, biofouling](https://www.imo.org/en/OurWork/Environment/Pages/Biofouling.aspx)
- [IIMS, recommendations in the IMO biofouling guidelines (inspections every 12–18 months)](https://www.iims.org.uk/imo-biofouling-guidelines-key-recommendations/)
- [DNV, biofouling management plan (fuel figures, binding framework no earlier than 2029)](https://www.dnv.com/news/improve-environmental-performance-with-a-ship-specific-biofouling-management-plan/)
- [DNV, remote inspection techniques require an approved service supplier](https://www.dnv.com/news/2019/survey-by-remote-inspection-techniques-use-of-approved-service-suppliers-144572/)
- [Lloyd's Register, RIT service suppliers from 2019](https://www.lr.org/en/knowledge/class-news/26-18/)
- [UK MCA, MGN 546 in-water surveys](https://www.gov.uk/government/publications/mgn-546-m-amendment-1-in-water-surveys/mgn-546-m-amendment-1-in-water-surveys)
- [IIMS, UNCTAD Review of Maritime Transport 2025 (fleet of 112,500 ships)](https://www.iims.org.uk/unctad-review-of-maritime-transport-2025-report/)

## Founder, turn 2
thanks, super helpful. answers to your list:

1. what the 3.4M is made of - honestly dont know, the lines are what i have. also dont know yet where the 30% own share comes from
2. pilot data (no of inspections 2025, avg price, time vs diver, ferry operator savings) - dont know, dont have those numbers
3. class society - we havent ordered the class certification yet, so no approval progress. dont know which society or exactly what the 450k covers
4. LOIs - dont know
5. investors - dont know who's talked co-investing. the 6M equity (with the grant) is to fund certification and scale-up
6. navy interest - dont know
7. IP - all IP was assigned from our swedish AB to the Delaware Inc. in the 2025 flip. FTO - dont know
8. surnames - dont know. background: Elin ex-defence industry, Marco PhD robotics KTH and still an unpaid affiliated researcher at KTH, Jonas - dont know beyond COO

yes pls fill in the numbers, here's what else we have:

Market: about 60k merchant ships over 5,000 GT need hull inspections roughly every 2.5 years; we guess a 1.2B EUR/yr inspection market. Pilot customers: 2 ferry operators, 1 tanker company. Cap table: founders 64%, Y Combinator 7%, Nordic seed fund 18%, angels 6%, ESOP 5%. Seed round 3.5M USD in 2025. Hiring plan: +12 FTE over 24 months (robotics, ML, certification).

## Assistant, turn 2
Thanks, that's clear. Short version: **don't submit on 4 Nov. Aim for 3 Feb 2027.** Below: why, a new problem with your Delaware structure, the numbers I could fill in, and who has to answer what this week.

---

## 1. The decision: 4 Nov isn't realistic

In my last reply I set four checks for 26 Oct. As of today none of them is met:
- the budget doesn't add up, and nobody knows what the €3.4M is made of
- no known signed letters of intent
- no pilot numbers
- no freedom-to-operate note

Your answers also raised a new problem: the IP sits in the Delaware company (section 2). A rejected full proposal uses one of your three allowed unsuccessful attempts, so a rushed submission is expensive.

Your GO lets you submit at any time in 2026 or in 2027 (EIC FAQ). The draft 2027 work programme has four full-proposal cut-offs: **3 Feb, 1 Apr, 1 Sep and 3 Nov 2027**. It isn't adopted yet, so confirm the dates with Vinnova. Aim for 3 Feb and keep 1 Apr as the fallback. After April the next cut-off is September.

It's Elin's call. If she still wants 4 Nov, then by 26 Oct you need all four checks plus a lawyer's written plan for the IP. I don't think that can be done.

One more reason the team has to own this: at the jury interview (45 minutes: a 10-minute pitch, then 35 minutes of questions), only staff, board members and investors may attend. Consultants can't. Elin, Marco and Jonas must know every number in the proposal, so most of the open questions below go straight to them.

---

## 2. New blocker: the IP belongs to the Delaware Inc.

This mainly hits the €6M equity, not the grant.

**Equity.** The EIC Fund's 2026 investment guidelines say:
- Companies must be established and operating in the EU or an associated country (§1.7).
- The Fund can invest in a parent instead of the applicant only if that parent is itself in an eligible country (§1.8). A Delaware Inc. isn't.
- The Fund must make sure supported companies keep most of their value, including IP, in the EU or associated countries (§1.9).

Today the Swedish AB would apply, its US parent owns the IP, and your investors hold shares in the parent. Until that changes, the €6M is at risk.

**Grant.** The Swedish AB can still apply: the FAQ says a company in an EU member state is eligible on its own. But the AB must have the right to use and develop the technology. At a minimum it needs a written licence from the Inc. Also check which legal entity submitted the short proposal. If it was the Inc., call Vinnova or the EIC helpdesk now.

**Options for Elin, a lawyer and your board (the seed fund, YC):**
1. **Assign the IP back to the AB.** This fixes the grant side and goes a long way on §1.9. The Fund would still be investing in a subsidiary of a US company, so agree the structure with them early.
2. **Put an EU holding company on top (a reverse flip).** This is the cleanest route for the equity, but it's the most work and needs tax advice.
3. **Keep the structure, license the IP to the AB and apply for the grant only.** Check with Vinnova or the EIC whether you can change the funding type from your short proposal, because the jury can't change it later. Grant-only applicants must also show how they'll fund scale-up.

This week: book a lawyer who has done both flips and EIC deals, and a call with Vinnova.

---

## 3. Correction to my last reply: ferries don't skip drydocks

In section 2.1 I wrote that the drone can replace the intermediate drydock bottom survey for eligible ships. That's true for many cargo ships, but not for your beachhead:
- Passenger ships need a bottom inspection **every year** (SOLAS I/7), and at least two of them in each five-year period must be in drydock.
- The option to cut that to one drydock (MSC.1/Circ.1348) excludes ro-ro passenger ships.

So for ferries and ro-pax your value is replacing the diver on about three of the five mandatory annual bottom inspections in each five-year period, the ones that can be done in the water. You don't avoid any drydocks. That's still a strong case, because the inspection is required and it recurs. Change the last sentence of 2.1 to:

> For passenger ships, which need a bottom inspection every year, it replaces the diver on the in-water inspections between drydockings. For eligible cargo ships it can also replace the intermediate drydock bottom survey.

Check the details with your ferry customers' flag state and class society.

---

## 4. Market: the €1.2B doesn't hold up

Do the division on your own numbers: 60,000 ships ÷ 2.5 years = 24,000 inspections a year, and €1.2B ÷ 24,000 = **€50,000 per inspection**. A diving contractor in West Africa quotes about USD 7,000–20,000 for an in-water survey, plus the surveyor's fee. Prices in Nordic and North European ports are probably higher, but even double that is far below €50,000. Evaluators will do the same sum.

Two more problems:
- UNCTAD counts about **62,000 ships over 1,000 GT** (start of 2026). The number over 5,000 GT must be lower. Either cite a source for "60,000 over 5,000 GT", or use UNCTAD's figure and label the threshold correctly.
- "Every 2.5 years" is the two class bottom surveys in each five-year cycle. For cargo ships the one at the renewal survey has to be in drydock, so only about one per five years can be done in the water.

Replace the table in 2.2 with this one. The rows overlap a little, so read it as a ceiling.

| Segment | Inspections per year | Price | Market per year |
|---|---|---|---|
| Class in-water surveys (intermediate, eligible ships only) | ≤ 62,000 × 0.2 = ≤ 12,400 | USD 7–20k (diver benchmark) | ≤ USD 90–250M |
| Annual bottom inspections of passenger ships between drydockings | [passenger ships in target fleet] × 0.6 | €[your price] | [ ] |
| Biofouling inspections (IMO: every 12–18 months; voluntary today) | 62,000 × 0.67–1.0 = 41,500–62,000 | €[your price] | €41–62M for every €1,000 of price |
| Damage, charter and insurance surveys | [from your pilots] | €[ ] | [ ] |

In the text, call it "roughly USD 0.1–0.25B a year in class-driven in-water surveys today, plus biofouling inspections as the growth driver". DNV doesn't expect a binding IMO biofouling framework before 2029. If you want to keep a big number, present it as the value to shipowners (avoided off-hire, diver costs and fuel), not as the market.

Your pilot data is already in your 2025 invoices and field logs: the number of inspections, the average price and the hours per inspection. Pull those numbers this week, because the price column depends on them.

---

## 5. Budget: my proposal

Your lines add up to €2.93M. My guess is that the €3.4M is the lines plus 25% overhead on personnel only (2.93 + 0.475 = 3.405). Horizon Europe's 25% flat rate applies to all direct costs except subcontracting, so I propose:

| Line | € |
|---|---|
| Personnel | 1,900,000 |
| Equipment | 380,000 |
| Other | 200,000 |
| Subcontracting (class certification) | 450,000 |
| **Direct costs** | **2,930,000** |
| Indirect costs: 25% × 2,480,000 (excl. subcontracting) | 620,000 |
| **Total eligible costs** | **3,550,000** |
| Grant cap at 70% | 2,485,000 |
| Grant ask | 2,400,000 (up to 2,485,000) |
| Own share | 1,150,000 (1,065,000 at the maximum ask) |

**Lump sum per work package**, using my split from last time: WP1 €1,100,000 · WP2 €687,500 · WP3 €700,000 · WP4 €937,500 · WP5 €125,000 = €3,550,000.

Four things can change this:
- **Equipment.** If equipment counts only as depreciation (the Horizon Europe default unless the call says otherwise), it could be, for example, €152k (24 months of a 5-year life). Total costs then fall to about €3.27M and the cap to about €2.29M, so €2.4M would be too high. Check this in the budget template.
- **The €450k has no quote behind it.** The technology expert will ask about it first. Ask your two ferry operators which class society classes their ships, and get a quote from that society plus one more. The quote should say what you get: service-supplier approval, type approval, or both.
- **Class fees.** If they count as purchase of services rather than subcontracting, the 25% applies to them too. Total costs then rise to about €3.66M and the grant cap to the €2.5M ceiling.
- **Personnel.** €1.9M over 24 months is about €79k a month. Divide that by your average monthly cost per person from payroll (salary, employer contributions, pension). At €7k per person, for example, it's about 11 FTE on average. Check that this fits 11 staff today plus 12 hires spread over two years.

**Own share (€1.07–1.15M over 24 months).** The EIC FAQ says the investment component has no restrictions on use, so equity can in principle co-finance the project. But the EIC Fund only pays out after its own due diligence, so you need bridge cash. Show what's left of the USD 3.5M seed, your revenue for 2026–27 and any commitment from your current investors.

---

## 6. Equity: check the size

- The EIC Fund seeks at least €1 from other investors for every €1 it puts in (§1.25). €6M from the EIC means a round of about **€12M or more**.
- The Fund usually aims for a 10–20% stake (§1.16). €6M at that stake implies a post-money valuation of about **€30–60M**.

After a USD 3.5M seed in 2025 and €0.8M revenue, decide whether that's realistic. If it isn't, ask for less equity. Start with your existing investors, the Nordic seed fund (18%) and YC (7%), and ask whether they would join the round.

---

## 7. What I filled into the drafts

**2.3 Traction:**
> In 2025 our inspection-as-a-service pilots with two ferry operators and one tanker company generated about €0.8M in revenue, from [N] inspections at an average of €[X]. Sea trials with [ferry operator] and the Port of Gothenburg validated the system in real operations (TRL 6).

**3.4 Need for EU support / financial plan:**
> Fjordline raised a USD 3.5M seed round in 2025. Shareholders: founders 64%, [Nordic seed fund] 18%, Y Combinator 7%, angels 6%, employee option pool 5%. [Group structure: [legal name] AB, the applicant, wholly owned by [legal name] Inc., Delaware. Describe it once you've settled section 2.] The EIC grant (€[2.4]M) funds certification and the TRL 8 demonstration. The EIC investment (€[6]M), together with [co-investors, €X], funds commercial scale-up.

**3.1 Team:**
> 11 employees in Gothenburg today, growing to 23 by M24: [n] in robotics, [n] in machine learning and [n] in certification.
> Marco [surname], CTO: PhD in robotics from KTH and still an affiliated researcher at KTH, which keeps us close to [research group].

Two flags on the team:
- **Your hiring plan has no sales or field-operations roles.** Evaluators will ask who sells to shipowners and who runs inspections in new ports. Add those roles, funded by the equity if needed.
- **Marco's KTH affiliation.** Check his affiliation agreement and any KTH project agreements for IP clauses. Also confirm that what he has built for Fjordline belongs to the company. Put the result in the FTO note.

**Risk table:**
- Risk 1 (class approval): likelihood **H**, not M, until you've chosen a class society and have a quote. With both in place before submission, it can go back to M.
- Risk 8 (equity and own share): likelihood **H** until co-investors are named.
- **New risk 10:** group structure and IP ownership (legal; L = H, I = H until fixed; owner Elin). Write the mitigation once you've picked an option from section 2.

**Defence:** since nobody knows of any navy interest, keep the proposal strictly civil and leave defence out.

**FTO:** if there is no analysis, upload a note of at most 2 pages (EIC FAQ). It should cover:
- what IP you have and which company owns it
- the licence to the AB
- Marco and KTH
- a quick search for competing patents in hull inspection drones
- when a full FTO will be done (WP5)

---

## 8. Who answers what, this week

- **Elin:** structure and funding type (with the lawyer and Vinnova), which entity submitted the short proposal, co-investors, where the own share comes from, surnames and bios for all three, and navy yes/no.
- **Jonas:** 2025 pilot numbers from invoices and logs, class-society quotes, and letters of intent from the two ferry operators, the tanker company and the Port of Gothenburg.
- **Marco:** list of IP and patents, the KTH agreement, a draft FTO note, and time and cost per inspection compared with a diver.

**Plan for 3 Feb:**
- **By 31 Oct:** target date agreed, Vinnova call done, lawyer engaged.
- **By 30 Nov:** class-society quotes in, pilot data pulled, letters of intent signed, budget final.
- **By 20 Dec:** at least a signed licence from the Inc. to the AB, plus the FTO note and a full Part B draft.
- **January:** pitch deck, video, implementation plan and financial plan. Submit a week before 3 Feb.

Send me the pilot numbers and the class quote as soon as you have them. I'll then finish 2.2, 2.3 and the budget.

---

**Sources**
- [EIC FAQ, Accelerator (GO valid 2026 or 2027, three unsuccessful applications, parent/sister companies, investment can co-finance innovation work, interview format, the jury can't change the funding type, grant-only conditions, FTO note)](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-eic-accelerator_en)
- [EIC Fund Investment Guidelines 2026, official PDF](https://eic.ec.europa.eu/document/download/6df458e7-fa47-4ace-93fa-86099606bdb0_en?filename=EIC_Fund_Investment_2026_guidelines_f.pdf). I read §1.7–1.9, §1.16 and §1.25 in a [third-party text version (ChatEIC)](https://www.chateic.com/library/eic-fund-investment-guidelines-2026), so check the wording against the PDF.
- [EIC Work Programme 2027 draft: cut-offs 3 Feb, 1 Apr, 1 Sep, 3 Nov 2027 (evolution-europe, third-party, draft not adopted)](https://evolutioneurope.eu/blog/eic-work-programme-2027-draft/)
- [UNCTADstat, world fleet at the start of 2026 (about 116,000 ships ≥100 GT, about 62,000 over 1,000 GT)](https://unctadstat.unctad.org/insights/theme/25)
- [IIMS on Marshall Islands registry rules: annual bottom inspection of passenger ships, two drydockings in five years, ro-ro passenger ships excluded from MSC.1/Circ.1348](https://www.iims.org.uk/?p=30775)
- [Cameroon Diving Services, UWILD costs USD 7,000–20,000 in West African ports (vendor)](https://cameroondivingservices.com/blog/uwild-surveys-explained/)
- [DNV, biofouling management plan (binding framework no earlier than 2029)](https://www.dnv.com/news/improve-environmental-performance-with-a-ship-specific-biofouling-management-plan/)
- [IIMS, IMO biofouling guidelines (inspections every 12–18 months)](https://www.iims.org.uk/imo-biofouling-guidelines-key-recommendations/)
