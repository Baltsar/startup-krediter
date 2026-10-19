# r08 with-skill

## Founder, turn 1
Hei! saisko meidän startup ilmasta GPU-aikaa LUMI:lta sen AI Factoryn kautta? tarvittais n. 30 000 GPU-tuntia suomenkielisen puhemallin fine-tuneen. mitä hakemukseen tarvii ja kuinka nopeesti pääsee alkuun? pari meidän tyyppiä on käyttäny LUMIa väikkärin aikana joten slurm on tuttu

## Assistant, turn 1
Hei! Ensin pieni korjaus: LUMI AI Factory ei itse myönnä GPU-tunteja. Se neuvoo ilmaiseksi, ja tunnit haetaan EuroHPC:n kutsusta tai Business Finlandin laskentatuesta. 30 000 GPU-tuntia mahtuu EuroHPC:n Fast Lane -hakuun: LUMI-G:llä 10 000–50 000 tuntia, 1–3 kk. Fast Lane on auki yrityksille koko EU:sta; vain Business Finlandin reitti ja maksullinen pääsy ovat suomalaisille. Startupille laskenta on ilmaista T&K-käyttöön, jos alla olevat asiat täyttyvät.

Nopeus: LUMI AI Factoryn sivun mukaan ensikontaktista pääsee töihin jo 2–5 päivässä, yleensä pienellä pilotilla. Ne 30 000 tuntia tulevat erillisestä Fast Lane -hakemuksesta, jolle Fast Lane -sivu ilmoittaa pääsyn 4 työpäivässä. Sen voi jättää suoraan portaaliin. Tunnit jaetaan saapumisjärjestyksessä, kunnes kutsun resurssit loppuvat.

**Mikä ratkaisee**

1. Onko teillä jo rekisteröity yhtiö, ja missä maassa? Yksityishenkilöt ja tilapäiset tiimit eivät saa ilmaista palvelua.
2. Oletteko nyt opiskelijoita, tutkijoita tai töissä yliopistossa? Yliopiston IPR-säännöt voivat koskea teitä.

**Tilanne**

```
◐  LUMI AI Factory (Finnish national track)
○  Suomessa
○  yhtiö
○  alle 250 työntekijää
?  Missä maassa yhtiö on rekisteröity, tai mihin se rekisteröidään?
→  Määrää ei julkaista sivulla; aloitetaan pienellä laskentapilotilla, ja tiimi arvioi tarvittavat resurssit
```

**Ennen hakemista**

- Yhteydenottolomake: tiedustelun tyyppi, nimi, sähköposti, yritys, organisaatiotyyppi, maa, toimiala, viesti, tietosuojahyväksyntä.
- LUMI-tiimi arvioi idean toteutettavuuden, riskit ja resurssitarpeen ennen kuin haette tunteja.
- Tunnit haette itse EuroHPC:n portaalissa, tili yrityksen omalla työsähköpostilla.
- Fast Lane: jatkuvasti auki, ei määräpäivää (sivu tänään); yksi järjestelmä.
- Hakemus englanniksi; ALV-numero, PIC jos on; siviilikäyttö ja AI Act itsearvioinnissa.
- Tarkistakaa: projektin vetäjällä työsopimus yhtiöön vielä 3 kk allokaation päättymisen jälkeen.
- Tekninen arvio ratkaisee: näyttäkää, että fine-tune-koodi toimii LUMI-G:n AMD-GPU:illa.
- Ei jatkoaikaa eikä lisätunteja; yksi Fast Lane -allokaatio per vetäjä kerrallaan.
- Malli ja data jäävät teille, ja startup saa käyttää niitä kaupallisesti.
- Jälkeenpäin loppuraportti 3 kk:ssa, EuroHPC voi julkaista sen vuoden päästä.
- Business Finlandin laskentatuki: vain BF:n t&k-projektiin, laskentakulut yli 15 000 EUR, enintään 100 000 EUR.
- Kansallinen reitti on valtiontukea: tarkistakaa jäljellä oleva tila, enintään 300 000 EUR / 3 v.
- Puhedata: LUMI ei salaa levossa automaattisesti eikä varmuuskopioi; poisto 90 pv projektin jälkeen.

**Epäselvää**

- Julkaisuvelvoite: ehdot sanovat tulokset, FAQ lyhyen raportin. Kysykää aif.access@eurohpc-ju.europa.eu.
- LUMIn laskutuksessa GPU-tunti on MI250X-moduuli (2 GCD); laskeeko arvionne samoin? Kysykää LUMI AI Factorylta.
- Saako startup ilmaista kansallista laskentaa ilman BF:n t&k-rahoitusta, ei kerrota; kysykää Business Finlandilta.
- 300 000 EUR:n valtiontukiraja ja 100 000 EUR:n laskentatuen maksimi ovat eri rajoja; kysykää BF:ltä.
- Maksullinen pääsy (ei julkaisuvelvoitetta) on suomalaisille; hintoja ei sivulla, kysykää CSC:ltä.

**Seuraava askel**

Täyttäkää LUMI AI Factoryn lomake (tyyppi "Powerful AI Computing"): puhemalli, 30 000 GPU-tuntia, aikataulu. Tiimi ehdottaa reitin ja pilotin; lähetysnapin painatte itse. https://lumi-ai-factory.eu/contact/

Voin kirjoittaa viestin ja Fast Lane -hakemuksen kanssanne, kun vastaatte noihin kahteen kysymykseen.

## Founder, turn 2
kiitos! vastaukset:

1. joo, Puhekaari Oy, rekisteröity kaupparekisteriin 10.1.2024, Suomessa (Tampere).
2. CTO opettaa 10 % dosenttina Tampereen yliopistolla. muut ei oo tällä hetkellä opiskelijoita, tutkijoita eikä yliopistolla töissä.

ja joo, kirjoitetaan yhdessä. tässä mitä meillä on valmiina:

Puhekaari Oy, Tampere. 12 henkeä. Malli: suomenkielinen puheentunnistus ja -synteesi suoratoistopalveluun. Data: n. 8 000 h lisensoitua yleisradiopuhetta + Common Voice. Tarve: 30 000 GPU-tuntia yhdellä koneella, 2-3 kk.

## Assistant, turn 2
Joo, kirjoitetaan: alla on LUMI AI Factoryn lomakeviesti ja Fast Lane -hakemuksen tekstit kenttä kentältä, valmiina liitettäviksi. Portaaliin rekisteröidytte itse yhtiön sähköpostilla ja ratkaisette reCAPTCHAn, ruksaatte itsearvioinnit ja painatte Submit; LUMIn lomakkeella ruksaatte tietosuojan ja painatte Send.

**Mitä vastauksenne ratkaisivat**

- Puhekaari Oy, Suomi, 12 henkeä: LUMI AI Factoryn ilmaisten palvelujen yhtiöehdot täyttyvät. Idea arvioidaan vielä teknisesti.
- Muut eivät ole yliopistolla, joten IPR-kysymys koskee vain CTO:ta.
- CTO:n 10 % dosentuuri ei ole este: Fast Lanen ehdot vaativat vetäjältä työsuhteen hakijayhtiöön, eivätkä sano yliopistotyöstä mitään.
- Käyttäkää hakemuksessa Puhekaaren nimeä ja sähköpostia, ja pitäkää mallityö ja data erillään yliopistotyöstä.

**Korjaus edelliseen viestiini**

- Fast Lane -sivulla on tänään vain yläraja, 50 000 GPU-tuntia. LUMI-G:n alarajaa en löytänyt.
- Sivun mukaan määräpäiviä ei ole, mutta portaalin 2026-kutsu (/calls/59) sulkeutuu 31.12.2026 klo 22:59 UTC.
- Sivun Apply Now -nappi vie suljettuun 2025-kutsuun (/calls/49). Hakekaa /calls/59:ssä.
- Viime vuodenvaihteessa kutsu sulkeutui 31.12. ja seuraava avautui 21.1.2026. Vuoden 2027 kutsua ei vielä ole.

**Fast Lane: tilanne**

```
◐  EuroHPC AI Factories Fast Lane Access
●  yhtiö
○  työsuhteessa oleva projektipäällikkö allokaation jälkeen
○  ALV-rekisterissä
○  sähköposti omassa verkkotunnuksessa
○  työkuorma määritelty: koodi, yksi järjestelmä, GPU-tunnit
○  tiimi ajaa jo koodiaan HPC-järjestelmässä
?  Onko projektipäällikkö työsuhteessa vähintään kolme kuukautta allokaation päättymisen jälkeen?
→  Enintään 50 000 GPU-tuntia, 1–3 kk, yksi järjestelmä
```

**Tarvitsen vielä nämä**

1. Kuka on vetäjä? Onko hänellä työsopimus Puhekaaren kanssa 3 kk allokaation jälkeen (tammi–maaliskuun allokaatiolla kesäkuun 2027 loppuun)?
2. Onko Puhekaari ALV-rekisterissä? Y-tunnus ei sitä kerro. Onko teillä PIC-koodi?
3. Onko vetäjällä sähköposti yhtiön omassa domainissa?
4. Mikä pohjamalli ja kehys? Onko juuri tätä fine-tune-koodia ajettu LUMI-G:llä (AMD, ROCm)?
5. Missä yksikössä 30 000 on laskettu? LUMIn ohjeissa GPU-tunti on yksi MI250X-moduuli (2 GCD:tä), solmutunti 4 GPU-tuntia.
6. Salliiko yleisradiopuheen lisenssi datan käsittelyn LUMIssa (CSC, Kajaani)?

Laskuni, tarkistakaa:

- PyTorch näkee solmussa 8 GCD:tä GPU:ina. Jos 30 000 on GCD-tunteja, haette 15 000 GPU-tuntia.
- "Yhdellä koneella" käy, jos tarkoitatte yhtä järjestelmää (LUMI-G).
- Yhdellä solmulla 30 000 GPU-tuntia veisi noin 10 kk. 3 kk:ssa se on keskimäärin 3,4 solmua ympäri vuorokauden.

**1. LUMI AI Factoryn lomake:** https://lumi-ai-factory.eu/contact/

- Inquiry type: Powerful AI Computing
- First name, Last name: vetäjä · Company / organisation: Puhekaari Oy
- Type of organisation: Start-up · Country: Finland · Domain area: Software Development
- Email: vetäjän yhtiöosoite
- Message:

> Puhekaari Oy (Tampere, Finland; registered January 2024, 12 people) develops Finnish speech recognition and speech synthesis for [TÄYDENNÄ: our own / a customer's] streaming service. We plan to fine-tune our models on about 8,000 hours of licensed broadcast speech and Mozilla Common Voice. Our estimate is about 30,000 GPU-hours on LUMI-G over 2–3 months, and we intend to apply to the EuroHPC AI Factories Fast Lane call. We would like your help with (1) a short pilot to verify our training pipeline on LUMI-G and check the estimate, and (2) handling licensed speech data on LUMI. Two of our team members used LUMI during their doctoral research and are familiar with Slurm. We would like to start in [TÄYDENNÄ: month].

**2. Fast Lane -hakemus (englanniksi)**

Lomakkeen kentät näkyvät vasta kirjautuneena, joten otsikot tulevat ehtojen (Terms of Reference V3, 31.3.2026) vaatimuksista. Lähettäkää kenttien nimet ja merkkirajat, niin sovitan tekstit.

*Organisation:* Puhekaari Oy, Tampere, Finland · VAT [TÄYDENNÄ: FI + Y-tunnus ilman väliviivaa] · PIC [TÄYDENNÄ, jos on]

*Principal Investigator:* [TÄYDENNÄ: nimi, rooli, yhtiön sähköposti], employed by Puhekaari Oy

*Title (ehdotus):* Fine-tuning Finnish speech recognition and synthesis models on LUMI-G

*Relevance:*

> Puhekaari Oy is a Finnish startup (registered January 2024, 12 people) building Finnish automatic speech recognition (ASR) and text-to-speech (TTS) for [TÄYDENNÄ] streaming service. We will fine-tune [TÄYDENNÄ: base models] on about 8,000 hours of licensed broadcast speech and Mozilla Common Voice Finnish. Target: [TÄYDENNÄ: measurable goal, e.g. WER on a named test set, latency]. Innovation: [TÄYDENNÄ: what existing Finnish models do not do]. The allocation is for model development only: fine-tuning and evaluation. Production inference will run outside LUMI. The purpose is civilian; the models remain Puhekaari's and will be used in our product.

*Technical feasibility:*

> Software: [TÄYDENNÄ: framework and version, ROCm version, container]. Models: [TÄYDENNÄ: architecture, parameters]. Data: about 8,000 hours of audio, [TÄYDENNÄ: TB] on LUMI storage. Readiness: [TÄYDENNÄ: test run of this pipeline on LUMI-G: nodes used, audio hours processed per GPU-hour, multi-node scaling]. Team: two team members used LUMI during their doctoral research and are familiar with Slurm.

*Requested resources (ehdotus):*

> System: LUMI-G. Period: 3 months. Request: 30,000 GPU-hours (one GPU-hour = one MI250X module for one hour), i.e. 7,500 node-hours, on average 3.4 nodes. Breakdown: ASR [TÄYDENNÄ] h, TTS [TÄYDENNÄ] h, evaluation [TÄYDENNÄ] h.

Ehdotan 3 kk, koska jatkoaikaa tai lisätunteja ei saa. Luku muuttuu, jos vastaus 5 on GCD-tunnit.

*Ethics (teidän päätöksenne, itsearviointia varten):*

> The training data contains voice recordings, which can be personal data. Broadcast speech is used under licence [TÄYDENNÄ: licensor, terms that allow training]; Common Voice under its own terms. We do not build speaker identification or clone the voices of named people [TÄYDENNÄ: vahvistakaa]. Speech generated by our TTS will be marked as AI-generated, in line with the AI Act's transparency obligations (Art. 50) [TÄYDENNÄ: miten].

**Tarkistus kuten käsittelijä**

Fast Lane ei pisteytä: ensin kelpoisuus itsearvioinnilla, sitten LUMIn tekninen arvio, ja hyväksytyt saavat tunnit saapumisjärjestyksessä.

- Kelpoisuus: ratkeaa kysymyksillä 1–3.
- Tekninen arvio: heikoin kohta. Ilman teknistä näyttöä hakemus hylätään hallinnollisesti (ehdot, kohta 6d).

Kolme muutosta, jotka auttavat eniten:

1. Testiajo tällä koodilla LUMI-G:llä, esim. LUMI-pilotissa, ja sen luvut hakemukseen.
2. Tunnit laskuna: audiotunnit × epookit ÷ läpimeno.
3. Lisenssi ja tunnistettavien äänten käsittely kirjoitettuna auki.

**Lähetyksen jälkeen**

- Hyväksyntä 4 työpäivässä Fast Lane -sivun mukaan.
- Ennen pääsyä allekirjoitatte käyttöehdot (Acceptable Use Policy).
- EuroHPC:n sivut eivät sano tekoälyavusta mitään. Vastaatte jokaisesta lauseesta, joten lukekaa tekstit ennen lähettämistä.

**Seuraava askel**

Lähettäkää LUMI-lomake nyt ja vastatkaa kuuteen kysymykseen, niin viimeistelen Fast Lane -tekstit. Portaalissa Save Changes tallentaa luonnoksen; Submit on lomakkeen viimeisessä vaiheessa: https://access.eurohpc-ju.europa.eu/calls/59
