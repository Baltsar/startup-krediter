# r10 without-skill

## Founder, turn 1
We're a 4-person ltd building scheduling software for construction subcontractors (concrete, electricians etc). ~€18k MRR, bootstrapped. Looking at whether there's any grant money for building an AI feature that reads drawings and auto-generates material lists. Also would take cloud credits, our Azure bill is getting silly.

## Assistant, turn 1
Short version: there's probably money in this, but the best source depends on which country your ltd is registered in. Can you tell me? "Ltd" plus euros makes me think Ireland. If it's Malta, Cyprus or somewhere else, the answer changes a lot.

Here's what I'd say before knowing that.

**Grants for the drawing-reading AI feature**

- **Pitch it as R&D, not as a feature.** Funders don't pay for "adding AI to our product". They do pay for solving a hard technical problem. Reading messy construction drawings (scanned PDFs, mixed symbols, revision clouds, cross-referenced sheets) and turning them into reliable quantities is a real research problem. Write the application around that.
- **R&D tax credits may beat grants.** Many EU countries refund part of the payroll spent on qualifying development. Ireland's credit is generous: 30% of qualifying spend, partly payable in cash even if you're not in profit. For a bootstrapped 4-person team, that's often more money than a grant, with less competition and less admin. It's worth checking before anything else.
- **Small national grants are the realistic first step.** Most countries have innovation vouchers or small R&D grants for firms your size. They're quick to apply for and often pay for work with a university or research institute. A computer-vision group could be a good fit for drawing recognition. In Ireland these are Enterprise Ireland's Innovation Vouchers and its R&D funding for established SMEs.
- **The big EU programs are possible but probably not the right first move.** The EIC Accelerator is open to bootstrapped companies. But it's very competitive, the process is long, and it wants a big "scale-up" story. A drawing-to-materials feature inside a scheduling tool will struggle to look that big. Eurostars requires a partner in another country.

**Cloud credits for Azure**

- **Microsoft for Startups (Founders Hub)** doesn't need an investor for the entry tier. Reports say it's about $1k at signup and up to about $5k after business verification. You'll need a company email domain and a live product. The large $100k–150k tiers generally need a referral from an investor in Microsoft's network, so as a bootstrapped company you probably won't reach them. Credits also run out. They help for a while but won't fix a bill that keeps growing.
- **Check whether you're already too far along.** Some offers exclude companies that already pay for Azure, or that have used credits before. Read the terms before you plan around the money.
- **Honestly, cost work may save you more than credits.** At €18k MRR, a "silly" Azure bill usually comes from a few big items. Common ones are oversized databases, always-on dev and test environments, and paying full price where reserved capacity or savings plans would be cheaper. An afternoon in Azure Cost Management often saves more per year than $5k of credits. If you send a rough breakdown of the bill, I can help you look for savings.

**To narrow this down, tell me:**
1. Which country is the company registered in, and where is your team?
2. Roughly what will the AI feature cost to build? Mostly your own salaries, or also outside help and compute?
3. About how big is the Azure bill per month, and what are the main costs?
4. Have you used any startup credits or received any public funding before?

With those answers I can give you a short list of specific programs, with deadlines and your realistic chances.

Sources (cloud credits): [Microsoft Founders Hub overview](https://guptadeepak.com/startup-offers/guides/microsoft-for-startups), [Impakter on Azure credits](https://impakter.com/free-azure-credits-for-your-startup-what-you-can-really-get/), [Klymentiev, April 2026](https://klymentiev.com/blog/microsoft-for-startups). These are third-party summaries that disagree in places. Confirm the current terms on Microsoft's own pages before applying.

## Founder, turn 2 (simulated)
1. Sweden, we're an AB in Gothenburg. Not sure about the team part beyond that. 2. We're hoping for roughly 1-2M SEK for the feature, not sure on the split between salaries and outside help. 3. Not sure off the top of my head. 4. We got an Almi innovation loan of 300k SEK in 2023, partly paid back. Not sure about credits.

## Assistant, turn 2
Thanks, that helps a lot. First, a correction: I guessed Ireland last time, so ignore the Irish programs and the 30% credit I mentioned. Sweden works differently. Here's how it looks for a Gothenburg AB.

**1. Lower employer contributions on R&D salaries (forskningsavdrag). Start here.**
This isn't a grant you compete for. If staff spend most of their working time on qualifying R&D, you pay less arbetsgivaravgift on their salaries. You claim it each month in your normal employer return to Skatteverket. Building a model that reads construction drawings and turns them into quantities is a strong candidate. Routine feature work around it is not.
- If most of your 1–2M SEK goes to your own developers' salaries, this probably gives you the most reliable money of anything here.
- The rules require proper records of who did R&D and for how many hours. Start keeping them now, before the work starts.
- I couldn't confirm this year's exact rate and monthly cap, and a reform has been proposed. Check the current rules on Skatteverket, or ask your accountant, before you count on a number.

**2. Vinnova grants: possible, but set expectations.**
- Vinnova usually covers at most about **50%** of a small company's project costs. For a 1–2M SEK project, that's roughly 0.5–1M SEK from Vinnova at best. You'd fund the rest yourselves.
- I found no open general "innovation project for SMEs" call right now. Vinnova runs themed calls that open and close. Check their list of open calls for anything on AI, digitalisation or construction.
- **ITEA** is software-focused and Vinnova co-funds the Swedish part. But it needs an international group of partners and takes a lot of admin. It's probably too heavy for a 4-person team unless a partner invites you in.
- Your project has a good angle for these funders. Drawings come in very different formats and quality, symbols aren't standardised, and a wrong material list costs real money. Make that the research problem you're solving.

**3. Almi.**
Your current innovation loan doesn't rule out more help. Almi Väst knows you, so they're an easy first conversation. They also know which regional programs in Västra Götaland are open right now. Ask them about a new innovation loan and any regional innovation funding.
One warning: most of these programs are state aid with limits on combined amounts. Keep a list of everything you've received (the 2023 Almi loan, any credits, any grants), because applications will ask for it.

**4. Cloud and compute.**
- **Microsoft for Startups**: the tier without an investor is about $5k in Azure credits. It's worth taking, but it won't fix a bill that keeps growing. Check whether earlier credits or your current Azure use disqualify you.
- **Training the drawing model**: if you need GPUs to train or fine-tune it, the Sweden AI Factory (Mimer in Linköping) offers compute to Swedish companies, including SMEs. Check their current terms and how to apply. It could keep the heavy work off your Azure bill.
- On the bill itself: when you get a minute, pull a breakdown by service from Azure Cost Management. A few line items usually explain most of it.

**Three things would sharpen this:**
1. Are all your developers employed by the AB in Sweden? This matters for the employer-contribution reduction.
2. Roughly how much of the 1–2M SEK would be your own salaries, and how much outside help or compute?
3. Roughly what the Azure bill is per month. A ballpark is fine.

With those, I can tell you which of these is worth doing first and what the next 2–3 months would look like.

Sources: [Vinnova ITEA 2026](https://www.vinnova.se/e/eureka-kluster-medfinansiering/internationella-projekt-inom-2026-02377), [Vinnova Test and Demo 2026](https://www.vinnova.se/en/calls-for-proposals/utlysning-2026-01600), [Vinnova Impact Innovation Start/Scale](https://www.vinnova.se/en/utlysningstextsidor/2023/2024-00343-impact-innovation-startscale---ett-erbjudande-till-sma-och-medelstora-foretag), [Fortnox on employer contributions 2026](https://www.fortnox.se/fortnox-foretagsguide/lon-och-loneadministration/arbetsgivaravgift-hur-mycket), [Government bill on raising the R&D cap](https://www.regeringen.se/contentassets/d94f5fd79907452ea106dcf60e0b2215/forstarkt-nedsattning-av-arbetsgivaravgifter-for-personer-som-arbetar-med-forskning-eller-utveckling.pdf), [BDO on the R&D deduction](https://www.bdo.se/getmedia/7670c232-090e-4f80-8050-a0c2dd256f0f/Forskningsavdraget-mellan-praxis-och-politik.pdf), [Microsoft for Startups overview (third-party)](https://guptadeepak.com/startup-offers/guides/microsoft-for-startups)
