# s01 without-skill

## Founder, turn 1
Hej! Vi är ett lönsamt mjukvarubolag inom lager och 3PL i Jönköping, 14 anställda, startade 2016. Nu vill vi bygga in AI-baserad efterfrågeprognos och ruttoptimering i vårt WMS, budget runt 6 MSEK över två år. Finns det något hos Vinnova som passar ett etablerat bolag som oss, eller är allt bara för startups? Och var kan man få GPU-tid billigt för att träna modellerna?

## Assistant, turn 1
Hej! Kort svar: nej, Vinnova är inte bara för startups. Men det som finns för ett etablerat bolag som ert kräver nästan alltid en utländsk partner eller ett konsortium. Det täcker också bara en del av kostnaden, aldrig hela 6 MSEK. Den säkraste pengen för er är troligen inget bidrag alls, utan FoU-avdraget (mer om det längre ner).

**Det som inte passar er**
Innovativa Startups har öppet just nu, till 12 januari. Den kräver färre än 10 anställda och högst 10 MSEK i omsättning eller balansomslutning, och bolaget får inte ha delat ut vinst. Med 14 anställda och lönsam drift är ni utanför.

**1. Eurostars passar er bäst**
- Eurostars är till för innovativa små och medelstora bolag som driver ett FoU-projekt tillsammans med minst en part i ett annat Eurostars-land. Ett SMF ska leda projektet, och det kan vara ni. Projektet får vara högst 36 månader, och SMF-parterna ska stå för minst hälften av budgeten.
- Nästa deadline är **4 mars 2027** (Call 12).
- Vinnova finansierar den svenska delen. I senaste svenska rundan (hösten 2025) var taket 5 MSEK per projekt. Bolaget behövde också omsättning eller eget kapital på minst halva det sökta beloppet, vilket ni bör klara. Hur stor andel av kostnaden bidraget täcker står i utlysningstexten. Räkna med att ni själva bär en stor del.
- Produkten ska komma ut på marknaden inom två år efter projektslut. Det passar bra för en ny funktion i ett WMS.
- Haken är den utländska partnern. Det kan vara en kund med lager i Norge, Danmark eller Tyskland, en teknikpartner eller ett universitet utomlands. Fyra och en halv månad är kort tid, så börja där.

**2. Avancerad digitalisering, "Tillämpad AI för industrin"**
- Det här är Vinnovas stora program för AI i industrin och pågår 2025–2027. Senaste rundan stängde 16 januari 2026. Då fick 20 AI-projekt 120 MSEK, oftast 3–12 MSEK per projekt.
- Ett av de två spåren var "AI-baserat beslutsstöd". Prognoser och ruttoptimering passar där.
- Ni måste söka som konsortium: minst två parter, varav minst ett företag. I praktiken är nästan alltid en högskola eller ett institut med. Jönköping University fanns bland de beviljade, så ni har en möjlig partner i stan.
- Vinnova vill se ett industriellt behov, så ta in en eller ett par kunder som "behovsägare".
- Någon ny deadline är inte publicerad än. Bevaka programsidan.

**3. Mindre möjligheter**
- *Test och demo för SMF*: här kan ett bolag söka ensamt, upp till 1 MSEK, för att köpa tester i externa testmiljöer. Senaste rundan stängde i september, men utlysningen brukar komma tillbaka.
- *FFI*: Vinnovas program för vägtransporter har utlysningar planerade hösten 2026. De är fordonsinriktade, så de passar bara om ni kan beskriva ruttoptimeringen som transporteffektivitet. Exakta datum har inte publicerats.

En sak gäller för alla Vinnova-utlysningar: de finansierar forskning och utveckling, inte att bygga in färdig funktionalitet i produkten. Beskriv därför den nya delen som projektet. Det kan till exempel vara prognoser för många 3PL-kunder med kort historik, eller att optimera plock och rutter tillsammans.

**FoU-avdraget är troligen er största post**
- För anställda som jobbar med FoU får ni dra av 20 % av deras lön från arbetsgivaravgifterna, upp till 3 MSEK per månad.
- Exempel: fyra utvecklare med 50 000 kr i månadslön ger cirka 40 000 kr i avdrag per månad. Det blir nära 1 MSEK över två år.
- Ni behöver inte söka något. Avdraget görs direkt i arbetsgivardeklarationen.
- Arbetet ska vara systematiskt och sikta på ny kunskap eller en ny eller väsentligt förbättrad produkt. Skatteverket granskar mjukvaruutveckling hårt, så dokumentera vem som gör vad.
- Reglerna för hur mycket tid varje anställd måste lägga på FoU har setts över de senaste åren. Kolla Skatteverkets aktuella sida innan ni räknar på det.

**GPU-tid: ni behöver troligen mindre än ni tror**
- Ruttoptimering är ett optimeringsproblem (VRP). Det löses med solvers som OR-Tools, PyVRP eller Timefold på vanliga processorer, och det finns ingen modell att träna.
- Efterfrågeprognoser för lager görs oftast bäst med gradient boosting (till exempel LightGBM) på vanliga processorer. Alternativet är att finjustera en förtränad tidsseriemodell som Chronos eller TimesFM på ett enda GPU. Det handlar om tiotals till några hundra GPU-timmar, inte tusentals.

Billiga vägar till GPU-tid:
1. **Sweden AI Factory** (hette Mimer AI Factory fram till augusti). De erbjuder gratis GPU:er och hjälp av AI-experter för små och medelstora bolag, men villkor kan gälla, till exempel EU:s de minimis-regler för statsstöd.
   - Det minsta spåret heter Playground och söks via EuroHPC. Det ger upp till cirka 5 000 GPU-timmar under 1–3 månader, och besked kommer inom ett par arbetsdagar.
   - Börja med deras kontaktformulär, så hjälper de er välja spår. För ett team på 14 personer kan experterna vara värda mer än själva datorkraften.
   - Två saker att kolla. Det är en superdatormiljö med köer, inte ett vanligt molnkonto. Och ni flyttar kunddata dit, så stäm av mot kundavtalen och GDPR, eftersom ruttdata innehåller adresser.
2. **Hyra per timme.**
   - Hos specialiserade GPU-moln kostar en L40S runt 1 USD i timmen och en H100 ungefär 2–4 USD.
   - Hos AWS, Google och Azure kostar en H100 ungefär 7–12 USD i timmen om man hyr utan avtal.
   - 200 timmar på en L40S blir alltså ett par tusen kronor. Välj datacenter inom EU för kunddata.
3. **Startup-krediter** (AWS Activate, Google, Microsoft) är byggda för unga bolag, ofta med riskkapital. Ni grundades 2016 och ligger troligen utanför. Fråga hellre er nuvarande molnleverantör om krediter för ett proof of concept.

Tre frågor, så kan jag göra det här mer konkret:
1. Har ni någon kund, partner eller högskola utomlands som kunde vara med i ett Eurostars-projekt?
2. Är ni öppna för att driva projektet tillsammans med Jönköping University eller forskningsinstitutet RISE?
3. Hur ser er data ut (antal lagerkunder, antal artiklar, hur lång historik), och hur många av de 14 kommer att jobba med AI-delen?

Källor:
- [Eureka: Eurostars, Call 12 stänger 4 mars 2027](https://www.eurekanetwork.org/programmes-and-calls/eurostars/)
- [Vinnova: Eurostars hösten 2025 (villkor för svenska parter)](https://www.vinnova.se/en/calls-for-proposals/eurostars/eurostars-autumn-2025)
- [Vinnova: Avancerad digitalisering, alla utlysningar](https://www.vinnova.se/en/calls-for-proposals/advanced-digitalization-industrial-2024-04161)
- [Vinnova: Tillämpad AI för industrin](https://www.vinnova.se/en/calls-for-proposals/advanced-digitalization-industrial-2024-04161/industrial-applied-ai-by-advanced-digitalization/)
- [Vinnova: 160 MSEK till AI och digital infrastruktur (april 2026)](https://www.vinnova.se/en/news/2026/042/160-million-for-innovation-in-ai-digital-infrastructure-and-communication-for-swedish-industry/)
- [Vinnova: Innovativa Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026) och [Lunds universitet om villkoren](https://www.ch.lu.se/evenemang/info-meeting-vinnovas-call-innovative-startups-2026)
- [Vinnova: Test och demo för SMF 2026](https://www.vinnova.se/e/utlysning-2026-01600/test-och-demo-for-sma-och-medelstora-foretag-2026)
- [Skatteverket: Forskningsavdrag i arbetsgivardeklarationen](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm)
- [Sweden AI Factory](https://swedenaifactory.se) och [NAISS om namnbytet](https://www.naiss.se/?p=6302)
- [EuroHPC: Playground-åtkomst](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories_en) och [Fast Lane](https://www.eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en)
- [Hostinger: GPU-priser per timme 2026](https://www.hostinger.com/tutorials/?p=158956)

## Founder, turn 2 (simulated)
Tack! 1. Inte säker, vet inte om vi har nån sån utomlands. 2. Inte säker, vet inte riktigt. 3. Inte säker på siffrorna för datan, och vet inte heller exakt hur många av oss som kommer jobba med AI-delen.

## Assistant, turn 2
Det är helt okej att ni inte vet än. Ni behöver inte svaren för att komma igång, och en del av stegen nedan ger er svaren. Planen fungerar även om svaret på alla tre frågorna blir nej.

**Gör nu (oberoende av svaren)**
1. **FoU-avdraget.** Prata med er redovisningskonsult eller revisor. Börja logga tid per person på AI-arbetet från första dagen. Då behöver ni inte veta i förväg hur många som jobbar med det, eftersom tidloggen visar vilka som når upp till kraven.
2. **Sweden AI Factory.** Skicka en kort förfrågan via deras kontaktformulär. Det är gratis, och de hjälper er bedöma hur mycket datorkraft ni egentligen behöver. Det besvarar halva fråga 3 åt er.
3. **En liten proof of concept internt.** Ta en kund och ett lager, med ett par års orderhistorik. Testa prognoser med LightGBM och rutter med OR-Tools, båda på vanliga datorer. Ett par utvecklare under några veckor räcker. Då får ni fram datasiffrorna, ser hur många som behövs och får underlag till en ansökan.

**Datakoll, ungefär en timme**
Be den som kan er databas ta fram fyra siffror:
- Hur många lagerkunder finns i systemet?
- Hur många artiklar har de ungefär?
- Hur många månaders orderhistorik har ni?
- Har ni leveransadresser och tidsstämplar för transporterna?

**Partners: ta reda på det inom två veckor**
- **Utlandet.** Fråga dem som har hand om era kunder om någon kund har lager eller flöden utanför Sverige. Hör också av er till Vinnovas Eurostars-kontakt. De kan hjälpa er hitta partners via finansiärerna i andra länder och via Enterprise Europe Networks partnerdatabas. Bestäm i mitten av januari om deadlinen 4 mars är realistisk. Om inte finns nästa Eurostars-runda (de brukar vara två per år) eller nästa runda av Tillämpad AI.
- **Jönköping University.** De har en forskningsmiljö för tillämpad AI med fokus på flöden, AFAIR, som drivs tillsammans med företag. De forskar också om logistik på Internationella Handelshögskolan. Science Park Jönköping ordnar matchning mellan företag och forskare. Min information om dem är delvis från 2023, så kolla vad som gäller nu. Ett kaffemöte räcker för att se om det är intressant.

Om båda partnerspåren blir nej är planen FoU-avdraget, Sweden AI Factory och er egen budget. Det räcker långt för det här projektet.

Vill du att jag skriver de två mejlen, till Sweden AI Factory och Jönköping University? Då behöver jag bara bolagsnamnet och två eller tre meningar om ert WMS.

Källor:
- [Eureka: partnersökning och Vinnova som första kontakt](https://www.eurekanetwork.org/?p=585)
- [Sweden AI Factory: kontakt](https://swedenaifactory.se/contact-us/)
- [Jönköping University: forskningsprojekt med regionala företag (2023)](https://ju.se/en/about-us/contact-and-press/press/news/news-archive/2023-03-30-three-research-and-innovation-projects-with-ju-awarded-over-sek-15-million.html)
- [Skatteverket: Forskningsavdrag i arbetsgivardeklarationen](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm)
- [Eureka: Eurostars, Call 12 stänger 4 mars 2027](https://www.eurekanetwork.org/programmes-and-calls/eurostars/)
