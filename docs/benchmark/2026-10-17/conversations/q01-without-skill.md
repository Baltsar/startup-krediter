# q01 without-skill

## Founder, turn 1
Hej! Vi är två som driver ett AB sen i våras, bygger en AI-agent som sköter avstämningar åt redovisningsbyråer. Bränner typ 4000 kr/mån på OpenAI och Claude API nu och det blir bara mer ju fler piloter vi kör. Finns det nåt sätt att få gratis krediter eller GPU tid? Vi har ingen investerare än

## Assistant, turn 1
Hej! Ja, det finns flera vägar. På er nivå (4 000 kr/mån, ungefär 400 USD) kan krediter täcka API-kostnaden i flera månader, kanske ett år. Uppgifterna nedan kommer mest från tredjepartssajter som säger emot varandra om belopp. Kolla därför villkoren på programmets egen sida innan ni räknar med något.

**API-krediter som ni kan söka utan investerare**

1. **Anthropic (Claude for Startups)**, claude.com/programs/startups. Tidigare krävdes att man kom in via en partner-VC. Enligt flera källor kan man nu söka direkt, även utan VC. Beloppet är oklart, källorna säger allt från cirka 1 000 till 5 000 USD. Krediterna gäller bara Anthropics eget API, inte Claude via Bedrock eller Vertex. Sök den här först, den passar er bäst.
2. **AWS Activate Founders.** Ungefär 1 000 USD för bolag utan VC eller accelerator. AWS skrev i maj 2026 att Activate-krediter nu går att använda på tredjepartsmodeller i Amazon Bedrock, även Anthropics. Det blir alltså ett andra sätt att få gratis Claude-anrop.
3. **Microsoft for Startups (Founders Hub).** Ni behöver ingen investerare. Ni börjar med cirka 1 000 USD och kommer upp i ungefär 5 000 USD när bolaget är verifierat. Krediterna går till Azure och kan användas på OpenAI-modeller via Azure OpenAI. Räkna inte med en separat kredit för OpenAIs eget API.
4. **Google for Startups Cloud, Start-nivån.** Ungefär 2 000 USD för bolag utan riskkapital. Det stora AI-paketet (upp till 350 000 USD) kräver VC-finansiering från seed till serie A. Krediterna gäller bara Googles egna modeller (Gemini och Gemma), alltså inte Claude eller GPT.

**OpenAI direkt:** Här finns inget öppet program som man söker själv. Krediterna går främst via partner-VC:er och acceleratorer. Ett Ramp-konto ska ge runt 2 500 USD, men det har jag inte kunnat bekräfta för svenska bolag.

**GPU-tid:** Ni anropar API:er, så ni behöver troligen ingen GPU just nu. Ska ni senare finjustera eller köra egna modeller kan startups och SMF få gratis GPU-tid via EUs **EuroHPC AI Factories**. Playground är för nybörjare och Fast Lane ger upp till 50 000 GPU-timmar. Playground stod som "tillfälligt stängt" under en plattformsflytt när jag kollade.

**Pengar i stället för krediter:** Vinnovas **Innovativa startups 2026** verkar vara öppen just nu, enligt en källa från 12 oktober 2026 till 12 januari 2027. Den ger upp till 500 000 kr till AB med färre än 10 anställda. Ni måste ha en svårkopierad kunskapsbas och kunna konkurrera internationellt. Pengarna går till att testa kundbehov och betalningsvilja, och era piloter med redovisningsbyråer passar bra in där. Kolla datum och villkor på vinnova.se.

**Kostnaden går också att sänka direkt:** Med prompt caching blir återkommande systemprompter och kontoplaner mycket billigare. Avstämningar som inte måste gå i realtid kan köras som batch, vilket ger ungefär halva priset hos både OpenAI och Anthropic. Låt dessutom en mindre modell sköta enkla matchningar och skicka bara svåra fall till den stora.

Två frågor så att jag kan prioritera bättre:
- Ungefär hur fördelas kostnaden mellan OpenAI och Claude?
- Har ni redan sökt något av programmen ovan, eller fått krediter tidigare? Flera av dem gäller bara första gången.

Källor: [Anthropic-guide (guptadeepak)](https://guptadeepak.com/startup-offers/guides/anthropic-for-startups), [ecosistemastartup om Claude for Startups](https://ecosistemastartup.com/?p=115543), [fin.ai om AI-krediter 2026](https://fin.ai/learn/ai-credits-for-startups), [OpenAI-guide (guptadeepak)](https://guptadeepak.com/startup-offers/guides/openai-for-startups), [AWS om Activate-krediter på Bedrock](https://aws.amazon.com/aws-startups/learn/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/), [Microsoft Founders Hub-guide](https://guptadeepak.com/startup-offers/guides/microsoft-for-startups), [Google Cloud AI-program](https://cloud.google.com/startup/ai), [EuroHPC Playground-access](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en), [LUMI om AI Factory-calls](https://lumi-supercomputer.eu/access-calls-for-ai-factories/), [Vinnova Innovativa startups 2026](https://www.vinnova.se/en/calls-for-proposals/innovative-startups/innovative-startups-2026), [Lunds universitet om utlysningen](https://www.ch.lu.se/evenemang/info-meeting-vinnovas-call-innovative-startups-2026)

## Founder, turn 2 (simulated)
Vet inte exakt hur det fördelas mellan OpenAI och Claude faktiskt, har inte kollat. Och nej, vi har inte sökt nåt av dem eller fått krediter innan vad jag vet

## Assistant, turn 2
Okej, då har ni alla program kvar att söka. Så här skulle jag göra:

**1. Kolla hur kostnaden fördelas (tar fem minuter)**
- OpenAI: platform.openai.com, under Usage.
- Anthropic: console.anthropic.com, under Usage eller Cost.
Svaret avgör vilka krediter som är värda mest. Belastar Claude mest bör ni lägga mest kraft på Anthropic och AWS. Belastar OpenAI mest gäller det Microsoft.

**2. Sök i den här ordningen**
1. **Anthropic Claude for Startups.** Ansökan sker direkt och krediterna gäller ert befintliga API.
2. **AWS Activate Founders.** Krediterna kan användas på Claude via Bedrock. Det kräver en kodändring, men inte så stor om ni redan använder Anthropics SDK.
3. **Microsoft for Startups.** Krediterna gäller OpenAI-modeller via Azure OpenAI. Här behöver ni också ändra lite kod, framför allt endpoint och nyckel.
4. **Google Start-nivån.** Bara om ni är beredda att testa Gemini.

Krediterna har ofta ett utgångsdatum, ibland 6–12 månader. Sök gärna allt nu, men aktivera AWS och Azure först när ni är redo att flytta trafik dit.

**3. Vinnova parallellt**
Innovativa startups har sista ansökningsdag 12 januari, om datumen jag hittade stämmer. Det ger pengar och inte bara krediter, och era piloter räknas som underlag. Det är mer jobb att söka, så börja i god tid.

**Inför ansökningarna**
De flesta frågar efter organisationsnummer och en bolagsmejl på egen domän, inte gmail. De vill också se en webbplats eller produktsida och få en kort beskrivning av produkten. En mening som "AI-agent som automatiserar avstämningar åt redovisningsbyråer, X piloter igång" räcker långt.

Vill du att jag hjälper till med beskrivningen eller kollar villkoren för något av programmen närmare?
