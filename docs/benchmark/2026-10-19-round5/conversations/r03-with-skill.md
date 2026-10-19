# r03 with-skill

## Founder, turn 1
hej! vi är en startup i linköping som tränar en egen visionmodell för att hitta defekter i gjutgods. behöver typ 20-30k gpu-timmar. kan vi söka beräkningstid via SNIC? tänkte Berzelius eller Alvis. vad krävs, kostar det nåt och hur lång tid tar det innan man får tillgång?

## Assistant, turn 1
Hej! SNIC finns inte längre. NAISS tog över 2023, och enligt NAISS allokeringssida i dag får bara forskare vid svenska lärosäten (minst doktorand) gratis beräkningstid, inte bolag. Berzelius kräver enligt sin access-sida ett akademiskt forskningsprojekt med Wallenberg-finansiering. Alvis är pensionerad enligt C3SE och ersatt av Arrhenius.

För den som får söka är det gratis, och Small granskas varje vecka och Berzelius varje månad, men ingen av vägarna är öppen för ert AB.

- Det som ändrar det: en forskare vid t.ex. LiU söker som projektledare (PI) för ett forskningsprojekt ni deltar i. För Berzelius krävs dessutom att PI:n har eget Wallenberg-anslag och att arbetet ska publiceras.
- Nästa steg för företag: NAISS driver tillsammans med RISE Sweden AI Factory, som gratis hjälper bolag att söka EuroHPC-timmar. Deras FAQ nämner i dag Fast Lane, upp till 50 000 GPU-timmar i högst tre månader. Vill ni att jag går igenom den? https://swedenaifactory.se/about/faq/

## Founder, turn 2
ok, synd men tack! ja gärna, gå igenom fast lane. kan vi som AB söka den? vad krävs, kostar det nåt och hur lång tid tar det innan man får tillgång?

## Assistant, turn 2
Ja, som svenskt AB kan ni söka EuroHPC AI Factories Fast Lane Access. Villkoren öppnar den för företag och startups i EU-länder, och fem frågor avgör resten.

Det kostar inget: enligt EuroHPC:s Access Policy är spåret gratis för AI-SME:er och startups i innovationssyfte. Sidan anger godkännande inom 4 arbetsdagar; villkoren säger först till kvarn tills timmarna tar slut, sedan onboarding hos AI-fabriken utan publicerad tid. Era 20–30 000 GPU-timmar ryms under taket på 50 000.

**Det som avgör**

1. Är projektledaren anställd i bolaget nu och minst tre månader efter perioden? Villkoren kräver det.
2. Är bolaget momsregistrerat? Momsnumret är beviset på att ni är ett företag.
3. Har ni e-post på egen domän? Alla adresser i ansökan måste vara jobbadresser.
4. Kör ni redan träningskoden på ett HPC-system? Fast Lane är för HPC-vana; saknade tekniska data ger avslag.
5. Vilken kod, vilket system och hur många månader? Formuläret kräver det, inte bara timantalet.

**Status**

```
◐  EuroHPC AI Factories Fast Lane Access
●  ett bolag
○  anställd projektledare efter allokeringen
○  momsregistrerat
○  e-post på egen domän
○  arbetslast definierad: kod, ett system, GPU-timmar
○  teamet kör redan sin kod på ett HPC-system
?  Är projektledaren anställd minst tre månader efter att allokeringen tar slut?
→  Upp till 50 000 GPU-timmar, 1 till 3 månader, ett system
```

**Innan ni söker**

- Sök i 2026 års utlysning, öppen till 31 december 2026 enligt portalens call-lista i dag.
- Sidans Apply Now-knapp leder till 2025 års utlysning, som stängde 31 december 2025.
- Konto på access.eurohpc-ju.europa.eu; registreringen har en reCAPTCHA som ni löser själva.
- Formuläret på engelska, med egenbedömning av behörighet och etik.
- Timmarna gäller träning; produktionsdrift är inte tillåten, inferens bara i liten motiverad del.
- Civilt syfte och förenligt med EU:s AI-förordning.
- Ingen annan pågående EuroHPC-tilldelning för samma projekt.
- En Fast Lane-tilldelning per projektledare åt gången; ingen förlängning, inga extra timmar.
- Data och modeller förblir era, och startups får använda dem kommersiellt.
- Efter beviljande: skriv under AI-fabrikens Acceptable Use Policy innan ni får åtkomst.
- Slutrapport inom tre månader, med energi och CO2; EuroHPC får publicera den efter ett år.
- Nämn EuroHPC och AI-fabriken i publikationer.

**Oklart**

- Vad "HPC-vana" kräver definieras inte; fråga aif.access@eurohpc-ju.europa.eu eller Sweden AI Factory.
- Vilka system som är öppna och gränsen per system står inte på sidan; fråga aif.access.
- Villkoren: ni publicerar resultat utom konfidentiella delar. Access Policy: SME:er undantas. Fråga aif.access.

**Nästa steg:** registrera konto, öppna Fast Lane 2026, välj system och fyll i formuläret; skicka trycker ni själva.
https://access.eurohpc-ju.europa.eu/calls/59

Vill ni att jag skriver ansökan med er när ni har svaren på frågorna ovan?
