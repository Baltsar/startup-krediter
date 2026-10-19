<h1 align="center">startup-krediter</h1>

<p align="center">
  <b>Check a Nordic grant, GPU program or credits program before you apply.</b><br>
  An AI skill that tells you whether you can apply, what the application will ask of you, and helps you write it.
</p>

<p align="center">
  <img alt="Status: beta, testers wanted" src="https://img.shields.io/badge/status-beta%20%C2%B7%20testers%20wanted-orange">
  <img alt="73 programs" src="https://img.shields.io/badge/programs-73-blue">
  <img alt="Languages: sv, en, fi, no, da" src="https://img.shields.io/badge/languages-sv%20%C2%B7%20en%20%C2%B7%20fi%20%C2%B7%20no%20%C2%B7%20da-blue">
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green">
</p>

<p align="center">
  <a href="#try-it">Try it</a> ·
  <a href="#what-you-get">What you get</a> ·
  <a href="#give-feedback">Give feedback</a> ·
  <a href="#how-good-is-it">How good is it</a> ·
  <a href="#coverage">Coverage</a>
</p>

---

## Try it

You need [Claude Code](https://claude.com/claude-code), git and Python 3.10 or later. Cursor and Codex should work too, but we have not tested them.

```bash
git clone -b feature/rebuild https://github.com/Baltsar/startup-krediter.git
cd startup-krediter && sh bootstrap.sh
```

Then ask your assistant about a program you are actually considering, in your own language:

```text
Vi vill söka Vinnovas Innovativa startups. Svenskt AB, två år, fyra personer. Vad behöver vi ha klart?
```

<details>
<summary>More examples</summary>

- *Haemme Business Finlandin Sprint-rahoitusta. Suomalainen Oy, pre-seed. Mitä hakemukseen tarvitaan?*
- *Kan vi søke Oppstartstilskudd 1? Norsk AS, ett år gammelt.*
- *Vi vil søge Innobooster. Dansk ApS, 2 år, 6 ansatte. Hvad kræver det?*
- *Help us apply for AWS Activate credits. Swedish AB, angel-funded, building on Bedrock.*

You can also type `/startup-krediter`.

</details>

## What you get

| | |
|---|---|
| **A straight answer** | Whether you can apply, and the few questions about your company that decide it. |
| **The full checklist** | Everything the application will ask of you: login, attachments, co-financing, deadline, how the money is paid. Read from the program's own pages, today. |
| **Help writing it** | Section by section, in the form's order and limits, with the budget in the program's template. You log in and press submit. It never does. |

Example, shortened:

```text
◐  Vinnova Innovativa Startups 2026
●  in Sweden
●  a company
●  at most 10 years old
○  the project lead employed by the company
○  not lost more than half the share capital
?  Net revenue last fiscal year, in MSEK?
→  Up to 500 000 SEK
```

`●` met · `○` not known yet · `×` rules you out · `?` the next question

## Give feedback

Try it on a real program, then tell us:

1. Did it catch something you would have missed?
2. Was anything wrong, outdated or missing?
3. Would you use it again?

**[Give feedback →](https://github.com/Baltsar/startup-krediter/issues/new?title=Feedback%3A%20&body=%2A%2AProgram%20I%20tested%3A%2A%2A%0A%0A%2A%2AWhat%20I%20asked%20%28paste%20or%20summarise%29%3A%2A%2A%0A%0A%2A%2ADid%20it%20catch%20something%20I%20would%20have%20missed%3F%2A%2A%0A%0A%2A%2AAnything%20wrong%2C%20outdated%20or%20missing%3F%2A%2A%0A%0A%2A%2AWould%20I%20use%20it%20again%3F%20Why%2C%20or%20why%20not%3F%2A%2A%0A)** It takes two minutes. You can also comment on [the pull request](https://github.com/Baltsar/startup-krediter/pull/2).

## How good is it

We test every version against the same AI with web search and no skill. Each round uses new founder questions, and graders who don't know which answer is which check both against the programs' official pages. Latest round, 19 October 2026, 15 questions:

| | With the skill | Without |
|---|:---:|:---:|
| Requirements that can stop an application, named before you apply | **89%** | 77% |
| Factual errors | **5** | 8 |
| Length of the first answer (median words) | **416** | 626 |
| Better answer overall | 9 of 15 | 6 of 15 |

It is more complete and more accurate, but not yet clearly better: it still asks too little about your own situation, such as who owns the company or how big the project is. That is why we want testers. [Full report and every conversation →](docs/benchmark/2026-10-19-round5/README.md)

## Coverage

73 programs, each read from its own pages between 15 and 18 October 2026.

| You need | Programs include |
|---|---|
| **Grants and loans** | Vinnova, Almi, Energimyndigheten, EIC Accelerator, Eurostars, Innovasjon Norge, SkatteFUNN, Business Finland, Finnvera, InnoFounder, Innobooster, Rannís |
| **GPU and compute** | EuroHPC Playground, Fast Lane, Sweden AI Factory, LUMI, Sigma2, NAISS, Berzelius |
| **Cloud and AI credits** | AWS Activate, Google for Startups, Microsoft for Startups, Claude Startups, OpenAI for Startups, NVIDIA Inception, Modal, Vercel |
| **Accelerators** | Sting, Norrsken, Antler, Accelerace, Kiuas, KTH Innovation, Chalmers Ventures |

| Sweden | EU-wide | Global | Finland | Norway | Denmark | Iceland |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 29 | 14 | 14 | 7 | 5 | 3 | 1 |

A program that is not in the list still works: the skill reads its official pages instead.

## Good to know

- **It checks a program you have chosen.** It does not pick one for you.
- **It reads the live page** before it quotes a date or an amount, and says so when a page cannot be read.
- **It never logs in, signs or submits.** That stays with you.
- **Not financial or legal advice.** The program decides.

## Add a program

Not a developer? [Open an issue](https://github.com/Baltsar/startup-krediter/issues/new) with the program's name, link and country.

Developer? Each program is one record in `data/programs.json`; its rules are data, not code. See the shape in `data/schema.json`, then run:

```bash
python3 scripts/validate.py && uv run --with pytest pytest tests/ -q
```

<details>
<summary>How it works</summary>

- `SKILL.md` tells the assistant how to read the chat, which questions to ask, when to read the live page, and how to answer.
- `scripts/match.py` finds a program by name (`--find`) and checks it against your company (`--door`): every rule met, open or failed, and the checklist. Standard library only.
- `references/*.md` hold longer notes per area; `references/applying.md` covers writing the application.
- `docs/benchmark/` holds every test round: the plan, the questions, all conversations and the grades.

```bash
python3 scripts/match.py --find "innovativa startups"
echo '{"country":"SE","legal_form":"company","age_years":2,"employees":4,"lang":"en"}' \
  | python3 scripts/match.py --door vinnova-innovativa-startups
```

</details>

---

<p align="center">MIT licensed · Made by <a href="https://opensverige.se">OpenSverige</a>, Sweden's open community for AI agents</p>
