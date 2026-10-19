# s06 without-skill

## Founder, turn 1
Tja! Vi har lagt ca 1,2 mille på utveckling av vår plattform i år (AI som skriver produkttexter åt e-handlare). Hur mycket kan vi få tillbaka via FoU-avdraget och hur söker man? Behövs revisor eller kan vi fixa det själva i deklarationen?

## Assistant, turn 1
Tja! Kort svar: FoU-avdraget betalar inte tillbaka utvecklingskostnaden. Det sänker arbetsgivaravgifterna på lön till anställda som jobbar med forskning eller utveckling. Ni gör det själva i arbetsgivardeklarationen, ingen revisor behövs. Den stora frågan är om ert arbete räknas som FoU enligt dagens regler. Där är ribban hög för en tjänst byggd ovanpå språkmodeller.

**Vad det kan ge i kronor**

Avdraget är 20 % av bruttolönen för de personer som kvalar. Det beror alltså på vad era 1,2 mille består av:

- 1,2 mkr i bruttolön till anställda som alla kvalar: ca 240 000 kr. Ni grundare räknas om ni tar lön från ett AB.
- 1,2 mkr som total lönekostnad inklusive arbetsgivaravgifter (lön ca 913 000 kr): ca 183 000 kr.
- Konsulter, frilansare, byråer, API- och molnkostnader: 0 kr för er. Avdraget gäller bara lön som ni själva betalar arbetsgivaravgifter på.
- Enskild firma: 0 kr för ägarnas eget arbete, eftersom de betalar egenavgifter.

Varje person måste dessutom ha jobbat med FoU minst hälften av sin arbetstid och minst 15 timmar under månaden. Det bedöms månad för månad. Klarar personen gränsen räknas hela lönen den månaden, annars blir det normalt ingenting. Ledning, support, underhåll och marknadsföring räknas inte. För anställda under 23 blir avdraget lägre, eftersom deras avgift redan är sänkt.

**Räknas ert arbete som FoU?**

Det här är det svåra. I dag ska utvecklingen vara systematisk och kvalificerad och bygga på forskningsresultat. Löpande utveckling, justering och anpassning av en produkt räknas normalt inte.

Kammarrätten i Göteborg nekade 2025 ett mjukvarubolag avdraget (Consat-målet). Domstolen sa att mjukvara kan vara FoU, men bara om projektet löser en verklig vetenskaplig eller teknisk osäkerhet. Kunskapen ska också vara ny för fler än bolaget självt. Att anpassa befintlig programvara räckte inte.

För en tjänst som skriver produkttexter betyder det ungefär:

- **Troligen inte FoU:** promptarbete mot färdiga modeller som GPT eller Claude, integrationer mot Shopify och liknande, gränssnitt och drift.
- **Kan vara FoU:** ett tekniskt problem där ni inte visste om det gick att lösa. Till exempel egen träning eller finjustering av modeller, nya sätt att mäta och styra textkvalitet, eller ny teknik för att hålla texterna faktamässigt korrekta mot produktdatan.

Ni ansöker inte i förväg. Ni gör avdraget själva och Skatteverket kan granska i efterhand. Nekas det får ni betala tillbaka med ränta och kan få skattetillägg. Räkna därför inte med pengarna förrän ni har ett underlag ni tror håller.

**Så gör ni**

1. Bestäm per person och månad vem som kvalar. Spara tidrapporter, projektbeskrivningar och vad som var tekniskt osäkert.
2. I arbetsgivardeklarationen fyller ni i ruta 470 (total lön till FoU-personalen) och ruta 475 (själva avdraget). Lönesystemen har fälten.
3. För månader ni redan har deklarerat i år lämnar ni en rättad arbetsgivardeklaration per månad. Det går att rätta upp till sex år bakåt. Mellanskillnaden hamnar på skattekontot och kan betalas ut.

Revisor behövs inte. Den som sköter era löner eller er bokföring kan lägga in det. Är ni osäkra på FoU-bedömningen är en timme med en skatterådgivare bättre använd än en revisor.

**Det som kan komma 2027**

Regeringen har lagt förslag som ska gälla från 1 januari 2027. FoU-definitionen blir bredare: utveckling ska bygga på nya lösningar på vetenskapliga eller tekniska problem, inte på forskningsresultat. Kravet på 15 timmar försvinner. Dessutom föreslås ett extra avdrag i inkomstskatten på 200 % av lönekostnaden för FoU-personal. Går ni med förlust ger det bara ett större underskott att spara. Inget av detta är beslutat än, det avgörs i budgeten efter valet. Det gäller inte heller 2026.

**För att räkna på just er**

1. Är det ett AB? Hur mycket av de 1,2 mkr är lön, och hur mycket är konsulter, API och annat?
2. Hur många personer jobbar med det, och ungefär hur stor del av deras tid går till de tekniskt svåra delarna?
3. Vad bygger ni tekniskt: egna eller finjusterade modeller, eller främst prompter och integrationer ovanpå en färdig modell?

Källor:
- [Skatteverket: Forskningsavdrag i arbetsgivardeklarationen](https://skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm)
- [Lag (2023:747) om FoU-avdraget](https://lagen.nu/2023:747)
- [Skatteverket: Rätta en arbetsgivardeklaration](https://www.skatteverket.se/foretag/arbetsgivare/lamnaarbetsgivardeklaration/rattaenarbetsgivardeklaration.4.2cf1b5cd163796a5c8b6698.html)
- [BDO om Consat-målet, KamR Göteborg 1930-1931-24](https://www.bdo.se/getmedia/7670c232-090e-4f80-8050-a0c2dd256f0f/Forskningsavdraget-mellan-praxis-och-politik.pdf)
- [Lagrådsremiss 13 augusti 2026: Ett nytt skatteincitament för FoU](https://www.regeringen.se/rattsliga-dokument/lagradsremiss/2026/08/ett-nytt-skatteincitament-for-forskning-och-utveckling/)

## Founder, turn 2
1. Ja, AB. Ingen lön alls, vi grundare tar ingen lön. All utveckling är köpt: en polsk utvecklingsbyrå och en svensk frilansare som fakturerar via sin enskilda firma. Exakt hur mycket som är API och annat vet jag inte.
2. Vi är två grundare, plus byrån och frilansaren som gör själva utvecklingen. Hur stor del av tiden som går till de tekniskt svåra delarna vet jag inte riktigt.
3. Mest ovanpå färdiga modeller: OpenAI och Anthropic via API, plus en Shopify-app. Inga egna eller finjusterade modeller.

## Assistant, turn 2
Tack, då är svaret tyvärr enkelt: FoU-avdraget ger er 0 kr för det här året.

**Varför**

- Avdraget sänker bara arbetsgivaravgifter på lön. Ni betalar ingen lön, så det finns inget att sänka.
- Den polska byrån betalar inga svenska arbetsgivaravgifter för sina utvecklare. Det svenska avdraget gäller inte dem.
- Frilansaren betalar egenavgifter i sin enskilda firma, inte arbetsgivaravgifter. Avdraget gäller arbetsgivaravgifter. Ett eventuellt avdrag hade dessutom gått till frilansaren, inte till ert bolag.
- Även med anställda vore det svårt. Utveckling ovanpå OpenAI och Anthropic plus en Shopify-app räknas troligen som anpassning av befintlig teknik. Enligt dagens regler är det inte FoU.

Ni har alltså inget att rätta i arbetsgivardeklarationerna. Det finns heller ingen anledning att betala en konsult för att "söka" avdraget.

**Lönar det sig att börja ta lön för att få avdraget?**

Nej. Avdraget tar bort 20 av de 31,42 procenten i arbetsgivaravgift, så varje lönekrona kostar ändå mer än ingen lön alls. Dessutom måste minst halva er arbetstid gå till FoU. Grundararbete som ledning och försäljning räknas inte.

**Ändrar förslagen för 2027 något?**

Nej, inte för er som det ser ut nu. Det föreslagna extra avdraget på 200 % bygger också på lön till anställda som jobbar med FoU. Köpta tjänster från byråer och frilansare ingår inte.

**Vad som gäller för era 1,2 mkr**

De dras av som vanliga kostnader i bolagets deklaration. Har ni aktiverat dem som tillgång skrivs de av över tid i stället. Går bolaget med förlust sparas underskottet och sänker skatten när ni börjar gå med vinst.

Avdraget kan bli aktuellt om ni längre fram anställer egna utvecklare i Sverige som löser tekniskt nya problem. Börja i så fall föra tidrapporter direkt.

Vill ni att jag kollar andra sätt att få tillbaka pengar för utvecklingen? Till exempel bidrag, lån eller API-krediter från OpenAI och Anthropic.

Källor:
- [Skatteverket: Forskningsavdrag i arbetsgivardeklarationen](https://skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/forskningsavdrag.4.8dcbbe4142d38302d7cb4.htm)
- [Lag (2023:747) om särskilt avdrag vid beräkning av arbetsgivaravgifter för FoU-personal](https://lagen.nu/2023:747)
- [Lagrådsremiss 13 augusti 2026: Ett nytt skatteincitament för forskning och utveckling](https://www.regeringen.se/rattsliga-dokument/lagradsremiss/2026/08/ett-nytt-skatteincitament-for-forskning-och-utveckling/)
- [Prop. 2023/24:14 Teknisk översyn av vissa nedsättningar av socialavgifterna](https://www.regeringen.se/rattsliga-dokument/proposition/2023/09/prop.-20232414)
