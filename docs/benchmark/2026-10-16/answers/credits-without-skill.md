TURN 1:
Short answer: with an angel round and no VC, you can count on two things right now. One is AWS Activate credits, which you can spend on Claude through Amazon Bedrock. The other is Microsoft's self-serve credits. The direct programs for your actual stack (Anthropic, Vercel, Supabase) are closed to you, gated behind a VC partner, or unclear.

**Most realistic**

1. **AWS Activate, spent on Claude through Amazon Bedrock.** AWS says Activate credits can pay for third-party models on Bedrock, Anthropic included. So AWS credits can cover your biggest variable cost.
   - **Founders tier:** starts at $1,000, up to $5,000 for selected companies. You apply yourself, no investor needed. AWS describes it as for "bootstrapped or self-funded" startups, and it doesn't say whether an angel round rules you out.
   - **Portfolio tier:** up to $200,000. It needs an Org ID from an "Activate Provider", and AWS lists angel investors as possible providers. Ask your angels, or any syndicate or angel network they invest through, whether they have one.
   - **Other requirements:** pre-Series B, founded within 10 years, an AWS account on a paid plan, and no Activate credits before.
2. **Microsoft for Startups (Founders Hub).** The entry tier is self-serve, no investor needed, worth roughly $1,000 to $5,000 in Azure credits. Higher tiers come through use or a partner referral. Only useful if you'd actually run something on Azure. Some founders report activation problems tied to account type, so sign up with a work account.

**Possible, but check first**

3. **Google for Startups Cloud.** The AI tier is reported at up to $350,000, but third-party sources say it needs a VC or institutional investor, and one says angel-only funding is excluded. There's usually a smaller tier for unfunded startups. Credits could cover Claude on Vertex AI. I couldn't read Google's own terms, so check them.
4. **Vercel for Startups.** Up to $30,000 for one year, at most 50% of it on AI Gateway. You must be affiliated with an approved Vercel partner (accelerator or VC) and apply within 12 months of your latest round. Without a partner you don't qualify today. Your angels can ask Vercel to add them as a partner at vercel.com/startups/partners.
5. **Supabase.** Third-party sites mention offers worth $300 to $3,000. I couldn't find an official startup credits page, so don't plan around it. Ask Supabase sales directly.

**Not available right now**

- **Anthropic (Claude for Startups):** applications are closed ("current cohort is now full"). Join the newsletter to hear when the next cohort opens. The bigger API credits (up to $100k) only go through Anthropic's partner VCs.
- **OpenAI:** credits seem to come only through partner VCs. And it isn't your stack anyway.

**What I'd do this week:** ask your angels whether any of them is an AWS Activate Provider or a Vercel partner. That single question decides whether you're at $1–5k or $100k+. In parallel, apply to AWS Activate Founders and Microsoft Founders Hub, and sign up for Anthropic's startup newsletter.

Separately, since you're a Swedish AB: Vinnova and Almi offer grants and loans, not credits. Ask me if you want those covered too.

Amounts and criteria change often, so confirm on each official page before applying: [Claude for Startups](https://claude.com/programs/startups), [Vercel](https://vercel.com/startups/credits), [AWS Activate](https://aws.amazon.com/startups/credits), [AWS: Activate credits for Bedrock models](https://aws.amazon.com/blogs/startups/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/), [Google for Startups](https://cloud.google.com/startup), [Microsoft guide (third party)](https://guptadeepak.com/startup-offers/guides/microsoft-for-startups).

TURN 2:
**AWS Activate, used to pay for Claude**

**Why it fits you:** you're building on Anthropic, and Activate credits can be spent on Anthropic's models through Amazon Bedrock. Credits that would otherwise go to EC2 you'll never use end up paying for model calls.

**The two tiers**

| | Founders | Portfolio |
|---|---|---|
| Amount | Starts at $1,000, up to $5,000 for selected companies | Up to $200,000 |
| How | Apply yourself | Needs an Org ID from an Activate Provider (VC, accelerator, or angel investor) |
| Fits you if | You have no provider connection | One of your angels, or their syndicate or network, is a provider |

**Shared requirements:** pre-Series B, founded within 10 years, an AWS account on a paid plan, and no Activate credits before. Both tiers require a company website and an email address on that domain.

**The open question for you:** AWS describes Founders as for "bootstrapped or self-funded" startups. It doesn't say whether an angel round counts against you. In practice, apply honestly and describe the round as an angel round with no institutional investor. If AWS says no, you've lost nothing.

**Steps**
1. Ask your angels whether any of them has an AWS Activate Provider Org ID. If yes, go for Portfolio. That's the difference between $1k and up to $200k.
2. Create an AWS account for the AB, using a company email, and move it to a paid plan.
3. Apply at aws.amazon.com/startups/credits.
4. Once approved, turn on Claude models in Amazon Bedrock and check that usage draws down the credits on your first invoice.

**Practical caveats**
- **Code changes:** you'd call Claude through the Bedrock API, not Anthropic's own API. With the Anthropic SDK that's mostly a client swap (`AnthropicBedrock`) plus AWS auth, but model IDs and feature timing can differ. New features sometimes land on the first-party API first.
- **Region and quotas:** pick a region where the Claude models you need are available, such as an EU region if data residency matters. Expect low default rate limits. Request quota increases early, before you go to production.
- **Credits expire.** Check the expiry date and time the application for when you'll actually have usage.
- **Bedrock billing:** some founders on forums report errors at the Marketplace subscription step for Anthropic models on Bedrock. Do a small test call before you plan your budget around the credits.

**Bottom line:** Founders is a quick, cheap win of $1–5k. The real money ($100k+) depends on whether someone in your round is an Activate Provider, so ask them that first.

Sources: [AWS Activate](https://aws.amazon.com/startups/credits), [AWS: Activate credits for Bedrock models](https://aws.amazon.com/blogs/startups/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/), [AWS application guide](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/), [forum report on Bedrock billing](https://www.repost.aws/questions/QUGBeWfZc-R-Sc9n49TzmysA/has-anyone-with-an-aws-india-aispl-account-successfully-subscribed-to-anthropic-claude-on-amazon-bedrock-using-aws-activate-credits).