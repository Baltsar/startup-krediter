# s11 without-skill

## Founder, turn 1
Hei, ollaan oululainen medtech-startup (Oy, perustettu 2022), tehdään tekoälypohjaista EKG-analyysiä kotimittauksiin. Saatiin siemenkierros viime vuonna. Nyt tarvittais laskentatehoa mallin koulutukseen (LUMI?) ja lisää rahoitusta kliiniseen validointiin, n. 800 000 €. Mitä vaihtoehtoja on Business Finlandin kautta tai muualta?

## Assistant, turn 1
Hei! Lyhyesti: Business Finlandin kautta validointiin sopii parhaiten T&K-rahoituksen laina. Isompaa avustusta haetaan EU:sta (EIC Accelerator). LUMIn laskenta on startupille maksutonta. Kahdessa ensimmäisessä on kuitenkin portti, joka kannattaa tarkistaa ensin. Tilanne lokakuussa 2026:

**1. Kliininen validointi (~800 k€)**

- **Business Finland: Tutkimus, kehitys ja pilotointi.** Haku on jatkuva, ja sivu on päivitetty 22.9.2026.
  - Pk-yritys saa avustusta enintään 50 % tutkimuskuluista.
  - Kehitys- ja pilotointikuluihin saa lainaa 50 %, perustellusti 70 %.
  - Kliininen validointi luetaan yleensä kehittämiseksi, joten se rahoitetaan todennäköisesti lainalla eikä avustuksella.
  - 800 k€:n hankkeessa laina olisi 400–560 k€, ja omaa rahoitusta tarvitaan 240–400 k€.
  - Lainan korko on peruskorko miinus 3 %-yksikköä, kuitenkin vähintään 1 %. Vakuuksia ei yleensä vaadita. Laina-aika on 7 tai 10 vuotta, ja siitä 3 tai 5 vuotta on lyhennysvapaita.
  - Ennakkona saa vain 30 %, ja 20 % maksetaan vasta loppuraportin jälkeen. Kassan on siis kestettävä kulut ennen rahoitusta.
  - **Portti:** EU:n valtiontukisääntöjen mukaan "vaikeuksissa olevaa yritystä" ei rahoiteta. Yrityksenne on perustettu 2022, joten alle 3-vuotiaiden poikkeus ei enää koske teitä. Jos kertyneet tappiot ovat syöneet vapaan oman pääoman (SVOP mukaan lukien) ja yli puolet osakepääomasta, hakemus kaatuu. SVOP:iin merkitty siemenkierros yleensä riittää, mutta tarkistakaa viimeisin tase.
- **Sprint** (jatkuva haku 1.9.2026 alkaen) on 75–100 k€:n avustus, joka kattaa 75 % kuluista. Sitä saa vain alle 5-vuotias yritys, joka ei ole aiemmin saanut Business Finlandin rahoitusta, ja oman pääoman ehtoista rahoitusta pitää olla vähintään 50 k€. Validointiin summa on liian pieni. Mallikehitykseen se voisi sopia, jos Business Finlandin rahaa ei ole aiemmin tullut.
- Nuorten innovatiivisten yritysten (NIY) rahoitus on käytännössä kiinni vuonna 2026. Deep Tech Acceleratorin vuoden 2026 haku päättyi 16.8., ja se on vain tutkimuksesta syntyneille spin-offeille.

**2. EU**

- **EIC Accelerator** antaa avustusta enintään 2,5 M€ TRL 6–8 -työhön. Kliinisen tutkimuksen voi rahoittaa avustusosalla, ja lisäksi on mahdollinen pääomasijoitus.
  - Vaatimuksena on TRL 5 eli validointi relevantissa ympäristössä.
  - Lyhyen hakemuksen voi jättää milloin tahansa, ja vastaus tulee 4–6 viikossa. Täysi hakemus jätetään vuoden 2027 hakupäivinä, jotka vahvistetaan vuoden 2027 työohjelmassa.
  - Kilpailu on kovaa, mutta tämä on ainoa reitti, jolla validointiin voi saada ison summan avustuksena.
- **Eurostars** sopii, jos teillä on kumppani toisesta maasta, esimerkiksi sairaala tai yritys. Business Finland rahoittaa suomalaisen pk-yrityksen osuudesta 50 % avustuksena. Hakuja on kaksi vuodessa, mutta vuoden 2027 päivät eivät ole vielä vahvistettuja.

**3. Laskenta (LUMI)**

- LUMI AI Factoryn ja EuroHPC:n teollisuusreitit ovat maksuttomia tekoäly-pk-yrityksille ja startupeille innovaatiokäyttöön.
  - Fast Lane: enintään 50 000 GPU-tuntia, ja hyväksyntä tulee noin 4 arkipäivässä. EKG-mallille tämä todennäköisesti riittää.
  - Large Scale: yli 50 000 GPU-tuntia, ja hakupäiviä on jatkuvasti.
- **Portti:** CSC:n mukaan LUMI ei sovellu arkaluonteiselle terveysdatalle (tilanne 6/2026). Pseudonymisoitu EKG on edelleen henkilötietoa. LUMIin sopii siis vain aidosti anonymisoitu data tai avoimet aineistot. Findatan luvalla saatu data on käsiteltävä auditoidussa ympäristössä. Jos data on henkilötietoa, EU-alueen pilvi startup-krediiteillä ja tietojenkäsittelysopimuksella voi olla helpompi reitti.

**4. Oulu**

OuluHealth Labs ja OYS TestLab tekevät validointia ja pilotointia oikeissa sairaalaprosesseissa. Se voi pienentää validoinnin kustannuksia ja vahvistaa Business Finlandin hakemusta.

Jotta voin sanoa, mikä näistä oikeasti toimii teille, vastaatko näihin:
1. Onko yritys saanut aiemmin Business Finlandin rahoitusta (esim. Tempo, NIY tai T&K)?
2. Onko oma pääoma viimeisimmässä tilinpäätöksessä selvästi positiivinen?
3. Paljonko siemenrahasta voitte sitoa omaan rahoitusosuuteen?
4. Mikä on laitteen MDR-luokka? Onko validointi CE-merkintää varten tehtävä kliininen tutkimus?
5. Mistä koulutusdata tulee: itse suostumuksella kerätty, sairaalan tai Findatan kautta vai avoimet aineistot?

Lähteet:
- [BF: Tutkimus, kehitys ja pilotointi 2026](https://www.businessfinland.fi/en/services/funding/calls/2026/research-development-and-piloting/)
- [BF: Sprint](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)
- [BF: rahoituspalvelut 2026](https://www.businessfinland.fi/en/whats-new/news/2026/what-do-business-finlands-funding-services-look-like-at-the-beginning-of-2026/)
- [BF: DTA 2026](https://www.businessfinland.fi/en/services/funding/calls/2026/dta-funding-call-2026/)
- [EIC Accelerator FAQ](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-eic-accelerator_en)
- [BF: Eurostars](https://www.businessfinland.fi/en/for-finnish-customers/services/programs/european-programs/eurostars)
- [LUMI AI Factory -haut](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [LUMI FAQ](https://lumi-supercomputer.eu/faq/)
- [CSC/Kielipankki: arkaluonteinen data](https://www.kielipankki.fi/support/sensitive-data/)

## Founder, turn 2
1. Joo, Business Finlandin tutkimus-, kehitys- ja pilotointiavustus 350 000 €, myönnetty 2024. Projekti jatkuu 31.12.2026 asti, eikä loppuraporttia ole vielä jätetty.
2. En ole varma.
3. En ole varma.
4. Luokka IIa MDR:n mukaan, ja CE-prosessi on käynnissä. Onko validointi juuri CE-merkintää varten tehtävä kliininen tutkimus, siitä en ole varma.
5. En ole varma.

## Assistant, turn 2
Kiitos, tämä selkeyttää paljon. Eniten kuvaa muuttaa käynnissä oleva Business Finland -projekti.

**Mitä vastauksenne muuttavat**

- **Sprint putoaa pois.** Sitä ei myönnetä alle 5-vuotiaalle yritykselle, joka on jo saanut Business Finlandin T&K-rahoitusta.
- **Uutta T&K-rahoitusta voi silti hakea.** Aiempi rahoitus ei estä sitä, mutta Business Finland arvioi, miten edellinen projekti toteutui ja mitä se tuotti. Uusi projekti ei saa vaarantaa edellisen tavoitteita, eikä samaa kulua voi olla kahdessa projektissa. Validointi sopii luontevasti jatkoprojektiksi: nykyinen projekti tuottaa mallin, ja uusi validoi sen.
- **Ajoitus:** kulut hyväksytään vasta siitä, kun hakemus on vireillä. Hakemus kannattaa siis jättää ennen kuin validointikuluja syntyy. Ottakaa yhteyttä nykyisen projektinne yhteyshenkilöön jo nyt, ennen 31.12.
- **Loppuraportti:** se on jätettävä 4 kuukauden kuluessa projektin päättymisestä, eli noin huhtikuun 2027 loppuun mennessä.
  - Vuodesta 2026 alkaen myöhästynyttä raporttia ei käsitellä, eikä rahoitusta makseta.
  - Jatkoaikaa on haettava ennen määräaikaa.
  - Viimeinen erä maksetaan vasta hyväksytyn loppuraportin jälkeen. Nykyisissä ehdoissa se on vähintään 10 % avustuksesta, teillä siis noin 35 000 €. Tarkistakaa tarkka osuus omasta rahoituspäätöksestänne.
- **Validointi rahoitetaan todennäköisesti lainalla.** Nykyinen projektinne on avustusta, mutta kliininen validointi luetaan yleensä kehittämiseksi.

**Kaksi asiaa, jotka saatte selville nopeasti**

1. **Oma pääoma (kysymys 2).** Katsokaa viimeisimmän tilinpäätöksen taseesta kohta "Oma pääoma yhteensä". Jos se on alle puolet osakepääomasta, yritys on EU:n sääntöjen mukaan "vaikeuksissa". Silloin Business Finlandin uutta T&K-rahoitusta ei voi saada. Jos siemenkierros on kirjattu SVOP:iin, se nostaa omaa pääomaa. Tilitoimisto osaa vastata tähän heti.
2. **Kliininen tutkimus (kysymys 4).** MDR vaatii jokaiselle laitteelle kliinisen arvioinnin, mutta kliininen tutkimus on eri asia.
   - Jos laitteella ei vielä ole CE-merkkiä ja tutkimuksen tuloksia käytetään vaatimustenmukaisuuden arviointiin, tutkimukselle tarvitaan Fimean lupa (MDR 62 artikla).
   - Ohjelmistolle voi joskus riittää kirjallisuus ja olemassa oleva data. Se riippuu käyttötarkoituksesta ja siitä, mitä laitteesta väitetään (MDCG 2020-1).
   - Vastaus löytyy CE-dokumentaationne kliinisen arvioinnin suunnitelmasta (CEP), tai sen tietää regulatory-konsulttinne.
   - Tämä ratkaisee kustannukset ja aikataulun. Siitä riippuu myös, kannattaako hakea EIC:n avustusta.

**Oma rahoitusosuus (kysymys 3)**

800 000 €:n hankkeessa Business Finlandin laina kattaa 50–70 %, joten itse maksettavaksi jää 240 000–400 000 €. Lainasta saa ennakkona vain 30 %, ja 20 % maksetaan vasta lopussa. Kassan on siis kestettävä suurin osa kuluista etukäteen.

Jos tämä ei riitä, EIC Accelerator on suurin avustusreitti validointiin. Avustusta voi saada enintään 2,5 M€, ja kliininen tutkimus kuuluu katettaviin kuluihin. Business Finlandin rahoitus ei estä EIC:tä, kunhan samoja kuluja ei rahoiteta kahdesti.

**Data ja LUMI (kysymys 5)**

Nyrkkisääntö: jos EKG:t on mitattu teidän käyttäjiltänne tai sairaalassa, ne ovat henkilötietoa. Silloin niitä ei voi viedä LUMIin. LUMIa voi kuitenkin käyttää mallin esikoulutukseen avoimilla aineistoilla, kuten PhysioNetin PTB-XL:llä (tarkistakaa lisenssi). Hienosäätö omalla datalla tehdään ympäristössä, jossa henkilötietoja saa käsitellä.

**Seuraavat askeleet**
1. Pyytäkää tilitoimistolta oma pääoma ja osakepääoma viimeisimmästä tilinpäätöksestä.
2. Selvittäkää CEP:stä tai konsultilta, tarvitaanko 62 artiklan mukainen kliininen tutkimus.
3. Varatkaa palaveri Business Finlandin yhteyshenkilön kanssa jatkoprojektista ennen vuodenvaihdetta.

Kaksi kysymystä, jotta voin tarkentaa:
- Mistä kotimittausten EKG-data tulee: omilta käyttäjiltä, omasta tutkimuksesta vai sairaalasta?
- Paljonko kassaa teillä on nyt, ja kuinka pitkälle se riittää?

Lähteet:
- [BF: loppuraporttien määräajat](https://www.businessfinland.fi/en/whats-new/news/2025/reminder-to-funding-beneficiaries-deadlines-for-final-reports-must-be-met/)
- [BF: Tutkimus, kehitys ja pilotointi 2026](https://www.businessfinland.fi/en/services/funding/calls/2026/research-development-and-piloting/)
- [BF: Sprint](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)
- [BF: rahoitusehdot](https://www.businessfinland.fi/en/services/funding/funding-services/guidelines-terms-and-forms/funding-terms/)
- [BF: CETP 2026 -ohje (aiempi rahoitus)](https://cetpartnership.eu/wp-content/uploads/2026/06/Finland_BF_CETP-JC2026-National-regional-requirements-and-guidelines_FINAL_260513_0.pdf)
- [Fimea: kliiniset laitetutkimukset](https://fimea.fi/medical-devices/investigations-with-devices/clinical-evaluation-and-clinical-investigations)
- [MDCG 2020-1](https://ec.europa.eu/docsroom/documents/40323)
- [EIC Accelerator FAQ](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-eic-accelerator_en)
- [PTB-XL, PhysioNet](https://physionet.org/content/ptb-xl/1.0.0)
