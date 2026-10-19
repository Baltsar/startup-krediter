# r11 without-skill

## Founder, turn 1
Hei, vi skal søke AWS Activate. de gir jo 100k dollar i credits til alle startups? hva må vi ha klart, og kan creditsene brukes på Claude via Bedrock? trenger det helst før jul

## Assistant, turn 1
Hei!

Kort svar: nei, AWS gir ikke 100 000 dollar til alle. "Opptil 100 000 dollar" står på noen av AWS' markedsføringssider, men det er et tak og ikke det dere får. Slik er pakkene nå (sjekket 19. oktober 2026):

- **Activate Founders**, for selvfinansierte startups: dere starter på 1 000 dollar. Noen få kan få mer over tid, opptil 5 000 dollar.
- **Activate Portfolio**, for pre-Series B-selskaper med en Org ID fra en Activate Provider (akselerator, engleinvestor eller VC): credits-siden sier opptil 200 000 dollar, mens andre AWS-sider sier opptil 100 000. Uansett er det et tak, ikke en garanti.
- **AWS Credits for AI Startups** (200 000+ dollar): bare på invitasjon, for selskaper som har vokst ut av Portfolio. Det kan dere ikke søke på.

**Det første dere må avklare:** Har dere en investor, akselerator eller inkubator i ryggen? Spør dem i dag om de er Activate Provider og kan gi dere en Org ID. Hvis ja, er Portfolio veien, og det er Org ID-en som tar tid. Har dere hentet penger fra noen som ikke er provider, er det uklart hvilken pakke dere hører til. AWS beskriver Founders som for selvfinansierte, så ikke regn med noe beløp før det er avklart.

**Dette må være klart før dere søker**
1. En nettside for selskapet som fungerer.
2. En AWS Builder ID laget med jobb-e-post, gjerne på samme domene som nettsiden. Ulike e-postdomener i profil og søknad gir forsinkelser.
3. En AWS-konto på Paid plan. Kontoer laget etter 15. juli 2025 kan stå på Free plan, og da må dere oppgradere. Kontoen kan ikke være inaktiv eller allerede koblet til en annen Builder ID.
4. Selskapet er grunnlagt for under 10 år siden og er pre-Series B. For Portfolio må siste finansieringsrunde være innen de siste 12 månedene, hvis dere har hatt en.
5. Dere har ikke fått Activate-credits før, eller dere ber om mer enn dere fikk sist.
6. Til selve søknaden: produkt, målmarked, traction, finansieringsfase og dato for siste runde. Vær nøyaktig. Feil finansieringsfase er en kjent grunn til forsinkelse.
7. Org ID fra provideren (bare for Portfolio).

**Rekker dere det før jul?** Ja, med god margin. AWS oppgir 5–10 virkedager behandlingstid på én side og 7–10 på en annen. Flaskehalsen er Org ID og Paid plan, så ordne det denne uka.

**Kan creditsene brukes på Claude via Bedrock?**
Ja. Activate-vilkårene (oppdatert 22. januar 2026) sier at credits kan dekke tredjepartsmodeller i Amazon Bedrock. Det gjelder også Marketplace-kostnadene for disse modellene, og AWS nevner Anthropic ved navn. Noen praktiske ting:

- I den vanlige Bedrock-integrasjonen starter første kall mot Claude et AWS Marketplace-abonnement. IAM-rollen som gjør kallet trenger `aws-marketplace:Subscribe`, `Unsubscribe` og `ViewSubscriptions`.
- Kontoen må ha et gyldig betalingskort for Marketplace-kjøp, selv om creditsene betaler.
- Anthropic krever et engangsskjema med bruksområde og nettside før første kall. Det nye bedrock-mantle-endepunktet ("Claude in Amazon Bedrock") krever ikke dette skjemaet.
- **Claude Platform on AWS** er et annet produkt. Det driftes av Anthropic og faktureres via AWS Marketplace, ikke som Bedrock. Vilkårene dekker bare Marketplace-kostnader for Bedrock-modeller. Ikke regn med at creditsene dekker det før AWS har bekreftet det.
- Når dere er godkjent, sjekk under Credits i Billing-konsollen hvilke tjenester akkurat deres credit gjelder for, og når den går ut (vanligvis 1–2 år).
- Creditsene er til deres egen bruk og kan ikke gis videre til kundene deres.
- Vær realistiske: 1 000 dollar fra Founders går fort med de største Claude-modellene. Sett opp et budsjettvarsel med en gang.

Si fra om dere har investor eller akselerator, så tar vi neste steg derfra.

**Kilder**
- AWS Activate credits: https://aws.amazon.com/startups/credits
- AWS sin søknadsguide: https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/
- Activate-vilkårene: https://aws.amazon.com/activate/terms/
- Activate benefits overview: https://startups.aws.com/lp/activate-benefits-overview?lang=en-US
- Bedrock modelltilgang: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html
- Claude Platform on AWS: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws

## Founder, turn 2
ingen akselerator, inkubator eller VC. investoren vår er Lysfjord Energi AS, et regionalt energikonsern eid av 12 kommuner i Rogaland. de eier 66 % og har lagt inn 25 av de 27 MNOK vi har hentet totalt. vi har ingen Activate Provider-relasjon.

## Assistant, turn 2
Hei!

Takk, det endrer svaret.

**Kort svar: Med det eierskapet er dere etter alt å dømme ikke kvalifisert for AWS Activate. Det gjelder både Founders og Portfolio.**

Dette burde jeg ha spurt om i forrige svar. Det viktigste for planen deres er at dere ikke bør regne med Activate-credits før jul.

**Hvorfor**
Punkt 1.1 i Activate-vilkårene (oppdatert 22. januar 2026) sier: "Government Entities are not eligible to participate in the Program." En Government Entity er definert som en enhet som er del av, majoritetseid, styrt, kontrollert eller "substantially funded by" offentlige myndigheter "at any level". Definisjonen nevner offentlig eide selskaper ved navn.

Slik treffer det dere:
- Lysfjord Energi er eid av 12 kommuner. Det er et offentlig eid selskap, og kommuner er et forvaltningsnivå.
- Lysfjord eier 66 % av dere. Dere er altså majoritetseid og kontrollert av et offentlig eid selskap.
- 25 av 27 MNOK kommer fra Lysfjord, altså over 90 % av kapitalen. Det alene holder trolig til "substantially funded", selv om noen skulle mene at indirekte eierskap ikke teller.

Det er AWS som avgjør, etter eget skjønn. Men ordlyden treffer dere fra flere kanter. Unntaket gjelder hele programmet, så en Org ID fra en akselerator ville ikke hjulpet.

**Ikke søk som "selvfinansiert"**
Founders er for selvfinansierte startups, og dere har hentet 27 MNOK. Søker dere der, eller utelater eierskapet, gir dere AWS feil opplysninger. AWS sine credit-vilkår sier at credits blir ugyldige ved brudd på vilkårene, og at dere da må betale tilbake det dere har brukt.

**Vil dere ha et sikkert svar fra AWS?**
Spør dem skriftlig før dere bruker mer tid på søknaden. Beskriv eierskapet nøyaktig: 66 % eid av Lysfjord Energi AS, som eies av 12 kommuner, og 25 av 27 MNOK derfra. Spør om dere regnes som Government Entity etter punkt 1.1. Den eneste kontaktkanalen jeg fant er chatten "Ask AWS Startups" på kontaktsiden deres. Det er en AI-assistent, så et ja derfra er en pekepinn og ikke en godkjenning.

**Claude via Bedrock før jul går fint uten credits**
Dere trenger ikke Activate for å bruke Claude i Bedrock. En vanlig AWS-konto på Paid plan holder, og dere betaler etter forbruk. Det praktiske fra forrige svar gjelder fortsatt: Marketplace-tillatelser på IAM-rollen, betalingskort på kontoen, Anthropics engangsskjema og budsjettvarsel fra dag én.

**Anthropics eget startup-program er ingen omvei**
Det tar ikke imot søknader nå fordi kullet er fullt (sjekket 19. oktober 2026). Creditsene der kan uansett ikke brukes på AWS eller Bedrock, bare på Anthropics eget API.

Vil dere at jeg ser på andre ordninger som kan dekke skykostnader for et selskap eid slik dere er?

**Kilder**
- Activate-vilkårene, oppdatert 22. januar 2026, punkt 1.1: https://aws.amazon.com/activate/terms/
- AWS Promotional Credit-vilkårene, punkt 4: https://aws.amazon.com/awscredits/
- AWS sin søknadsguide: https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/
- AWS Activate credits: https://aws.amazon.com/startups/credits
- Kontakt AWS Startups: https://startups.aws.com/contact-us
- Claude for Startups: https://claude.com/programs/startups
