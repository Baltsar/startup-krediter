# q15 with-skill

## Founder, turn 1
We're a Helsinki based AI startup (Oy), closed a 2.5M EUR seed in spring led by a Nordic VC. We're spending heavily on inference, mostly AWS Bedrock and some OpenAI. What's the biggest stack of cloud/AI credits we can realistically get at this stage? We already used the AWS Activate founders tier ages ago. Also heard about some EuroHPC AI factory thing, is that for companies like us or just universities?

## Assistant, turn 1
The biggest stack you can realistically get is AWS Activate Portfolio, up to $200,000 in credits. It goes through an Activate Provider, which can be a VC, so your lead investor decides it. Having used the Founders tier before doesn't block you, because you'd be asking for more than you got then.

Is your lead VC an AWS Activate Provider, and can they give you an Org ID?

◐ AWS Activate Portfolio: up to $200,000 in AWS credits, pre-Series B. After that, AWS Credits for AI Startups gives $200,000+, by invitation through your account manager. Decides it: your VC is a Provider and confirms you. 9 application requirements, 3 unclear points.
◐ OpenAI for Startups: API credits, amount not published, only through a partner VC. Decides it: your VC is in OpenAI's network. I couldn't load their page today, so I can't confirm it's open. 3 requirements, 3 unclear points.
◐ LUMI AI Factory (Finland): free GPU compute for startups and SMEs, not just universities. It's for R&D and training. You can't use it to serve 24/7 or commercial inference. Decides it: under 250 staff. 5 requirements, 4 unclear points.

Credits pay your AWS and OpenAI bills. LUMI GPU hours pay for neither.

More doors: EuroHPC Playground (fixed GPU-hour grant, rolling, first come first served), NVIDIA Inception, Kiuas.

Which one do you want to look at? Then you get the full list of what the application requires.

## Founder, turn 2 (simulated)
Not sure honestly, don't know if they're an Activate Provider or if they can give us an Org ID. Can you tell me more about AWS Activate Portfolio?

## Assistant, turn 2
```
◐  AWS Activate Credits
●  uses AWS, or uses Anthropic
●  stage: idea, pre-seed, seed or series A
○  at most 10 years old
○  new to AWS Activate credits, or asking for more than you received before
?  How old is the company, in years?
→  Activate Founders (self-funded) up to 5 000 USD, starting at 1 000 USD; Activate Portfolio (pre-Series B, with an Activate Provider Org ID) up to 200 000 USD; AWS Credits for AI Startups 200 000 USD+ by invitation only
```

Activate Portfolio is AWS's credit tier for pre-Series B startups backed by an "Activate Provider": an accelerator, angel or VC firm that can give you an Organization ID. It's the one that fits you, with one condition. I read AWS's credits page today (17 October). It says Portfolio gives "up to $200,000", and the company must be founded in the last 10 years and be new to Activate credits or asking for more than before. You'd be asking for more than your Founders credits (that tier tops out at $5,000), so that rule shouldn't block you. AWS's providers page has no searchable list of VCs, so the only way to find out is to ask your lead investor.

**Before you apply**
- Your VC gives you an Org ID or an email invitation. They must also answer AWS's verification email confirming you're in their portfolio. If they don't, the application is declined.
- Your latest round has to be within the last 12 months. Your spring seed fits.
- An AWS Builder ID verified by email, and an Activate profile with a business email on your own domain.
- An AWS account on a paid plan, linked to the Builder ID with root or admin access. Free plans don't qualify.
- A company website that fully works. AWS checks public information on it.
- The form asks for product, target market, traction, funding stage and the date of your latest round.
- If AWS asks for an ID document, you must provide it. Declining means rejection.
- Credits are for AWS services only. They don't pay your OpenAI invoice. The credit terms exclude AWS Marketplace, Enterprise Support, and upfront fees for Savings Plans and Reserved Instances.
- Credits expire. The date is set when they're issued. They can't be transferred, but you can share them inside your own AWS Organization.
- Bedrock: AWS's Activate FAQ has said credits also cover third-party foundation models on Bedrock. The general credit terms I read today list Marketplace as excluded and don't mention Bedrock at all. If most of your spend is third-party models, have AWS confirm before you count on it.
- The tier above Portfolio, AWS Credits for AI Startups ($200,000+), is by invitation only, after Portfolio. You get there through your AWS account manager. Given your Bedrock spend, ask them about it now.

**Unclear**
- How much Portfolio actually gives you. "Up to $200,000" is a ceiling, and the real amount depends on your provider. Ask your VC what their Portfolio package gives.
- Review time: AWS pages say 5–10 or 7–10 business days. Ask AWS Activate support if timing matters.
- AWS's FAQ answer on why applications are declined is broken. Ask AWS Activate support if you're rejected.

**Next step:** email your lead partner with one question: "Are you an AWS Activate Provider, and can you give us an Org ID?" If they are, create or sign in to your Builder ID at https://aws.amazon.com/startups/join?destination=/credits/apply, choose Activate Portfolio, and enter the Org ID. Then describe the product and funding, link the AWS account and submit. If they're not, other investors or programs you're in (an accelerator, an angel) can also be providers. And while you're writing to your VC, ask whether they're in OpenAI's startup partner network too.

Do you want to see the next door, or answer the question above?
