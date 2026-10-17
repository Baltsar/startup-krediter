# s14 without-skill

## Founder, turn 1
Hej! Vi är två grundare i Närpes som bygger ett AI-system för klimatstyrning i växthus (mest tomat och gurka). Bolaget grundades i fjol höstas. Vi skulle behöva pengar för att anställa en utvecklare och köra en pilot hos tre odlare nästa säsong, plus GPU-tid för att träna modellerna. Vad finns det att söka?

## Assistant, turn 1
Hej! Eftersom bolaget finns i Närpes är det de finländska programmen som gäller. Svenska Vinnova och Almi kräver ett svenskt bolag. Jag ser två vägar till pengar och en till GPU-tid. Vilken pengaväg som passar beror främst på hur mycket eget kapital ni har i bolaget.

**1. Business Finland Sprint passar er bäst, om ni uppfyller kraven**
- Bidraget är 75 000–100 000 €, alltså 75 % av ett projekt på 100 000–133 334 €. Bolag under 5 år får 70 % i förskott.
- Det täcker löner för FoU-arbetet plus 30 % för indirekta personalkostnader, så utvecklaren ni vill anställa ryms. Er egen lön räknas också, men för den som äger minst 10 % räknas högst 4 000 €/mån.
- Kundpilotering räknas som FoU, så piloten hos odlarna passar in. Minst två tredjedelar av projektet ska vara FoU. Försäljning och marknadsföring täcks inte.
- Krav:
  - Finländskt aktiebolag med färre än 50 anställda, och ingen tidigare finansiering från Business Finland.
  - Minst 50 000 € eget kapital i balansen. Det kan vara aktiekapital, SVOP-fond, kapitallån eller ett undertecknat investeringslöfte eller term sheet. Kapital ni redan har gjort av med räknas också.
  - Tillräckligt med pengar för att bära den del som förskottet inte täcker, grovt räknat 47 000–63 000 € beroende på projektets storlek.
  - Två personer som arbetar i Finland, varav minst en heltid i bolaget.
  - En ny lösning med internationell tillväxtpotential. Berätta om marknaden utanför Finland, inte bara Närpes.
- Sprint går att söka löpande sedan 1.9.2026. Först registrerar ni bolaget i My Business Finland (kräver stark autentisering). Sedan följer ett obligatoriskt möte med en expert, och först därefter skickar ni ansökan.

**2. Når ni inte 50 000 €: utvecklingsstöd från Livskraftscentralen i Österbotten**
- Stödet täcker upp till 50 % av högst 100 000 € i godtagbara kostnader, alltså högst 50 000 €.
- Lönen för en ny nyckelperson i projektet kan godkännas, men löner får vara högst hälften av projektkostnaderna. Resten kan vara köpta experttjänster, utredningar och prototyp.
- Närpes ligger inom stödområdet. Bara de centrala delarna av Vasa och Karleby är undantagna.
- Klimatvänliga lösningar som minskar utsläpp är en uttalad prioritering. Om ert system sänker energiåtgången i växthusen, lyft fram det.
- Verksamheten ska ge minst en person i bolaget sin huvudsakliga inkomst.
- Ett annat alternativ är att ta in änglakapital med ett undertecknat term sheet. Då uppfyller ni kapitalkravet för Sprint.

**3. GPU-tid: LUMI AI Factory (CSC, Kajaani)**
- Det är gratis för AI-startups och små och medelstora företag när det gäller innovation. Ni söker via EuroHPC:s portal.
- Playground ger tillgång inom ungefär 2 arbetsdagar. Fast Lane ger upp till 50 000 GPU-timmar, med beslut inom ungefär 4 arbetsdagar. Kontrollera aktuell status i portalen innan ni söker.
- Börja med Playground. En modell för klimatstyrning behöver troligen betydligt mindre än så.
- LUMI har AMD-grafikkort (ROCm). PyTorch fungerar, men kod som är skriven specifikt för CUDA måste anpassas.
- Molnkrediter från Google, AWS och Microsoft finns också. De stora nivåerna kräver i regel investerare i ryggen, och utan dem ger en egen ansökan några tusen dollar.

**Fällor att undvika**
- Kostnader räknas först när ansökan har lämnats in. Skriv inte anställningsavtal eller pilotavtal innan ni har sökt.
- Samma kostnad kan inte få stöd både från Sprint och från Livskraftscentralen.
- Anställer ni någon som är arbetslös arbetssökande kan lönesubvention kombineras med Sprint. Den ska redovisas, och sammanlagt får stödet inte överstiga det belopp som Sprint-beslutet anger.
- Börja nu. Expertmötet tar tid, och piloten ska köras nästa säsong.

**Några frågor, så kan jag säga vilken väg som gäller för er:**
1. Är bolaget ett finländskt Ab? Hur mycket eget kapital finns i balansen i dag (aktiekapital, SVOP, kapitallån, undertecknade investeringslöften)?
2. Arbetar ni båda i Finland, och jobbar minst en av er heltid i bolaget?
3. Har bolaget fått offentligt stöd tidigare (Business Finland, NTM-centralen eller Livskraftscentralen, Leader)?
4. Ungefär vilken budget har ni för utvecklarens lön, och vad kostar piloten hos de tre odlarna?
5. Vilken typ av modeller tränar ni och på hur mycket data? Har ni kört på HPC-kluster förut?

Källor:
- [Business Finland: Sprint, löpande utlysning](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)
- [Sprint, villkor 2.3.2026 (PDF)](https://www.businessfinland.fi/globalassets/finnish-customers/01-funding/08-guidelines--terms/funding-terms/sprint_funding.pdf)
- [Livskraftscentralen i Österbotten: landsbygdens företagsstöd (PDF)](https://maaseutu.fi/wp-content/uploads/2026/03/Landsbygdens-foretagsstod-inriktning-POH-Elinvoimakeskus-2023-2027-Slutlig-1.1.2026.pdf)
- [LUMI: tillgång via AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [EuroHPC: utlysningar för AI Factories](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en)

## Founder, turn 2 (simulated)
1. Ja, finländskt Oy Ab. Vi grundare har lagt in 60 000 € och en lokal ängel 40 000 € i år, men hur det är bokfört (aktiekapital, SVOP osv.) är jag inte säker på.
2. Vi jobbar båda i Finland, men ingen av oss är heltid i bolaget. Agronomen får 50 % lön från bolaget, och utvecklaren jobbar heltid på ett energitechbolag i Vasa och tar ingen lön från oss.
3. Nej, inget offentligt stöd tidigare.
4. Runt 150 000 € totalt för utvecklaren och piloten. Hur det fördelar sig vet vi inte riktigt än.
5. PyTorch på data från LoRaWAN-sensorer som vi lagrar i TimescaleDB, och vi kör på Hetzner idag. Exakt modelltyp och hur mycket data är jag inte säker på. HPC-kluster har vi inte kört på vad jag vet.

## Assistant, turn 2
Tack, det gör bilden mycket tydligare. Kort sagt ser Sprint ut att ligga inom räckhåll, och kravet på eget kapital klarar ni sannolikt. Det som stoppar er i dag är kravet på en person som jobbar heltid i bolaget.

**1. Kravet på heltid måste lösas först**
- Minst en person i teamet måste lägga all sin arbetstid på bolaget. Det är arbetstiden som avgör, inte lönen, och 50 % lön tolkas nog som 50 % arbetstid.
- Har agronomen ett annat jobb? Säkrast är att hon går upp till 100 % i bolaget innan ni söker. Ta upp just den frågan på det obligatoriska expertmötet.
- Den nya utvecklaren kan inte vara heltidspersonen när ni söker. Arbete som avtalats innan ansökan lämnats in godkänns inte, så anställningen ska ske efter att ansökan lämnats in.
- Er utvecklare, grundaren, räknas som den andra teammedlemmen på deltid eftersom han äger en betydande andel, även utan lön. Hans obetalda tid är däremot ingen kostnad som stödet täcker.
- Han bör läsa igenom sitt anställningsavtal i Vasa, särskilt om konkurrerande verksamhet och immateriella rättigheter. Klimatstyrning och energiteknik kan överlappa, och både Business Finland och investerare kommer att fråga.

**2. Eget kapital och likviditet är två olika krav**
- **50 000 € eget kapital:** Grundarnas pengar räknas, men bara om de är bokförda som aktiekapital, SVOP-fond eller kapitallån enligt 12 kap. aktiebolagslagen. Pengar som redan är använda räknas också.
- Ett vanligt aktieägarlån räknas inte. Ett konvertibelt lån från ängeln räknas bara om det uppfyller kraven för kapitallån. Lån kan ofta omvandlas före ansökan, fråga bokföraren.
- Be bokföraren om en balansräkning nu. Ni behöver ändu en kontospecificerad balans- och resultaträkning, högst två månader gammal, som bilaga till ansökan.
- **Likviditet:** För ett fullt projekt (133 334 €) krävs 63 334 € i finansiella nettotillgångar, alltså kassa plus kortfristiga fordringar minus kortfristiga skulder. Det kravet avgörs av hur mycket som finns kvar av de 100 000 €.

**3. Budgeten**
- 150 000 € är mer än Sprints tak på 133 334 € i projektkostnader, vilket ger högst 100 000 € i bidrag. Om agronomens lön inte ingår blir skillnaden större, och ni får välja vilka delar som ska in i Sprint.
- Regler för budgeten:
  - Sprint täcker 75 % av kostnaderna.
  - Löner räknas för högst 11 månader per år, plus 30 % för indirekta personalkostnader.
  - För ägare med minst 10 % räknas högst 4 000 € i månadslön.
  - Molntjänster som Hetzner räknas som hyra av utrustning.
- Anställ utvecklaren i stället för att köpa tjänsten av en konsult. Eftersom stödet täcker mer än 50 % måste varje enskilt köp på 60 000 € eller mer handlas upp offentligt. Om grundaren fakturerar via ett eget bolag räknas det sannolikt som närstående part, och då godkänns kostnaden inte.
- Skaffa avsiktsförklaringar från de tre odlarna nu. De stärker ansökan och räknas inte som inköp. Om ett pilotavtal måste skrivas tidigt behöver det en klausul om att det hävs om ni får avslag.
- Skriv in i pilotavtalen att ni får träna modeller på odlarnas sensordata.

**4. GPU-tid**
- Mät först hur lång en träningskörning är i dag. Tidsserier från LoRaWAN-sensorer brukar inte kräva mycket, så en dedikerad GPU-server hos Hetzner kan räcka, och den kan ingå i Sprint-budgeten.
- LUMI Playground är gratis och gjort för nya användare. Räkna ändå med en tröskel: Slurm-köer, AMD-grafikkort med ROCm, containrar och export av data från TimescaleDB till filer. Se det som ett tillskott för tyngre experiment, inte som er driftmiljö.

**Nästa steg**
1. Kontakta bokföraren och ta reda på hur de 100 000 € är bokförda.
2. Bestäm om agronomen kan gå upp till 100 %, och från vilket datum.
3. Registrera bolaget i My Business Finland och boka expertmötet.

Tre frågor:
1. Hur mycket pengar finns kvar i kassan, och vilka kortfristiga skulder har bolaget?
2. Har agronomen ett annat jobb, och från när kan hon jobba heltid i bolaget?
3. Ingår hennes lön i de 150 000 €?

När jag har svaren gör jag ett utkast till projektplan och budget för Sprint.

Källor:
- [Business Finland: Sprint, löpande utlysning](https://www.businessfinland.fi/en/services/funding/calls/2026/ongoing-sprint-grant-funding/)
- [Sprint, villkor 2.3.2026 (PDF)](https://www.businessfinland.fi/globalassets/finnish-customers/01-funding/08-guidelines--terms/funding-terms/sprint_funding.pdf)
- [Sprint, frågor och svar 8.4.2026 (PDF)](https://www.businessfinland.fi/globalassets/latest/events/2026/qa-about-sprint-funding-8.4.2026.pdf)
- [LUMI: tillgång via AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)
- [LUMI: workshop om att flytta AI-träning till LUMI](https://www.lumi-supercomputer.eu/events/moving-your-ai-training-jobs-to-lumi-a-hands-on-workshop/)
