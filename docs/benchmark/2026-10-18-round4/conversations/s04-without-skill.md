# s04 without-skill

## Founder, turn 1
Hej. Vi er en agritech-virksomhed i Aarhus (ApS, 3 år, 11 ansatte) der laver en lugerobot med kamera til økologiske grøntsagsavlere. Vi har lige lukket en seedrunde. Nu skal vi træne en ny vision-model og bygge næste prototype, ca. 2,5 mio. kr. i alt. Hvad kan vi søge hos Innovationsfonden, og findes der GPU-adgang i DK for startups? Har hørt om Gefion

## Assistant, turn 1
Hej. Kort svar: I har gode muligheder, men timingen betyder mest. Både Innobooster og GUDP dækker kun arbejde, der starter efter tilsagn. Det, I sætter i gang nu for seed-pengene, kan ikke finansieres bagud.

**1. Innovationsfonden (Danmarks Innovationsfond)**

**Innobooster** passer bedst til jer:
- Fonden dækker 35 %, med et tilskud på 200.000 kr. til 5 mio. kr., og projektet kan vare op til 2 år.
- På et budget på 2,5 mio. kr. kan I højst få ca. 875.000 kr. Det er under 1 mio., så I søger under de minimis-reglerne. Loftet er 300.000 euro i de minimis-støtte over tre år, lagt sammen fra alle offentlige kilder.
- I opfylder sandsynligvis de formelle krav: dansk CVR, SMV og mindst 100.000 kr. i risikovillig kapital inden for tre år. Jeres seedrunde tæller her.
- Jeres egne timer regnes til en fast sats på 750 kr./time, uanset faktisk løn. Hver person kan højst bidrage med 135 timer om måneden.
- Udstyr tæller kun på fakturaer over 10.000 kr. Nyindkøbt udstyr tæller kun med afskrivningen i projektperioden.
- GPU og cloud nævnes ikke direkte i retningslinjerne. Spørg fonden, før I budgetterer med det.
- Temaet "Grøn teknologi" nævner både landbrug og fødevareproduktion og brug af AI i den grønne omstilling. Det passer godt til en lugerobot til økologer.
- **Faldgrube:** Innobooster støtter ikke videreudvikling eller optimering af et produkt, der allerede er på markedet. Sælger I robotten i dag, skal ansøgningen vise et reelt og risikabelt teknologispring, ikke bare en "version 2".
- **Timing:** Sidste pulje i 2026 lukkede 15. oktober, altså for tre dage siden. Datoerne for 2027 er ikke offentliggjort. I 2026 åbnede første pulje 22. januar med frist 12. marts, og svaret kom i slutningen af juni. Følger 2027 samme rytme, kan projektet tidligst starte i sommeren 2027.

**Erhvervsforsker:** Har vision-delen en reel forskningskomponent, kan I ansætte en erhvervs-ph.d. eller -postdoc sammen med et universitet, fx Aarhus Universitet. Fonden giver bl.a. 22.000 kr./md. i løn til en erhvervspostdoc og i alt 612.000 kr. i løn til en erhvervs-ph.d. Der er ingen åbne opslag lige nu.

**Grand Solutions** giver 5-40 mio. kr. til konsortier, og processen tager ca. 9 måneder. Det er næppe besværet værd til et projekt på 2,5 mio.

**2. Uden for fonden: GUDP er nok jeres bedste match**

GUDP under Fødevarestyrelsen er lavet til netop jordbrugs- og fødevareinnovation, og støttesatsen er højere end Innoboosters:
- Som lille virksomhed får I 45 % til et udviklingsprojekt alene. I et samarbejdsprojekt får I 60 %, fx med en vidensinstitution, der bærer mindst 10 % af udgifterne, og hvor resultaterne formidles bredt.
- Tilskuddet er 250.000 kr. til 15 mio. kr., og projektet kan vare op til 4 år.
- I skal sætte tal på både en grøn effekt og en økonomisk effekt.
- Næste runde forventes at åbne i december 2026. Den seneste runde var åben i ca. 10 uger. Projektet må ikke starte før tilsagn, og start anbefales tidligst 4 måneder efter fristen.
- I kan ikke få GUDP og Innobooster til de samme udgifter. I kan dog dele projektet op, fx vision/software i den ene og felttest hos avlere i den anden. Begge ansøgninger skal i så fald oplyses.

**3. GPU-adgang**

**Gefion (DCAI)** er åben for startups, men er kommerciel. Gefion AI Cloud betales efter forbrug uden lang binding og kører på H100- og B300-GPU'er. Priserne er ikke offentlige, så I skal skrive til hello@dcai.dk. Startups kom med i pilotfasen i 2024, men jeg har ikke fundet et aktuelt gratis startupprogram.

**EuroHPC AI Factories er gratis for AI-startups.** Danmark er med i LUMI AI Factory sammen med bl.a. Finland. Som dansk SMV kan I søge:
- **Playground:** en lille kvote i 1-3 måneder, med svar på ca. 2 arbejdsdage. Tjek status på portalen, for siderne er uklare om, hvorvidt den er åben.
- **Fast Lane:** op til 50.000 GPU-timer i 1-3 måneder. Ansøgninger behandles efter først-til-mølle, med svar på ca. 4 arbejdsdage. Det kræver, at I kan arbejde i et HPC-miljø.
- **Bemærk:** LUMI kører AMD-GPU'er (ROCm), ikke NVIDIA/CUDA. PyTorch virker, men tjek resten af jeres pipeline. I kan også vælge et andet EuroHPC-system med NVIDIA.
- DeiC står for Danmarks del af LUMI og hjælper virksomheder med adgang. De er et godt første opkald.

**Realitetstjek:** En ukrudt/afgrøde-model kræver typisk få hundrede til få tusinde GPU-timer, ikke en supercomputer. Det klarer 1-2 måneder på Fast Lane eller en almindelig cloud-regning. Jeres store udgifter bliver data (indsamling og annotering) og prototype-hardware. Lad ikke GPU-spørgsmålet styre planen.

**Det ville jeg gøre**
1. Brug seed-pengene på det, der skal ske nu, fx modeltræning på Fast Lane.
2. Afgræns et tydeligt næste skridt, fx felttest af den nye prototype i sæsonen 2027/2028. Søg det i GUDP-runden, der åbner i december, og/eller i første Innobooster-pulje i 2027.

For at give en mere præcis plan har jeg brug for svar på fire ting:
- Sælger I allerede robotten, og hvad er nyt i næste prototype?
- Hvordan fordeler de 2,5 mio. sig på løn, hardware, data/annotering og compute?
- Skal alt i gang nu, eller kan dele vente til efter sommeren 2027?
- Har I fået offentlig støtte før (fx Innobooster eller anden de minimis-støtte), eller samarbejdet med et universitet?

Kilder:
- [Innobooster (programside og puljer 2026)](https://danmarksinnovationsfond.dk/en/programmes/innobooster/)
- [Innobooster-retningslinjer under de minimis 2026](https://www.innovationsfonden.dk/sites/default/files/2026-01/Innobooster%20retningslinjer%20under%20De%20minimis%202026.pdf)
- [Erhvervsforsker](https://danmarksinnovationsfond.dk/en/programmes/industrial-researcher/)
- [Grand Solutions](https://danmarksinnovationsfond.dk/en/programmes/grand-solutions/)
- [GUDP-puljer](https://gudp.dk/tilskudsguiden/gudp-puljer)
- [GUDP-indkaldelse, runde 2 2026](https://gudp.dk/Media/639221200149388238/GUDP_RUNDE_2_2026_Indkaldelse.pdf)
- [Gefion AI Cloud](https://dcai.dk/products/gefion-cloud)
- [EuroHPC Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en)
- [LUMI: adgang til AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [LUMI AI Factory-konsortiet inkl. Danmark](https://www.lovguiden.dk/en/det-offentlige/eurohpc-joint-undertaking/2026-08-31-ny-lumi-ai-supercomputer-giver-ti-foldig-ai-kapacitet-i-europa)
- [DI om startup-piloter på Gefion (2024)](https://www.danskindustri.dk/di-business/arkiv/nyheder/2024/11/ivarksattere-jubler-over-lynadgang-til-supercomputer/)

## Founder, turn 2
- Ja, vi leaser robotten ud til pilotavlere i dag. Det nye er primært en ny vision-model, hvad der ellers er nyt i prototypen er jeg ikke sikker på i detaljer.
- Den præcise fordeling af de 2,5 mio. er jeg ikke sikker på. Compute-delen er ca. 5.000 H100-timer.
- Om noget kan vente til efter sommeren 2027, ved jeg ikke.
- Ja, vi fik Innobooster på 1 mio. kr. i 2024 og et tilskud til grøn omstilling via Erhvervshus Midtjylland på 600.000 kr. i 2025, begge som de minimis. Samarbejde med et universitet er jeg ikke sikker på.

## Assistant, turn 2
Tak. Jeres svar ændrer tre ting, og den vigtigste er de minimis-loftet.

**1. De minimis-loftet kan begrænse jeres næste Innobooster**

Loftet er 300.000 euro (ca. 2,24 mio. kr.) over en løbende periode på tre år. Det regnes fra datoen for tilsagnet, ikke fra udbetalingen.
- I har fået 1,6 mio. kr.: 1 mio. fra Innobooster 2024 og 600.000 kr. fra Erhvervshuset 2025. Tæller begge stadig med, har I ca. 640.000 kr. tilbage.
- En fuld Innobooster på jeres budget giver ca. 875.000 kr., og det er mere, end I har plads til. Bringer et tilskud jer over loftet, kan fonden slet ikke give det under de minimis. I skal derfor søge et beløb, der kan være der.
- **Men** Innobooster-tilsagnet fra 2024 holder op med at tælle, når det er tre år gammelt. Er det over tre år gammelt både når I søger, og når I får svar, har I ca. 1,6 mio. kr. tilbage, og så kan I søge de fulde ca. 875.000 kr.
- **Opgave:** Find tilsagnsdatoen i bevillingsbrevet fra 2024. Tjek også, om I har fået anden de minimis-støtte; det skal stå i bevillingsbrevene. Bekræft regnestykket med fonden, før I søger.

Tæller 2024-tilsagnet stadig, har I to veje:
- Søg ca. 600.000 kr. Det svarer til 35 % af et projekt på ca. 1,7 mio. kr.
- Eller søg over 1 mio. kr. Så falder tilskuddet ind under gruppefritagelsen, som ikke tæller med i de minimis. Det kræver et projekt på mindst ca. 2,9 mio. kr. Gør kun budgettet større, hvis projektet reelt er større. Jeg har ikke kunnet finde retningslinjerne for det spor i 2026-udgaven, så tjek dem.

Med 1 mio. fra 2024 og under 1 mio. nu holder I jer også under 2 mio. kr. i Innobooster på tre år. Går I over 2 mio., skal I præsentere for et paneludvalg. Fonden vurderer under alle omstændigheder, hvad 2024-projektet leverede.

**2. En ny model til en robot, der allerede er ude, kan give afslag**

Innobooster afviser projekter, der mest er optimering eller videreudvikling af noget, der allerede er på markedet. Pilotleasing er ikke nødvendigvis "på markedet". Men I skal kunne vise tre ting:
- hvad den nye model skal kunne, som den nuværende ikke kan, fx luge tættere på afgrøden, nye afgrøder eller ukrudt på tidligere stadier
- hvorfor det er teknisk usikkert
- hvad der ellers er nyt i prototypen

Det sidste skal jeres tekniske ansvarlige skrive ned. Uden det kan ingen af ansøgningerne skrives.

**3. GUDP er ikke ramt af loftet**

GUDP gives under gruppefritagelsen og ikke under de minimis, så jeres 1,6 mio. tæller ikke med. Satsen er også højere: 45 % hvis I søger alene, og 60 % i et samarbejde.
- GUDP forventer som udgangspunkt samarbejde. 60 %-satsen kræver fx en vidensinstitution (Aarhus Universitet eller et GTS-institut), der bærer mindst 10 % af udgifterne, og at resultaterne bliver formidlet bredt. Pilotavlerne kan være partnere med marker og data.
- I 2026 var fristen i første runde 19. februar, og tilsagnet kom i starten af juni. Følger 2027 samme rytme, kan I tidligst starte i juni 2027. Runden forventes at åbne i december.
- Et samarbejde med et universitet tager tid at få på plads, så tag kontakt nu. Send også gerne en kort projektbeskrivelse til gudp@fvst.dk og få en vurdering af, om projektet passer.

**4. 5.000 H100-timer er en lille post**
- Hos specialiserede GPU-clouds koster det groft 65.000-130.000 kr. (ca. 2-4 USD pr. time). AWS, Google og Azure er typisk dyrere. Bed Gefion om et tilbud.
- EuroHPC Fast Lane er gratis og giver op til 50.000 GPU-timer i højst 3 måneder. Men systemerne med H100-klassen (MareNostrum 5 og JUPITER Booster) er lige nu lukket for Fast Lane på grund af stor efterspørgsel.
- Regn derfor med A100 eller AMD-GPU'er på LUMI. På A100 skal I bruge groft 2-3 gange så mange timer, men det er stadig langt under grænsen.
- Compute udgør ca. 3-5 % af budgettet. Søg Fast Lane, hvis I vil spare pengene, men lad det ikke styre tidsplanen.

**Mit forslag til opdeling**

Intet af det her dækker arbejde før tilsagn, og tidligst tilsagn er omkring juni 2027.
- **Nu, med seed-penge og evt. Fast Lane:** Træn vision-modellen, så den kan testes i sæsonen 2027.
- **Fra sommeren 2027, med tilskud:** Byg den nye prototype og felttest den hos avlerne ind i sæsonen 2028. Det er også lettere at forsvare som nyt og usikkert end en opdatering af modellen.

**Find ud af det her først**
1. Tilsagnsdatoen for Innobooster 2024 og al anden de minimis-støtte.
2. Hvad der er nyt i prototypen ud over modellen, og en grov fordeling af de 2,5 mio.
3. Om I vil gå efter GUDP. Så skal I kontakte AU eller et GTS-institut nu.

Når I har svar på 1 og 2, regner jeg de konkrete beløb og foreslår, hvordan projektet kan deles mellem GUDP og Innobooster.

Kilder:
- [Innobooster-retningslinjer, de minimis 2026](https://www.innovationsfonden.dk/sites/default/files/2026-01/Innobooster%20retningslinjer%20under%20De%20minimis%202026.pdf)
- [Innobooster (programside)](https://danmarksinnovationsfond.dk/en/programmes/innobooster/)
- [De minimis-forordningen (EU) 2023/2831](https://eur-lex.europa.eu/legal-content/da/TXT/?uri=CELEX%3A32023R2831)
- [GUDP-puljer](https://gudp.dk/tilskudsguiden/gudp-puljer)
- [GUDP-indkaldelse, runde 2 2026](https://gudp.dk/Media/639221200149388238/GUDP_RUNDE_2_2026_Indkaldelse.pdf)
- [GUDP årshjul 2026](https://gudp.dk/Media/639014660005597654/GUDP_%C3%85rshjul_2026.pdf)
- [EuroHPC Fast Lane (status og systemer)](https://www.eurohpc-ju.europa.eu/fast-lane-access-ai-factories-temporarily-closed_en)
- [H100-priser 2026](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)
- [Gefion AI Cloud](https://dcai.dk/products/gefion-cloud)
