# q06 without-skill

## Founder, turn 1
anyone know where to get free gpu hours? we're training a vision model for a warehouse picking robot and our runpod bill is getting silly, like 2-3k a month. small team, no funding yet but we have a working prototype

## Assistant, turn 1
Short version: yes, there is free compute, but the big headline amounts mostly assume you've raised money or been referred by an accelerator. With no funding, here's roughly what you can get. Check the current terms on each program's own page, because these numbers change often.

**Things you can apply for now, without funding**
- **NVIDIA Inception**: free, no equity, open to most incorporated AI startups. You don't get guaranteed cash credits. What you get is partner cloud deals, discounts, training credits and VC intros. It's quick to apply for and it helps you get into the programs below. A robotics/vision team fits well.
- **AWS Activate Founders**: self-serve, but small (around $1k now). The real money is the Portfolio tier (up to about $100k), and that needs a referral ID from a VC, accelerator or incubator.
- **Google for Startups Cloud**: the Start tier is small (about $2k) without equity funding. The AI tier goes up to $350k over 2 years, but Google lists seed to Series A funding as a requirement, so it isn't for you yet.
- **Microsoft for Startups (Founders Hub)**: self-serve Azure credits. GPU availability on the free tiers can be limited, though.

**If you're in Europe, this is probably your best option**
The **EuroHPC AI Factories** offer free GPU access to startups and SMEs for innovation work, up to about 50k GPU hours on the "Fast Lane" track. That's a lot more than your RunPod spend. Some national AI factories and supercomputer centres also have their own startup access calls. Which ones you can use depends on where you're incorporated. The entry-level Playground track was listed as temporarily closed, so check what's open right now.

**The quickest way to unlock the big credit tiers**
Join an accelerator or get a small pre-seed check. Even a modest one usually gives you a referral ID that unlocks the $100k+ AWS/Google/Azure tiers. Many accelerators bundle these perks in.

**While you wait**, there are some ways to cut the RunPod bill:
- Use spot or community instances.
- Use mixed precision.
- Start from a strong pretrained backbone and fine-tune it instead of training from scratch.
- Do your hyperparameter sweeps on a smaller subset of the data.

A $2-3k bill can often drop a lot this way.

To point you at the right programs, a few questions:
1. Which country is the company registered in, or do you not have a company yet?
2. Are you talking to any accelerators or angels?
3. Roughly how many GPU hours a month do you use, and on what GPUs?

Sources: [NVIDIA Inception guide](https://www.thundercompute.com/blog/nvidia-inception-program-guide), [Google for Startups AI program](https://cloud.google.com/startup/ai), [AWS Activate tiers](https://guptadeepak.com/startup-offers/guides/aws-activate), [EuroHPC AI Factories access](https://www.euacc.ai/programmes/ai-factories), [EuroHPC Playground status](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories-temporarily-closed_en), [robotics credit overview](https://creditforstartups.com/robotics-startup-funding)

## Founder, turn 2 (simulated)
1. sweden, AB in gothenburg. 2. no, not talking to any accelerators or angels. 3. not sure exactly per month, we train on A100s on runpod, probably a few thousand gpu hours a year

## Assistant, turn 2
That helps a lot. A Swedish AB with a few thousand A100 hours a year is a good fit for free public compute. That's far less than what these programs are built for. In order:

**1. Mimer, Sweden's AI Factory (Linköping University and RISE)**
This one fits you best. It is meant to give Swedish startups and SMEs compute, AI expertise and business support free of charge. Autonomous systems is one of its priority areas, and a warehouse picking robot falls under that. Two caveats:
- Access is by selection, not automatic. For companies it is given as de minimis state aid, so it counts toward the EU cap on small subsidies a company can receive.
- The new system is being installed during 2026, so timelines may still shift.

Contact them directly through mimer-ai.eu or NAISS and tell them what you're training. Ask whether they can start you on existing capacity before the new system goes live.

**2. EuroHPC AI Factories industrial access (the same EU network, with calls across Europe)**
This is free for AI startups and SMEs:
- **Playground** is the entry track. First come, first served, with no deadlines. It suits your volume.
- **Fast Lane** gives up to 50k GPU hours for up to 3 months, with approval in a few days.

Both were listed as "temporarily closed" while EuroHPC moves to a new platform. Their pages say you can still apply through the old portal. Check the access-calls page for what's open today.

One thing to know: these are supercomputers (Slurm, containers), not RunPod-style pods. Plan a few days to port your training pipeline. Also make sure your data and licensing terms allow you to train there.

**3. Vinnova Innovative Startups 2026: open now, deadline 12 January 2027**
- Up to SEK 500,000.
- You must be an AB with fewer than 10 employees, turnover or balance sheet of at most 10 MSEK, and no profit distributions yet. That sounds like you.
- The money goes to testing customer needs, the business model and willingness to pay, with an international market in view. It does not go to compute.

Even so, it's worth applying in parallel. It pays for pilots with warehouses, and that frees up your own money for GPUs.

**4. NVIDIA Inception**
Apply today. It's free and takes 10 minutes. It doesn't give you GPU hours directly, but you get discounts and partner offers. It also makes you look more credible in other applications.

Skip the big credit tiers at AWS, Google and Azure for now. They require a VC or accelerator referral. Once you have a referral, you can open them up later.

If I were you, I'd do this this week:
1. Email Mimer.
2. Check whether the EuroHPC Playground is open and apply.
3. Sign up for Inception.
4. Start drafting the Vinnova application. Its deadline is in January.

With some luck you can cover most of next year's training for free. Want help writing the project description for Mimer or EuroHPC? They want to know what you're training, why it requires HPC, and the expected impact.

Sources: [Mimer (RISE)](https://www.ri.se/en/mimer-swedens-ai-factory-powers-up-supercomputing-race-to-tomorrows-ai-solutions), [EuroHPC: new AI system in Sweden](https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en), [EuroHPC Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en), [Fast Lane status](https://www.eurohpc-ju.europa.eu/fast-lane-access-ai-factories-temporarily-closed_en), [AI Factories overview](https://www.euacc.ai/programmes/ai-factories), [Vinnova Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026), [Lund University info on the call](https://www.ch.lu.se/evenemang/info-meeting-vinnovas-call-innovative-startups-2026)
