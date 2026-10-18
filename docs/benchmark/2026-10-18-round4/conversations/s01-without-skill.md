# s01 without-skill

## Founder, turn 1
Hej! Jag är vd på ett logistikbolag i Jönköping, vi kör tredjepartslager + egna lastbilar. Startade 2016, går med vinst, är typ 23 pers. Nu vill vi bygga en egen AI-modell för ruttplanering och prognoser på lagerflödet, ihop med Jönköping University. Budgeten landar på runt 4 mkr över 18 mån. Vad kan vi söka? Vinnova? Har hört nåt om FoU-avdrag också. Och finns det gratis GPU-tid nånstans eller måste vi köpa i molnet?

## Assistant, turn 1
Hej! Det finns något att söka för alla tre delarna. Men räkna inte med att bidrag täcker 4 mkr. Ni får själva stå för en stor del, ofta i form av egen arbetstid. Så här ser det ut idag (18 oktober 2026):

**1. KK-stiftelsen, Forskningsprojekt 26: det mest konkreta just nu**
Den passar bäst för ett samarbete med JU. Deadline är 26 november, alltså om drygt fem veckor.
- Det är JU som söker och får pengarna, inte ni. JU kan söka upp till 4 mkr till sin egen forskartid. Om en del av er budget skulle gå till att betala JU kan den täckas här.
- Minst två oberoende företag ska medfinansiera, främst med egen arbetstid. Tillsammans ska de lägga minst lika mycket som JU söker, och inget enskilt företag får stå för mer än 70 %. Exempel: söker JU 2 mkr ska företagen lägga minst 2 mkr, varav ni högst 1,4 mkr.
- Projektet får starta tidigast 1 juni 2027. Beslut kommer i april 2027.
- JU behöver en disputerad projektledare och en projektägare som skriver under. Fem veckor räcker bara om JU redan har en forskare som vill driva det.
- Ansökan granskas som forskning, med internationell granskning av den vetenskapliga kvaliteten. Ett rent IT-införande klarar sig inte.
[Utlysningstexten](https://www.kks.se/app/uploads/2022/09/Forskningsprojekt-2026.pdf)

**2. Vinnova: inget öppet som passar rakt av idag**
- Närmast var [Tillämpad AI för industrin genom avancerad digitalisering](https://www.vinnova.se/e/avancerad-digitalisering-industriell-2024-04161/tillampad-ai-for-industrin-genom-2025-03809/). Där räknades logistik och transport uttryckligen som industri, med 2–10 mkr per projekt. Den stängde 16 januari 2026, och jag har inte sett något om att den kommer tillbaka.
- [Cybersäkerhet, AI och resiliens](https://www.vinnova.se/en/calls-for-proposals/advanced-digitalization-industrial-2024-04161/cybersecurity-ai-and-resilience) är öppen till 19 januari 2027. Den handlar om säker och robust AI, till exempel validering och spårbarhet, och inte om prognoser eller ruttoptimering. Den passar dåligt om inte det är kärnan i ert projekt.
- FFI har haft utlysningar om [transportlösningar för vägtransporter](https://www.vinnova.se/e/transport-och-mobilitetstjanster-ffi/transport-och-mobilitetstjanster-ffi-2025-03400/), senast med deadline 18 mars 2026. De är värda att bevaka.

Så här mycket kan ni få: ett litet företag får normalt 45 % av sina kostnader för utvecklingsarbete. Med ett verkligt samarbete med JU blir det 60 %. Klassas arbetet som industriell forskning blir det 70–80 %. JU kan få 100 % av sina kostnader. De här utlysningarna har dessutom ett tak på 50 % av projektets totala kostnader. På 4 mkr blir det alltså som mest runt 2 mkr.

**3. FoU-avdraget (forskningsavdrag)**
- Ni betalar lägre arbetsgivaravgifter, motsvarande 20 % av lönen, för anställda som arbetar med FoU.
- Personen måste arbeta minst 50 % av sin tid med FoU och minst 15 timmar i månaden. Ni måste kunna visa det varje månad, till exempel med tidrapporter och projektplan.
- Avdraget gäller bara er egen personal. Det ni betalar till JU eller konsulter ger inget avdrag.
- Skatteverkets definition är snäv. Det ska vara systematiskt arbete som ger ny kunskap, eller som bygger på forskningsresultat för att ta fram väsentligt förbättrade tjänster eller processer. Att införa ett färdigt ruttverktyg räknas troligen inte.
- Bara som illustration: två anställda med 50 000 kr i månadslön som uppfyller kraven i 18 månader ger ungefär 360 000 kr.
- Skatteverket skriver att avdraget inte gäller FoU-projekt som bedrivs i offentlig regi och betalas med offentliga medel. Stäm av med er revisor hur avdraget fungerar ihop med ett bidrag.
- Utredningen SOU 2026:1 föreslår ett större FoU-avdrag eller en skattekredit från 2027. Inget är beslutat.
[Skatteverket om forskningsavdrag](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm) · [KPMG om SOU 2026:1](https://kpmg.com/se/en/insights/newsletters/taxnews/2026/nya-forslag-om-skatteincitament-till-forskning-och-utveckling.html)

**4. GPU-tid**
Först en sak att känna till: ruttplanering är oftast optimering som körs på vanliga processorer. Prognoser på lagerflöden kräver sällan stora GPU-kluster. En "egen AI-modell" betyder inte att ni måste träna en stor modell från grunden. GPU blir därför oftast en liten del av budgeten, men det beror på vad JU föreslår. Det finns tre gratis vägar:
- **Via JU:** forskare vid svenska lärosäten kan söka gratis beräkningstid hos NAISS. Den får användas till forskningsdelen, inte till ert driftsystem.
- **Mimer, Sveriges AI-fabrik** (Linköping, drivs av LiU och RISE): erbjuder gratis beräkningskraft och expertstöd för innovation. Erbjudandet riktar sig främst till AI-startups och små AI-företag, så fråga dem om ni räknas. En ny superdator beställdes i april 2026, och jag har inte sett att den är i drift än.
- **EuroHPC:s AI-fabriker** har [snabbspår för små företag](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en): Playground för att testa, och Fast Lane för upp till 50 000 GPU-timmar.

**Fyra frågor så att jag kan ge ett skarpare svar:**
1. Vem gör jobbet: er egen personal, nyanställda, JU eller konsulter? Ungefär hur fördelar sig de 4 mkr?
2. Finns det ett andra företag som kan vara med, till exempel en kund eller er TMS/WMS-leverantör?
3. Måste ni starta nu, eller kan ni vänta till sommaren 2027?
4. Ligger omsättningen eller balansomslutningen under 10 miljoner euro, och ingår ni i en koncern? Det avgör om ni räknas som ett litet företag.

## Founder, turn 2
1. Vår egen IT-personal, en dataingenjör och två systemutvecklare, plus JU. Exakt hur de 4 mkr fördelas är jag inte säker på än.
2. Inte säker. Vårt WMS är egenutvecklat, så där finns ingen leverantör.
3. Inte säker.
4. Omsättningen var 61 mkr 2025, så under 10 miljoner euro. Balansomslutningen vet jag inte på rak arm. Och ja, vi ingår i en koncern: ett danskt börsnoterat logistikbolag äger 70 % sedan 2023, vi grundare har kvar 30 %.

## Assistant, turn 2
Tack, det här ändrar en del. Viktigast är ägarbilden.

**Ni räknas troligen som ett stort företag**
Om ett annat företag äger mer än 50 % räknas ni enligt EU:s definition som "anknutna" till det. Då gäller hela koncernens anställda, omsättning och balansomslutning, inte bara era 23 personer och 61 mkr. Att ni grundare äger 30 % spelar ingen roll.

För att vara ett litet eller medelstort företag måste koncernen ha färre än 250 anställda. Dessutom måste antingen omsättningen vara högst 50 miljoner euro eller balansomslutningen högst 43 miljoner euro. Ett börsnoterat logistikbolag klarar nästan säkert inte det. Kolla koncernens siffror med ägarens ekonomiavdelning. ([EU-kommissionen om definitionen](https://single-market-economy.ec.europa.eu/smes/sme-fundamentals/sme-definition_en))

**Det här från mitt förra svar gäller troligen inte er:**
- Stödnivåerna jag gav för små företag (45–80 %) och att ni som mest skulle få runt 2 mkr på 4 mkr.
- Gratis beräkningstid hos Mimer och EuroHPC.

**Vinnova**
- Stora företag får 25 % i bidrag för utvecklingsarbete, eller 40 % om ni samarbetar på riktigt med JU. Industriell forskning ger 50 respektive 65 %. ([Stödnivåer i en tidigare AI-utlysning](https://www.vinnova.se/e/avancerad-digitalisering-industriell-2024-04161/tillampad-ai-for-industrin-genom-2025-03809/))
- JU kan fortfarande få upp till 100 %. Ju mer av forskningen som ligger hos JU, desto större del av budgeten kan bidrag täcka. Taket på 50 % av projektets totala kostnad gäller fortfarande.
- Utlysningar som bara riktar sig till små och medelstora företag faller bort.
- I den [Vinnova-utlysning jag läste](https://www.vinnova.se/en/calls-for-proposals/advanced-digitalization-industrial-2024-04161/cybersecurity-ai-and-resilience) räknas företag i samma koncern som en enda part. Den danska ägaren kan alltså inte vara er andra part.

**KK-stiftelsen: fungerar fortfarande**
- KK har [ingen storleksgräns](https://www.kks.se/samproduktion/vad-menas-med-naringsliv/) för medfinansierande företag, och pengarna går ändå till JU.
- Det andra företaget måste vara oberoende av er. En ägare med 70 % räknas inte.
- Ni har inget köpt WMS, så det naturligaste är en kund. Prognoser på lagerflödet bygger på kundens order och försäljning, så kunden har egen nytta av resultatet. Andra alternativ är leverantören av telematiksystemet i lastbilarna eller ett mjukvarubolag.

**FoU-avdraget**
- Det påverkas inte av storleken. Taket på 3 mkr i månaden delas inom koncernen, men det når ni inte.
- Det som avgör är tiden. Dataingenjören och utvecklarna måste lägga minst halva arbetstiden på FoU, varje månad. Drift, support och underhåll av ert WMS räknas inte. Sköter de den dagliga IT:n är 50 % svårt att nå.
- Bara som illustration: tre personer med 50 000 kr i månadslön som uppfyller kraven i 18 månader ger ungefär 540 000 kr.

**GPU**
- EuroHPC:s AI-fabriker, där Mimer ingår, är [gratis för små och medelstora AI-företag och startups](https://lumi-supercomputer.eu/access-calls-for-ai-factories/). Andra företag hänvisas till betald användning. Räkna med att betala.
- Via JU gäller samma som innan: forskarna kan söka gratis tid hos NAISS för forskningsdelen.
- Ruttoptimering och lagerprognoser kräver oftast lite GPU. Molnkostnaden blir troligen liten jämfört med lönerna.

**Ett möjligt upplägg, eftersom ni inte har bestämt när ni ska starta**
- Ett bidrag måste sökas innan arbetet det ska täcka har börjat. Det som era tre börjar bygga nu kan ett senare Vinnova-bidrag inte täcka. Det betalar ni själva.
- Det ni startar nu kan kanske ge FoU-avdrag, men bara om det är utveckling som bygger på forskningsresultat. Att förbättra ert eget system räcker troligen inte. Dokumentera tiden från första månaden ändå.
- Håll forskningsfrågan med JU separat. JU kan söka KK-stiftelsen senast 26 november, och då kan projektet starta sommaren 2027.

**Tre frågor:**
1. Har koncernen redan ett data- eller AI-team, eller ett verktyg för ruttplanering? Behöver ägaren godkänna hur data och resultat delas? Finns verktyget redan blir det svårare att visa att ert projekt är nytt, både för bidrag och för FoU-avdraget.
2. Vilken kund skulle kunna vara med och dela data?
3. Har ni en kontakt på JU som har doktorsexamen och kan tänka sig att söka till 26 november?
