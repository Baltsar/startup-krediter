# s07 without-skill

## Founder, turn 1
Hi! We're a small indie studio in Stockholm, company is about a year old. Our game has AI-driven NPC dialogue and we want to train our own small voice + animation models instead of paying per API call forever. Looking for GPU time and cloud credits (AWS, Google, whatever works). Also, are there Swedish grants for game studios or is that not really a thing?

## Assistant, turn 1
Hi! Short version: you can get GPU time, and probably for free. Sweden has no grants made specifically for game studios, but a few general programs could work for you.

**GPU time: start with the Sweden AI Factory, then add cloud credits**

[Sweden AI Factory](https://swedenaifactory.se/) (Mimer) is Sweden's part of the EU network of AI factories. It gives startups and SMEs free GPU time and help from experts. Gaming is one of its four focus sectors.
- **Playground:** about 5,000 GPU hours over 1–3 months, with a decision in about two working days. It's built for teams that are new to supercomputers.
- **Fast Lane:** up to 50,000 GPU hours for up to 3 months, for teams already used to running jobs on a supercomputer cluster.
- **How to start:** describe your project on their [contact form](https://swedenaifactory.se/contact-us/) and they'll tell you which route and which machine fits.

There are two catches:
- It's a supercomputer: you queue batch jobs and run them in containers. That works for training, but it can't run the NPC dialogue live for your players.
- Your time starts when you're approved. Clean your data and test your training scripts on one small GPU before you apply.

**Cloud credits: real, but small unless you have investors**
- **[AWS Activate](https://aws.amazon.com/startups/credits):** if you're self-funded, you start at $1,000 and can get up to $5,000. The bigger tier (up to $200k) needs an ID from an AWS-approved accelerator, angel investor or VC.
- **[Google for Startups Cloud](https://cloud.google.com/startup/faq):** about $2,000 if you haven't raised equity. The bigger tier (up to $200k, or $350k for AI startups) needs equity funding. I couldn't load Google's full terms, so check them there.
- **[Microsoft for Startups](https://learn.microsoft.com/en-us/startups/overview):** anyone can get up to $5,000 in Azure credits, with $1,000 right away. More needs a referral from an investor.
- **NVIDIA Inception:** free to join. It gives no cash itself, but it opens up GPU-cloud offers from partner companies.

A few thousand dollars buys far fewer high-end GPU hours than one Playground allocation. I'd do the training on the AI Factory and use cloud credits for experiments and hosting. New cloud accounts often start with zero GPU quota, so request more quota as soon as you sign up.

**Grants: Sweden has no national games fund**

The Swedish Arts Council (Kulturrådet) doesn't fund commercial companies. There's also no games version of the Swedish Film Institute. A [2025/26 Riksdag research overview](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/rapport-fran-riksdagen/kunskapsoversikt-om-dataspel-och-bradspel_hd0wrfr6/html/) describes this gap. What can still work:

1. **[Creative Europe MEDIA – Video Game and Immersive Content Development](https://www.filminstitutet.se/sv/sok-stod/kreativa-europa/vara-stod-utlysningar-och-deadlines/innehallskluster/stod-till-utveckling-av-dataspel-och-immersivt-innehall/).** This is the one real games grant you can apply for.
   - **Money:** up to €200,000, covering 60% of costs, paid as a lump sum.
   - **Deadline:** 2 February 2027 at 17:00 Brussels time.
   - **Catch:** you must have a finished game that was sold commercially and earned money between 1 January 2024 and the deadline.
   - **What it funds:** a new project up to its first prototype, not a game already in production.
   - The Swedish Film Institute runs the Swedish Creative Europe desk and can advise you.
2. **[Vinnova Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026).**
   - **Dates:** open now, closes 12 January 2027 at 14:00. Info meetings are on 2 and 9 November.
   - **Money:** up to SEK 500,000.
   - **Who can apply:** a Swedish AB, at most 10 years old, with at most 10 full-time staff. Turnover or balance sheet total must be at most SEK 10M (only one of them can be higher).
   - **How it's judged:** games aren't excluded, but it's scored on how new your solution is and its international market. Pitch your NPC voice and animation technology and how it makes money, not "funding our game." Competition is tough.
3. **[Almi](https://www.almi.se/en/loan/verification-grant/who-can-receive-a-verification-grant/):** offers verification grants and innovation loans (loans must be repaid). Worth a call to Almi Stockholm.
4. **R&D tax relief (FoU-avdrag):** if your model work counts as R&D, your employer contributions drop by 20% of the salaries of the people doing it. It's not a grant, but it's real money. Ask your accountant.

**Check licenses before you train**

Some popular open voice models can't be used in a commercial product:
- F5-TTS's pretrained weights are licensed CC-BY-NC (non-commercial).
- XTTS-v2's license only allows non-commercial use. Coqui, the company that could sell a commercial license, has shut down.

Pick a base model whose license lets you ship it in a game. Also make sure your voice actors' contracts give written consent for AI training and voice synthesis.

**Three questions so I can narrow this down:**
1. Are you self-funded, or do you have angels, a VC or an accelerator behind you? That decides which cloud credit tier you get.
2. Have you released a game that earned money since January 2024? That decides whether you can apply to Creative Europe.
3. Roughly what will you train: how big are the models, and how many hours of audio or motion capture do you have? Has anyone on the team run jobs on a supercomputer before? That decides between Playground and Fast Lane.

Sources: [Sweden AI Factory](https://swedenaifactory.se/), [EuroHPC Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en), [EuroHPC Playground](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en), [EuroHPC: Mimer contract and focus sectors, April 2026](https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en), [AWS Activate](https://aws.amazon.com/startups/credits), [Google for Startups FAQ](https://cloud.google.com/startup/faq), [Microsoft for Startups](https://learn.microsoft.com/en-us/startups/overview), [Creative Europe at the Swedish Film Institute](https://www.filminstitutet.se/sv/sok-stod/kreativa-europa/vara-stod-utlysningar-och-deadlines/innehallskluster/stod-till-utveckling-av-dataspel-och-immersivt-innehall/), [Vinnova Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026), [Riksdag report on games](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/rapport-fran-riksdagen/kunskapsoversikt-om-dataspel-och-bradspel_hd0wrfr6/html/), [Almi verification grant](https://www.almi.se/en/loan/verification-grant/who-can-receive-a-verification-grant/), [Coqui Public Model License (XTTS-v2)](https://huggingface.co/Borcherding/XTTS-v2_CarliG/blob/418d3f6406d97c9c4d1ff2767be43db54e380643/LICENSE.txt)

## Founder, turn 2
1. Self-funded. We've put in SEK 250k of our own money, no angels, VC or accelerator.
2. No. We only have a free demo on Steam, no sales yet.
3. An open-weight 8B model for the NPC dialogue and an open-source TTS model we want to fine-tune. We figure around 2,000 GPU hours for the fine-tuning. How many hours of audio or mocap we have, not sure. And not sure whether anyone on the team has run jobs on a supercomputer before.

## Assistant, turn 2
Thanks, that helps a lot. Here's what changes for you:

**What you can and can't get right now**
- **You can get:** free GPU time from the Sweden AI Factory, the cloud credits for self-funded companies, Vinnova Innovative Startups, and Almi.
- **Not yet:** Creative Europe. A free demo doesn't count. You need a finished game that's been sold and earned money. Once you have sales, you can apply in a later round, but the money is for your next game.
- **Not for you:** the big credit tiers (AWS Portfolio, Google Scale, Microsoft's investor offer). They all need a backer: an investor, an accelerator or similar.

**Your estimate of 2,000 GPU hours is probably high**

Most teams fine-tune an 8B model with LoRA, a method that trains a small add-on to the model instead of all of it. That usually takes hours per run, not hundreds. One [public write-up](https://app.readytensor.ai/publications/llamavox-humanizing-ai-through-advanced-llm-fine-tuning-AP9aLhK7YAyh) fine-tuned Llama 3.1 8B this way on 5,000 examples in 25 minutes on one A100 GPU. A 50,000-example run fit inside 4 hours. I'd expect your TTS fine-tune to be a similar size, but it depends on how much audio you have. Even with many test runs, you might land at tens to a few hundred GPU hours. Retraining the whole model, or training from scratch, would be a different story.

So measure before you apply for anything big:
1. Take about 10% of your dialogue data and voice recordings.
2. Run one LoRA fine-tune of the 8B model and one TTS fine-tune on a single rented GPU, paid with credits.
3. Time both runs, scale up to your full data, and add room for 5–10 reruns.

**Cloud credits you can get as a self-funded company**
- **[AWS Activate Founders](https://aws.amazon.com/startups/credits):** $1,000 to start, up to $5,000.
- **[Microsoft for Startups](https://learn.microsoft.com/en-us/startups/microsoft-for-startups/mfs-faqs), if you're new to Azure:** $1,000 that lasts 90 days. Then another $4,000 for 180 days once they've verified your business. Sign up when you're ready to run the test, so the first $1,000 doesn't expire unused.
- **[Google for Startups Cloud](https://cloud.google.com/startup/faq), Start tier:** about $2,000. Confirm the amount on Google's page.
- **NVIDIA Inception:** free to join, and gives you access to GPU-cloud offers from its partners.

That's up to about $12,000 in total. At standard prices, $1,000 buys very roughly 150–500 hours on one data-centre GPU, depending on the GPU and provider. That may cover all of your fine-tuning. Ask for GPU quota the day you sign up, because new accounts often start at zero.

**Use the Sweden AI Factory if the real number is big**

If your test shows you need many hundreds of hours or more, apply for Playground. It gives about 5,000 GPU hours over 1–3 months, so 2,000 would fit.
- **Cost:** [free for AI startups and SMEs](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en) doing innovation work.
- **Experience needed:** none. It's built for first-time users, and [Sweden AI Factory](https://swedenaifactory.se/) offers onboarding, expert support and free self-paced lessons.
- **Learning curve:** expect a few days learning to queue jobs with the cluster's job scheduler (Slurm) and to package your code in a container.
- **Before applying:** read the access terms, especially any reporting duties.

**Grants**
- **[Vinnova Innovative Startups](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026):** the realistic one.
  - **Deadline:** 12 January 2027 at 14:00. Info meetings are on 2 and 9 November.
  - **Money:** up to SEK 500,000, and Vinnova can cover up to 100% of project costs.
  - **Who can apply:** a Swedish AB with at most 10 full-time staff.
  - **Timing:** the project runs from March 2027, so it won't pay for training you do this autumn.
  - **Pitch:** your NPC technology and how you'll test that players will pay for it, not the game itself. Competition is tough.
- **Almi Stockholm:** ask about verification grants and loans. Loans must be repaid.
- **R&D tax relief (FoU-avdrag):** only helps if you pay salaries. If you do, employer contributions drop by 20% of the salaries of the people doing R&D.

**Two things to decide before you train**
1. **Licenses.** Pick models you're allowed to ship in a commercial game. A fine-tuned version keeps its base model's license.
   - **8B models:** Qwen3-8B and Ministral 3 8B are Apache 2.0, which allows commercial use. Llama 3.1 8B uses Meta's own license, which allows commercial use with conditions.
   - **TTS:** avoid weights that only allow non-commercial use, such as F5-TTS and XTTS-v2. Chatterbox (MIT license) is one model that allows commercial use.
2. **Where the 8B model runs.**
   - **On your servers:** you swap per-call API fees for GPU hosting fees, which is still an ongoing cost.
   - **On players' PCs:** a compressed (4-bit) 8B model needs roughly 5–6 GB of graphics memory, which takes memory away from the game's own graphics. A smaller model of 1–4B might be enough for NPC lines.

**Three questions:**
1. Is the company an AB, and do you pay yourselves salaries? That decides Vinnova and the R&D tax relief.
2. Which 8B and TTS models are you looking at? I'll check their licenses.
3. Do you want the 8B model to run on players' PCs or on your servers?

Sources: [Sweden AI Factory](https://swedenaifactory.se/), [EuroHPC AI Factory access modes](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en), [EuroHPC Playground](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en), [AWS Activate](https://aws.amazon.com/startups/credits), [Microsoft for Startups FAQ](https://learn.microsoft.com/en-us/startups/microsoft-for-startups/mfs-faqs), [Google for Startups FAQ](https://cloud.google.com/startup/faq), [Vinnova Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026), [Creative Europe video game support (Swedish Film Institute)](https://www.filminstitutet.se/sv/sok-stod/kreativa-europa/vara-stod-utlysningar-och-deadlines/innehallskluster/stod-till-utveckling-av-dataspel-och-immersivt-innehall/), [LlamaVox fine-tuning write-up](https://app.readytensor.ai/publications/llamavox-humanizing-ai-through-advanced-llm-fine-tuning-AP9aLhK7YAyh), [Ministral 3 8B model page](https://friendli.ai/models/mistralai/Ministral-3-8B-Instruct-2512-BF16), [Qwen3-8B vs Llama 3 8B licenses](https://bestllmfor.com/compare/qwen3-8b-vs-llama3-8b/), [FoU-avdrag (Azets)](https://www.azets.com/sv-se/resurser/blogg/skatteincitament-for-forskning-och-utveckling)
