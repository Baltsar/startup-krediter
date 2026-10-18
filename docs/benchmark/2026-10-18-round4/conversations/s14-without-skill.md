# s14 without-skill

## Founder, turn 1
Hi! We're 3 people building an AI tool that separates stems (vocals/drums/bass) from live DJ sets in real time, so DJs can remix on the fly. We need roughly €40k worth of GPU compute over the next 6 months to train the model, plus ideally some grant money so we can work on it full time for 6 months instead of evenings. What programs should we be applying to?

## Assistant, turn 1
Thanks, this is a clear brief. You can probably get the GPU compute without paying for it. The grant money for salaries is national, so it depends on where your company is. I need a few facts from you before I can name the right grants. The questions are at the end.

**1. GPU compute: EuroHPC AI Factories**
The EU's AI Factories give AI startups and SMEs free supercomputer time "for innovation purposes". There are three ways in:
- **Playground:** a small allocation for first-time users, with access in about 2 working days. One EuroHPC page says it is temporarily closed and another says it is open, so check the portal.
- **Fast Lane:** up to 50,000 GPU hours for 1–3 months on one system. Approval takes about 4 working days, first come first served. It is meant for teams that already know how to run jobs on a supercomputer.
- **Large Scale:** more than 50,000 GPU hours for up to a year, with fixed application deadlines.

For 6 months of training, you could do two Fast Lane rounds back to back, or make one Large Scale application. Some practical points:
- These are supercomputers where you queue batch jobs, not cloud machines you log into.
- Some run AMD GPUs instead of NVIDIA (LUMI does), so pick one that suits your code.
- Before you plan around this, check the call's Terms of Reference. They say which countries qualify and whether you need a registered company.

**2. Cloud credits: useful, but they won't pay for training**
Google for Startups Cloud, AWS Activate and Microsoft for Startups each give a few thousand dollars if you apply on your own. Their six-figure tiers usually need a referral from a VC or an accelerator. Take the small ones anyway, for development and for running the model.

**3. Grants to pay your salaries**
These depend entirely on your country. A few things hold almost everywhere:
- **You need a registered company.** The grant pays the company's costs, and you pay yourselves salaries through it. It is not a personal stipend.
- **You pay part of it yourselves.** Most grants cover only part of the project cost, and the company funds the rest.
- **Decisions are slow.** Expect weeks to months. If you want to work full time within 6 months, apply soon.

**Three questions grant reviewers will ask**
- **What's new?** Serato, rekordbox, VirtualDJ and djay already split stems in real time. Does yours do something they can't, like working on the mixed output of a whole set, or on vinyl and CDJs? Innovation grants are decided largely on this answer.
- **Training data:** The two standard datasets don't allow commercial use. MUSDB18 is "academic purposes" only, and MoisesDB is CC BY-NC-SA 4.0. Training a product on them is a licensing risk. Get legal advice and budget for licensed multitrack recordings.
- **Who owns the code:** You're building this in your evenings. Check that your employment contracts don't give your employers a claim on it.

**To name the right grants, I need to know:**
1. Which country is the company in, or will it be in? Do all three of you live there?
2. Is the company registered yet? Do you have an investor or accelerator?
3. Can you put in some of your own money? Would all three of you quit your jobs if you got funding?

Sources:
- [EuroHPC AI Factories access calls](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en)
- [EuroHPC Fast Lane access](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en)
- [EuroHPC AI Factories access modes](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en)
- [LUMI: access calls for AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [Google for Startups, AI program](https://cloud.google.com/startup/ai)
- [AWS Activate application guide](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide)
- [MUSDB18 dataset terms (sigsep)](https://sigsep.github.io/datasets/musdb.html)
- [MoisesDB licence](https://github.com/moises-ai/moises-db)
- [Stem separation support in DJ software (DJ.Studio, a competitor)](https://dj.studio/blog/dj-software-stem-separation-compatibility)

## Founder, turn 2
1. Norway, we'll set up an AS in Oslo. And yes, all three of us live in Oslo.
2. Not registered yet. No investor or accelerator.
3. Own money, not sure. But yes, the plan is for all three of us to go full time on it for the 6 months if we get funding.

## Assistant, turn 2
Thanks, that answers my questions. The GPU compute looks very doable from Norway. Salaries are harder. I found no Norwegian grant that pays three people full time for 6 months unless you also put in your own or an investor's money. The biggest startup grant requires you to match it krone for krone.

This is the order I'd go in:

**1. Register the AS first**
You need NOK 30,000 in share capital, plus a registration fee of a few thousand kroner through Altinn. Every program below needs a registered AS, and EuroHPC almost certainly does too. After that, apply before you spend anything. Innovasjon Norge doesn't cover costs from before you applied.

**2. GPU compute: EuroHPC, with help from KI-fabrikken**
Norway is part of EuroHPC. Sigma2's KI-fabrikken is Norway's member of the LUMI AI Factory group. Ask them to help with a Playground or Fast Lane application. Fast Lane gives up to 50,000 GPU hours per round, for 1–3 months, so two rounds cover your 6 months. Ask which machines you can use: LUMI has AMD GPUs, while Norway's new Olivia has NVIDIA chips. Also check that you qualify, in the call's Terms of Reference.

**3. Innovasjon Norge, Oppstartstilskudd 1: start here**
- Up to NOK 150,000, covering up to 100% of invoices from outside suppliers.
- It does not pay your own salaries.
- It's for finding out whether customers will pay, for example testing the tool with DJs with outside help.
- You get up to half at the start. You cover the rest yourselves until the final report.
- They expect customer interviews and a test plan before you apply. Answers currently take 3–4 weeks.

This builds the proof of demand that the bigger grant asks for.

**4. Innovasjon Norge, Oppstartstilskudd 2: big enough for salaries, if it allows them**
- Up to NOK 1 million, covering at most 50% of the project's costs.
- You must put in at least as much as the grant, and it must be in the account before the first payment. Savings, money from private investors and subordinated loans all count.
- Its 2026 budget was cut by 60%, so expect more rejections. The 2027 budget proposal cuts business support further overall.
- The page doesn't say whether founders' salaries count. Ask Innovasjon Norge before you plan around this.

**5. SkatteFUNN: money back later, not money now**
- You get back 19% of your R&D project costs. If the company has no tax to deduct it from, it's paid out in cash with the tax settlement after the year ends.
- Only costs the company actually pays and logs on timesheets count. Free EuroHPC compute earns you nothing here.
- This year's guaranteed deadline (1 September) has passed. Plan a 2027 project and check the 2027 rules.
- If you want other support for the same project, apply for it before the SkatteFUNN project starts.

SkatteFUNN and Oppstartstilskudd 2 both need an auditor or authorised accountant to approve your costs, so budget for one.

**What this means for going full time**
The realistic route is a small round from angel or early-stage investors. That money counts as your share for Oppstartstilskudd 2. It also opens the large cloud-credit offers I mentioned earlier. Until then, keep working evenings and train on free EuroHPC compute. Use Oppstartstilskudd 1 to show that DJs will pay.

Two questions before the next step:
1. Have you talked to DJs yet? Has anyone said they would pay?
2. What does yours do that the stems in Serato, rekordbox or djay don't? Both the grants and investors will ask.

Sources:
- [Innovasjon Norge: Oppstartstilskudd 1](https://www.innovasjonnorge.no/tjeneste/oppstartstilskudd-1)
- [Innovasjon Norge: Oppstartstilskudd 2](https://www.innovasjonnorge.no/tjeneste/oppstartstilskudd-2)
- [Forskningsrådet: SkatteFUNN 2026 call](https://www.forskningsradet.no/utlysninger/2026/skattefunn-skattefradrag-for-forskning-og-utvikling-i-et-nyskapende-naringsliv/)
- [Sigma2: KI-fabrikken](https://www.sigma2.no/node/387)
- [Sigma2: Norway and EuroHPC](https://www.sigma2.no/eurohpc)
- [EuroHPC AI Factories access calls](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en)
- [Regjeringen: 2027 budget and business support](https://www.regjeringen.no/no/aktuelt/tydelegare-prioriteringar-innanfor-det-naringsretta-verkemiddelapparat/id3174956/)
- [HPE: Olivia supercomputer](https://www.hpe.com/us/en/newsroom/press-release/2025/11/hpe-delivers-olivia-norways-most-powerful-supercomputer-to-accelerate-national-research-and-ai-innovation.html)
