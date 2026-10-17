# q01 with-skill

## Founder, turn 1
Hej! Vi är två som driver ett AB sen i våras, bygger en AI-agent som sköter avstämningar åt redovisningsbyråer. Bränner typ 4000 kr/mån på OpenAI och Claude API nu och det blir bara mer ju fler piloter vi kör. Finns det nåt sätt att få gratis krediter eller GPU tid? Vi har ingen investerare än

## Assistant, turn 1
Det som passar er bäst är AWS Activate Founders. Det är krediter för självfinansierade bolag, och de räcker också till Claude om ni kör den via Amazon Bedrock. Det som avgör är om bolaget har fått Activate-krediter förut.

Har bolaget fått AWS Activate-krediter tidigare, och i så fall hur mycket?

◐ AWS Activate Founders: från 1 000 USD i krediter, upp till 5 000 USD för vissa. Gäller Claude via Bedrock, inte Anthropics eget API. Avgör: tidigare Activate-krediter. 9 krav i ansökan, 3 oklarheter.
● Sweden AI Factory: gratis hjälp att välja GPU-call och granska ansökan. Inga egna GPU-timmar än. 4 krav, 4 oklarheter.
◐ NVIDIA Inception: gratis medlemskap med molnkrediter, men beloppet är inte publicerat. Avgör: en publik webbplats. 8 krav, 5 oklarheter.

Krediterna är till för API-fakturan. GPU-timmar hjälper bara om ni kör egna modeller.

Anthropics startupprogram tar inte emot ansökningar just nu, och OpenAI:s kräver en investerare.

Fler dörrar: EuroHPC Playground, upp till 5 000 GPU-timmar gratis.

Vilken vill ni titta på? Då får ni hela listan över vad ansökan kräver.

## Founder, turn 2 (simulated)
Nej, inte vad jag vet, vi har aldrig sökt Activate. Berätta mer om AWS Activate Founders!

## Assistant, turn 2
```
●  AWS Activate Credits
●  använder AWS, eller använder Anthropic
●  högst 10 år
●  fas: idé, pre-seed, seed eller serie A
●  ny i AWS Activate, eller ber om mer än ni fått tidigare
→  Activate Founders (självfinansierade): från 1 000 USD, upp till 5 000 USD för vissa. Activate Portfolio (före serie B, kräver Org ID från en Activate-partner): upp till 200 000 USD. AWS Credits for AI Startups: 200 000 USD+, bara på inbjudan.
```

Activate Founders är AWS-krediter för bolag utan investerare. Det passar er på det vi vet.

En sak avgör nyttan för er: krediterna betalar Claude bara via Amazon Bedrock, inte via Anthropics eget API. De betalar inte heller er OpenAI-faktura. Ni behöver alltså flytta Claude-anropen till Bedrock för att spara pengar.

**Det här behöver ni ha klart innan ni söker:**
1. Ett AWS Builder ID, verifierat via e-post. Ni behöver också en Activate-profil med jobbmejl på er egen domän.
2. Ett AWS-konto på betalplan, eftersom gratisplaner inte godkänns. Kontot ska vara kopplat till ert Builder ID med root- eller admin-åtkomst.
3. En fungerande hemsida för bolaget. AWS bedömer det som syns offentligt där.
4. Formuläret frågar efter produkt, målmarknad, traction, finansieringsfas och datum för senaste rundan.
5. Ni kan behöva visa en ID-handling. Säger ni nej blir det avslag.
6. Founders är för självfinansierade bolag. Tar ni in en ängel senare syns det i formuläret.
7. Krediterna går till Claude via Bedrock, inte Anthropics eget API.
8. Gäller bara Portfolio, inte er nu: Org ID från en partner och en runda de senaste 12 månaderna.
9. Gäller bara Portfolio: partnern måste bekräfta er koppling via mejl.
10. Krediterna har ett slutdatum. Det syns först i AWS Billing-konsolen när ni fått dem.
11. AWS räknar tidigare Activate-krediter på alla era AWS-konton. Har någon av er fått krediter via ett tidigare bolag kan det ge avslag. Kolla det, eftersom du skrev "inte vad jag vet".

**Oklart:**
- Handläggningstiden: sidorna säger 5–7, 5–10 eller 7–10 arbetsdagar. Räkna med ungefär två veckor.
- Vem som får mer än 1 000 USD: "upp till 5 000 USD" står utan kriterier. Fråga AWS Startups support.
- Varför ansökningar får avslag: det svaret i FAQ:n är trasigt i dag. Fråga AWS Startups support.

**Nästa steg:** Skapa ett Builder ID med jobbmejl och välj Activate Founders. Beskriv sedan produkt, fas och bolag, och koppla AWS-kontot. Ni klickar själva på skicka. Ingen ansökningsdeadline syns, och ansökan går inte att ändra efter att den skickats.
https://aws.amazon.com/startups/join?destination=/credits/apply

Villkor och FAQ, lästa i dag: https://aws.amazon.com/startups/credits/ och https://startups.aws.com/faq/

Vill ni se nästa dörr, eller svara på frågan ovan?
