# s02 without-skill

## Founder, turn 1
hey, 3 cofounders here building an open source LLM eval / red teaming toolkit. ~4k github stars, a couple of companies run it in their CI. we need GPU time to run evals against bigger open weight models and ideally some api credits (openai/anthropic/google). no funding yet, company is registered. what can we apply for?? something like 50k gpu hours would be a dream lol

## Assistant, turn 1
50k GPU hours isn't a "lol" number. There's a program whose cap is exactly that. Whether you can use it depends on one thing you didn't say: **which country the company is registered in.** Here's what's available, with the most useful first.

**1. GPU hours: EuroHPC AI Factories (if you're registered in the EU, or a country like Norway, Switzerland or the UK)**
These are free for startups and SMEs doing "innovation" work, and it's allocation time on EU supercomputers, not cash. There are three levels:
- **Playground:** small allocations, first-come first-served, 1–3 months.
- **[Fast Lane](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en):** up to 50,000 GPU hours on one system, for 1–3 months. They aim to decide within about 4 working days.
- **Large Scale:** more than 50k hours, for up to a year.

The catches:
- It's a Slurm/HPC setup, so you'd run vLLM or SGLang in containers. They expect you to know HPC.
- 50k hours in 3 months means about 23 GPUs running nonstop. Size the request honestly.
- They're moving to a new platform, and some pages say "temporarily closed". Check the [access portal](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en) before you plan around a date.

The smart order is Playground first. Get your eval harness running on one of their systems and measure how many GPU hours one full run takes. Then apply for Fast Lane with real numbers.

If you're registered in the US, this route is closed. The US equivalent (the NAIRR pilot) only takes startups that already hold federal grants.

**2. API credits: the programs are small without funding**
- **Anthropic [External Researcher Access](https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program):** usually $1,000, reviewed monthly. Red teaming fits, but you still have to follow their usage policy. Jailbreak findings go to their bug bounty instead.
- **OpenAI [Researcher Access](https://help.openai.com/en/articles/10139500-researcher-access-program-faq):** up to $1,000, reviewed quarterly (next round December). You need a link to a university or research organisation. If you work with an academic, apply through them.
- **Cloud startup programs:** without an investor, expect roughly $1k–5k each.
  - [AWS Activate Founders](https://aws.amazon.com/startups/credits): $1k to start, up to $5k.
  - Google for Startups Start tier: about $2k.
  - Microsoft: about $1k–5k.

  Google Cloud credits can pay for Gemini on Vertex. Credits often don't cover outside models like Claude on Bedrock or Vertex, so check the terms first.
- **The $100k–350k tiers** at AWS, Google and Microsoft all need an investor or accelerator referral.

**3. Your real leverage is 4k stars and companies running you in CI**
None of these programs will give you $50k in credits. Email the labs and the inference providers (Together, Fireworks and similar) directly. Offer first-class support for their models and published results in exchange for sponsored credits. For open-weight models, paying per token through those providers may also cost less than renting GPUs, depending on how bursty your runs are.

**Smaller things worth applying for anyway**
- **[TPU Research Cloud](https://sites.research.google/trc/about/):** free Google TPUs if you publish your work. vLLM runs on TPU.
- **[Codex for Open Source](https://developers.openai.com/codex/community/codex-for-oss) and Claude for Open Source:** mostly subscriptions for maintainers. The Claude one's stated path is 5k stars and its window may have closed. Good for your own dev work, but they won't pay for eval runs.

**Three questions so I can make this concrete:**
1. Which country is the company registered in?
2. What's the biggest model you want to run, and roughly how many GPU hours does one full eval run take?
3. Is anyone on the team comfortable with Slurm or HPC clusters?

## Founder, turn 2 (simulated)
1. Norway. 2. not sure tbh, haven't pinned down the biggest model or how many gpu hours one full run takes. 3. kinda, one of us had an allocation on Sigma2 (the norwegian national HPC) during a PhD at uni of Bergen, so there's some HPC experience

## Assistant, turn 2
Norway is good news. Norway is one of the six countries in the **[LUMI AI Factory](https://lumi-ai-factory.eu/pricing-and-eligibility/)**, and Norwegian startups are part of the main group it serves. Computing there is free for startups and SMEs doing R&D. Sigma2 runs Norway's part of it under the name **[KI-fabrikken](https://www.sigma2.no/nb/ki-fabrikken)**. Your cofounder's Sigma2 background helps directly.

**Plan for the GPU hours, in order:**

**1. Contact Sigma2's KI-fabrikken this week.** Use the form on that page or contact@sigma2.no. Their expert consultations are aimed at businesses. Ask them two things:
- Is Playground or Fast Lane the right route for you?
- Which system should you run on?

The choice of system matters:
- **LUMI** is AMD MI250X. vLLM runs on it, but that hardware has no FP8, so big models need about twice the GPUs.
- **Olivia**, Sigma2's newer system, is NVIDIA GH200. That's less work to set up. Ask whether startups can get free time on Olivia through KI-fabrikken. I couldn't find published terms for that.

**2. Apply for EuroHPC Playground first.** It's meant for testing, and they aim to grant access within 2 working days. Use it to run your full eval on 2–3 model sizes and measure the GPU hours. That also answers the question you couldn't answer yet.

**3. Then apply for Fast Lane with real numbers.** It gives up to 50k GPU hours on one system, for 1–3 months. Their stated aim is a decision within 4 working days. LUMI says new users usually start with a small pilot, so steps 2 and 3 are the expected order. You'll need to write a final report and credit LUMI AI Factory and EuroHPC in anything you publish. That's easy for an open-source project.

**How to estimate GPU hours per run (rough numbers, check them with a test run):**

GPU hours per run = number of GPUs × hours the run takes.

To get the number of GPUs, start from the model weights. In BF16 a model needs about 2 bytes per parameter; in FP8, about 1 byte. Add 20–40% on top for the KV cache. Roughly:
- **~70B model:** about 140 GB in BF16, so 2–4 GPUs with 80–96 GB each.
- **~400B dense model:** about 400 GB in FP8, so 8 GPUs with 80 GB each.
- **~700B MoE model (DeepSeek-class):** about 700 GB in FP8, so 8 GPUs with 141 GB each, or 16 with 80 GB each.

Example: if a full red-team suite takes 6 hours on 8 GPUs, that's 48 GPU hours. 50k hours would then be about 1,000 full runs. You may need far less than 50k, and reviewers like a request that adds up.

**If the free route is slow, the paid price is low.** Sigma2's [commercial price list](https://www.sigma2.no/user-contribution-model) says:
- **Olivia:** NOK 35 per GPU hour.
- **LUMI:** NOK 5.35 per GPU hour. On LUMI, one "GPU hour" means one full MI250X module for an hour.

At that rate, 50k LUMI hours would be about NOK 270k. Confirm with Sigma2 that the rate applies to a company like yours.

**Norwegian money that can pay the API bills**

The API credit programs from my last message don't change because you're in Norway. They're still small without funding. Two Norwegian routes give you cash you can spend on API use:
- **[SkatteFUNN](https://www.forskningsradet.no/skattefunn/sok/):** a tax deduction of 19% of the costs of an R&D project, and compute and API costs can count. If you pay no tax yet, the difference is paid out to you in cash. The deadline that guarantees a decision for 2026 was 1 September, so aim for an approved project covering 2027 costs. Changes to the rules have been proposed for 2027, so check the current call text.
- **Innovasjon Norge oppstartstilskudd:** a startup grant, around NOK 150k in the first phase. The 2026 rules are stricter and often want your own or investor money alongside it, so don't count on it while you're unfunded.

**One question:** which 2–3 open-weight models do your users ask about most? Tell me and I'll turn the estimate above into a first draft of the Playground and Fast Lane request.
