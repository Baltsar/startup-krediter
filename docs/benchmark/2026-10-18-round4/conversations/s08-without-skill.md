# s08 without-skill

## Founder, turn 1
Góðan dag. Við erum lítið fyrirtæki á Akureyri (ehf., stofnað 2023) sem þróar myndgreiningu sem metur gæði fisks á færiböndum í fiskvinnslum. Við erum að skoða Tækniþróunarsjóð hjá Rannís og hvort hægt sé að fá GPU-tíma einhvers staðar til að þjálfa líkanið. Hvenær er næsti umsóknarfrestur og hversu mikið er hægt að sækja um?

## Assistant, turn 1
Góðan dag!

**Stutta svarið:** Næsti umsóknarfrestur fyrir stóru flokkana í Tækniþróunarsjóði hefur ekki verið auglýstur. Síðasti frestur fyrir Sprota, Vöxt og Markað rann út 15. september 2026. Lögin um Tækniþróunarsjóð falla úr gildi 1. janúar 2027 (lög nr. 54/2026). Samkvæmt frumvarpinu sameinast sjóðurinn Nýsköpunarsjóði námsmanna í nýjum **Nýsköpunarsjóði**. Vorfresturinn hefur verið um miðjan febrúar (16. febrúar 2026). Ég myndi samt ekki treysta á að dagsetningar, flokkar og upphæðir haldist óbreytt. **Fræ/Þróunarfræ er opið allt árið, líka núna.**

**Eitt sem liggur á: frestur á miðvikudaginn**
Uppbyggingarsjóður Norðurlands eystra (SSNE) er opinn núna. Frestur er **miðvikudaginn 21. október kl. 14:00**. Þið eruð á svæðinu og flokkurinn „verkefnastyrkir til atvinnulífs“ gæti átt við ykkur. Helstu atriði úr reglunum:
- Sjóðurinn styrkir að jafnaði mest 50% af styrkhæfum kostnaði. Verkefnið á að klárast innan 12 mánaða.
- Tölvukaup eru ekki styrkhæf. Kostnaður sem fellur til fyrir lok umsóknarfrests er það ekki heldur.
- Hámarksupphæð kemur ekki fram í reglunum. 80% styrksins er greitt í lok janúar.

Ef þið náið þessu ekki er næsta tækifæri líklega haustið 2027. Sjóðurinn auglýsir almennt einu sinni á ári.

**Upphæðir í Tækniþróunarsjóði eins og þær eru í dag (2026)**

| Flokkur | Hámark | Lengd | Mótframlag | Hverjir mega sækja |
|---|---|---|---|---|
| Fræ / Þróunarfræ | 2 m.kr. | 12 mán. | ekkert | fyrirtæki yngri en 5 ára (þið uppfyllið það) |
| Sproti | 24 m.kr. (mest 12 m.kr. á ári) | 2 ár | ekkert | fyrirtæki 5 ára eða yngri (þið uppfyllið það) |
| Vöxtur | 60 m.kr. (mest 30 m.kr. fyrra árið) | 2 ár | skv. ríkisaðstoðarreglum ESA | lítil og meðalstór fyrirtæki |
| Markaður | 12 m.kr. | 1 ár | 50% | lítil og meðalstór fyrirtæki sem verja minnst 10% rekstrarkostnaðar í rannsóknir og þróun |

Samkeppnin er hörð. Í vorúthlutun 2026 bárust 373 umsóknir og 49 verkefni fengu styrk, um 13%. Sproti fer fram í tveimur þrepum. Aðeins umsóknir sem fá A1 eða A2 í fyrra þrepi mega senda fulla umsókn.

**Það sem ég myndi gera**
1. Senda Fræ-umsókn núna, t.d. fyrir merkingu gagna og fyrstu prófanir í vinnslu. Spyrjið Rannís hvað verður um umsóknir sem eru enn í mati um áramótin.
2. Skrifa Sprota-umsóknina strax, svo hún sé tilbúin þegar Nýsköpunarsjóður auglýsir fyrsta kallið.
3. Spyrja Rannís beint hvenær fyrsta kallið kemur: taeknithrounarsjodur@rannis.is.

**GPU-tími**
Besta ókeypis leiðin er líklega EuroHPC AI Factories. Aðgangurinn er gjaldfrjáls fyrir sprotafyrirtæki og lítil og meðalstór fyrirtæki sem vinna að nýsköpun í gervigreind:
- **Playground:** litlar úthlutanir í 1–3 mánuði og svar innan 2 virkra daga. Ætlað nýjum notendum.
- **Fast Lane:** allt að 50.000 GPU-tímar í allt að 3 mánuði og samþykki innan 4 virkra daga.

Ísland á hlut í LUMI. Frá 1. janúar 2026 er líka starfrækt íslenskt „AI Factory Antenna“, AIFA-ICE. Almannarómur leiðir það ásamt HÍ, HR og Vísindagörðum HÍ. Hlutverk þess er að tengja íslensk sprotafyrirtæki við LUMI AI Factory, með ráðgjöf og litlu staðbundnu kerfi til prófana. Ég fann ekki landaskilyrðin orðrétt í kallinu sjálfu, svo staðfestið þau áður en þið sækið um.

Tvennt hagnýtt um þetta:
- Í umsókninni veljið þið eitt kerfi. LUMI keyrir á AMD-skjákortum (ROCm). Ef kóðinn ykkar byggir á CUDA, athugið hvaða kerfi í kallinu eru með NVIDIA-kort.
- Myndgreiningarlíkan af þessu tagi þarf yfirleitt tugi til nokkur hundruð GPU-tíma, ekki tugi þúsunda. Þetta er mitt mat, ekki tala frá sjóðnum. Playground dugar því líklega. Oft kostar merking gagna meira en reikniaflið.

**Tvennt annað sem gæti skilað peningum**
- **Skattfrádráttur vegna rannsókna og þróunar:** 35% af styrkhæfum kostnaði fyrir lítil og meðalstór fyrirtæki. Frestur fyrir árið 2026 var 1. október. Ef þið sóttuð ekki um, setjið frestinn fyrir 2027 strax í dagatalið.
- **Matvælasjóður:** fresturinn hefur verið snemma árs (2026: 4. mars). Sjóðurinn snýr að matvælaframleiðslu og ég er ekki viss um að myndgreiningarkerfi falli undir hann. Spyrjið sjóðinn, t.d. um rannsóknaflokkinn Kelda með fiskvinnslu eða Matís sem samstarfsaðila.

**Svo ég geti sagt hvaða flokkur hentar ykkur best:**
1. Hvar er kerfið statt: frumgerð í þróun, eða þegar í prófun á færibandi hjá fiskvinnslu?
2. Hafið þið áður fengið styrk úr Tækniþróunarsjóði eða Uppbyggingarsjóði?
3. Sóttuð þið um skattfrádrátt fyrir árið 2026?

Heimildir:
- [Sproti (Styrkjatorg)](https://island.is/styrkjatorg/styrkur/1-46) · [Vöxtur](https://island.is/styrkjatorg/styrkur/1-47) · [Fræ/Þróunarfræ](https://island.is/styrkjatorg/styrkur/1-42) · [Yfirlit styrkjaflokka](https://island.is/v/taeknithrounarsjodur/yfirlit-styrkjaflokka)
- [Vorúthlutun 2026](https://island.is/frett/fulltruar-49-verkefna-fa-styrk-ad-andvirdi-803-milljona-krona-i-voruthlutun-taeknithrounarsjods) · [Lög nr. 26/2021 (falla úr gildi 1.1.2027)](https://www.althingi.is/lagas/157c/2021026.html) · [Samráðsgátt: frumvarpið](https://island.is/samradsgatt/mal/3858) · [Stjórnarráðið 1. júní 2026](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2026/06/01/Sjodir-sameinadir-og-haskolasamstaeda-verdur-til-)
- [Uppbyggingarsjóður SSNE](https://www.ssne.is/is/malaflokkar/soknaraaetlun/uppbyggingarsjodur) · [Úthlutunarreglur 2027](https://www.ssne.is/static/files/Soknaraaetlun/Uppbyggingarsjodur/uthlutunarreglur-2027.pdf)
- [EuroHPC Playground](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/playground-access-ai-factories_en) · [Fast Lane](https://eurohpc-ju.europa.eu/ai-factories/ai-factories-access-calls/fast-lane-access-ai-factories_en) · [LUMI AI Factory aðgangur](https://lumi-supercomputer.eu/access-calls-for-ai-factories/) · [AIFA-ICE (CORDIS)](https://cordis.europa.eu/project/id/101263254)
- [Skattfrádráttur 2026 (Rannís)](https://island.is/s/rannis/frett/opid-fyrir-nyjar-umsoknir-um-skattfradratt-vegna-rannsokna-og-throunarverkefna-a-arinu-2026) · [Matvælasjóður](https://www.stjornarradid.is/verkefni/atvinnuvegir/matvaeli-og-matvaelaoryggi/matvaelasjodur/)

## Founder, turn 2
Takk fyrir þetta!
1. Kerfið er komið í prófun, við erum með tvær tilraunauppsetningar í fiskvinnslum.
2. Nei, höfum ekki fengið styrk úr Tækniþróunarsjóði og ekki úr Uppbyggingarsjóði heldur.
3. Við höfum fengið endurgreiðslu fyrir kostnað 2024 og 2025, en ég er ekki viss hvort það var sótt um fyrir 2026.

## Assistant, turn 2
Takk, þetta skýrir margt. Með tvær tilraunauppsetningar í gangi eruð þið komin fram yfir Fræ. Þið passið hins vegar í Sprota eða Vöxt þegar nýi sjóðurinn opnar. Tvennt þarf þó að gera strax í þessari viku.

**1. Athugið skattfrádráttinn fyrir 2026 strax**
Samkvæmt reglugerð nr. 758/2011 gildir staðfesting Rannís aðeins fyrir eitt tekjuár í senn. Það þarf því að sækja um á hverju ári:
- **Framhald á sama verkefni:** sótt er um framlengingu fyrir 1. apríl. Þeir sem fengu staðfestingu eftir 1. apríl 2025 máttu þó sækja um fyrir 2026 til 1. október 2026.
- **Nýtt verkefni:** umsókn fyrir 1. október.

Báðir frestirnir fyrir 2026 eru liðnir. Kíkið á Mínar síður hjá Rannís eða spyrjið endurskoðandann hvort umsókn fyrir 2026 hafi farið inn. Ef ekki, sendið strax póst á skattfradrattur@rannis.is og spyrjið hvort eitthvað sé hægt að gera. Ég fann ekkert ákvæði sem leyfir umsóknir eftir frest. Gerið því ráð fyrir að kostnaður ársins 2026 falli utan. Þá missið þið allt að 35% af þróunarkostnaði ársins.

Fyrir 2027: sama verkefni má aðeins framlengja þrisvar. Ef verkefnið hefur verið í gangi síðan 2024 er 2027 líklega síðasta árið sem má framlengja það. Eftir það þarf nýtt verkefni og umsókn fyrir 1. október.

**2. Uppbyggingarsjóður SSNE: frestur á miðvikudag, 21. október kl. 14:00**
Þið hafið ekki fengið styrk þaðan áður, svo engar ógerðar lokaskýrslur standa í vegi. Tilraunauppsetningarnar gefa ykkur raunhæft 12 mánaða verkefni. Dæmi: að breyta tveimur tilraunauppsetningum í kerfi sem er tilbúið í rekstur. Hafið þetta í huga:
- Sjóðurinn styrkir að jafnaði mest 50% af styrkhæfum kostnaði.
- Kostnaður sem fellur til fyrir 21. október er ekki styrkhæfur. Tölvukaup eru það ekki heldur, svo skjákort eða vinnustöð fyrir þjálfun fellur líklega utan.
- Laun eru reiknuð af greiddum launum að viðbættum launatengdum gjöldum, ekki af útseldum taxta.

Ég get hjálpað ykkur að setja saman verkáætlun og fjárhagsáætlun fyrir miðvikudag ef þið viljið.

**3. Hvaða flokkur í Tækniþróunarsjóði (eða arftaka hans)**
- **Fræ** er fyrir verkefni „á hugmyndastigi eða á frumstigi í þróun afurðar“. Þið eruð líklega komin fram yfir það.
- **Þróunarfræ** er forkönnunarstyrkur til að ráðast í þróunarsamvinnuverkefni. Hann gæti átt við ef þið ætlið í formlegt samstarf við vinnslurnar. Hann er opinn núna, 2 m.kr. án mótframlags, en spyrjið Rannís hvort hann passi.
- **Sproti:** allt að 24 m.kr., ekkert mótframlag. Hann er fyrir ung fyrirtæki með verkefni á frumstigi, og þið eruð á mörkunum.
- **Vöxtur:** allt að 60 m.kr., fyrir verkefni sem eru komin af hugmyndastigi eins og ykkar. Þar þarf mótframlag samkvæmt ríkisaðstoðarreglum ESA. Ég fann ekki fasta prósentu, svo spyrjið Rannís.

Hvorki Sproti né Vöxtur eru opnir núna. Næsta kall kemur frá nýja Nýsköpunarsjóðnum. Notið veturinn til að skrifa umsóknina og lagið hana svo að kallinu þegar það birtist.

**Athugið: þak á samanlagðan stuðning**
Reglugerðin um skattfrádrátt setur þak á samanlagðan opinberan stuðning við sama kostnað. Fyrir lítið fyrirtæki er þakið 45% í þróunarverkefni og 60% í samstarfsverkefni. Styrkur frá SSNE eða Tækniþróunarsjóði á sama kostnað getur því lækkað endurgreiðsluna. Haldið styrktum kostnaði aðskildum í bókhaldi og farið yfir þetta með endurskoðanda.

**Tvær spurningar:**
1. Eru vinnslurnar tvær á Norðurlandi eystra? Sjóðurinn metur umsóknir út frá sóknaráætlun landshlutans, svo það gæti styrkt umsóknina til SSNE.
2. Hvað kostar þróunin á ári, gróflega, og hversu mikið getið þið lagt fram sjálf? Þá get ég sagt hvort Sproti eða Vöxtur hentar betur.

Heimildir:
- [Reglugerð nr. 758/2011 um skattfrádrátt](https://island.is/reglugerdir/nr/0758-2011) · [Tilkynning Rannís, 26. mars 2026](https://island.is/s/rannis/frett/tilkynning-vegna-urvinnslu-umsokna-um-endurgreidslu-rannsoknar-og) · [Skattfrádráttur 2026](https://island.is/s/rannis/frett/opid-fyrir-nyjar-umsoknir-um-skattfradratt-vegna-rannsokna-og-throunarverkefna-a-arinu-2026)
- [Uppbyggingarsjóður SSNE](https://www.ssne.is/is/malaflokkar/soknaraaetlun/uppbyggingarsjodur) · [Úthlutunarreglur](https://www.ssne.is/static/files/Soknaraaetlun/Uppbyggingarsjodur/uthlutunarreglur-2027.pdf)
- [Fræ/Þróunarfræ](https://island.is/styrkjatorg/styrkur/1-42) · [Sproti](https://island.is/styrkjatorg/styrkur/1-46) · [Vöxtur](https://island.is/styrkjatorg/styrkur/1-47) · [Yfirlit styrkjaflokka](https://island.is/v/taeknithrounarsjodur/yfirlit-styrkjaflokka)
