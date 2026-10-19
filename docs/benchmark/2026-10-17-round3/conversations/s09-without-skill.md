# s09 without-skill

## Founder, turn 1
Hi! We're a game studio in Helsinki, raised a €1.8M seed in April, 9 people. Building a co-op survival game where the NPCs run on fine-tuned LLMs, and our inference + training bill is getting scary. Looking for GPU/compute and cloud credits, and wondering if Business Finland has anything for game studios at our stage. Would love ~€500k non-dilutive on top of the round if that exists.

## Assistant, turn 1
Short answer: Business Finland has no €500k *grant* for a game studio right now. €500k of non-dilutive money is still realistic, but most of it would have to be a soft R&D loan. Compute is easier. You can get free GPU hours for training and cloud credits for inference. No public program pays for live player inference, though.

**Business Finland (as of mid-October 2026)**

The program that used to fit you was Young Innovative Company (NIY), which gave grants on the scale of €500k. It has been closed since October 2025, and Business Finland says it will most likely stay closed. Tempo is gone too. Here is what's left:

1. **R&D loan** ("Research, development and piloting"). Applications are taken all year round ([call page](https://www.businessfinland.fi/en/services/funding/calls/2026/research-development-and-piloting/)).
   - It covers 50% of project costs, or up to 70% if you can justify it.
   - Interest is 3 percentage points below the base rate, with a 1% minimum.
   - The term is 7–10 years, with 3–5 years before repayments start. It usually needs no collateral.
   - Up to 30% is paid as an advance. Part of the loan can be written off if the project fails.
   - For €500k you need a project of about €1M at 50%, or about €715k at 70%.
   - Grants (50%, or 60% for industrial research) only cover the parts that are genuinely research.
2. **Creative industries R&D call.** This pays a 35% *grant* instead of a loan. The budget is €9M a year and is now permanent. Game studios made the largest requests in the last round.
   - The 2026 round closed on 29 April. On 15 September Business Finland said the next call opens "later in 2026", but no date has been published yet. Ask luovat@businessfinland.fi.
   - The arithmetic: a €500k grant at 35% means a project of about €1.43M, with about €930k from your own money.
3. **Sprint.** This is a grant of €75–100k (75% of a €100–133k project), open all year since 1 September ([call page](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)).
   - If your company is under 5 years old, you only qualify with no earlier Business Finland R&D, Tempo or NIY funding.
   - It's small for you. Decide with Business Finland in the required advisor meeting whether to do it before the loan, or instead of it.
4. **Free LUMI compute inside a Business Finland project.** Business Finland has offered startups free LUMI supercomputer capacity worth about €20–80k as part of a funded R&D project. That information is from 2024, so ask your advisor whether it still applies.

Three things decide whether you get any of this:
- **Business Finland funds R&D, not game production.** Their own guidance for game studios calls normal game development "standard development". So pitch the NPC tech, not the game. Your inference bill is actually a good R&D project: make fine-tuned LLM NPCs cheap and reliable enough to ship. That covers distillation, memory, keeping characters consistent, and cost per player-hour.
- **Only costs after you apply count.** Nothing you've already spent is covered, so apply before you start the work you want funded.
- **Funding is paid after you report costs** (apart from the loan advance). Your seed round has to carry the cash flow.

The first step is to register in My Business Finland and book a talk with one of their game-industry advisors: https://www.businessfinland.fi/en/games

**Free GPU hours for training and fine-tuning**

The EU's EuroHPC AI Factories are free for AI startups and SMEs doing innovation work. They include the LUMI AI Factory in Kajaani. There are three ways in:
- **Playground:** small allocations, access in about 2 working days.
- **Fast Lane:** up to 50,000 GPU hours for 1–3 months on one system. Approval takes about 4 working days, and you write a short final report afterwards.
- **Large Scale:** more than 50,000 GPU hours for up to a year, with fixed cut-off dates.

Apply at https://access.eurohpc-ju.europa.eu. Some caveats:
- LUMI runs AMD GPUs, so check that your fine-tuning stack works on ROCm.
- Two of the large NVIDIA systems (MareNostrum5 ACC and JUPITER Booster) are currently unavailable for Fast Lane because of demand.
- This compute is for R&D, not for serving your live game.
- A studio training its own NPC models should count as an "AI SME", but confirm that with them.

**Cloud credits for inference**
- **AWS Activate Portfolio:** up to $200k, according to AWS's own page from June 2026. You need an Org ID from an Activate Provider, so ask your seed lead. AI startups can get more by talking to an account manager.
- **Google for Startups Cloud:** reportedly up to $350k for AI-first startups.
- **Microsoft for Startups:** reportedly up to $150k with an investor referral.
- **NVIDIA Inception** is free to join and unlocks partner offers. One example is Nebius AI Lift, reportedly up to $150k.

The Google, Microsoft and Nebius figures come from third-party sites, so check the official pages. Credits usually expire within 1–2 years and tie you to one cloud. Go deep on the cloud you'll actually serve players from rather than spreading out. Credits buy you time; lowering the cost per player is the real fix.

**EU money for games**

The Creative Europe MEDIA video game development call closes on 2 February 2027. Under the 2025 rules it pays up to €200k at 60%. Your studio needs a commercially released game since 2022, backed by a sales report; Early Access and work-for-hire don't count. The funded game must also be before its first prototype. That probably rules out your current game, but maybe not your next one.

**A realistic combination**
- A Business Finland R&D loan of €350–500k.
- A creative-industries grant on a separate part of the work, if that call opens in time.
- Free EuroHPC GPU hours.
- Roughly $200k in cloud credits.

Business Finland won't fund the same costs twice.

To narrow this down:
1. When was the company registered, and have you had any Business Finland funding before?
2. Roughly how does your bill split between training/fine-tuning and live inference? Is your stack NVIDIA/CUDA-only?
3. Which cloud are you on, and have you already used startup credits there?
4. What is technically new in your NPC stack compared with off-the-shelf LLM NPC tools?

## Founder, turn 2 (simulated)
1. Registered 19 August 2024, and no, we haven't had any Business Finland funding before. 2. Not sure on the split, and not sure if we're CUDA-only. 3. AWS. Not sure if we've used startup credits there. 4. Not sure, hard to say.

## Assistant, turn 2
That helps. The good news: you qualify for Sprint, and taking it doesn't block anything later.

**What your answers mean**
- **You qualify for Sprint.** You registered in August 2024 and have had no Business Finland funding. Sprint is a grant of €75–100k, covering 75% of a €100–133k project over 6–12 months ([call page](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)).
- **Sprint first, then the bigger loan.** Business Finland's own Q&A says Sprint does not block later funding. The reverse is not true: an R&D loan first would rule out Sprint while you're under 5 years old. So the natural order is Sprint now and the R&D loan as the bigger next step. Ask your advisor whether a loan for *different* work can run in parallel. That would get you to €500k faster.
- **You likely meet the other requirements.** You need €50k of equity on the balance sheet (your seed covers that) and enough cash to run the project. You also need at least one full-time person plus one more full-time equivalent in Finland. At least two thirds of the project must be R&D, with some preparation for commercial launch.
- **Timing of costs.** You can start at your own risk on the day you submit. Nothing you spend before that day counts.

**Question 4 is what makes or breaks this**

"Hard to say" is exactly what the Business Finland advisor will push on. They fund new technology, not normal game development. They will compare you with what already exists, such as Convai, NVIDIA ACE, or simply calling a big API model. Sit down with your tech lead for an hour and answer these three questions:
1. What breaks if you use an off-the-shelf NPC tool or a big API model? For example: cost per player-hour, response time with four co-op players, NPCs forgetting things or breaking character, or keeping their output safe.
2. What have you built yourselves to fix that? For example: your own fine-tuning data, small or distilled models, a memory system, or several NPCs coordinating.
3. What number would the project move? For example: "cut inference cost per player-hour from X to Y at the same quality", or "keep responses under Z ms with four players".

If you find a real answer, your inference bill becomes the project. If you don't, Business Finland will see it as standard game development.

**AWS: three things to do this week**
- **Check your existing credits.** In the AWS console, open Billing → Credits to see whether you've had any and what's left.
- **Ask your seed lead for an Activate Org ID.** They need to be an AWS Activate Provider. The Org ID unlocks Activate Portfolio, worth up to $200k. It requires that your latest round is within 12 months, so apply before April 2027. You also can't already have had credits of the same or greater value.
- **Split your bill.** In Cost Explorer, group last month's costs by instance type. Big GPU jobs that run for hours or days are training; always-on endpoints are inference. That split shows how much of the bill free EuroHPC compute could replace.

**The CUDA question: test it for free**

Ask whoever runs your fine-tuning whether your code depends on anything that only ships for NVIDIA. Typical examples are custom CUDA kernels or certain quantization or attention libraries. Then apply for EuroHPC Playground access on LUMI at https://access.eurohpc-ju.europa.eu (about 2 working days) and try one fine-tuning run.
- If it works on LUMI's AMD GPUs, apply for Fast Lane, which gives up to 50,000 GPU hours.
- If it doesn't, free NVIDIA capacity in the network is tighter right now.

**Order of play**
1. **This week:** register in [My Business Finland](https://www.businessfinland.fi/en/services/Advice-and-market-information/mybusiness-finland/), fill in the company profile and book the advisor call. Check your AWS credits and ask your seed lead for the Org ID.
2. **Before the advisor call:** write one page answering the three questions above, plus a rough Sprint budget of about €133k.
3. **In the call, ask:**
   - Should you do Sprint first, or go straight to a loan?
   - Can a loan project run in parallel with Sprint?
   - Is free LUMI capacity still offered inside funded projects?
   - When does the next creative-industries call open?
4. **Submit Sprint before you start the work you want covered.**

If you send me your answers to the three questions, I can help turn them into that one-page project draft.
