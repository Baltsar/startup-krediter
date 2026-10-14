# startup-krediter

A skill for a builder in Sweden or the Nordics who asks if they have a chance. It checks one door. It does not quote a percentage. It does not submit the application.

`/startup-krediter` loads it. So does Sweden AI Factory, EuroHPC, Playground, Fast Lane, Vinnova, NVIDIA Inception, Claude Startups, AWS Activate, GPU hours, or "do we have a chance".

## Sweden AI Factory

Sweden AI Factory does not hand out GPU hours by email. The email asks them which call to use. The skill writes that draft. It does not send it. Address: `info@swedenaifactory.se`.

The GPU call for a Swedish company is EuroHPC Playground, on the factory's machines. Playground is open, permanent, industry only. Eligibility check, then a technical assessment of one system, then first come, first served until the reserved hours run out. The same terms also say innovation can decide the last allocation. Both sentences stay. The form is behind an account. Registration has a captcha. The skill does not solve the captcha and does not click Register.

Fast Lane is the sibling industrial call in the same terms: also rolling, also eligibility plus technical assessment. Large Scale is the scored call. Innovation and impact are scored there, not in the Playground section. Academia and the public sector belong in EuroHPC AI for Science, not in Playground.

RISE has no application form. Paid GPU is ICE Connect, or an invoice from Berget, ICE, or Stormgrid. Hyperight, Agorify, HP, Bull, Consumeit, and Aderian are booths at Nordic AI Factory Summit 2026. A booth is not a call.

## The catch

Free GPU, a grant, and a cloud-credit program are three doors. GPU time does not pay the API invoice.

Nothing here has a submit API. `submit` is `no`. A portal needs the account owner's login. The last click stays with them.

## Money

| Country | Door | What the page says |
|---|---|---|
| Sweden | Vinnova Innovativa Startups | Swedish page: up to SEK 500,000, decision 23 March 2027. Low scores are rejected. Very high scores are granted. High and equal scores are drawn by lot. English page: same cap, and a line that the full assessment text is published when the call opens. A March 2026 slide deck says scores of 0–5, a ranked total, and an opening on 1 September. Do not pick. |
| Norway | Oppstartstilskudd 1 | Up to NOK 150,000. The 2026 assignment letter targets companies up to three years old, five in an exception. |
| Norway | Startup grant 2 | Up to NOK 1 million. The 2026 pot is cut by 60 percent. More applications are rejected. |
| Finland | Business Finland | Young-company funding. GPU time is LUMI, not this grant. |
| Finland | Sprint Grant | Continuous from 1 September 2026. EUR 75,000–100,000, after a meeting with an officer. |
| Finland | Deep Tech Accelerator | At most six companies. The 2026 window closed 16 August. |
| Denmark | Innofounder | Spring round closed 17 February 2026. Autumn round closed 25 August 2026 at 12:00. Final grant or rejection is expected in mid-December 2026. |
| Iceland | Fræ | Open year-round at Rannís, on the skill's last read. A different call, Icelandic Research Fund Startup grants for postdocs, closed 15 June 2026. |

No named award list for the 2026 Vinnova round exists yet. The decision date is 23 March 2027. The last named cohort is Vinnova's own October 2025 note: 103 companies, more than SEK 50 million. That sits outside this six-month window.

Almi is named, and the map says it has no coded call. Fetch Almi’s own page before quoting an amount.

## GPU by country

| Country | Door |
|---|---|
| Sweden | EuroHPC Playground. Sweden AI Factory only points at the call. |
| Finland | LUMI, national track. Consortium country. |
| Norway | KI-fabrikken at Sigma2. The machine is Olivia. |
| Denmark | LUMI consortium. The national grant name is not on the page. Do not guess it. |
| Iceland | EuroHPC. Iceland is a LUMI antenna, not a consortium country. No national GPU pot on that page. |

## Credits

Credits sit with the vendor. No stack, no answer. The short map is AWS Activate, Cloudflare for Startups, Neon, Google for Startups Cloud, Microsoft for Startups, and Claude Startups.

Claude Startups, as of 13 October 2026: the cohort is full. No new applications. Fetch the page again before saying it is open. Partner stack up to USD 45,000. A partner VC can add up to USD 100,000 in API credits. The expansion article also says up to USD 7,000 in Claude products, of which USD 1,000 is API credit. Credits apply to the Claude Console, not Bedrock or Vertex.

NVIDIA Inception: incorporated, under 10 years, one developer, a website, a work email on your own domain. No published credit amount. The public page has one field, Business Email. The rest is behind Sign Up / Login.

An OpenAI invoice matches nothing in the map.

## Install

```bash
git clone https://github.com/Baltsar/startup-krediter.git
cd startup-krediter
sh bootstrap.sh
```

That links this directory into Cursor, Claude, Codex, and the shared agent skills folder. Python 3. No packages.

## Run

Chance, one door:

```bash
echo '{"view":"chance","need":"gpu","legal_form":"ab","country":"SE","age_years":2,"employees":4}' | python3 match.py
```

`●` met. `×` closes the door. `○` unknown. `?` the only question, the first unknown requirement. `→` what they did not ask.

Every door:

```bash
echo '{"view":"matrix","legal_form":"ab","country":"SE"}' | python3 match.py
```

The packet, once the profile is filled. Every list stops before send:

```bash
echo '{"view":"packet","legal_form":"ab","country":"SE","age_years":2,"employees":4}' | python3 match.py
```

Use only what the chat already said. Do not guess age, headcount, revenue, VAT, or employment. If the country is missing, ask. Do not guess Sweden.

A human map: https://opensverige.se/blogg/startup-krediter-gpu-sverige

MIT. Copyright 2026 OpenSverige.
