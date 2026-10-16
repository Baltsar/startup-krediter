TURN 1:
Hej! Ja, ni har en god chans. Det bästa gratisalternativet för er är troligen EU:s AI Factories, som drivs av EuroHPC. Sveriges AI Factory heter Mimer och finns i Linköping. AI-startups och SME:er får GPU-tid där gratis, så länge den används för innovation. Ett svenskt AB med fyra anställda räknas som SME, så storleken stoppar er inte.

Tre vägar att titta på, i den här ordningen:

1. **EuroHPC AI Factories (via Mimer eller en annan AI Factory i EU).** Det finns tre ansökningsnivåer:
   - **Playground** är till för nybörjare med små behov. Man kan söka när som helst, och ansökningar behandlas i turordning.
   - **Fast Lane** ger upp till 50 000 GPU-timmar under 1–3 månader. Beslut kommer inom 4 arbetsdagar.
   - **Large Scale** gäller för mer än 50 000 GPU-timmar. Där finns flera ansökningsdatum.

   Det här kostar inget för AI-startups. Det passar ofta bra för en finjustering.
2. **Molnkrediter från de stora leverantörerna,** som Google for Startups, AWS Activate och Microsoft for Startups. Det här har jag inte kontrollerat nu. Belopp och krav ändras ofta, och de högre nivåerna kräver oftast en investerare eller accelerator i ryggen. Kolla deras sidor innan ni räknar med något.
3. **NVIDIA Inception** ger främst rabatter och nätverk, inte gratis GPU-tid. Det är bra att ha, men det löser inte er beräkningsfråga.

Kort sagt: börja med AI Factories. Vill du att jag går igenom hur man söker där?

Källor: [EuroHPC – AI Factories access calls](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls_en), [LUMI – Access calls for AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/), [RISE om Mimer](https://www.ri.se/en/mimer-swedens-ai-factory-powers-up-supercomputing-race-to-tomorrows-ai-solutions), [EuroHPC – Sverige](https://eurohpc-ju.europa.eu/ai-factories/sweden_en)

TURN 2:
Här är mer om EuroHPC AI Factories och Mimer.

**Vad det är**
EU har finansierat ett antal "AI Factories". Det är superdatorcentra med GPU-kluster, och de erbjuder också experthjälp. Sveriges heter Mimer och drivs av NAISS vid Linköpings universitet tillsammans med RISE. Mimer startade i april 2025 och har sedan dess hjälpt över 200 europeiska företag. EuroHPC skrev i april 2026 kontrakt om en ny AI-superdator i Linköping som byggs för Mimer. Fram till den är på plats kör ni på befintliga system. Det kan vara Mimers nuvarande kluster eller en annan AI Factory, till exempel LUMI i Finland.

**Vad det kostar**
Inget, så länge ni är en AI-startup eller SME och använder tiden för innovation, alltså att utveckla er produkt. Företag som inte uppfyller det kan köpa tid i stället.

**Vilken nivå ni ska söka**
- **Playground:** Passar om ni aldrig har kört på en superdator. Tilldelningen gäller 1, 2 eller 3 månader på ett system. Ni skickar in en kort ansökan som förklarar varför projektet är relevant. Man kan söka när som helst, ansökningar tas i turordning och ni kan få åtkomst inom 2 arbetsdagar. **Obs:** EuroHPC har haft en sida som säger att Playground är tillfälligt stängt medan de byter plattform. Samtidigt listas utlysningen som öppen. Kolla läget på deras sida innan ni söker.
- **Fast Lane:** Passar om ni är vana vid HPC, till exempel Slurm, containers och kluster med flera noder. Ni kan få upp till 50 000 GPU-timmar under 1–3 månader på ett system. Ni får beslut inom 4 arbetsdagar och experthjälp från den AI Factory ni väljer. För en finjustering av en modell i normal storlek räcker 50 000 GPU-timmar oftast med god marginal.
- **Large Scale:** Gäller för mer än 50 000 GPU-timmar under upp till ett år. Där finns flera ansökningsdatum, och beslut kommer inom cirka 10 arbetsdagar.

**Så kommer ni igång**
1. Räkna ut ungefär hur mycket ni behöver: modellstorlek, datamängd, antal körningar och GPU-timmar. Det ska stå i ansökan.
2. Kontakta Mimer först, på info@mimer-ai.eu (finns på [EuroHPC:s Sverigesida](https://eurohpc-ju.europa.eu/ai-factories/sweden_en)). De kan hjälpa er välja nivå och system, och fråga gärna vilken hårdvara som finns ledig just nu.
3. Sök via EuroHPC:s sidor för [Playground](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/playground-access-ai-factories_en) eller [Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en).

**Saker att tänka på**
- Det här är superdatorer, inte en molntjänst där ni bara startar en maskin. Räkna med Slurm, köer och containers.
- Ni kan bara söka tid på ett system per ansökan.
- Gratis GPU löser inte allt. Er data, er pipeline och er utvärdering behöver vara klara innan klockan börjar ticka.
- Jag hittade inga detaljer om rapportkrav eller villkor kring IP. Fråga Mimer om det innan ni skickar in.

Källor: [EuroHPC – Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en), [EuroHPC – Playground](https://www.eurohpc-ju.europa.eu/playground-access-ai-factories-temporarily-closed_en), [EuroHPC – ny superdator i Sverige (2026-04-21)](https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en), [LUMI – Access calls for AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/), [RISE om Mimer](https://www.ri.se/en/mimer-swedens-ai-factory-powers-up-supercomputing-race-to-tomorrows-ai-solutions)