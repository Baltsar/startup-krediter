# s15 without-skill

## Founder, turn 1
Hi, we're a 5-person team in Gothenburg building AI that drafts radiology reports from CT scans (started 2024, spun out of hospital research). We burn about $6k/month on cloud + Claude API right now. Mainly looking for credits, and GPU time to train on ~40k anonymized scans. What should we apply to first?

## Assistant, turn 1
Short answer: get free EU GPU time for the training run first, because you don't need an investor or partner to vouch for you. Then go after cloud credits for the $6k/month. How much you can get there depends on who's backing you.

**1. GPU time: Sweden AI Factory, contact them this week**
- Sweden AI Factory is the old Mimer, run by NAISS and RISE in Linköping. It gives startups and SMEs free GPU access and help from AI experts. Life science and health is one of its focus areas.
- The entry option, **Playground**, gives about 5,000 GPU-hours over 1–3 months, with a decision in about 2 working days. **Fast Lane** gives up to 50,000 GPU-hours over up to 3 months, with a decision in about 4 working days, and is meant for teams already used to HPC. Both are free for AI startups doing innovation work.
- Start by emailing info@swedenaifactory.se rather than going straight to the portal. One EuroHPC page says Playground is temporarily closed and another says it's open. They can tell you which option is open now, pick a system for you, and say whether your data is acceptable. If Playground is closed, Fast Lane is listed as open and you can apply any time.
- Their own machine in Linköping isn't installed yet, so you'll probably run on a EuroHPC system in another EU country. If your code only runs on NVIDIA (CUDA), ask for an NVIDIA system. LUMI, for example, has AMD GPUs.
- Rough size, as a guess only: fine-tuning a 3D image encoder plus a language model of about 7B parameters on 40k studies is likely a few hundred GPU-hours per full run. With experiments and restarts it's more like a few thousand. Playground may cover your first serious round, but your architecture changes this a lot.

**2. Credits for the $6k/month: depends on your backers**
- **AWS Activate** is probably your biggest lever. AWS says its credits also pay for Claude on Bedrock (Amazon's hosted model service). If you move your Claude calls to Bedrock in an EU region, credits could cover both cloud and Claude, and your data stays in the EU.
  - The Portfolio tier gives up to $200k. You need an ID from an "Activate Provider", which is a VC, accelerator or incubator in AWS's network. Ask your investors or incubator whether they are one.
  - The Founders tier gives $1k, and some startups get up to $5k. It's only for self-funded companies. If your investor isn't an Activate Provider, you may not qualify for either tier.
  - Before you move $6k/month over, check in AWS billing that Claude usage really comes out of the credits. AWS's own pages don't fully agree on this.
- **Anthropic's own startup program** isn't taking applications right now because the current round is full. Sign up for their newsletter. Larger amounts, up to $100k in API credits, only come through a VC in Anthropic's partner network.
- **Google and Microsoft** work much the same way: the big tiers need an investor, and the open ones are worth a few thousand dollars. Google's standard credits don't cover Claude on Vertex AI, its hosted model service. Pick one main cloud rather than spreading across three.

**The one thing that can block all of this: rights to the data**
A model that drafts reports trains on pairs of scans and reports. Free-text reports are much harder to anonymize than images, and head CTs can be re-identified from the face unless the face is removed. Also, ethics approval for hospital research usually doesn't cover a spin-out building a commercial product. Any compute provider will ask about this first.

**Three questions so I can firm up the order:**
1. Do you have investors, an incubator or an accelerator behind you? If so, which ones?
2. Who has the right to use the 40k scans and reports: your company, under an agreement with the region, or the research group, under its ethics approval? Can anyone trace them back to patients, and does any agreement say where the data may be processed?
3. Which cloud is the $6k/month on, and do you send anything from patient data through the Claude API today?

Sources:
- [Sweden AI Factory](https://swedenaifactory.se)
- [NAISS: Mimer becomes Sweden AI Factory](https://www.naiss.se/?p=6302)
- [EuroHPC Playground access](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en)
- [EuroHPC Playground "temporarily closed" page](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories-temporarily-closed_en)
- [EuroHPC Fast Lane access](https://www.eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en)
- [LUMI: AI Factories access calls (free for AI SMEs)](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [AWS Activate step-by-step guide (June 2026)](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/)
- [AWS: Activate credits for third-party models on Bedrock](https://aws.amazon.com/blogs/startups/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/)
- [Claude for Startups](https://claude.com/programs/startups)
- [Google for Startups AI program](https://cloud.google.com/startup/ai)

## Founder, turn 2 (simulated)
1. We raised a SEK 4M pre-seed in 2025 from a university-affiliated holding company and two angels. Incubator or accelerator, not sure.
2. Honestly not sure on the data rights: who holds them, whether the scans can be traced back, or what any agreement says about where they can be processed.
3. The cloud is AWS, Stockholm region. We use the Claude API to draft the reports, but whether anything that counts as patient data goes through it, I'm not sure.

## Assistant, turn 2
Thanks, that changes the order. Sorting out the data rights is now step one. You can send two emails alongside it this week.

**This week**

1. **Ask your holding company about AWS credits.** You've raised from investors, so you aren't "self-funded". AWS's open Founders tier ($1k) is meant only for self-funded companies. The tier that makes a real difference is Portfolio (up to $200k), and it needs an ID from an investor or incubator that is an AWS Activate Provider. Ask the holding company:
   - Are you an Activate Provider, or is an incubator you run?
   - Are you, or either of your angels, in Anthropic's VC partner network? That's the only way to its larger API credits, and Anthropic's startup program isn't taking applications right now.

   If they say no, ask AWS for a startup account manager. You already pay AWS, and once Claude runs through AWS (see below), the whole ~$6k/month is on their bill.

2. **Email Sweden AI Factory** (info@swedenaifactory.se). Describe the project and ask which access option is open now, which system they'd suggest, and what they need before you bring health data. Don't upload any scans yet.

3. **Find out who holds the data rights.** Ask these four:
   - **The research lead** behind the dataset: which ethics approval covers the 40k scans and reports? Does it mention your company or commercial use?
   - **The hospital or region holding the records:** is there an agreement that lets the company use the data? Does it allow processing anywhere in the EU, or only in Sweden?
   - **Your holding company:** investors in spin-outs usually check what rights the company actually has before investing. Their papers may already answer this.
   - **Whoever prepared the dataset:**
     - Does a key exist anywhere that links scans to patients?
     - Were the patient details in the image files' metadata (DICOM headers) and any text printed on the images removed?
     - Were faces removed from head CTs?
     - Were names, ID numbers and dates removed from the report text?

   If a key exists anywhere, treat the data as patient health data until a lawyer says otherwise.

**The Claude API: assume patient data goes through it**
If Claude drafts reports on real patients' scans, what you send is about a specific person's scan, even with no name attached. Once you're live, the hospital is normally the "controller" of that data under GDPR. That means it has to approve subprocessors like Anthropic, and any transfer outside the EU.

Anthropic's own page offers EU processing only through cloud partners. Independent guides say the direct API runs in the US. Since you're already on AWS Stockholm:
- **Call Claude through Bedrock with an EU profile** (the `eu.` model IDs). Current Claude models are available that way from Stockholm. Requests are served in other EU regions, such as Frankfurt or Ireland, but not in Stockholm itself. So the data stays in the EU, though not necessarily in Sweden. Your data agreement decides whether that's enough.
- **Don't use the `global.` profile.** It has no geographic limit.
- **Check Bedrock's price for the `eu.` profile before you switch.** It may differ from the direct API.
- **The code change is small.** Anthropic's SDK has a built-in Bedrock client.
- **Credits can cover it.** Claude costs then land on your AWS bill, so Activate credits can pay for them. Check in billing that the credits actually go down.

**Then: GPU time**
Once the data rights are clear, apply for Playground or Fast Lane, whichever Sweden AI Factory recommends.

Two answers would help me with the next step:
- Which holding company is it, and which hospital or region? I can check what's public about their programs and data rules.
- Are you live with real patients yet, or still piloting on research data?

I can also draft the email to Sweden AI Factory and the questions for the research lead if that helps.

Sources:
- [AWS Activate step-by-step guide (tiers and eligibility)](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/)
- [AWS: Activate credits for third-party models on Bedrock](https://aws.amazon.com/blogs/startups/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/)
- [Amazon Bedrock regional availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)
- [Anthropic regional compliance](https://claude.com/regional-compliance)
- [Claude EU data residency in 2026 (third-party guide)](https://sonomos.ai/blog/claude-eu-data-residency-2026/)
- [Claude for Startups](https://claude.com/programs/startups)
- [Sweden AI Factory](https://swedenaifactory.se)
