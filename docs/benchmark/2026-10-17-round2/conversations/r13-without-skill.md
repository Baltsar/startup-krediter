# r13 without-skill

## Founder, turn 1
Founder here, we're an AS registered in Trondheim but half our team (3 people) sits in Linköping. We build counter-drone detection software (passive RF + vision), dual-use but mainly defence customers. Raised NOK 12M pre-seed last year. Need GPU for training on ~40TB of sensor data and want to know what Nordic/EU defence money we can go after. Our swedish devs are contractors via their own firmor if that matters

## Assistant, turn 1
Short version: Norway should be your home base for funding. Your Swedish setup affects Swedish programmes and export control more than anything else. Several of the big 2026 deadlines have already passed, so this is mostly about getting ready for the 2027 rounds.

**Defence money you can realistically go after**

1. **EIC Accelerator (EU), now open to dual-use.** Since mid-2026 the EIC accepts dual-use companies, meaning a credible business in both civilian and defence markets. It offers a grant of up to €2.5M, plus optional equity. As a Norwegian AS you can apply, because Norway is associated with Horizon Europe. Pitch the civilian side seriously: airports, prisons, energy sites. If you pitch as defence-only, I'm not sure you qualify. Check the current cut-off dates on the EIC site. The separate EIC STEP Defence call (deadline 28 Oct, €10–30M equity) is for companies raising €50M+ rounds, so it's not for you yet.
2. **NATO DIANA.** Norway and Sweden are both members. Two of the six 2027 challenges fit you almost exactly: "Multidomain Sensing… for Intelligence and Surveillance" and "Scalable and Adaptable Countermeasures for Air Defence". That call closed on 3 July 2026, so aim for the 2028 call, which will probably open around June 2027. It pays €100k in the accelerator, with more possible later. The rule that matters for you: the company must be majority owned and controlled by nationals of NATO countries. Check your cap table.
3. **European Defence Fund (EDF), including the SME open calls run through EUDIS.** Norway takes part through the EEA. There are non-thematic SME calls of up to €4M for research and €6M for development, plus thematic calls. In practice you join a consortium of at least three entities from three countries. The 2026 deadline was late September. Start lining up partners now, such as a Nordic prime or FFI/FOI, for the 2027 work programme. EDF also checks for control by non-EU/EEA owners.
4. **Norwegian national routes:**
   - **LINC.** Innovasjon Norge, FFI and NADIC's defence launchpad. The 2026/27 cohort started in August, so apply for the next intake.
   - **Brave-Norway.** A €20M Norway–Ukraine programme run by FFI and Brave1, focused on unmanned systems. Counter-drone is right in its focus.
   - **SkatteFUNN** for the R&D tax deduction, plus Innovasjon Norge grants. Bought-in R&D from the Swedish contractors' firms can usually be included as purchased services.
5. **Sweden: mostly closed to you as you're set up today.** Vinnova and the Swedish Armed Forces run a civil-military call worth up to SEK 1M plus an accelerator. It requires a Swedish AB that does business in Sweden, and contractors billing through their own firms don't make you eligible. That 2027 round closed on 6 Oct anyway. A Swedish subsidiary would open these doors, as well as FMV's counter-drone procurements, which are growing fast (Sweden announced roughly €800M for air and drone defence in April). Don't set one up only for grants, though. It brings tax and permanent-establishment questions.

**GPU for ~40 TB of sensor data**

Answer the data question before the compute question. What are you legally allowed to put where?
- **Export control.** Passive RF counter-UAS signatures and models may fall under military-list or dual-use controls. Your Linköping contractors working on that data could also count as an export from Norway that needs a licence. Clarify this with DEKSA/the Ministry of Foreign Affairs and your customers before you choose a cloud.
- **Public EuroHPC/national machines.** These are Olivia (Sigma2's AI Factory, now open to industry), LUMI and Sweden's AI Factory. Access is free or cheap, but the terms are written for open research. I couldn't find their rules on defence use or controlled data, so don't put customer data there without written confirmation. They're fine for non-sensitive pre-training.
- **Commercial Nordic GPU clouds or US hyperscaler credits.** AWS, Google, Microsoft and NVIDIA Inception run startup programmes. They're fine for unclassified, non-controlled data. Many defence customers will still ask for EU/Nordic sovereign hosting.
- **Sizing.** 40 TB is manageable. For RF plus vision models, a few H100/H200-class GPUs for a few months is probably enough. Storage and data movement will likely cost you more than the compute. Owning a small on-prem cluster is worth pricing if your customers require air-gapped data.

**What I need from you to narrow this down:**
1. Who owns the cap table? Is everyone from NATO or the EU/EEA, or are there investors from elsewhere?
2. Has any of your data or tech been classified for export control, or come from a customer under restrictions?
3. How mature is it? Is it already in field trials (TRL), and do you have a civilian customer or pilot?
4. Would you consider a Swedish AB, or employing the Linköping people properly?

Sources: [DIANA 2027 challenges](https://www.diana.nato.int/connect/nato-diana-unveils-six-new-challenges-to-tackle-evolving-defence-and-security-needs.html) · [EIC dual-use expansion](https://www.openaccessgovernment.org/eu-innovation-fund-expands-into-defence-and-dual-use-technologies/210715/) · [EIC STEP Defence (PNO)](https://www.pnoinnovation.com/fr/points-de-vue/eic-step-scale-up-defence-2026/) · [EUDIS SME calls](https://eudis.europa.eu/eudis-tracks/sme-calls_en) · [EDF 2026 deadline](https://www.hezelburcht.com/en/news/european-defence-fund-edf-2026-open-for-applications-until-29-september/) · [Vinnova civil-military 2027](https://www.vinnova.se/en/calls-for-proposals/civil-military-synergies/acceleration-of-civil-military-innovations-2027) · [LINC](https://www.innovasjonnorge.no/en/tjeneste/linc-launchpad-for-innovative-norwegian-companies) · [Brave-Norway](https://www.kmu.gov.ua/en/news/mintsyfry-ukrainski-ta-norvezki-defence-tech-startapy-otrymaiut-20-mln-ievro-na-rozvytok-tekhnolohii) · [Olivia GPU expansion](https://www.sigma2.no/node/407) · [Sweden drone defence investment](https://www.euronews.com/video/2026/04/02/sweden-announces-800-million-investment-in-air-and-drone-defence-systems)

## Founder, turn 2 (simulated)
1. Norwegian angels plus a Nordic defence-focused VC. 2. Not sure. 3. We have a paid pilot with a Norwegian defence procurement customer, not sure about TRL or a civilian pilot. 4. Not sure.

## Assistant, turn 2
Thanks, that helps. Two of your answers make things easier. One "not sure" needs sorting before anything else.

**What your answers change**

- **Ownership is fine.** Norwegian angels plus a Nordic VC meets DIANA's rule that the company is majority owned by NATO nationals. It should also pass EDF's control check. The one thing to confirm: no investor outside the EU/EEA/NATO has special rights, such as a veto or board control.
- **The paid pilot is your biggest asset.** A paying Norwegian defence procurement customer means you're likely around TRL 6–7, depending on whether the system has been tested in a realistic environment. That's exactly the range DIANA and the EDF development calls fund. Ask your customer contact to confirm the TRL in writing. It's worth a lot in applications.
- **No civilian pilot is the gap for the EIC.** The EIC Accelerator only funds dual-use companies, and without a civilian customer you'll look defence-only. Try to get one letter of intent from a civilian site. Airports (Avinor), the power grid (Statnett), offshore operators and prisons all have real drone problems. A single LOI is enough to make the EIC application credible.

**The thing to sort out first: export control**

This is the "not sure" that matters most, for three reasons:
1. It decides where you can train on the 40 TB.
2. It affects the Linköping team. The Norwegian technology guidance (UD, August 2025) has exemptions for technology transfers *inside Norway* to EU/EEA/NATO nationals. Developers sitting in Sweden are a transfer *out of* Norway. If your RF signatures or models are controlled, that may need a licence from DEKSA (Direktoratet for eksportkontroll og sanksjoner).
3. EDF and defence customers will ask about it.

What to do:
- Ask your pilot customer how they classify the pilot data and the system. They often already know.
- Read [UD's technology export guidance](https://www.regjeringen.no/contentassets/ca0e63363cc54c448928ed14e6726445/veileder-for-eksport-av-teknologi-august-2025-utenriksdepartementet.pdf) and contact DEKSA if anything is unclear.
- Check the pilot contract's clauses on security and data handling.

**GPU, once you know the classification**

- **Not controlled and not customer-restricted:** apply to Sigma2's AI Factory (Olivia), which is now open to industry. Hyperscaler startup credits also work.
- **Controlled or restricted:** use a Norwegian sovereign provider or a small on-prem cluster. With your customer's rules, the second is often simplest.
- **Until then:** train only on data you collected yourselves that isn't sensitive.

**The Swedish team (your question 4)**

Don't set up a Swedish AB just for grants. Two things matter more right now:
- Get the contractors covered by the export-control check above.
- Make sure their contracts give you the IP.

Revisit a Swedish entity only if FMV or the Swedish Armed Forces become a real sales target. That's when Vinnova's civil-military calls open up as well.

**Suggested order**

1. **Now:** clarify export control with the customer and DEKSA. Contact Innovasjon Norge about the next LINC intake and Brave-Norway.
2. **Now:** apply for SkatteFUNN for 2027 if you haven't already. The contractors' R&D can usually be included as purchased services.
3. **This winter:** get a civilian LOI, then submit a short proposal to the EIC Accelerator.
4. **Spring 2027:** use the customer's network (FFI, primes) to build an EDF consortium for the 2027 calls.
5. **About June 2027:** apply to the next DIANA call, under sensing or counter air defence.

Two quick questions: is the pilot customer Forsvarsmateriell or a branch of the armed forces directly? And is the pilot data recorded on your own sensors, or does it come from the customer?

Sources: [UD technology export guidance 2025](https://www.regjeringen.no/contentassets/ca0e63363cc54c448928ed14e6726445/veileder-for-eksport-av-teknologi-august-2025-utenriksdepartementet.pdf) · [SNL: Eksportkontroll / DEKSA](https://snl.no/eksportkontroll) · [DIANA 2027 challenges](https://www.diana.nato.int/connect/nato-diana-unveils-six-new-challenges-to-tackle-evolving-defence-and-security-needs.html) · [EIC dual-use expansion](https://www.openaccessgovernment.org/eu-innovation-fund-expands-into-defence-and-dual-use-technologies/210715/) · [LINC](https://www.innovasjonnorge.no/en/tjeneste/linc-launchpad-for-innovative-norwegian-companies) · [Olivia / AI Factory](https://www.sigma2.no/node/407)
