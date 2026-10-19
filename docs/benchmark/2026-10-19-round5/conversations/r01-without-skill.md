# r01 without-skill

## Founder, turn 1
hej! vi är ett litet ai-bolag i gbg med 4 anställda och håller på med FoU typ hela tiden. hörde att man kan få forskningsavdrag på arbetsgivaravgiften?? kan vi dra av för alla fyra? måste man ansöka nånstans innan eller fyller man bara i det på AGI:n? och ungefär hur mkt blir det

## Assistant, turn 1
Hej!

Kort svar: ja, forskningsavdraget finns. Man ansöker inte i förväg, och det är 20 % av lönen för den som kvalar in. Men "FoU" betyder något snävare här än i vardagsspråk, och det är där det avgörs.

**Kan ni dra av för alla fyra?**
Bara för den som en viss månad jobbat med FoU minst hälften av sin faktiska arbetstid och minst 15 timmar. Det prövas per person och månad.
- Det ska vara direkt FoU. Ledning, sälj, support, drift, kvalitetssäkring och marknad räknas inte. I ett bolag på fyra är det ofta vd:n som hamnar under 50 %.
- Grundare räknas om de tar ut lön med arbetsgivaravgift. Utan lön finns inget att dra av.
- Inte för den som fyllt 67 vid årets ingång.
- En svag månad, t.ex. semester, går ändå om personen kvalade in de fyra månaderna innan och inte bytt arbetsuppgifter.

**Det viktigaste: vad räknas som FoU?**
Forskning är systematiskt, kvalificerat arbete som tar fram ny kunskap. Utveckling är att använda forskningsresultat för att ta fram nya eller väsentligt förbättrade produkter, och forskningsresultaten ska vara avgörande. Skatteverket har länge varit restriktiva med mjukvaruutveckling. Att bygga produkt ovanpå befintliga modeller och API:er, eller vanlig ML-engineering, räcker ofta inte.

**Måste man ansöka innan?**
Nej. Ni gör avdraget själva i arbetsgivardeklarationen varje månad:
- ruta 470: underlaget, alltså lönen till dem som kvalar in
- ruta 475: själva avdraget

Men ni måste kunna visa att kraven är uppfyllda per person och månad om Skatteverket frågar. Spara tidrapporter, projektbeskrivningar och hur arbetet bygger på forskning. Underkänns avdraget i efterhand får ni betala tillbaka med ränta och kan få skattetillägg.

**Hur mycket blir det?**
20 % av bruttolönen för varje person som kvalar in. Arbetsgivaravgiften går då från 31,42 % till 11,42 % för dem.

Exempel: 50 000 kr/mån i lön ger 10 000 kr/mån, ca 120 000 kr/år per person. Kvalar alla fyra in på den lönen blir det ca 480 000 kr/år. Taket på 3 miljoner kr/mån når ni inte.

Får ni växa-stöd för någon blir den återbetalningen mindre, så nettovinsten för just den personen blir lägre.

**Bakåt i tiden**
Har ni kvalat in tidigare utan att göra avdraget kan ni rätta gamla arbetsgivardeklarationer upp till sex år bakåt. Då gäller reglerna som fanns just då. Före juli 2021 var kravet 75 % av arbetstiden, och procentsats och tak var andra.

**Förslag från 2027, inte beslutat**
Regeringen har föreslagit att 15-timmarskravet tas bort och att FoU-definitionerna breddas från 1 januari 2027. Det finns också ett förslag om ett frivilligt extra avdrag på 200 % av FoU-lönekostnader i inkomstskatten. Det har varit val sedan dess, så kolla läget innan ni räknar med något av det.

Mitt tips: skriv en kort projektbeskrivning per FoU-spår och börja tidrapportera FoU per person nu. Gör sedan en ärlig bedömning av vem som når 50 %. Är ni osäkra på om arbetet räknas, låt en skatterådgivare läsa beskrivningen innan ni gör avdraget.

Källa: Skatteverket, [Forskningsavdrag i arbetsgivardeklarationen](https://skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm)

## Founder, turn 2
ok tack! om vi vill börja dra av redan på nästa lönekörning, vad behöver vi konkret ha klart innan och vad ska vi ge till den som gör AGI:n?

## Assistant, turn 2
Hej!

En sak först som gör det enklare än det låter: avdraget görs i arbetsgivardeklarationen, inte i lönekörningen. Lönerna och lönebeskeden ändras inte. Det enda som ändras är rutorna 470 och 475, och att ni betalar mindre arbetsgivaravgift.

**Tidslinjen**
Betalar ni ut lön i slutet av oktober hör den till AGI:n för oktober, som ska vara inne senast 12 november. Kravet på 50 % och 15 timmar prövas för hela kalendermånaden. Ni behöver alltså underlaget för hela oktober när AGI:n lämnas, inte redan på lönedagen.

Betalar ni lön i efterskott (oktoberlön i november), fråga Skatteverket eller en rådgivare vilken månad som ska prövas.

**Det här behöver ni ha klart**

1. **En projektbeskrivning per FoU-spår.** 1–2 sidor räcker. Den ska visa:
   - vilket tekniskt problem ni försöker lösa och varför det inte går med känd teknik
   - vilka forskningsresultat ni bygger på och varför de är avgörande
   - hur ni jobbar systematiskt: hypoteser, experiment, utvärdering, även det som misslyckats
   - vad som inte är FoU hos er, t.ex. produktbygge på färdiga modeller, drift, integrationer, kundanpassning och sälj

2. **Tidrapporter per person.** Total faktisk arbetstid och FoU-tid per projekt, helst per dag eller vecka. Semester och sjukfrånvaro räknas inte som arbetstid. Dela upp tiden så att FoU skiljs från allt annat, det är där Skatteverket granskar. Börja i dag. Oktober hittills får ni rekonstruera från kalendrar, commits och tickets, men det håller sämre än löpande rapportering.

3. **En månadssammanställning.** Per person: totala timmar, FoU-timmar, andel, och om personen kvalar in (minst 50 % och minst 15 timmar). Vd godkänner den och ni sparar den. Det är ert beslut om avdraget.

4. **Övrigt som Skatteverket nämner som underlag:** bemanningsplan (vem jobbar med vad), hur FoU:n finansieras (egna medel, bidrag, kundbetalt) och forskningsrapporter. Lägg gärna till en rad om varje persons kompetens, eftersom lagen kräver kvalificerat arbete.

**Det här ger ni den som gör AGI:n, varje månad**
- Vilka personer som kvalar in just den månaden. Ingen stående lista, det kan ändras mellan månader.
- Besked om någon får växa-stöd eller har sänkt ungdomsavgift. Då blir stödet eller avdraget mindre.

Hen fyller sedan i:
- **ruta 470:** hela avgiftsunderlaget den månaden för dem som kvalar in, alltså lön plus ev. bonus och skattepliktiga förmåner
- **ruta 475:** 20 % av det beloppet

Ni skickar inget underlag med AGI:n, men Skatteverket kan begära in det. Den som gör AGI:n bedömer inte om det är FoU, det ansvaret ligger på er.

**Mitt råd för första månaden**
Ta bara med dem som tydligt kvalar in och där tidsunderlaget är bra. Är oktober svår att belägga, börja med november. Oktober kan ni rätta i efterhand när underlaget finns. Det är billigare än att få avdraget underkänt.

Kolla också läget inför januarilönen. Blir de föreslagna ändringarna av kan reglerna ändras från 1 januari 2027.

Källor: Skatteverket, [Forskningsavdrag i arbetsgivardeklarationen](https://skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm), och [lag (2023:747)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023747-om-sarskilt-avdrag-vid-berakning_sfs-2023-747/)
