# s02 without-skill

## Founder, turn 1
hey any free gpus for startups?? we need a LOT for training lol

## Assistant, turn 1
Short answer: yes, but where your company is registered changes the answer a lot. Free GPU compute at "a LOT" scale mostly exists in Europe. Elsewhere, you'll mostly be looking at cloud credits.

Three quick questions so I can narrow it down:
1. Which country is the company registered in?
2. Roughly how much compute do you need? GPU-hours is ideal, or just model size plus training tokens.
3. Have you raised from VCs or joined an accelerator, or are you bootstrapped?

Here's the rough picture in the meantime.

**If you're in the EU (or an associated country): EuroHPC AI Factories**
This is the big one. Industrial Innovation access is free for AI SMEs and startups when it's for innovation. There are three levels:
- **Playground:** limited resources, meant for getting started.
- **Fast Lane:** up to 50,000 GPU-hours, for teams already familiar with HPC. These are supercomputers that use Slurm, not a cloud console.
- **Large Scale:** more than 50,000 GPU-hours, with peer review.

A good order is to start in Playground or Fast Lane, show your training actually scales on their cluster, and then apply for Large Scale. The conditions I've confirmed: civilian use, AI Act compliance, the proposal in English, and a report afterwards. I haven't checked what they say about IP or publishing results. Read the Terms of Reference on that before you put proprietary training there.

**Cloud credits (available more broadly)**
- **Google for Startups Cloud, AI tier:** up to $350k over 2 years. You need to be AI-first with Gemini or Vertex at the core, and funded from seed to Series A.
- **AWS Activate:** up to $100k, but the top amount usually comes through an accelerator or VC partner. Bootstrapped teams usually get much less. I couldn't confirm the exact tiers on AWS's own site.
- **Microsoft for Startups:** up to $150k. The top tier usually needs an investor referral. That figure comes from third-party sources, so check Microsoft's current page.

Credits run out fast on H100-class instances. If you really need a lot, the free European compute is the place to start, and credits can cover inference and experiments.

Tell me the country and rough size and I'll tell you exactly where to start.

Sources:
- [EuroHPC AI Factories access modes](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en)
- [EuroHPC Fast Lane](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en)
- [EuroHPC Large Scale](https://www.eurohpc-ju.europa.eu/large-scale-access-ai-factories_en)
- [Terms of Reference, AI Factories Industrial Innovation](https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms+of+Reference+-+AIF+Access+Calls.pdf)
- [Google Cloud AI startup program](https://cloud.google.com/startup/ai)
- [AWS Activate credits](https://aws.amazon.com/aws-startups/learn/everything-you-need-to-know-about-aws-activate-credits/)
- [Microsoft for Startups blog](https://startups.microsoft.com/blog/?p=250)
- [SpendBase: Azure credit tiers](https://spendbase.co/blog/saas-management/azure-credits-for-startups/) (third-party)

## Founder, turn 2
no company registered yet, we're in denmark. compute wise roughly 20k H100 hours over the next 4 months. and no funding at all, no VCs, no accelerator, just us lol

## Assistant, turn 2
OK, that changes things. The free EU compute is a good fit for your size, but you can't apply until you have a registered company. So start the company setup now.

**Why you need the company first**
The rules for EuroHPC AI Factories industrial access say:
- The company must be established in the EU. Denmark is fine.
- You prove that with a valid VAT number, plus an EU PIC number if you don't have one yet. You can register the PIC for free on the EU Funding & Tenders Portal.
- The person who applies (the "PI") must be employed by the company when you apply. The contract must also last at least 3 months past the end of the allocation.

**Setup checklist**
1. Register an ApS. The minimum share capital has been DKK 20,000 since 2025. A sole proprietorship is cheaper, but you can't be employed by your own sole proprietorship, so an ApS is the safer choice.
2. Register the ApS for VAT (moms), not just for a CVR number. Alternatively, ask EuroHPC whether a CVR number is enough.
3. Register the PIC on the EU Funding & Tenders Portal.
4. Put one of you on an employment contract with the ApS. Being employed by your own company can bring payroll and admin obligations, so check with an accountant.
5. Set up a company-domain email address, since they require a professional one.
6. Email aif.access@eurohpc-ju.europa.eu and ask whether a founder employed by their own new ApS meets the employment rule. I'd confirm this before relying on it.

**20k H100 hours fits Fast Lane, but it's tight on time**
- Fast Lane covers up to 50,000 GPU hours, so you don't need Large Scale (that's for more than 50k).
- Fast Lane allocations last at most 3 months, with no extensions and no extra hours. Your 20k hours therefore need to fit into 3 months or less. That's about 9–10 GPUs running nonstop.
- If your code already runs on a Slurm cluster across several nodes, apply straight to Fast Lane. You must include technical feasibility data when you submit, and your own test runs can provide it.
- Use Playground only if you need to learn the cluster first, and ask for the shortest allocation. Two awards can't run at the same time, and with company setup a Playground month won't fit in your 4 months.
- Fast Lane approval should take about 4 working days. Capacity goes first come, first served, so keep a backup plan.
- Hours are counted per system, and not every system has H100-class GPUs. Denmark is part of the LUMI AI Factory, but LUMI's current GPUs are AMD. If you end up on a system that isn't NVIDIA Hopper, recalculate your hours and check that your stack runs there. The access portal shows which systems you can request.

**The terms (I've now checked the IP part)**
- Your models and data stay yours, and startups are allowed to use them commercially.
- You commit to publishing your results, but you can leave out confidential parts. You also commit to crediting EuroHPC.
- You send a final report within 3 months of the end, and EuroHPC may publish it a year later.
- They expect you to take part in at least one EuroHPC event or interview within two years.
- The work must be civilian, comply with the AI Act, and the proposal must be in English.

**Why not just cloud credits?**
Without funding or an accelerator you'd mostly qualify for the smallest tiers, around $1–5k. Most credit programs probably also expect a registered company. On specialist GPU clouds, 20k H100 hours costs very roughly $40–80k right now. At AWS, Azure or Google list prices it's well over $100k. Gefion here in Denmark now seems to charge per GPU hour. Its free access was a pilot call back in 2024.

Two questions, so I can help with the application:
1. What are you training? A model for a product, or research?
2. Does your training code already run across several multi-GPU nodes, or only on one machine so far?

Sources:
- [EuroHPC Terms of Reference, AI Factories Industrial Innovation (v3, 31 Mar 2026)](https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms+of+Reference+-+AIF+Access+Calls.pdf)
- [EuroHPC Fast Lane access](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en)
- [EuroHPC AI Factories access modes](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en)
- [Latvian government: LUMI AI Factory consortium includes Denmark](https://www.izm.gov.lv/en/article/latvia-joins-european-artificial-intelligence-factories-network-strengthening-science-innovation-and-digital-literacy)
- [DCAI / Gefion](https://www.dcai.dk/)
- [Denmark halves the cost of starting your own company (CPH Post)](https://cphpost.dk/2025-03-04/general/denmark-halves-the-cost-of-starting-your-own-company)
- [H100 rental prices across cloud providers, 2026](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison) (third-party)
- [SpendBase: Azure credit tiers](https://spendbase.co/blog/saas-management/azure-credits-for-startups/) (third-party)
