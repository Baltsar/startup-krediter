# r07 without-skill

## Founder, turn 1
Bor i Malmö men vårt bolag är ett danskt ApS (startade det när jag jobbade i Köpenhamn). Vi gör en budgetapp för unga som håller koll på prenumerationer och autogiron. Kan jag söka svenska grejer typ Almi eller Vinnova eller måste allt gå via Danmark? Funderar på att starta ett svenskt AB också om det behövs

## Assistant, turn 1
Kort svar: inte med ApS:et ensamt. De svenska statliga pengarna kräver i praktiken ett svenskt aktiebolag med verksamhet i Sverige. Ett svenskt AB kan alltså behövas, men starta det inte bara för att kunna söka. Det har konsekvenser.

**Vad som gäller**

- **Vinnova Innovativa startups 2026** kräver ett svenskt aktiebolag som har verksamhet i Sverige. Bolaget får vara högst 10 år gammalt, räknat från registreringen hos Bolagsverket, och ha högst 10 anställda. Ni kan få upp till 500 000 kr. Utlysningen är öppen nu och stänger **12 januari 2027 kl 14:00**. Beslut kommer 23 mars 2027. ApS:et kan inte söka. Ett nytt AB kan söka, men om ApS:et äger det räknas hela koncernen in i storleksgränserna. Vinnova vill också se kunskap som är svår att kopiera. En app som spårar prenumerationer får det tufft om den inte har något tekniskt unikt, till exempel egen klassning av transaktioner eller något kring open banking. Skriv ärligt vad som är svårt att kopiera hos er.
- **Almi** (Almi Syd för Malmö) lånar ut till företag som är registrerade och driver verksamhet i Sverige. Innovationslånet börjar på 50 000 kr och täcker högst halva finansieringsbehovet. Du som nordisk medborgare är inget problem. Problemet är att bolaget är danskt. Jag hittade inga regler för filial till utländskt bolag, så ring Almi Syd och fråga. Räkna med ett nej.
- **Danmark går redan nu med ApS:et.** Innovationsfonden **Innofounder** kräver ett danskt CVR-nummer, och bolaget får vara högst 3 år gammalt när ni söker. Läs de nya riktlinjerna från 1 juli 2026 om hur programmet ser ut. Det är 12 månader på heltid, så kolla om det funkar att bo i Malmö. Kolla också **Innobooster** och EIFO.

**Innan du startar ett AB**

1. **Skatt och fast driftställe.** Du bor i Sverige och jobbar för ett danskt bolag. Då kan ApS:et redan ha ett fast driftställe i Sverige, och det påverkar både bolagsskatt och arbetsgivaravgifter. Prata med en revisor som kan Öresundsfrågor innan du gör något mer.
2. **Var sitter koden och IP:n?** Vinnova-pengarna ska gå till arbete i det svenska bolaget. Om allt ägs av ApS:et får du reda ut hur AB:et får använda det, till exempel genom licens eller överlåtelse.
3. **Struktur.** Ett AB som ägs av ApS:et är enklast, men då räknas koncernen. Ett AB som du äger direkt kräver att ni delar upp verksamheten ordentligt.
4. **Open banking.** Om appen läser kontodata direkt från banker krävs tillstånd som kontoinformationstjänst (AISP), eller en partner som Tink. Det påverkar också hur bidragsgivarna bedömer risken.

**Tre frågor så jag kan ge ett skarpare svar**
- Hur gammalt är ApS:et, och har det omsättning?
- Var jobbar teamet i praktiken, och vilken marknad tar ni först, Sverige eller Danmark?
- Läser appen bankdata via open banking, eller lägger användaren in prenumerationerna själv?

Källor:
- [Vinnova – Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026)
- [Innovationsfonden – Innofounder](https://innovationsfonden.dk/en/p/innofounder)
- [Innofounder-retningslinjer 1 juli 2026](https://innovationsfonden.dk/sites/default/files/2026-07/Innofounder%20retningslinjer_DK_01.07.26.pdf)
- [Innovationsfonden – Innobooster](https://innovationsfonden.dk/en/p/innobooster)
- [Driva Eget – Almis lån och villkor](https://driva-eget.se/artiklar/olika-typer-av-almilan-vad-ar-villkoren)

## Founder, turn 2 (simulated)
- ApS:et startades 2023, omsättning ca 90 000 DKK om året
- jag bor i malmö och pendlar, utvecklaren sitter i köpenhamn. vi vill lansera i sverige nu, idag är det mest danska användare
- ja, via open banking (PSD2) genom en aggregator-partner

## Assistant, turn 2
Tack, det ändrar bilden en del. Här är läget.

**Danmark: sämre än jag trodde**

- **Innofounder passar troligen inte.** Bolaget får vara högst 5 år när bidraget beviljas, så 2023 går bra. Men programmet stöder inte bolag vars produkt redan finns på marknaden och vars utmaning främst är försäljning, marknadsföring eller skalning. Lansering i Sverige är skalning. Det kräver också heltid (37 timmar i veckan), högst 10 timmar annat jobb i veckan, högskoleexamen och minst 12,5 % ägande. Det funkar bara om ni har en stor ny teknisk del kvar att bygga.
- **Innobooster är stängt just nu.** Pool 4 stängde 15 oktober, alltså i förrgår. Ni behöver också en av två saker: minst 250 000 DKK i bruttovinst ett av de senaste tre åren, eller minst 100 000 i riskkapital eller utvecklingsbidrag. Med 90 000 DKK i omsättning når ni inte vinstgränsen. Har ni tagit in pengar? Då kan ni sikta på 2027 års omgångar. Bidraget täcker högst 35 % av projektkostnaden.

**Sverige: ett AB kan vara rimligt nu, men av rätt skäl**

Ni ska lansera i Sverige. Då är ett svenskt dotterbolag, ett AB som ApS:et äger, en naturlig struktur även utan bidrag. Det ger ett svenskt bolag mot svenska användare och partners. Det gör er också sökbara hos Vinnova och Almi.

- **Vinnova Innovativa startups** stänger **12 januari 2027 kl 14:00**. Max 500 000 kr. Ett nystartat AB är inget problem. ApS:et och AB:et räknas ihop, men ni ligger långt under gränserna. Två villkor är viktiga:
  1. AB:et ska ha verklig verksamhet i Sverige. Projektkostnaderna ska ligga i AB:et. Det funkar inte om all utveckling görs av en utvecklare som anställd i ApS:et.
  2. Projektet måste innehålla något som är svårt att kopiera. "Lansera i Sverige" räcker inte. Ett exempel som kan bära: att hitta och tolka svenska autogiron och prenumerationer automatiskt i transaktionsdata. Svenska banker och Bankgirot ser annorlunda ut än de danska.
- **Almi Syd** passar för ett innovationslån när AB:et finns. Lånet täcker högst halva finansieringsbehovet. Ett helt nytt AB utan historik får ofta en tuffare kreditprövning, så ring dem tidigt.

**Tre saker att reda ut innan du registrerar AB:et**

1. **IP och licens.** ApS:et äger koden. Skriv ett licens- eller tjänsteavtal mellan bolagen, med marknadsmässigt pris. Det är internprissättning, och både Skatteverket och SKAT tittar på det.
2. **Din egen skatt.** Du är gränspendlare nu. Om du börjar jobba från Malmö åt AB:et ändras din skatt och var du är socialförsäkrad. Fråga Øresunddirekt, det är gratis. Ta också en revisor som kan både danska och svenska regler.
3. **PSD2 i Sverige.** Kolla att er aggregator har tillstånd som täcker Sverige och stöder svenska banker med BankID. Kolla också om avtalet kan läggas på AB:et eller måste ligga kvar på ApS:et. Tillståndet ligger hos partnern, så ni behöver inget eget så länge ni bara visar data via dem.

**Förslag på ordning**
1. Prata med revisor och Øresunddirekt den här veckan.
2. Registrera AB:et i november. Bolagsverket tar oftast några dagar till ett par veckor.
3. Skriv Vinnova-ansökan i december, med fokus på det svenska tekniska problemet.
4. Ta Almi-samtalet parallellt.

Vill du att jag hjälper dig skissa projektbeskrivningen till Vinnova? Säg i så fall vad som tekniskt är svårast i appen idag.

Källor:
- [Danmarks Innovationsfond – Innofounder guidelines 1 juli 2026](https://danmarksinnovationsfond.dk/sites/default/files/2026-07/Innofounder%20Guidelines_%20ENG_01.07.2026.pdf)
- [Danmarks Innovationsfond – Innobooster](https://danmarksinnovationsfond.dk/en/programmes/innobooster/)
- [Vinnova – Innovative Startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026)
- [Driva Eget – Almis lån och villkor](https://driva-eget.se/artiklar/olika-typer-av-almilan-vad-ar-villkoren)
