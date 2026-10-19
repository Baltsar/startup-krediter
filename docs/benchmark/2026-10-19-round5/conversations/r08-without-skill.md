# r08 without-skill

## Founder, turn 1
Hei! saisko meidän startup ilmasta GPU-aikaa LUMI:lta sen AI Factoryn kautta? tarvittais n. 30 000 GPU-tuntia suomenkielisen puhemallin fine-tuneen. mitä hakemukseen tarvii ja kuinka nopeesti pääsee alkuun? pari meidän tyyppiä on käyttäny LUMIa väikkärin aikana joten slurm on tuttu

## Assistant, turn 1
Moi!

Lyhyesti: todennäköisesti saatte. LUMI AI Factoryn laskenta-aika jaetaan EuroHPC:n "AI for Industrial Innovation" -haun kautta, ja se on maksutonta startupeille ja pk-yrityksille, kun käyttö on tutkimus- ja kehitystyötä. Kyse on laskenta-allokaatiosta, ei rahasta. 30 000 GPU-tuntia mahtuu Fast Lane -moodiin, ja teidän Slurm- ja LUMI-tausta on juuri sitä, mitä Fast Lane olettaa.

**Fast Lane lyhyesti**
- Enintään 50 000 GPU-tuntia, kestoltaan 1, 2 tai 3 kuukautta.
- Yksi järjestelmä per hakemus, teillä siis LUMI-G.
- Haku on jatkuvasti auki ilman määräpäiviä, ja hakemukset käsitellään saapumisjärjestyksessä ilman kilpailua.
- Päätös tulee 4 työpäivän sisällä.
- Maksuton AI-alan pk-yrityksille ja startupeille innovaatiokäyttöön.
- Pk-yritys tarkoittaa alle 250 henkeä ja liikevaihtoa enintään 50 M€ tai tasetta enintään 43 M€. Yrityksen pitää olla EU:ssa, joten Suomi on ok. Jos isompi yritys omistaa teistä merkittävän osuuden, tarkistakaa, laskeeko sen koko mukaan.

**Tarkistakaa ensin kaksi asiaa**

1. **LUMI-G:n saatavuus.** Kysyntä on kova. EuroHPC on sulkenut LUMI-G:n uusilta Large Scale -allokaatioilta (yli 50 000 h). Fast Lane -sivulla suljetuiksi on merkitty vain MareNostrum5 ACC ja JUPITER Booster, joten LUMI-G:tä ei ole Fast Lanessa merkitty kiinni. Katsokaa portaalin osiolistasta ennen hakemista, että LUMI-G on valittavissa. Jos ei ole, joudutte valitsemaan toisen koneen.

2. **GPU-tunnin yksikkö.** LUMIssa 1 GPU-tunti on yksi kokonainen MI250X-moduuli (2 GCD:tä) tunnin ajan. standard-g-solmu laskuttaa 4 GPU-tuntia tunnissa, vaikka PyTorch näkee 8 laitetta. 30 000 GPU-tuntia on siis noin 7 500 solmutuntia. Jos arvio on tehty NVIDIA-korteilla tai GCD-määrällä, laskekaa se uudelleen LUMI-yksiköissä. Perusteltu puskuri kannattaa, kunhan pysytte alle 50 000:n.

Kolmen kuukauden allokaatiossa 30 000 h on noin 10 000 h kuussa, eli keskimäärin 3–4 solmua jatkuvasti käynnissä. Miettikää, ehtivätkö ajot valmiiksi jonotuksen kanssa, ja valitkaa kesto sen mukaan.

**Mitä hakemukseen tarvitaan**

Hakemus on lyhyt verkkolomake EuroHPC:n portaalissa, ei pitkä tutkimussuunnitelma. Varautukaa kertomaan:
- yrityksen tiedot ja pk-status
- innovaatiotarkoitus: mitä suomenkielinen puhemalli ratkaisee ja miksi
- malli (pohjamalli ja koko) sekä datasetit ja oikeudet niihin
- ohjelmistopino ja skaalautuminen (montako solmua per ajo)
- resurssiperustelu: miten 30 000 h on laskettu, ja kesto 1–3 kk
- kohdejärjestelmä (LUMI-G)

Arvioijat tarkistavat, että kuorma oikeasti pyörii valitulla koneella. LUMI-G on AMD MI250X ja ROCm, joten varmistakaa, ettei fine-tune-pinossa ole CUDA-only-riippuvuuksia. LUMI AI Factoryllä on valmiita AI-kontteja, joista voi lähteä liikkeelle.

Lukekaa ennen lähettämistä Terms of Reference ja EuroHPC Access Policy. Ne löytyvät Fast Lane -sivun Documents-osiosta.

**Kuinka nopeasti pääsee alkuun**
- Päätös tulee enintään 4 työpäivässä. LUMI AI Factory sanoo itse, että ensimmäisestä yhteydenotosta työhön voi päästä 2–5 päivässä.
- Sen jälkeen tulee käyttäjien onboarding. 15.4.2026 jälkeen myönnetyt EuroHPC-projektit hallitaan EuroHPC Federation Platformissa (my-eurohpc.eu), ja jäsenet saavat kutsun sähköpostiin.
- LUMIn käyttöehdot vaativat organisaation sähköpostiosoitteen. Väikkäriajan tunnukset ovat yliopiston osoitteella, joten varautukaa uusiin tunnuksiin yrityksen osoitteilla.
- Realistinen arvio on noin 1–2 viikkoa hakemuksesta ensimmäiseen ajoon, jos LUMI-G on saatavilla ja pino toimii ROCm:llä.

**Ehdot, jotka kannattaa tietää**
- Vain T&K-käyttöön. Tuotanto ja 24/7-inferenssi pitää ajaa muualla.
- Immateriaalioikeudet jäävät teille.
- EuroHPC ja LUMI AI Factory mainitaan julkisessa viestinnässä, ja osallistutte tarvittaessa levitystapahtumiin.
- Allokaation jälkeen kirjoitetaan lyhyt loppuraportti. LUMI AI Factoryn mukaan pk-yritykseltä vaaditaan lyhyt julkinen raportti, ja arkaluonteiset osat voi suojata NDA:lla.
- Data on käytettävissä 90 päivää projektin päättymisen jälkeen. Varmuuskopiot ovat teidän vastuullanne.

**Vaihtoehdot, jos Fast Lane ei toimi**
- CSC:n kaupallinen LUMI-käyttö: maksullinen, tällä hetkellä vain suomalaisille yrityksille, eikä siinä ole julkaisuvelvoitetta.
- Business Finland: rahoitusta LUMI-laskentaan, jos teillä on jo Business Finlandin rahoittama T&K-projekti. Valtiontukisäännöt pätevät.
- LUMI AI Factoryn yhteydenottolomake: maksutonta neuvontaa siihen, mikä reitti sopii.

**Ehdotan tätä järjestystä**
1. Tarkistakaa portaalista, että LUMI-G on valittavissa Fast Lanessa, tai kysykää LUMI AI Factorylta.
2. Laskekaa GPU-tunnit LUMI-yksiköissä ja varmistakaa, että pino toimii ROCm:llä.
3. Täyttäkää Fast Lane -lomake ja valitkaa kesto, jossa ajot ehtivät valmiiksi.

**Linkit**
- Fast Lane -haku: https://eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en
- EuroHPC-hakuportaali: https://access.eurohpc-ju.europa.eu/
- LUMI AI Factory, hinnoittelu ja kelpoisuus: https://lumi-ai-factory.eu/pricing-and-eligibility/
- LUMI AI Factory, yhteydenotto: https://lumi-ai-factory.eu/contact-us/
- LUMIn GPU-tuntien laskutus: https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/
- LUMIin kirjautuminen (EFP): https://docs.lumi-supercomputer.eu/firststeps/accessLUMI/

Tiedot on tarkistettu 19.10.2026. Saatavuus muuttuu nopeasti, joten katsokaa LUMI-G:n tilanne portaalista juuri ennen hakemista.

## Founder, turn 2
kiitos! eli onko tää ihan varmasti ilmasta meille, ettei tuu mitään laskua jälkikäteen?

## Assistant, turn 2
Moi!

Lyhyesti: laskenta-ajasta ei tule laskua. EuroHPC:n Terms of Referencessa (versio 31.3.2026) lukee, että pääsy on maksutonta, kunhan kelpoisuusehdot ja käyttöehdot täyttyvät. Maksuttomuus on siis ehdollista, ja muutama asia voi silti maksaa rahaa tai työaikaa.

**Pitäkää nämä ehdot kunnossa**
- **Kelpoisuus.** Teidän pitää olla pk-yritys myös omistajat huomioiden. Hakijan (PI) työsuhteen pitää olla voimassa hakuhetkellä ja vähintään 3 kuukautta allokaation päättymisen jälkeen.
- **LUMIn käyttöehdot.** Jos EuroHPC:n ja LUMIn ehdot eroavat, LUMIn ehdot pätevät. Niiden mukaan käyttäjä vastaa LUMIlle aiheutuneista vahingoista ja kuluista, jos rikkoo käyttöehtoja tai kolmannen osapuolen lisenssiehtoja. Vastuu jatkuu tunnuksen sulkemisen jälkeenkin. Tämä on ainoa kohta, josta löysin mahdollisen jälkikäteisen rahavastuun.
- **Puhemallissa tämä tarkoittaa lisenssejä.** Tarkistakaa, että pohjamallin ja jokaisen puhedatasetin lisenssi sallii teidän käyttönne, myös kaupallisen.
- **Käyttötarkoitus.** LUMI on T&K-käyttöön. Tuotantoinferenssi ajetaan muualla.

**Mikä ei kuulu ilmaiseen**
- **Allokaatio on kiintiö, ei avoin tili.** LUMI AI Factory sanoo suoraan, ettei maksuton tarkoita rajatonta käyttöä. Myös levytila kuluttaa allokaatiota TB-tunteina, ei vain GPU-ajo.
- **Osa datasta maksaa.** Osa LUMIn kautta saatavista dataseteistä on ulkopuolisten toimittajien, ja ne laskuttavat suoraan.
- **CSC:n kaupallinen LUMI-käyttö on maksullista.** Se on eri reitti. Pysykää Fast Lanessa, niin sitä laskua ei tule.
- **Oma työaika.** Loppuraportti pitää palauttaa 3 kuukauden sisällä allokaation päättymisestä. EuroHPC saa julkaista sen vuoden kuluttua, joten kirjoittakaa se sen mukaan. Lisäksi osallistutte EuroHPC:n levitystapahtumaan vähintään kerran kahden vuoden sisällä.

**Valtiontuki: ei lasku, mutta kysykää**
Business Finlandin kautta saatu laskenta-aika ilmoitetaan valtiontukena, ja katto on 300 000 € kolmessa vuodessa. Myös LUMI AI Factoryn maksuttoman neuvonnan arvo ilmoitetaan valtiontukiraportointia varten. Fast Lane -reitistä en löytänyt julkista tietoa siitä, lasketaanko allokaation arvo valtiontueksi. EU:n neuvoston työryhmässä todettiin vuonna 2025, että AI Factoryjen valtiontukikohtelu vaatii selvitystä. Laskua tästä ei tule, mutta se voi syödä tilaa myöhemmiltä julkisilta tuilta.

**Varmistakaa kirjallisesti ennen hakemista**
Lähettäkää LUMI AI Factorylle kolme kysymystä:
1. Onko Fast Lane LUMI-G:llä meille kokonaan maksuton?
2. Lasketaanko allokaation arvo valtiontueksi, ja minkä arvon te ilmoitatte?
3. Mitä tapahtuu, jos GPU-tunnit tai levytila loppuvat kesken?

Kolmanteen en löytänyt vastausta LUMIn dokumentaatiosta. Ylitysmaksua ei mainita yhdessäkään lukemassani ehtodokumentissa, mutta varmistakaa se silti.

**Linkit**
- EuroHPC Terms of Reference, AI Factories -haut: https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms%20of%20Reference%20-%20AIF%20Access%20Calls.pdf
- LUMIn käyttöehdot 2026: https://lumi-supercomputer.eu/wp-content/uploads/2026/03/LUMI-General-Terms-of-Use_2026.pdf
- LUMI AI Factory, hinnoittelu ja kelpoisuus: https://lumi-ai-factory.eu/pricing-and-eligibility/
- LUMI AI Factory, yhteydenotto: https://lumi-ai-factory.eu/contact-us/
- LUMIn laskutus (GPU- ja TB-tunnit): https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/

Tiedot on tarkistettu 19.10.2026.
