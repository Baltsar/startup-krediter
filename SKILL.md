---
name: startup-krediter
description: >-
  Use when a builder in Sweden or the Nordics asks if their startup has a
  chance at funding, cloud credits, or GPU hours, or mentions Vinnova, Almi,
  EuroHPC, Sweden AI Factory, Mimer, RISE, LUMI, Sigma2, KI-fabrikken, NVIDIA
  Inception, Claude Startups, Anthropic, OpenAI, Nordic AI Factory Summit, AWS Activate,
  Playground, Fast Lane, startup-krediter, GPU-timmar, or "har vi en chans". Also use when they ask
  which grant or compute program fits a startup in Sweden, Finland, Norway,
  Denmark, or Iceland. Invoke as /startup-krediter.
---

# Startup-krediter

En builder frågar om chansen. Räkna behörighet. Hitta dörren de inte nämnde. Skriv ingen procent.

## Företagschatten

Läs bolaget som redan finns i chatten innan du frågar. Land, form, ålder och anställda som står där är uppfyllda. Fråga inte om dem igen.

Saknas landet i chatten: fråga landet. Gissa inte Sverige.

Ber de om compute och pengar: `"need":"both"`. Två glyfer. Inget extra förhör.

## Profil

Ta bara det chatten redan säger. Utelämna okända fält. Gissa inte ålder, anställda, omsättning, moms eller anställning.

`need` är `money`, `gpu` eller `credits`. `legal_form` är `ab`, `ideell_forening`, `academia` eller `unknown`. `country` är `SE`, `FI`, `NO`, `DK` eller `IS`. Sätt det bara om chatten säger landet. Gissa inte Sverige. Skriver de på engelska: `"lang":"en"`. Glyfen kommer då på engelska.

Pengar följer landet. Sverige är Vinnova. Norge är Oppstartstilskudd 1. Finland är Business Finland. Island är Fræ. Danmark: vårens Innofounder stängde 17 februari 2026. Höstomgången stängde 25 augusti 2026. Besked väntas i mitten av december 2026. GPU följer landet. Sverige är Playground. Finland är LUMI. Norge är KI-fabrikken. RISE, Hyperight och montrar är inte dörrar. Almi är namngiven och har ingen kodad dörr. Fast Lane är syskonet till Playground, inte en poängrunda.

`?` är första steget i den aktörens egen process. En stängd omgång får ingen startknapp.

## Kör

`match.py` ligger i samma katalog som den här filen.

```bash
python3 match.py <<'EOF'
{"view":"chance","need":"gpu","legal_form":"ab","country":"SE","age_years":2,"employees":4,"profit_distributed":false}
EOF
```

Kartan, när de vill se alla dörrar: samma profil med `"view":"matrix"`.

## Sidor

Skriptet räknar behörighet. Sidan säger om dörren är öppen idag.

Datum, belopp, eller om en omgång tar emot ansökningar: hämta `link` innan du skriver talet. curl räcker. Värden får kalla verktyget vad den vill. Bind inte anropet till en klient.

Nämner de ett program skriptet inte har: hämta programmets egen sida. Claude Startups är `https://claude.com/programs/startups`. NVIDIA Inception är `https://www.nvidia.com/en-us/startups/faq/`.

Pricka av sidans krav mot profilen. Ett krav chatten redan uppfyller är `●`. De andra förblir `○`.

Bråkar sidan och skriptet: visa båda. Välj inte.

En stängd omgång får ingen startknapp. Du skickar inget mejl och klickar inte skicka.

## v2

Full kontext betyder att varje krav på dörren är `●`. Kör då `"view":"packet"`.

Paketet fylls i värdens browser. Claude tar sin browser, inte desktop-computer-use. Cursor tar sin. Codex tar sin. Samma skill, samma paket. Kör `actions` i den ordning de står. `stop` betyder att knappen inte klickas. `actions_inloggad` körs bara när kontot redan är inloggat.

Bygg inte en MCP för att skicka. Aktören har inget skicka-API. Inloggningen och sista klicket sitter hos den som äger kontot.

Playground i Cursor-browsern: `https://access.eurohpc-ju.europa.eu/calls/60` är öppen och har ingen ansökningsblankett. Knappen är Register to apply. Formuläret är förnamn, efternamn, yrkesmejl, lösenord och captcha. Ansökan kommer efter kontot. Captcha är ett stopp. Lös den inte. Klicka inte Register.

NVIDIA Inception: `https://programs.nvidia.com/phoenix/application` har ett fält, Business Email. Resten sitter bakom Sign Up / Login. Fyll mejlet. Klicka inte Sign Up / Login.

Vinnova: Ansök här leder till `https://etjanster.vinnova.se/public/login`. Där finns Logga in och Skapa konto, och tvåstegsverifiering. Ingen ansökningsblankett före kontot. Klicka inte Skapa konto. `assess.questions` är sidans egna frågor. Svara på dem. Skriv inte en text som påstås bli beviljad. Hög och likvärdig grad lottas.

Claude Startups: sidan säger att kohorten är full och att de inte tar emot nya ansökningar. Ingen startknapp. Hämta `https://claude.com/programs/startups` igen innan du säger att den är öppen.

Sweden AI Factory kräver inget konto. Paketet skriver utkastet. Skicka inte mejlet.

## Svar

Visa `glyph` i ett kodblock, ordagrant. Lägg `link` under. Skriv inget annat.

`●` är uppfyllt. `×` är inte uppfyllt och stänger dörren. `○` är okänt. `?` är den enda frågan, det första okända kravet. `→` är det de inte frågade om.

Bråkar två datum eller två belopp på samma stöd: visa båda. Välj inte.

Nästa meddelande fyller ett fält. Lägg in det i samma profil, kör verktyget igen, visa den nya glyfen. Ett `○` som blev `●` är hela skillnaden. Börja inte om.

Du skickar inget mejl och klickar inte skicka. Säg aldrig att ansökan är skickad.

## Exempel

Builder: "Svenskt AB, två år, fyra personer, ingen VC. Har vi en chans på gratis GPU?"

Profilen ovan. Svaret följer verktyget. Pitchdecket är inte låset. Anställningen och arbetsbeskrivningen är det.
