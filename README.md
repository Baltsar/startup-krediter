# startup-krediter

En builder i Sverige eller Norden frågar om chansen. Skillen räknar behörighet mot en dörr. Den skriver ingen procent, och den skickar inte ansökan.

`/startup-krediter` drar upp den. Det gör också Vinnova, EuroHPC, Sweden AI Factory, Playground, NVIDIA Inception, Claude Startups, GPU-timmar eller "har vi en chans".

## Haken

Gratis GPU och ett bidrag är inte samma dörr som API-fakturan. GPU-tid betalar den inte.

Playground är behörighet och teknisk bedömning, sedan först till kvarn. Villkoren säger också att innovation kan avgöra den sista tilldelningen. Båda meningarna står kvar.

Vinnova, svenska sidan: upp till 500 000 kronor, beslut 23 mars 2027. Låg grad avslås. Mycket hög grad beviljas. Hög och likvärdig grad lottas. Engelska sidan har samma tak och skriver att den fulla bedömningstexten publiceras när utlysningen öppnar. En presentation från mars 2026 säger poäng 0–5 och rangordning. Välj inte.

Inget skicka-API finns. Portalen kräver konto. Captcha är ett stopp. `submit` är `nej`.

## Installera

```bash
git clone https://github.com/Baltsar/startup-krediter.git
cd startup-krediter
sh bootstrap.sh
```

Det länkar katalogen till Cursor, Claude, Codex och den gemensamma agentmappen. Kräver Python 3. Inga paket.

## Kör

```bash
echo '{"view":"chance","need":"gpu","legal_form":"ab","country":"SE","age_years":2,"employees":4}' | python3 match.py
```

`●` är uppfyllt. `×` stänger dörren. `○` är okänt. `?` är den enda frågan. `→` är det de inte frågade om.

Kartan, alla dörrar:

```bash
echo '{"view":"matrix","legal_form":"ab","country":"SE"}' | python3 match.py
```

Paketet, när profilen är ifylld. Varje lista stannar före skicka:

```bash
echo '{"view":"packet","legal_form":"ab","country":"SE","age_years":2,"employees":4}' | python3 match.py
```

## Dörrarna

| Behov | Land | Dörr |
|---|---|---|
| GPU | Sverige | EuroHPC Playground |
| GPU | Finland | LUMI |
| GPU | Norge | KI-fabrikken |
| Pengar | Sverige | Vinnova Innovativa Startups |
| Pengar | Norge | Oppstartstilskudd 1 |
| Pengar | Finland | Business Finland |
| Pengar | Island | Fræ |
| Krediter | den stack de redan kör | leverantörens egen sida |

Sweden AI Factory får ett utkast. Mejlet skickas inte. RISE, Hyperight och montrar är inte dörrar. Almi står i beskrivningen och har ingen dörr.

Ta bara det chatten redan sagt. Gissa inte ålder, anställda, omsättning, moms eller anställning. Saknas landet: fråga. Gissa inte Sverige.

Karta för människor: https://opensverige.se/blogg/startup-krediter-gpu-sverige

MIT. Copyright 2026 OpenSverige.
