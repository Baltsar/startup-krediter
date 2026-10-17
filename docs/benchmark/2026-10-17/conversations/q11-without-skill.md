# q11 without-skill

## Founder, turn 1
Vi er en frivillig forening (ikke AS) som trener en åpen norsk språkmodell på både bokmål og nynorsk. Har fått litt sponsing men trenger skikkelig GPU-kapasitet, snakker om kanskje 50 000 GPU-timer. Kan en forening søke om tid på LUMI eller hos Sigma2? Eller må vi ha med en forsker?

## Assistant, turn 1
Kort svar: Hos Sigma2 kan dere ikke søke som forening alene. Dere trenger en forsker med fast stilling, postdoc eller midlertidig forskerstilling ved en forskningsinstitusjon. Den personen blir prosjektleder. Det finnes også en EU-vei som kanskje passer bedre, men der er det usikkert om en forening kvalifiserer.

**1. Sigma2, inkludert Norges andel av LUMI**
- Retningslinjene for periode 2026.2 sier at søkeren må ha fast stilling, være postdoc eller være midlertidig ansatt forsker ved sin institusjon. En frivillig forening har ikke en slik person.
- Prosjektet må også være helt eller delvis finansiert med offentlige midler, for eksempel fra Forskningsrådet, et departement eller EU. Privat sponsing alene holder ikke. Det finnes en egen kommersiell vei, men da betaler dere.
- Tildelingsperiodene er på seks måneder og starter 1. april og 1. oktober. Nye prosjekter kan søke når som helst, men søknader utenom ordinær frist får lavere prioritet i køen.
- Uten forsker kan dere bare få en liten testkvote på e-post. På LUMI er grensen 150 GPU-timer, altså langt unna 50 000.

**2. Den realistiske veien: samarbeid med en forskningsgruppe**
Det er vanlig at en forsker står som prosjektleder mens dere gjør mye av arbeidet. Grupper som allerede trener norske språkmodeller på LUMI:
- Språkteknologigruppen (LTG) ved Universitetet i Oslo, som står bak NorMistral og NORA.LLM
- Nasjonalbibliotekets AI-lab

En åpen modell for både bokmål og nynorsk passer godt med det de jobber med. Det er en reell styrke når dere tar kontakt. Avklar på forhånd hvem som eier modell og data, og hvilken lisens dere slipper under. Avtal også hvordan dere blir kreditert.

**3. EuroHPC AI Factories, der LUMI AI Factory er én av dem**
- Fast Lane gir opptil 50 000 GPU-timer og svar på noen få virkedager. Large Scale er for mer enn 50 000 timer i opptil ett år.
- Begge er gratis for AI-SMB-er og startups med innovasjonsformål. Akademia og offentlig sektor skal i stedet bruke sporet «AI for Science and Collaborative EU projects».
- **Usikkert:** Jeg fant ingen regel om ideelle foreninger. En forening er verken AS eller universitet, så send et kort spørsmål til EuroHPC eller LUMI-helpdesken før dere skriver en hel søknad. Norge er med i LUMI-konsortiet og knyttet til Horizon Europe, så landkravet er trolig ikke problemet.
- Et lite Playground-prosjekt på én til tre måneder kan være en god start for å måle hvor mange GPU-timer dere faktisk trenger.

**Sjekk timetallet ditt.** På LUMI teller en «GPU-time» ofte per GCD, altså per halve MI250X-brikke. 50 000 timer kan derfor bety noe annet enn dere regner med. Hvis dere har tallet fra en A100- eller H100-beregning, regn det om før dere søker.

For å gi et mer presist råd trenger jeg svar på tre ting:
1. Har noen i foreningen en stilling ved et universitet, en høyskole eller et forskningsinstitutt? Eller har dere kontakt med en forskningsgruppe?
2. Kommer noe av sponsingen fra offentlige kilder?
3. Hvor stor modell skal dere trene, og hvor mye data? Når må treningen være ferdig?

Kilder:
- [Sigma2: Guidelines RFK 2026.2](https://www.sigma2.no/sites/default/files/2026-06/Guidelines-RFK-2026.2-Final_0.pdf)
- [NRIS: Applying for computing and storage](https://documentation.sigma2.no/getting_started/applying_resources.html)
- [EuroHPC: Large Scale access to AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/large-scale-access-ai-factories_en)
- [EuroHPC: Playground access](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en)
- [LUMI: Access calls for AI Factories](https://lumi-supercomputer.eu/access-calls-for-ai-factories/)

## Founder, turn 2 (simulated)
1. Ja, et styremedlem er doktorgradsstipendiat ved UiO. 2. Nei, sponsingen kommer fra et norsk tech-selskap. 3. Det vet vi ikke helt ennå

## Assistant, turn 2
Det hjelper mye. Doktorgradsstipendiaten deres er en god inngang, men vedkommende kan ikke søke selv.

**Hvem som kan søke hos Sigma2**
- Sigma2 sier at master- og ph.d.-studenter ikke kan søke direkte. Søknaden må gå via veilederen eller en annen ansatt med fast stilling eller postdocstilling. Den personen blir prosjektleder.
- Stipendiaten kan likevel gjøre det meste av jobben. Prosjektlederen kan gi en annen forsker rollen som Executive Officer (XO), som administrerer prosjektet i praksis.
- Sponsingen fra tech-selskapet regnes ikke som offentlig finansiering. Kravet kan likevel være oppfylt hvis prosjektet er forskning ved UiO, for eksempel en del av doktorgraden eller en gruppes forskning. Da finansieres prosjektet av offentlige midler gjennom stillingene. Dette må veilederen bekrefte, jeg kan ikke avgjøre det herfra.

**Neste skritt**
1. Stipendiaten tar det opp med veilederen. Er modellen relevant for avhandlingen eller gruppens forskning? Ville veilederen stå som prosjektleder?
2. Hvis veilederen ikke passer, er LTG (Språkteknologigruppen) ved UiO det naturlige alternativet. De har allerede trent norske modeller på LUMI.
3. Avklar eierskap før dere søker. Når prosjektet blir et UiO-prosjekt, gjelder UiOs regler for resultater, lisenser og data. Dere bør ha skriftlig at modellen slippes åpent, og hvilken rolle foreningen og sponsoren har. Sponsoren bør ikke få spesielle rettigheter til modellen. Da kan prosjektet bli sett på som kommersielt.
4. Fristen: De fleste ressursene fordeles før periodene som starter 1. april og 1. oktober. Neste naturlige frist er altså før 2027.1. Sjekk nøyaktig dato på sigma2.no. Nye prosjekter kan søke når som helst, men da med lavere prioritet i køen.

**Hvordan dere kan finne behovet for GPU-timer**
Søknaden må begrunne behovet, så dere trenger et anslag. Tommelfingerregelen er at treningen koster omtrent 6 × antall parametre × antall tokens i flyttallsoperasjoner. To eksempler, regnet med mine egne antakelser (ikke verifisert):
- **Videretrening av en eksisterende åpen modell på norsk tekst** er mye billigere enn å trene fra bunnen. En modell på 7 milliarder parametre med 50 milliarder tokens kan ende på noen få tusen til rundt 10 000 GPU-timer på LUMI.
- **Trening fra bunnen** av en modell av samme størrelse med flere hundre milliarder tokens kan fort bli 50 000 timer eller mer.

Antakelsene: Én «GPU» på LUMI er en halv MI250X-brikke (GCD), med en teoretisk topp på rundt 190 TFLOPS i bf16. I praksis får man ofte ut 30–40 %. Kjør en kort test for å måle deres egen hastighet. Sigma2 gir en liten testkvote på inntil 150 GPU-timer på LUMI, eller dere kan bruke EuroHPC Playground. Bruk det målte tallet i søknaden. Det gjør søknaden mye sterkere enn et anslag.

Er planen å trene fra bunnen, eller å bygge videre på en eksisterende modell? Hvor mye norsk tekst har dere? Med det kan jeg hjelpe dere å sette opp et konkret anslag til søknaden.

Kilder:
- [NRIS: Applying for computing and storage](https://documentation.sigma2.no/getting_started/applying_resources.html)
- [Sigma2: Guidelines RFK 2026.2](https://www.sigma2.no/sites/default/files/2026-06/Guidelines-RFK-2026.2-Final_0.pdf)
