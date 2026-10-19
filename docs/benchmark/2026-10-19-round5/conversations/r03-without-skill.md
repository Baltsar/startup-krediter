# r03 without-skill

## Founder, turn 1
hej! vi är en startup i linköping som tränar en egen visionmodell för att hitta defekter i gjutgods. behöver typ 20-30k gpu-timmar. kan vi söka beräkningstid via SNIC? tänkte Berzelius eller Alvis. vad krävs, kostar det nåt och hur lång tid tar det innan man får tillgång?

## Assistant, turn 1
Hej!

Kort svar: nej, som företag kan ni inte söka Berzelius eller Alvis själva. Men det finns en gratis väg som passar er bättre, och den drivs från Linköping.

**1. SNIC, Berzelius och Alvis**

- SNIC finns inte längre. NAISS tog över den 1 januari 2023, och man söker via SUPR (supr.naiss.se).
- NAISS-resurser är gratis, men bara för forskare vid svenska lärosäten. Huvudsökande (PI) måste vara minst doktorand för Small och minst biträdande lektor för Medium.
- Berzelius är inget NAISS-system. Det är en donation från Knut och Alice Wallenbergs stiftelse (KAW) till NSC. PI måste vara minst biträdande lektor med KAW-koppling, till exempel ett KAW-anslag eller WASP. Projektet ska vara AI/ML-forskning som ska publiceras, och det får inte hantera känsliga data.
- Alvis går inte att söka längre. Det avvecklas och ersätts av NAISS nya system Arrhenius, som också är akademiskt.

Den enda vägen in till Berzelius för er är ett riktigt forskningsprojekt med en forskargrupp där en behörig forskare står som PI. Då ska resultaten publiceras och datorn får bara användas för det syfte ansökan beskriver. Det passar dåligt om ni vill träna er egen produktmodell på kunddata.

**2. Det som passar er: EuroHPC AI Factories via Sweden AI Factory**

Sweden AI Factory (tidigare Mimer) drivs av LiU och RISE. Den hjälper svenska AI-startups att få beräkningstid via EuroHPC.

*Kostar det något?* Nej. Industrispåren är gratis för AI-startups och små och medelstora företag som använder tiden för innovation. Ni får beräkningstid, inte pengar. Fråga om tiden räknas som stöd av mindre betydelse (de minimis) för er.

*Vilket spår?* 20–30k GPU-timmar ryms i Fast Lane:

| Spår | Storlek | Tid till tillgång | Period |
|---|---|---|---|
| Playground | upp till 5 000 GPU-h | inom 2 arbetsdagar | 1–3 mån |
| Fast Lane | upp till 50 000 GPU-h | godkänt inom 4 arbetsdagar | 1–3 mån |
| Large Scale | över 50 000 GPU-h | fasta deadlines var 2:a vecka | 3–12 mån |

*Vad krävs?*
- Ni är en AI-startup eller ett litet eller medelstort företag i EU.
- Fast Lane är för team som redan kan köra på HPC-kluster. Er träning behöver alltså kunna köras på flera GPU:er via ett kösystem.
- Ni söker tid på ett enda system och använder den inom högst 3 månader. 25k GPU-h på 3 månader motsvarar ungefär 11–12 GPU:er dygnet runt.
- Har ni inte kört på ett kluster förut, börja med Playground och testa först.

*Tre saker att ha koll på:*
- Ni hamnar inte på Berzelius. Den nya svenska AI-datorn är beställd, men installationen startar under 2026 och inget startdatum är publicerat. I dag körs ni troligen på ett annat EuroHPC-system i Europa.
- En GPU-timme är inte lika mycket värd på alla GPU-typer. Räkna om behovet när ni vet vilket system ni får.
- Kolla att era kundavtal tillåter att gjutgodsbilderna flyttas till en extern dator.

**3. Om ni hellre vill betala**

PDC på KTH säljer CPU- och GPU-timmar till företag, kontakt business-unit@pdc.kth.se. Deras dator Dardel stängs vid årsskiftet, så fråga vad de erbjuder efter det. EuroHPC har också betald kommersiell tillgång för industri.

**Nästa steg**

Mejla Sweden AI Factory på info@swedenaifactory.se eller använd formuläret på swedenaifactory.se/contact-us. Skriv kort: visionmodell för defekter i gjutgods, 20–30k GPU-timmar, ramverk, och om ni kört på kluster förut. Be dem föreslå spår och system. Ansökan görs sedan på EuroHPC:s ansökningsportal.

Källor:
- NAISS ersatte SNIC: https://www.pdc.kth.se/about/pdc-news/naiss-rounds-for-compute-storage-allocations-in-2023-open-1.1218879
- NAISS behörighet och tider: https://hpc.pages.naiss.se/user-documentation/support-docs/allocations/
- Berzelius villkor: https://www.nsc.liu.se/support/systems/berzelius-resource-allocation
- Berzelius-rundan 2026: https://supr.naiss.se/round/berzelius2026
- Alvis och Arrhenius: https://supr.naiss.se/round/small
- Sweden AI Factory: https://swedenaifactory.se/all-services/access-to-compute-resources/
- EuroHPC Fast Lane: https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en
- EuroHPC, gratis för AI-startups: https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en
- Ny svensk AI-dator: https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en
- PDC för företag: https://www.kth.se/en/2.79567/hpc-services/computing-systems/dardel-hpc-system

## Founder, turn 2
ok tack, då kollar vi på sweden ai factory och fast lane istället. går det att söka nu men få tiden att börja i januari 2027? vi behöver köra jan–mars.

## Assistant, turn 2
Hej!

Kort svar: troligen inte. Fast Lane är gjort för att ni ska komma igång direkt, inte för att boka tid i förväg. Planera i stället att skicka in ansökan i början av januari.

**Varför det inte fungerar att söka nu**

- Fast Lane är öppen hela tiden och bedöms löpande, först till kvarn. Målet är godkännande inom 4 arbetsdagar.
- Tiden delas ut i perioder om 1, 2 eller 3 månader. Varken villkoren eller EuroHPC:s sidor beskriver något sätt att välja ett senare startdatum.
- Perioden kan inte förlängas och ni kan inte få fler timmar. Söker ni nu börjar tiden troligen redan i november och tar slut innan ni behöver den.

Det enda sättet att få en senare start är om Sweden AI Factory säger att det går. Fråga dem först (se mejlet nedan).

**Förslag på tidsplan**

| När | Vad |
|---|---|
| Nu | Mejla Sweden AI Factory och fråga om startdatum i januari. |
| November | Sök Playground (5 000 GPU-timmar, tillgång inom 2 arbetsdagar). Testa er träning, helst på det system ni vill ha i januari. Välj 1 månad. |
| December | Fyll i Fast Lane-ansökan med siffror från testet. Låt Sweden AI Factory granska den. |
| Måndag 4 januari | Skicka in Fast Lane och be om 3 månader. Räkna med tillgång runt 8–12 januari. Tiden räcker då en bit in i april. |

Två saker om tidsplanen:
- Låt Playground vara slut innan ni söker Fast Lane. En huvudsökande ska i princip bara ha en beviljad ansökan åt gången.
- Den tekniska delen måste vara komplett när ni skickar in. En ofullständig ansökan avvisas utan bedömning.

**Att ha koll på**

- Tiden delas ut tills den reserverade kapaciteten är slut. MareNostrum5 ACC och JUPITER Booster tar redan nu inte emot Fast Lane. Ha ett reservsystem om ert förstahandsval är fullt i januari.
- Huvudsökande ska vara anställd hos er när ni söker och minst 3 månader efter att perioden slutar. Med en period till april betyder det minst till juli 2027.
- Sweden AI Factorys egen dator väntas vara i drift tidigt 2027. Räkna inte med att den finns i januari.

**Mejl att skicka nu** till info@swedenaifactory.se

> Hej! Vi är en startup i Linköping som tränar en visionmodell för defekter i gjutgods. Vi behöver 20–30k GPU-timmar under januari–mars 2027 och vill söka Fast Lane.
> 1. Kan vi söka nu och få startdatum i januari?
> 2. Vilket system rekommenderar ni, och har det plats i januari?
> 3. Kan vi köra Playground på samma system i november för att testa?
> 4. Löper Fast Lane-utlysningen vidare över årsskiftet utan uppehåll?
> Vi använder [ramverk] och har [/inte] kört på kluster förut.

Svarar de att en senare start går, följ deras väg i stället för tidsplanen ovan.

Källor:
- EuroHPC Fast Lane (löpande bedömning, 4 arbetsdagar, 1–3 månader, system som är fulla): https://eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en
- Villkoren för AI Factories industrispår (inga förlängningar, en ansökan åt gången, krav på huvudsökande, komplett teknisk del): https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms%20of%20Reference%20-%20AIF%20Access%20Calls.pdf
- Sweden AI Factory, spår och tider: https://swedenaifactory.se/all-services/access-to-compute-resources/
- Sweden AI Factory FAQ (ingen förlängning, egen dator tidigt 2027): https://swedenaifactory.se/about/faq/
