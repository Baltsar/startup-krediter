# q15 without-skill

## Founder, turn 1
We're a Helsinki based AI startup (Oy), closed a 2.5M EUR seed in spring led by a Nordic VC. We're spending heavily on inference, mostly AWS Bedrock and some OpenAI. What's the biggest stack of cloud/AI credits we can realistically get at this stage? We already used the AWS Activate founders tier ages ago. Also heard about some EuroHPC AI factory thing, is that for companies like us or just universities?

## Assistant, turn 1
Short answer: if you're willing to run some workloads on more than one cloud, about **$500k–$750k in credits** is realistic at your stage. Expect most of it to come from the three hyperscalers. On top of that you can get free EU GPU hours from the AI Factory. Here's how it breaks down.

**1. AWS: you're not done just because you used the Founders tier**
Founders (~$1k) and **Activate Portfolio** are separate paths. Portfolio is worth up to **$100k** (one AWS guide this year says $200k, but the official credits page still says $100k). You get it through an Organization ID from an "Activate Provider", which is usually your VC. Ask your lead investor if they're an AWS Activate Provider. Many Nordic VCs are, and this is the single most useful email you can send this week. Eligibility is pre-Series B with a round in the last 12 months, so your spring seed qualifies. Credits you got earlier may be netted off the amount, but that doesn't stop you applying.
Since Bedrock is your main cost, check that your specific Bedrock models are credit-eligible. Some third-party and Marketplace models are excluded.
The bigger option is the **AWS Generative AI Accelerator**, worth up to **$1M** in credits. It runs as yearly cohorts and is very selective (reportedly under 2% acceptance). The 2026 intake seems to have closed in July, so watch for the 2027 call.

**2. Google Cloud: probably the biggest single amount**
The **Google for Startups Cloud Program, AI tier** gives up to **$350k** over two years if Gemini/Vertex AI is core to your product. It's open to seed through Series A. The catch is that it assumes you build on Google's AI stack, so it's only worth it if you'd move part of your inference to Gemini or open models on Vertex.

**3. Microsoft: matters because of OpenAI**
Through Microsoft for Startups, a referral from an investor in their Investor Network unlocks up to **$150k** in Azure credits. Self-serve is only about $5k. Azure credits can pay for **Azure OpenAI**, which is how to get your OpenAI spend covered. Direct OpenAI credits mostly go through specific VC partners (Sequoia, a16z, Thrive and similar) or accelerators, so for a Nordic-backed company Azure is the practical route.

**4. Model-provider credits (smaller amounts)**
- **Anthropic startup program**: reportedly up to tens of thousands in Claude credits. You can apply directly, and it goes higher via partner VCs. Note these are credits for Anthropic's own API, not Bedrock.
- **NVIDIA Inception**: free to join. It's mostly perks and discounts, but it opens doors to other offers.

**5. The EuroHPC AI Factory: yes, it's for companies like you**
It isn't just for universities. **LUMI AI Factory** is the Finnish-led one, run by CSC in Kajaani. It has access modes specifically for **startups and SMEs, free of charge**:
- **Playground**: small allocation, answer in about 2 working days
- **Fast Lane**: up to **50,000 GPU hours**, decision in about 4 working days
- **Large Scale**: over 50,000 GPU hours, through periodic calls

Two caveats:
- It's for **R&D and innovation**: training, fine-tuning, evals and experiments. It won't host your production inference traffic, so it reduces R&D compute cost, not your Bedrock bill.
- The EuroHPC Playground portal was marked temporarily closed during a platform migration. Check the LUMI access page for current status before you plan around it.

That said, 50k GPU hours costs a lot on any cloud, so if you fine-tune or train anything it's a strong fit.

**Rough realistic stack:** AWS Portfolio $100k + Google AI $350k + Azure $150k + Anthropic/other ~$25–50k, plus free LUMI GPU hours. That comes to about **$600k+ in credits**, before any long-shot accelerator. All figures come from mixed official and third-party sources and they change often, so check each one before you apply.

A few questions so I can sharpen this:
1. Who is your lead VC? That decides which provider networks (AWS, Microsoft, Google) you can get referral codes from.
2. Roughly what's your monthly inference spend, and how is it split between Bedrock and OpenAI?
3. Would you move some workloads to Gemini/Vertex or Azure OpenAI, or are you locked into specific models?
4. Do you train or fine-tune your own models, or is it all API inference? That decides how useful LUMI is.

Sources: [AWS Activate credits](https://aws.amazon.com/startups/credits), [AWS Activate guide](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide), [LUMI AI Factory access calls](https://lumi-supercomputer.eu/access-calls-for-ai-factories/), [EuroHPC Playground status](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories-temporarily-closed_en), [Google for Startups Cloud AI](https://startup.google.com/programs/accelerator/cloud-ai/north-america), [Microsoft Founders Hub tiers](https://spendbase.co/blog/saas-management/azure-credits-for-startups/), [AWS GenAI Accelerator 2026](https://startupintros.com/resources/aws-generative-ai-accelerator-2026), [AI credits overview](https://fin.ai/learn/ai-credits-for-startups)

## Founder, turn 2 (simulated)
1. A Nordic VC, I don't know which provider networks they're part of. 2. Don't have the exact monthly number or split at hand. 3. Not sure yet. 4. Yes, we fine-tune open-weight models on rented H100s.

## Assistant, turn 2
That helps a lot. Fine-tuning open-weight models on rented H100s changes the picture. **The free EU GPU hours are probably your biggest single win**, and they matter more than any one cloud credit pack.

**1. Use the AI Factory for fine-tuning**
Your use case is exactly what the industrial access modes are for: an SME doing AI R&D, free of charge. The one that fits you is **Fast Lane**:
- up to **50,000 GPU hours**
- for 1–3 months
- decision in about 4 working days

For comparison, 50k H100 hours costs well into six figures at typical rental prices. When the 3 months run out you can apply again. If you need more, the **Large Scale** calls cover over 50k hours.

Things to check before you count on it:
- **Hardware.** You request one specific system. LUMI's current GPU partition is **AMD (MI250X), not NVIDIA**, so you'd be on ROCm instead of CUDA. Most PyTorch/HF fine-tuning stacks run on it, but test before committing. The new LUMI AI system was only contracted in August, so it isn't available yet. Other EuroHPC AI Factories run NVIDIA hardware, and you don't have to use the Finnish one. Check the system list on the call page and pick the one that matches your stack.
- **R&D only.** The output can go into your product, but the hours have to go to development and innovation work, not production serving.
- **Portal status.** EuroHPC flagged Playground as temporarily closed during a platform migration. Check the current call on the access portal or email the LUMI AI Factory helpdesk. They exist to help startups write the application.

**2. Find out which networks your VC is in (one email)**
You don't need to know this yourself. Send your VC contact something like:
> "Are you an AWS Activate Provider, part of the Microsoft for Startups Investor Network, or a Google for Startups partner? If so, could you send us the org ID / referral codes?"

Each "yes" is worth roughly AWS up to $100k, Azure up to $150k (which can pay for Azure OpenAI), and Google's partner track. If the answer is no for any of them, you can still apply directly. The amounts are lower, but Google's AI tier (up to $350k) doesn't strictly need a partner.

**3. Who are you renting H100s from?**
Credits only help if you rent from a hyperscaler.
- **On AWS already:** Activate credits should cover the GPU instances as well as Bedrock.
- **On a GPU cloud (Lambda, CoreWeave, Nebius, etc.):** no hyperscaler credits apply. Then it's the AI Factory hours plus moving some jobs to whichever cloud gives you the biggest credit pack. Google credits can cover GPU VMs, but H100 quota can be hard to get on credits.

**4. Spend numbers can wait**
A rough order of magnitude is enough: under or over ~€20k/month, and roughly what share goes to fine-tuning versus inference. That tells us whether to steer inference to Azure OpenAI or Gemini to use those credits, or to just stack AWS for Bedrock.

**Suggested order this week:**
1. Email your VC the question above.
2. Look at the Fast Lane call and pick a system that matches your stack.
3. Apply to the Google AI tier and Anthropic's startup program directly, since neither strictly needs a partner.

Tell me which GPU provider you rent from and what the VC says, and I'll narrow it to the 2–3 applications worth your time.

Sources: [EuroHPC Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en), [AI Factories access modes](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en), [LUMI access calls for AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/), [EuroHPC Playground status](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories-temporarily-closed_en), [AWS Activate credits](https://aws.amazon.com/startups/credits)
