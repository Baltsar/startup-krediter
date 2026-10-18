"""Labels and questions generated from a rule, in the founder's language.

A rule is {field, op, value}. The text the founder sees is derived from those
three parts and nothing else, so the glyph can never claim more than the rule
checks. The old free-text labels let "early research spinout" stand for a rule
that only looked at the stage, and a founder with no company and no research
saw a green mark. Generated labels make that impossible by construction.

Languages: en, sv, fi, no, da. Unknown languages fall back to English.
"""

from __future__ import annotations

LANGS = ("en", "sv", "fi", "no", "da")
DEFAULT_LANG = "en"

COUNTRY_NAMES: dict[str, dict[str, str]] = {
    "en": {"SE": "Sweden", "FI": "Finland", "NO": "Norway", "DK": "Denmark", "IS": "Iceland", "EU": "the EU or an associated country"},
    "sv": {"SE": "Sverige", "FI": "Finland", "NO": "Norge", "DK": "Danmark", "IS": "Island", "EU": "EU eller ett associerat land"},
    "fi": {"SE": "Ruotsi", "FI": "Suomi", "NO": "Norja", "DK": "Tanska", "IS": "Islanti", "EU": "EU tai assosioitunut maa"},
    "no": {"SE": "Sverige", "FI": "Finland", "NO": "Norge", "DK": "Danmark", "IS": "Island", "EU": "EU eller et assosiert land"},
    "da": {"SE": "Sverige", "FI": "Finland", "NO": "Norge", "DK": "Danmark", "IS": "Island", "EU": "EU eller et associeret land"},
}

# Finnish "registered in X" takes the inessive case; the names above are nominative.
COUNTRY_IN_FI: dict[str, str] = {"SE": "Ruotsissa", "FI": "Suomessa", "NO": "Norjassa", "DK": "Tanskassa", "IS": "Islannissa", "EU": "EU:ssa tai assosioituneessa maassa"}

LEGAL_FORM_NAMES: dict[str, dict[str, str]] = {
    "en": {"company": "a company", "none": "no company yet", "sole_trader": "a sole trader", "nonprofit": "a non-profit", "academia": "a university or research institute", "public": "the public sector"},
    "sv": {"company": "ett bolag", "none": "inget bolag än", "sole_trader": "enskild firma", "nonprofit": "en ideell förening", "academia": "ett universitet eller forskningsinstitut", "public": "offentlig sektor"},
    "fi": {"company": "yhtiö", "none": "ei vielä yhtiötä", "sole_trader": "toiminimi", "nonprofit": "yhdistys tai säätiö", "academia": "yliopisto tai tutkimuslaitos", "public": "julkinen sektori"},
    "no": {"company": "et selskap", "none": "ikke noe selskap ennå", "sole_trader": "enkeltpersonforetak", "nonprofit": "en ideell organisasjon", "academia": "et universitet eller forskningsinstitutt", "public": "offentlig sektor"},
    "da": {"company": "et selskab", "none": "intet selskab endnu", "sole_trader": "enkeltmandsvirksomhed", "nonprofit": "en nonprofit-organisation", "academia": "et universitet eller forskningsinstitution", "public": "den offentlige sektor"},
}

STAGE_NAMES: dict[str, dict[str, str]] = {
    "en": {"idea": "idea", "pre_seed": "pre-seed", "seed": "seed", "series_a": "series A", "later": "after series A"},
    "sv": {"idea": "idé", "pre_seed": "pre-seed", "seed": "seed", "series_a": "serie A", "later": "efter serie A"},
    "fi": {"idea": "idea", "pre_seed": "pre-seed", "seed": "seed", "series_a": "A-kierros", "later": "A-kierroksen jälkeen"},
    "no": {"idea": "idé", "pre_seed": "pre-seed", "seed": "seed", "series_a": "serie A", "later": "etter serie A"},
    "da": {"idea": "idé", "pre_seed": "pre-seed", "seed": "seed", "series_a": "serie A", "later": "efter serie A"},
}

SECTOR_NAMES: dict[str, dict[str, str]] = {
    "en": {"ai": "AI", "deeptech": "deep tech", "energy": "energy", "climate": "climate", "health": "health", "fintech": "fintech", "saas": "SaaS", "hardware": "hardware"},
    "sv": {"ai": "AI", "deeptech": "deep tech", "energy": "energi", "climate": "klimat", "health": "hälsa", "fintech": "fintech", "saas": "SaaS", "hardware": "hårdvara"},
    "fi": {"ai": "tekoäly", "deeptech": "deep tech", "energy": "energia", "climate": "ilmasto", "health": "terveys", "fintech": "fintech", "saas": "SaaS", "hardware": "laitteisto"},
    "no": {"ai": "KI", "deeptech": "deep tech", "energy": "energi", "climate": "klima", "health": "helse", "fintech": "fintech", "saas": "SaaS", "hardware": "maskinvare"},
    "da": {"ai": "AI", "deeptech": "deep tech", "energy": "energi", "climate": "klima", "health": "sundhed", "fintech": "fintech", "saas": "SaaS", "hardware": "hardware"},
}

VENDOR_NAMES: dict[str, str] = {
    "aws": "AWS", "gcp": "Google Cloud", "azure": "Azure", "cloudflare": "Cloudflare", "vercel": "Vercel",
    "supabase": "Supabase", "neon": "Neon", "mongodb": "MongoDB", "anthropic": "Anthropic", "openai": "OpenAI",
    "mistral": "Mistral", "together": "Together AI", "modal": "Modal", "lambda": "Lambda", "runpod": "Runpod",
    "huggingface": "Hugging Face", "replicate": "Replicate", "nvidia": "NVIDIA",
}

# Hard requirements a page states that no company fact can express: an affiliation, a region, a research origin,
# a partner already committed. A record uses {"field": "confirmed", "op": "contains", "value": "<key>"} and the
# founder confirms with profile.confirmed: ["<key>"]. Until then the door stays open with this question, never green.
# Each key: lang -> (label, question).
CONFIRMATIONS: dict[str, dict[str, tuple[str, str]]] = {
    "kth_affiliation": {
        "en": ("a current KTH student, researcher or employee on the team", "Is one of you a current KTH student, researcher or employee?"),
        "sv": ("en nuvarande KTH-student, -forskare eller -anställd i teamet", "Är någon av er student, forskare eller anställd på KTH just nu?"),
        "fi": ("tiimissä nykyinen KTH:n opiskelija, tutkija tai työntekijä", "Onko joku teistä tällä hetkellä KTH:n opiskelija, tutkija tai työntekijä?"),
        "no": ("en nåværende KTH-student, -forsker eller -ansatt i teamet", "Er noen av dere student, forsker eller ansatt ved KTH nå?"),
        "da": ("en nuværende KTH-studerende, -forsker eller -ansat på holdet", "Er en af jer studerende, forsker eller ansat på KTH lige nu?"),
    },
    "research_background": {
        "en": ("the idea comes from research at a university or institute", "Is the idea based on research you did at a university or research institute?"),
        "sv": ("idén kommer från forskning vid universitet eller institut", "Bygger idén på forskning ni gjort vid ett universitet eller forskningsinstitut?"),
        "fi": ("idea perustuu yliopistossa tai tutkimuslaitoksessa tehtyyn tutkimukseen", "Perustuuko idea tutkimukseen, jonka teitte yliopistossa tai tutkimuslaitoksessa?"),
        "no": ("ideen kommer fra forskning ved et universitet eller institutt", "Bygger ideen på forskning dere har gjort ved et universitet eller forskningsinstitutt?"),
        "da": ("idéen kommer fra forskning på et universitet eller institut", "Bygger idéen på forskning, I har lavet på et universitet eller forskningsinstitut?"),
    },
    "hpc_experience": {
        "en": ("the team already runs its code on an HPC system", "Does the team already run its code on an HPC system?"),
        "sv": ("teamet kör redan sin kod på ett HPC-system", "Kör teamet redan sin kod på ett HPC-system?"),
        "fi": ("tiimi ajaa jo koodiaan HPC-järjestelmässä", "Ajaako tiimi jo koodiaan HPC-järjestelmässä?"),
        "no": ("teamet kjører allerede koden sin på et HPC-system", "Kjører teamet allerede koden sin på et HPC-system?"),
        "da": ("holdet kører allerede sin kode på et HPC-system", "Kører holdet allerede sin kode på et HPC-system?"),
    },
    "region_skane": {
        "en": ("the team is based in Skåne", "Is the team based in Skåne?"),
        "sv": ("teamet finns i Skåne", "Finns teamet i Skåne?"),
        "fi": ("tiimi toimii Skånessa", "Toimiiko tiimi Skånessa?"),
        "no": ("teamet holder til i Skåne", "Holder teamet til i Skåne?"),
        "da": ("holdet er baseret i Skåne", "Er holdet baseret i Skåne?"),
    },
    "region_vgr": {
        "en": ("the team is based in Västra Götaland", "Is the team based in Västra Götaland?"),
        "sv": ("teamet finns i Västra Götaland", "Finns teamet i Västra Götaland?"),
        "fi": ("tiimi toimii Länsi-Götanmaalla", "Toimiiko tiimi Länsi-Götanmaalla?"),
        "no": ("teamet holder til i Västra Götaland", "Holder teamet til i Västra Götaland?"),
        "da": ("holdet er baseret i Västra Götaland", "Er holdet baseret i Västra Götaland?"),
    },
    "consortium_partner": {
        "en": ("a partner organisation committed to apply with you", "Do you have a partner organisation committed to apply with you?"),
        "sv": ("en partnerorganisation som förbundit sig att söka med er", "Har ni en partnerorganisation som förbundit sig att söka tillsammans med er?"),
        "fi": ("kumppaniorganisaatio, joka on sitoutunut hakemaan kanssanne", "Onko teillä kumppaniorganisaatio, joka on sitoutunut hakemaan kanssanne?"),
        "no": ("en partnerorganisasjon som har forpliktet seg til å søke med dere", "Har dere en partnerorganisasjon som har forpliktet seg til å søke sammen med dere?"),
        "da": ("en partnerorganisation, der har forpligtet sig til at søge med jer", "Har I en partnerorganisation, der har forpligtet sig til at søge sammen med jer?"),
    },
    "dk_financial_foundation": {
        "en": ("at least DKK 100 000 raised in risk capital or grants in three years, or DKK 250 000 gross profit in one year", "Has the company raised at least DKK 100 000 in risk capital or development grants in the last three years, or had a gross profit of at least DKK 250 000 in one of its last three annual accounts?"),
        "sv": ("minst 100 000 DKK i riskkapital eller bidrag på tre år, eller 250 000 DKK i bruttovinst ett år", "Har bolaget tagit in minst 100 000 DKK i riskkapital eller utvecklingsbidrag de senaste tre åren, eller haft minst 250 000 DKK i bruttovinst i något av de tre senaste bokslut?"),
        "fi": ("vähintään 100 000 DKK riskipääomaa tai avustuksia kolmessa vuodessa, tai 250 000 DKK bruttokate yhtenä vuonna", "Onko yhtiö kerännyt vähintään 100 000 DKK riskipääomaa tai kehitysavustuksia kolmen viime vuoden aikana, tai onko sen bruttokate ollut vähintään 250 000 DKK jossakin kolmesta viimeisestä tilinpäätöksestä?"),
        "no": ("minst 100 000 DKK i risikokapital eller tilskudd på tre år, eller 250 000 DKK i bruttofortjeneste ett år", "Har selskapet hentet minst 100 000 DKK i risikokapital eller utviklingstilskudd de siste tre årene, eller hatt minst 250 000 DKK i bruttofortjeneste i ett av de tre siste regnskapene?"),
        "da": ("mindst 100.000 kr. i risikovillig kapital eller tilskud på tre år, eller 250.000 kr. i bruttofortjeneste ét år", "Har virksomheden rejst mindst 100.000 kr. i risikovillig kapital eller udviklingstilskud de seneste tre år, eller haft en bruttofortjeneste på mindst 250.000 kr. i et af de seneste tre årsregnskaber?"),
    },
    "baltic_marine_monitoring": {
        "en": ("a solution for monitoring the Baltic Sea marine environment", "Is your solution for monitoring the marine environment of the Baltic Sea, as the challenge asks?"),
        "sv": ("en lösning för att övervaka Östersjöns havsmiljö", "Är er lösning till för att övervaka Östersjöns havsmiljö, som utmaningen efterfrågar?"),
        "fi": ("ratkaisu Itämeren meriympäristön seurantaan", "Onko ratkaisunne tarkoitettu Itämeren meriympäristön seurantaan, kuten haaste edellyttää?"),
        "no": ("en løsning for å overvåke havmiljøet i Østersjøen", "Er løsningen deres laget for å overvåke havmiljøet i Østersjøen, slik utfordringen ber om?"),
        "da": ("en løsning til overvågning af Østersøens havmiljø", "Er jeres løsning til overvågning af Østersøens havmiljø, som udfordringen efterspørger?"),
    },
    "aws_paid_plan": {
        "en": ("AWS account on a paid plan (free plans are not eligible)", "Is your AWS account on a paid plan, or still on the free plan?"),
        "sv": ("AWS-konto på en betald plan (gratisplaner godkänns inte)", "Ligger ert AWS-konto på en betald plan, eller fortfarande på gratisplanen?"),
        "fi": ("AWS-tili maksullisella sopimuksella (ilmaiset eivät kelpaa)", "Onko AWS-tilinne maksullisella sopimuksella vai vielä ilmaisella?"),
        "no": ("AWS-konto på en betalt plan (gratisplaner godkjennes ikke)", "Er AWS-kontoen deres på en betalt plan, eller fortsatt på gratisplanen?"),
        "da": ("AWS-konto på en betalt plan (gratisplaner godkendes ikke)", "Er jeres AWS-konto på en betalt plan, eller stadig på gratisplanen?"),
    },
    "new_to_aws_activate": {
        "en": ("new to AWS Activate credits, or asking for more than you received before", "Has the company received AWS Activate credits before, and if so, how much?"),
        "sv": ("ny i AWS Activate, eller ber om mer än ni fått tidigare", "Har bolaget fått AWS Activate-krediter tidigare, och i så fall hur mycket?"),
        "fi": ("uusi AWS Activate -hyvitysten hakija, tai pyytää enemmän kuin aiemmin", "Onko yhtiö saanut AWS Activate -hyvityksiä aiemmin, ja jos on, kuinka paljon?"),
        "no": ("ny i AWS Activate, eller ber om mer enn dere har fått før", "Har selskapet fått AWS Activate-kreditter før, og i så fall hvor mye?"),
        "da": ("ny i AWS Activate, eller beder om mere end I har fået før", "Har virksomheden fået AWS Activate-kreditter før, og i så fald hvor meget?"),
    },
    "eip_competence_mix": {
        "en": ("at least two organisations covering two of: an entrepreneur in primary production or agri-food, a researcher, an adviser", "Can you bring together at least two organisations that between them have two of these: an entrepreneur in primary production or the agriculture and food sector, a researcher in the field, an adviser in the field?"),
        "sv": ("minst två organisationer med två av: företagare i primärproduktion eller jordbruk och livsmedel, forskare, rådgivare", "Kan ni samla minst två organisationer som tillsammans har två av de här: företagare inom primärproduktionen eller jordbruks- och livsmedelssektorn, forskare inom området, rådgivare inom området?"),
        "fi": ("vähintään kaksi organisaatiota, joilla on kaksi näistä: alkutuotannon tai maatalous- ja elintarvikealan yrittäjä, tutkija, neuvoja", "Saatteko koolle vähintään kaksi organisaatiota, joilla on yhdessä kaksi näistä: alkutuotannon tai maatalous- ja elintarvikealan yrittäjä, alan tutkija, alan neuvoja?"),
        "no": ("minst to organisasjoner med to av: næringsdrivende i primærproduksjon eller landbruk og mat, forsker, rådgiver", "Kan dere samle minst to organisasjoner som til sammen har to av disse: næringsdrivende i primærproduksjonen eller landbruks- og matsektoren, forsker på området, rådgiver på området?"),
        "da": ("mindst to organisationer med to af: erhvervsdrivende i primærproduktion eller landbrug og fødevarer, forsker, rådgiver", "Kan I samle mindst to organisationer, der tilsammen har to af disse: erhvervsdrivende i primærproduktionen eller landbrugs- og fødevaresektoren, forsker på området, rådgiver på området?"),
    },
    "se_rd_staff_on_payroll": {
        "en": ("someone on the payroll, with Swedish employer contributions, who spends at least half their actual working time and 15 hours a month on R&D", "Founders count only if the company pays them a salary: does the company pay salary, with Swedish employer contributions, to someone who works directly on research or development at least half their actual working time and at least 15 hours a month?"),
        "sv": ("någon på lönelistan, med svenska arbetsgivaravgifter, som lägger minst halva sin faktiska arbetstid och 15 timmar i månaden på FoU", "Grundare räknas bara om bolaget betalar dem lön: betalar bolaget lön, med svenska arbetsgivaravgifter, till någon som arbetar direkt med forskning eller utveckling minst halva sin faktiska arbetstid och minst 15 timmar i månaden?"),
        "fi": ("palkkalistalla oleva henkilö, jonka palkasta maksetaan Ruotsin työnantajamaksut ja joka tekee T&K-työtä vähintään puolet todellisesta työajastaan ja 15 tuntia kuukaudessa", "Perustajat lasketaan mukaan vain, jos yhtiö maksaa heille palkkaa: maksaako yhtiö palkkaa, josta maksetaan Ruotsin työnantajamaksut, henkilölle, joka tekee suoraan tutkimus- tai kehitystyötä vähintään puolet todellisesta työajastaan ja vähintään 15 tuntia kuukaudessa?"),
        "no": ("noen på lønningslisten, med svensk arbeidsgiveravgift, som bruker minst halvparten av sin faktiske arbeidstid og 15 timer i måneden på FoU", "Gründere teller bare hvis selskapet betaler dem lønn: betaler selskapet lønn, med svensk arbeidsgiveravgift, til noen som jobber direkte med forskning eller utvikling minst halvparten av sin faktiske arbeidstid og minst 15 timer i måneden?"),
        "da": ("en på lønningslisten, med svenske arbejdsgiverafgifter, der bruger mindst halvdelen af sin faktiske arbejdstid og 15 timer om måneden på F&U", "Stiftere tæller kun med, hvis virksomheden betaler dem løn: betaler virksomheden løn, med svenske arbejdsgiverafgifter, til en person, der arbejder direkte med forskning eller udvikling mindst halvdelen af sin faktiske arbejdstid og mindst 15 timer om måneden?"),
    },
    "eur_200k_raised_or_revenue": {
        "en": ("at least EUR 200 000 raised, or yearly revenue over EUR 200 000", "Has the company raised at least EUR 200 000 in total, from investors or non-dilutive sources such as grants, or does it have yearly revenue over EUR 200 000?"),
        "sv": ("minst 200 000 EUR i insamlat kapital, eller årsomsättning över 200 000 EUR", "Har bolaget tagit in minst 200 000 EUR totalt, från investerare eller som bidrag och annan icke-utspädande finansiering, eller har det en årsomsättning över 200 000 EUR?"),
        "fi": ("vähintään 200 000 EUR kerättyä rahoitusta tai yli 200 000 EUR vuosiliikevaihto", "Onko yhtiö kerännyt yhteensä vähintään 200 000 EUR sijoittajilta tai laimentamattomana rahoituksena, kuten avustuksina, tai onko sen vuosiliikevaihto yli 200 000 EUR?"),
        "no": ("minst 200 000 EUR hentet, eller årlig omsetning over 200 000 EUR", "Har selskapet hentet minst 200 000 EUR totalt, fra investorer eller som tilskudd og annen ikke-utvannende finansiering, eller har det en årlig omsetning over 200 000 EUR?"),
        "da": ("mindst 200.000 EUR rejst, eller årlig omsætning over 200.000 EUR", "Har virksomheden rejst mindst 200.000 EUR i alt, fra investorer eller som tilskud og anden ikke-udvandende finansiering, eller har den en årlig omsætning over 200.000 EUR?"),
    },
    "group_within_sme_limits": {
        "en": ("the group's combined figures within SME limits", "No public body owns 25% or more, and with the owner group's figures added as the EU SME rules require, are you still under 250 staff and EUR 50M turnover or EUR 43M balance sheet?"),
        "sv": ("koncernens samlade siffror inom SME-gränserna", "Äger ingen offentlig aktör 25 % eller mer, och med ägarkoncernens siffror inräknade enligt EU:s SME-regler, är ni fortfarande under 250 anställda och 50 MEUR i omsättning eller 43 MEUR i balansomslutning?"),
        "fi": ("konsernin yhteenlasketut luvut pk-rajoissa", "Jos mikään julkinen toimija ei omista 25 % tai enemmän, jäättekö omistajakonsernin luvut mukaan lukien EU:n pk-sääntöjen mukaan alle 250 henkilön ja 50 MEUR:n liikevaihdon tai 43 MEUR:n taseen?"),
        "no": ("konsernets samlede tall innenfor SMB-grensene", "Eier ingen offentlig aktør 25 % eller mer, og med eierkonsernets tall regnet med etter EUs SMB-regler, er dere fortsatt under 250 ansatte og 50 MEUR i omsetning eller 43 MEUR i balanse?"),
        "da": ("koncernens samlede tal inden for SMV-grænserne", "Ejer ingen offentlig aktør 25 % eller mere, og med ejerkoncernens tal medregnet efter EU's SMV-regler, er I stadig under 250 ansatte og 50 MEUR i omsætning eller 43 MEUR i balance?"),
    },
    "group_within_small_enterprise_limits": {
        "en": ("the group's combined figures within EU small-enterprise limits", "With the owner group's figures added as the EU rules require, are you still under 50 staff and EUR 10M turnover or balance sheet?"),
        "sv": ("koncernens samlade siffror inom EU:s gränser för små företag", "Med ägarkoncernens siffror inräknade enligt EU:s regler, är ni fortfarande under 50 anställda och 10 MEUR i omsättning eller balansomslutning?"),
        "fi": ("konsernin yhteenlasketut luvut EU:n pienyritysrajoissa", "Kun omistajakonsernin luvut lasketaan mukaan EU:n sääntöjen mukaan, jäättekö alle 50 henkilön ja 10 MEUR:n liikevaihdon tai taseen?"),
        "no": ("konsernets samlede tall innenfor EUs grenser for små foretak", "Med eierkonsernets tall regnet med etter EUs regler, er dere fortsatt under 50 ansatte og 10 MEUR i omsetning eller balanse?"),
        "da": ("koncernens samlede tal inden for EU's grænser for små virksomheder", "Med ejerkoncernens tal medregnet efter EU's regler, er I stadig under 50 ansatte og 10 MEUR i omsætning eller balance?"),
    },
    "group_unlisted_within_10msek": {
        "en": ("the whole group unlisted, with revenue or balance sheet at most 10 MSEK", "Is the whole group unlisted, with net revenue or balance sheet total of at most 10 MSEK?"),
        "sv": ("hela koncernen onoterad, med omsättning eller balansomslutning högst 10 MSEK", "Är hela koncernen onoterad, med nettoomsättning eller balansomslutning på högst 10 MSEK?"),
        "fi": ("koko konserni listaamaton, liikevaihto tai tase enintään 10 MSEK", "Onko koko konserni listaamaton, ja onko sen liikevaihto tai tase enintään 10 MSEK?"),
        "no": ("hele konsernet unotert, med omsetning eller balanse høyst 10 MSEK", "Er hele konsernet unotert, med omsetning eller balanse på høyst 10 MSEK?"),
        "da": ("hele koncernen unoteret, med omsætning eller balance højst 10 MSEK", "Er hele koncernen unoteret, med omsætning eller balance på højst 10 MSEK?"),
    },
    "owners_all_natural_persons": {
        "en": ("every shareholder a private person", "Are all shareholders private persons, with no holding company, fund or university among them?"),
        "sv": ("alla aktieägare är privatpersoner", "Är alla aktieägare privatpersoner, utan holdingbolag, fond eller universitet bland dem?"),
        "fi": ("kaikki osakkaat yksityishenkilöitä", "Ovatko kaikki osakkaat yksityishenkilöitä, ilman holdingyhtiötä, rahastoa tai yliopistoa?"),
        "no": ("alle aksjonærer er privatpersoner", "Er alle aksjonærene privatpersoner, uten holdingselskap, fond eller universitet blant dem?"),
        "da": ("alle aktionærer er privatpersoner", "Er alle aktionærer privatpersoner, uden holdingselskab, fond eller universitet blandt dem?"),
    },
    "equity_majority_eu_efta_uk": {
        "en": ("at least half the equity held in the EU, EFTA or the UK", "Is at least half of the company owned by owners in the EU, EFTA or the UK?"),
        "sv": ("minst hälften av ägandet inom EU, EFTA eller Storbritannien", "Ägs minst hälften av bolaget av ägare i EU, EFTA eller Storbritannien?"),
        "fi": ("vähintään puolet omistuksesta EU:ssa, EFTA-maissa tai Britanniassa", "Omistavatko EU:n, EFTA-maiden tai Britannian omistajat vähintään puolet yhtiöstä?"),
        "no": ("minst halvparten av eierskapet i EU, EFTA eller Storbritannia", "Eies minst halvparten av selskapet av eiere i EU, EFTA eller Storbritannia?"),
        "da": ("mindst halvdelen af ejerskabet i EU, EFTA eller Storbritannien", "Ejes mindst halvdelen af virksomheden af ejere i EU, EFTA eller Storbritannien?"),
    },
    "fulltime_team_member": {
        "en": ("at least one team member full-time in the company", "Does at least one person on the team work full-time in the company, with no duties elsewhere?"),
        "sv": ("minst en i teamet på heltid i bolaget", "Arbetar minst en person i teamet heltid i bolaget, utan uppdrag på annat håll?"),
        "fi": ("vähintään yksi tiimiläinen kokoaikaisesti yrityksessä", "Työskenteleekö vähintään yksi tiimin jäsen kokoaikaisesti yrityksessä ilman muita tehtäviä?"),
        "no": ("minst én i teamet på heltid i selskapet", "Jobber minst én person i teamet heltid i selskapet, uten oppgaver andre steder?"),
        "da": ("mindst én i teamet på fuld tid i virksomheden", "Arbejder mindst én person i teamet fuld tid i virksomheden, uden opgaver andre steder?"),
    },
    "project_lead_employed": {
        "en": ("the project lead employed by the company", "Will the project lead be employed by the company, with an employment contract and salary?"),
        "sv": ("projektledaren anställd i bolaget", "Kommer projektledaren att vara anställd i bolaget, med anställningsavtal och lön?"),
        "fi": ("projektipäällikkö työsuhteessa yritykseen", "Onko projektipäällikkö työsuhteessa yritykseen, työsopimuksella ja palkalla?"),
        "no": ("prosjektlederen ansatt i selskapet", "Blir prosjektlederen ansatt i selskapet, med arbeidskontrakt og lønn?"),
        "da": ("projektlederen ansat i virksomheden", "Bliver projektlederen ansat i virksomheden, med ansættelseskontrakt og løn?"),
    },
    "no_earlier_bf_funding_same_solution": {
        "en": ("no earlier Business Finland funding for the same solution", "Has Business Finland funded this same solution before, through Sprint, Tempo, R&D, YIC, DTA or ESA BIC, for you or another company?"),
        "sv": ("ingen tidigare finansiering från Business Finland för samma lösning", "Har Business Finland finansierat just den här lösningen förut, via Sprint, Tempo, FoU, YIC, DTA eller ESA BIC, hos er eller ett annat bolag?"),
        "fi": ("ei aiempaa Business Finlandin rahoitusta samalle ratkaisulle", "Onko Business Finland rahoittanut juuri tätä ratkaisua aiemmin Sprintin, Tempon, T&K-rahoituksen, YIC:n, DTA:n tai ESA BIC:n kautta, teille tai toiselle yritykselle?"),
        "no": ("ingen tidligere finansiering fra Business Finland for samme løsning", "Har Business Finland finansiert akkurat denne løsningen før, via Sprint, Tempo, FoU, YIC, DTA eller ESA BIC, hos dere eller et annet selskap?"),
        "da": ("ingen tidligere finansiering fra Business Finland til samme løsning", "Har Business Finland finansieret præcis denne løsning før, via Sprint, Tempo, FoU, YIC, DTA eller ESA BIC, hos jer eller en anden virksomhed?"),
    },
    "research_west_sweden_university": {
        "en": ("the idea builds on research at a university in western Sweden", "Does the idea build on research done at a university in western Sweden, such as Chalmers or the University of Gothenburg?"),
        "sv": ("idén bygger på forskning vid ett lärosäte i västra Sverige", "Bygger idén på forskning vid ett lärosäte i västra Sverige, till exempel Chalmers eller Göteborgs universitet?"),
        "fi": ("idea perustuu tutkimukseen länsiruotsalaisessa yliopistossa", "Perustuuko idea tutkimukseen, joka on tehty Länsi-Ruotsin yliopistossa, kuten Chalmersissa tai Göteborgin yliopistossa?"),
        "no": ("ideen bygger på forskning ved et universitet i Vest-Sverige", "Bygger ideen på forskning ved et universitet i Vest-Sverige, for eksempel Chalmers eller Göteborgs universitet?"),
        "da": ("idéen bygger på forskning ved et universitet i Vestsverige", "Bygger idéen på forskning ved et universitet i Vestsverige, for eksempel Chalmers eller Göteborgs universitet?"),
    },
    "eic_running_grant_only_applying_blended": {
        "en": ("a running EIC grant-only project, now applying for blended finance or investment only", "Is your running EIC project grant only, and are you now applying for blended finance or investment only?"),
        "sv": ("ett pågående EIC-projekt med enbart bidrag, och nu söker ni blandad finansiering eller enbart investering", "Är ert pågående EIC-projekt ett rent bidrag, och söker ni nu blandad finansiering eller enbart investering?"),
        "fi": ("käynnissä oleva pelkän avustuksen EIC-hanke, ja nyt haette yhdistelmärahoitusta tai pelkkää sijoitusta", "Onko käynnissä oleva EIC-hankkeenne pelkkä avustus, ja haetteko nyt yhdistelmärahoitusta tai pelkkää sijoitusta?"),
        "no": ("et løpende EIC-prosjekt med bare tilskudd, og nå søker dere blandet finansiering eller bare investering", "Er det løpende EIC-prosjektet deres bare tilskudd, og søker dere nå blandet finansiering eller bare investering?"),
        "da": ("et igangværende EIC-projekt med kun tilskud, og nu søger I blandet finansiering eller kun investering", "Er jeres igangværende EIC-projekt kun tilskud, og søger I nu blandet finansiering eller kun investering?"),
    },
    "no_third_country_control": {
        "en": ("not controlled from a country outside the EU and Norway", "Is the company free of control by any country or company outside the EU and Norway, or has your government approved guarantees?"),
        "sv": ("inte kontrollerat från ett land utanför EU och Norge", "Är bolaget fritt från kontroll av något land eller bolag utanför EU och Norge, eller har regeringen godkänt garantier?"),
        "fi": ("ei määräysvaltaa EU:n ja Norjan ulkopuolelta", "Onko yritys vapaa EU:n ja Norjan ulkopuolisen maan tai yrityksen määräysvallasta, tai onko hallitus hyväksynyt takuut?"),
        "no": ("ikke kontrollert fra et land utenfor EU og Norge", "Er selskapet fritt for kontroll fra land eller selskaper utenfor EU og Norge, eller har regjeringen godkjent garantier?"),
        "da": ("ikke kontrolleret fra et land uden for EU og Norge", "Er virksomheden fri for kontrol fra lande eller virksomheder uden for EU og Norge, eller har regeringen godkendt garantier?"),
    },
    "business_not_yet_fulltime": {
        "en": ("the business not yet run full-time", "Have you not yet started running the business full-time, by selling, marketing or registering for VAT or as an employer?"),
        "sv": ("verksamheten inte startad på heltid än", "Har du ännu inte börjat driva verksamheten på heltid, genom försäljning, marknadsföring eller registrering för moms eller som arbetsgivare?"),
        "fi": ("yritystoimintaa ei vielä aloitettu päätoimisesti", "Oletko vielä aloittamatta päätoimista yritystoimintaa, eli myyntiä, markkinointia tai rekisteröitymistä arvonlisäverovelvolliseksi tai työnantajaksi?"),
        "no": ("virksomheten ikke startet på heltid ennå", "Har du ennå ikke begynt å drive virksomheten på heltid, gjennom salg, markedsføring eller registrering for mva eller som arbeidsgiver?"),
        "da": ("virksomheden ikke startet på fuld tid endnu", "Er du endnu ikke begyndt at drive virksomheden på fuld tid, gennem salg, markedsføring eller registrering for moms eller som arbejdsgiver?"),
    },
    "owner_is_founders_own_holding": {
        "en": ("the owning company is the founders' own holding company", "Is the company that owns half or more of yours a holding company owned by the founders themselves?"),
        "sv": ("ägarbolaget är grundarnas eget holdingbolag", "Är bolaget som äger hälften eller mer av ert ett holdingbolag som grundarna själva äger?"),
        "fi": ("omistava yhtiö on perustajien oma holdingyhtiö", "Onko vähintään puolet yrityksestänne omistava yhtiö perustajien itse omistama holdingyhtiö?"),
        "no": ("eierselskapet er gründernes eget holdingselskap", "Er selskapet som eier halvparten eller mer av deres, et holdingselskap gründerne selv eier?"),
        "da": ("ejerselskabet er stifternes eget holdingselskab", "Er selskabet, der ejer halvdelen eller mere af jeres, et holdingselskab, som stifterne selv ejer?"),
    },
    "separate_from_owner_operations": {
        "en": ("the business clearly separate from the owning company's operations", "Is your business clearly separate from the operations of the company that owns 25% or more, with a different idea and its own chair or CEO?"),
        "sv": ("verksamheten tydligt skild från ägarbolagets drift", "Är er verksamhet tydligt skild från driften i bolaget som äger 25 % eller mer, med en annan idé och egen ordförande eller vd?"),
        "fi": ("liiketoiminta selvästi erillään omistajayhtiön toiminnasta", "Onko liiketoimintanne selvästi erillään vähintään 25 % omistavan yhtiön toiminnasta, eri idealla ja omalla hallituksen puheenjohtajalla tai toimitusjohtajalla?"),
        "no": ("virksomheten tydelig adskilt fra eierselskapets drift", "Er virksomheten deres tydelig adskilt fra driften i selskapet som eier 25 % eller mer, med en annen idé og egen styreleder eller daglig leder?"),
        "da": ("virksomheden tydeligt adskilt fra ejerselskabets drift", "Er jeres virksomhed tydeligt adskilt fra driften i selskabet, der ejer 25 % eller mere, med en anden idé og egen formand eller direktør?"),
    },
    "each_founder_owns_12_5_percent": {
        "en": ("each applying founder owns at least 12.5%", "Will each founder in the programme own at least 12.5% of the company at the start?"),
        "sv": ("varje sökande grundare äger minst 12,5 %", "Kommer varje grundare i programmet att äga minst 12,5 % av bolaget vid start?"),
        "fi": ("jokainen hakeva perustaja omistaa vähintään 12,5 %", "Omistaako jokainen ohjelmaan osallistuva perustaja vähintään 12,5 % yrityksestä ohjelman alkaessa?"),
        "no": ("hver søkende gründer eier minst 12,5 %", "Vil hver gründer i programmet eie minst 12,5 % av selskapet ved start?"),
        "da": ("hver ansøgende stifter ejer mindst 12,5 %", "Vil hver stifter i programmet eje mindst 12,5 % af virksomheden ved start?"),
    },
    "independent_investor_commits": {
        "en": ("an independent private investor puts in money alongside the loan", "Does an independent private investor, such as a business angel, put money into the company alongside the loan?"),
        "sv": ("en oberoende privat investerare skjuter till pengar vid sidan av lånet", "Skjuter en oberoende privat investerare, till exempel en affärsängel, till pengar i bolaget vid sidan av lånet?"),
        "fi": ("riippumaton yksityinen sijoittaja sijoittaa lainan rinnalla", "Sijoittaako riippumaton yksityinen sijoittaja, esimerkiksi bisnesenkeli, yritykseen rahaa lainan rinnalla?"),
        "no": ("en uavhengig privat investor skyter inn penger ved siden av lånet", "Skyter en uavhengig privat investor, for eksempel en engleinvestor, inn penger i selskapet ved siden av lånet?"),
        "da": ("en uafhængig privat investor skyder penge ind ved siden af lånet", "Skyder en uafhængig privat investor, fx en business angel, penge ind i virksomheden ved siden af lånet?"),
    },
    "need_owner": {
        "en": ("an established need owner committed to the project", "Do you have an established company or organisation committed as need owner in the project?"),
        "sv": ("en etablerad behovsägare som förbundit sig till projektet", "Har ni ett etablerat bolag eller en organisation som förbundit sig som behovsägare i projektet?"),
        "fi": ("vakiintunut tarpeen omistaja sitoutunut hankkeeseen", "Onko teillä vakiintunut yritys tai organisaatio sitoutuneena hankkeen tarpeen omistajaksi?"),
        "no": ("en etablert behovseier som har forpliktet seg til prosjektet", "Har dere et etablert selskap eller en organisasjon som har forpliktet seg som behovseier i prosjektet?"),
        "da": ("en etableret behovsejer, der har forpligtet sig til projektet", "Har I en etableret virksomhed eller organisation, der har forpligtet sig som behovsejer i projektet?"),
    },
}

# Grant keys a rule can name in prior_grants or active_grants: program ids from the data,
# or a short key for a grant the data does not list. The name is the funder's own, in every language.
GRANT_NAMES: dict[str, str] = {
    "vinnova-innovativa-startups-2025": "Vinnova Innovativa startups 2025",
    "eureka-innowwide-2022": "Eureka Innowwide 2022",
    "eureka-innowwide-2023": "Eureka Innowwide 2023",
    "eureka-innowwide-2024": "Eureka Innowwide 2024",
    "eureka-innowwide-2025": "Eureka Innowwide 2025",
    "business-finland-sprint": "Business Finland Sprint",
    "business-finland-tempo": "Business Finland Tempo",
    "business-finland-rd-funding": "Business Finland R&D funding",
    "business-finland-yic": "Business Finland Young Innovative Companies",
    "business-finland-deep-tech-accelerator": "Business Finland Deep Tech Accelerator",
    "business-finland-growth-engine-startup": "Business Finland Growth Engine startup funding",
    "esa-bic": "ESA BIC",
    "eic-accelerator": "EIC Accelerator",
    "eic-accelerator-pilot": "EIC Accelerator Pilot",
    "sme-instrument": "SME Instrument",
    "innovationsfonden-innofounder": "InnoFounder",
    "rannis-frae": "Rannís Fræ",
    "rannis-sproti": "Rannís Sproti",
    "rannis-voxtur": "Rannís Vöxtur",
    "rannis-hagnyt-rannsoknarverkefni": "Rannís Hagnýt rannsóknarverkefni",
}

AFFILIATION_NAMES: dict[str, dict[str, str]] = {
    "en": {"student": "a university student", "researcher": "a university researcher", "staff": "university staff", "none": "no university link"},
    "sv": {"student": "student vid ett lärosäte", "researcher": "forskare vid ett lärosäte", "staff": "anställd vid ett lärosäte", "none": "ingen koppling till ett lärosäte"},
    "fi": {"student": "korkeakouluopiskelija", "researcher": "yliopiston tutkija", "staff": "yliopiston henkilökuntaa", "none": "ei yliopistokytköstä"},
    "no": {"student": "student ved et universitet eller en høyskole", "researcher": "forsker ved et universitet", "staff": "ansatt ved et universitet", "none": "ingen tilknytning til et universitet"},
    "da": {"student": "studerende ved et universitet", "researcher": "forsker ved et universitet", "staff": "ansat ved et universitet", "none": "ingen tilknytning til et universitet"},
}

PERSONAL_DATA_NAMES: dict[str, dict[str, str]] = {
    "en": {"none": "no data about people", "anonymous": "anonymous, nobody can re-identify", "pseudonymised": "pseudonymised, the source can re-identify", "identifiable": "identifiable personal data"},
    "sv": {"none": "inga personuppgifter", "anonymous": "anonyma, ingen kan återidentifiera", "pseudonymised": "pseudonymiserade, källan kan återidentifiera", "identifiable": "identifierbara personuppgifter"},
    "fi": {"none": "ei henkilötietoja", "anonymous": "anonyymit, kukaan ei voi tunnistaa", "pseudonymised": "pseudonymisoidut, lähde voi tunnistaa", "identifiable": "tunnistettavia henkilötietoja"},
    "no": {"none": "ingen personopplysninger", "anonymous": "anonyme, ingen kan reidentifisere", "pseudonymised": "pseudonymiserte, kilden kan reidentifisere", "identifiable": "identifiserbare personopplysninger"},
    "da": {"none": "ingen personoplysninger", "anonymous": "anonyme, ingen kan genidentificere", "pseudonymised": "pseudonymiserede, kilden kan genidentificere", "identifiable": "identificerbare personoplysninger"},
}

# One question per situation topic for the first answer, and why it matters, in at most twelve words.
SCREEN_QUESTIONS: dict[str, dict[str, str]] = {
    "en": {
        "grants": "Which public grants or loans has the company had, and are any still running?",
        "work": "Will you work full-time in the company, or keep a job elsewhere?",
        "timing": "Has the project already started, and is the product already sold?",
    },
    "sv": {
        "grants": "Vilka offentliga bidrag eller lån har bolaget haft, och pågår något fortfarande?",
        "work": "Kommer du att jobba heltid i bolaget, eller ha kvar ett jobb vid sidan av?",
        "timing": "Har projektet redan börjat, och säljs produkten redan?",
    },
    "fi": {
        "grants": "Mitä julkisia avustuksia tai lainoja yrityksellä on ollut, ja onko jokin vielä käynnissä?",
        "work": "Teetkö yritystä kokoaikaisesti, vai jatkatko työssä muualla?",
        "timing": "Onko hanke jo alkanut, ja myydäänkö tuotetta jo?",
    },
    "no": {
        "grants": "Hvilke offentlige tilskudd eller lån har selskapet hatt, og løper noen fortsatt?",
        "work": "Skal du jobbe heltid i selskapet, eller beholde en jobb ved siden av?",
        "timing": "Har prosjektet allerede startet, og selges produktet allerede?",
    },
    "da": {
        "grants": "Hvilke offentlige tilskud eller lån har virksomheden haft, og løber nogen stadig?",
        "work": "Skal du arbejde fuld tid i virksomheden, eller beholde et job ved siden af?",
        "timing": "Er projektet allerede i gang, og sælges produktet allerede?",
    },
}
# Topics with one field reuse that field's question.
SCREEN_FIELD: dict[str, str] = {
    "ownership": "owner_company_share", "affiliation": "affiliation", "data": "personal_data",
    "finances": "lost_half_capital", "staff": "paid_staff",
}

SCREEN_WHY: dict[str, dict[str, str]] = {
    "en": {
        "basics": "Most of these programs depend on it.",
        "ownership": "25% or more owned by another company can end SME status.",
        "grants": "Some funders allow one grant at a time, or one per company.",
        "work": "Start-up allowances and founder grants often require full-time work.",
        "affiliation": "Universities run free startup support, and their IP rules may apply.",
        "data": "Data the source can re-link is personal data under GDPR.",
        "finances": "Over three years old with half the capital lost: most state aid closes.",
        "timing": "Many grants pay only for work after you apply, some only before launch.",
        "staff": "Some reliefs and grants count only people on your own payroll.",
    },
    "sv": {
        "basics": "De flesta av programmen hänger på det.",
        "ownership": "Äger ett annat bolag 25 % eller mer kan SME-statusen falla.",
        "grants": "Vissa finansiärer tillåter ett bidrag åt gången, eller ett per bolag.",
        "work": "Starta eget-stöd och grundarbidrag kräver ofta att du jobbar heltid.",
        "affiliation": "Lärosäten har gratis startup-stöd, och deras regler om rättigheter kan gälla.",
        "data": "Data som källan kan koppla tillbaka är personuppgifter enligt GDPR.",
        "finances": "Äldre än tre år och halva kapitalet förbrukat: de flesta statliga stöd stängs.",
        "timing": "Många bidrag betalar bara arbete efter ansökan, vissa bara före lansering.",
        "staff": "Vissa avdrag och bidrag räknar bara personer på er egen lönelista.",
    },
    "fi": {
        "basics": "Useimmat näistä ohjelmista riippuvat tästä.",
        "ownership": "Jos toinen yritys omistaa vähintään 25 %, pk-yritysasema voi kaatua.",
        "grants": "Osa rahoittajista sallii vain yhden avustuksen kerrallaan tai yritystä kohden.",
        "work": "Starttiraha ja perustajarahoitus edellyttävät usein päätoimisuutta.",
        "affiliation": "Korkeakouluilla on maksutonta startup-tukea, ja niiden IPR-säännöt voivat koskea teitä.",
        "data": "Lähteen yhdistettävissä oleva aineisto on GDPR:n mukaan henkilötietoa.",
        "finances": "Yli kolme vuotta vanha ja puolet pääomasta menetetty: useimmat valtiontuet sulkeutuvat.",
        "timing": "Moni avustus kattaa vain hakemuksen jälkeisen työn, osa vain ennen markkinoille tuloa.",
        "staff": "Osa vähennyksistä ja avustuksista koskee vain omalla palkkalistalla olevia.",
    },
    "no": {
        "basics": "De fleste av disse programmene avhenger av dette.",
        "ownership": "Eier et annet selskap 25 % eller mer, kan SMB-statusen falle.",
        "grants": "Noen finansiører tillater ett tilskudd om gangen, eller ett per selskap.",
        "work": "Oppstartsstøtte og gründerstipend krever ofte at du jobber heltid.",
        "affiliation": "Universiteter har gratis gründerstøtte, og reglene deres om rettigheter kan gjelde.",
        "data": "Data kilden kan koble tilbake, er personopplysninger etter GDPR.",
        "finances": "Over tre år gammelt og halve kapitalen tapt: det meste av statsstøtte stenger.",
        "timing": "Mange tilskudd dekker bare arbeid etter søknaden, noen bare før lansering.",
        "staff": "Noen fradrag og tilskudd teller bare folk på egen lønningsliste.",
    },
    "da": {
        "basics": "De fleste af disse programmer afhænger af det.",
        "ownership": "Ejer en anden virksomhed 25 % eller mere, kan SMV-status falde bort.",
        "grants": "Nogle bevillingsgivere tillader ét tilskud ad gangen, eller ét per virksomhed.",
        "work": "Iværksætterstøtte og stipendier kræver ofte, at du arbejder fuld tid.",
        "affiliation": "Universiteter har gratis iværksætterstøtte, og deres regler om rettigheder kan gælde.",
        "data": "Data, som kilden kan koble tilbage, er personoplysninger efter GDPR.",
        "finances": "Over tre år gammelt og halvdelen af kapitalen tabt: de fleste former for statsstøtte lukker.",
        "timing": "Mange tilskud dækker kun arbejde efter ansøgningen, nogle kun før lancering.",
        "staff": "Nogle fradrag og tilskud tæller kun folk på jeres egen lønliste.",
    },
}

ROUTE_NAMES: dict[str, dict[str, str]] = {
    "en": {"grant": "Grants", "tax": "Tax relief", "loan": "Loans", "compute": "Compute", "credits": "Cloud and AI credits", "equity": "Equity investment", "support": "Support programs"},
    "sv": {"grant": "Bidrag", "tax": "Skattelättnad", "loan": "Lån", "compute": "Beräkningskraft", "credits": "Moln- och AI-krediter", "equity": "Ägarkapital", "support": "Stödprogram"},
    "fi": {"grant": "Avustukset", "tax": "Verohelpotus", "loan": "Lainat", "compute": "Laskentateho", "credits": "Pilvi- ja tekoälykrediitit", "equity": "Pääomasijoitus", "support": "Tukiohjelmat"},
    "no": {"grant": "Tilskudd", "tax": "Skattefradrag", "loan": "Lån", "compute": "Regnekraft", "credits": "Sky- og KI-kreditter", "equity": "Egenkapital", "support": "Støtteprogrammer"},
    "da": {"grant": "Tilskud", "tax": "Skattefradrag", "loan": "Lån", "compute": "Regnekraft", "credits": "Cloud- og AI-kreditter", "equity": "Egenkapital", "support": "Støtteprogrammer"},
}

# Label templates keyed by language, then field, then op. {n} is a number,
# {country} a country name, {form} a legal form, {list} a joined list,
# {vendor} a vendor, {sector} a sector, {stage} a stage, {money} an amount.
LABELS: dict[str, dict[str, dict[str, str]]] = {
    "en": {
        "country": {"eq": "in {country}", "neq": "not in {country}", "in": "in {list}", "not_in": "not in {list}"},
        "residence_country": {"eq": "founders based in {country}", "neq": "founders not based in {country}", "in": "founders based in {list}", "not_in": "founders not based in {list}"},
        "legal_form": {"eq": "{form}", "neq": "not {form}", "in": "{list}", "not_in": "not {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "under {n} years old", "lte": "at most {n} years old", "gt": "over {n} years old", "gte": "at least {n} years old", "eq": "{n} years old"},
        "employees": {"lt": "fewer than {n} employees", "lte": "at most {n} employees", "gt": "more than {n} employees", "gte": "at least {n} employees", "eq": "{n} employees"},
        "revenue_msek": {"lt": "revenue under {n} MSEK", "lte": "revenue at most {n} MSEK", "gt": "revenue over {n} MSEK", "gte": "revenue at least {n} MSEK"},
        "balance_msek": {"lt": "balance sheet under {n} MSEK", "lte": "balance sheet at most {n} MSEK", "gt": "balance sheet over {n} MSEK", "gte": "balance sheet at least {n} MSEK"},
        "revenue_meur": {"lt": "turnover under {n} MEUR", "lte": "turnover at most {n} MEUR", "gt": "turnover over {n} MEUR", "gte": "turnover at least {n} MEUR"},
        "balance_meur": {"lt": "balance sheet under {n} MEUR", "lte": "balance sheet at most {n} MEUR", "gt": "balance sheet over {n} MEUR", "gte": "balance sheet at least {n} MEUR"},
        "funding_raised_usd": {"lt": "raised under {money}", "lte": "raised at most {money}", "gt": "raised over {money}", "gte": "raised at least {money}"},
        "stage": {"eq": "stage: {stage}", "in": "stage: {list}", "neq": "stage other than {stage}", "not_in": "stage other than {list}"},
        "vc_backed": {"true": "backed by an investor", "false": "no institutional investor"},
        "stack": {"contains": "uses {vendor}"},
        "sector": {"contains": "works in {sector}"},
        "has_vat": {"true": "VAT number", "false": "no VAT number"},
        "has_employment": {"true": "project lead employed past the allocation", "false": "no employed project lead"},
        "has_work_email": {"true": "email on your own domain", "false": "no email on your own domain"},
        "has_website": {"true": "a public website", "false": "no public website"},
        "has_developer": {"true": "a developer on the team", "false": "no developer on the team"},
        "workload_defined": {"true": "workload defined: code, one system, GPU hours", "false": "workload not defined"},
        "profit_distributed": {"true": "dividend paid last year", "false": "no dividend last year"},
        "owner_company_share": {"lte": "another company owns at most {n}%", "lt": "another company owns under {n}%", "gt": "another company owns over {n}%", "gte": "another company owns at least {n}%"},
        "paid_staff": {"lt": "fewer than {n} paid staff", "lte": "at most {n} paid staff", "gt": "more than {n} paid staff", "gte": "at least {n} paid staff", "eq": "{n} paid staff"},
        "de_minimis_eur": {"lt": "de minimis aid in 3 years under {n} EUR", "lte": "de minimis aid in 3 years at most {n} EUR"},
        "fulltime_in_company": {"true": "founder works full-time in the company", "false": "founder not full-time in the company"},
        "founder_employed_elsewhere": {"true": "founder has a full-time job elsewhere", "false": "no full-time job outside the company"},
        "lost_half_capital": {"true": "more than half the share capital lost", "false": "not lost more than half the share capital"},
        "work_started": {"true": "project work already started", "false": "project not started before applying"},
        "on_market": {"true": "product already on the market", "false": "product not yet on the market"},
        "prior_grants": {"excludes": "no earlier {list}", "contains": "earlier {list}"},
        "active_grants": {"excludes": "no running {list}", "contains": "a running {list}"},
        "affiliation": {"eq": "{list}", "in": "{list}", "neq": "not {list}", "not_in": "not {list}"},
        "personal_data": {"eq": "data: {list}", "in": "data: {list}", "neq": "data not {list}", "not_in": "data not {list}"},
    },
    "sv": {
        "country": {"eq": "i {country}", "neq": "inte i {country}", "in": "i {list}", "not_in": "inte i {list}"},
        "residence_country": {"eq": "grundarna bor i {country}", "neq": "grundarna bor inte i {country}", "in": "grundarna bor i {list}", "not_in": "grundarna bor inte i {list}"},
        "legal_form": {"eq": "{form}", "neq": "inte {form}", "in": "{list}", "not_in": "inte {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "yngre än {n} år", "lte": "högst {n} år", "gt": "äldre än {n} år", "gte": "minst {n} år", "eq": "{n} år"},
        "employees": {"lt": "färre än {n} anställda", "lte": "högst {n} anställda", "gt": "fler än {n} anställda", "gte": "minst {n} anställda", "eq": "{n} anställda"},
        "revenue_msek": {"lt": "omsättning under {n} MSEK", "lte": "omsättning högst {n} MSEK", "gt": "omsättning över {n} MSEK", "gte": "omsättning minst {n} MSEK"},
        "balance_msek": {"lt": "balansomslutning under {n} MSEK", "lte": "balansomslutning högst {n} MSEK", "gt": "balansomslutning över {n} MSEK", "gte": "balansomslutning minst {n} MSEK"},
        "revenue_meur": {"lt": "omsättning under {n} MEUR", "lte": "omsättning högst {n} MEUR", "gt": "omsättning över {n} MEUR", "gte": "omsättning minst {n} MEUR"},
        "balance_meur": {"lt": "balansomslutning under {n} MEUR", "lte": "balansomslutning högst {n} MEUR", "gt": "balansomslutning över {n} MEUR", "gte": "balansomslutning minst {n} MEUR"},
        "funding_raised_usd": {"lt": "tagit in under {money}", "lte": "tagit in högst {money}", "gt": "tagit in över {money}", "gte": "tagit in minst {money}"},
        "stage": {"eq": "fas: {stage}", "in": "fas: {list}", "neq": "annan fas än {stage}", "not_in": "annan fas än {list}"},
        "vc_backed": {"true": "har en investerare", "false": "ingen institutionell investerare"},
        "stack": {"contains": "använder {vendor}"},
        "sector": {"contains": "verksam inom {sector}"},
        "has_vat": {"true": "momsregistrerat", "false": "inte momsregistrerat"},
        "has_employment": {"true": "anställd projektledare efter allokeringen", "false": "ingen anställd projektledare"},
        "has_work_email": {"true": "e-post på egen domän", "false": "ingen e-post på egen domän"},
        "has_website": {"true": "en publik webbplats", "false": "ingen publik webbplats"},
        "has_developer": {"true": "en utvecklare i teamet", "false": "ingen utvecklare i teamet"},
        "workload_defined": {"true": "arbetslast definierad: kod, ett system, GPU-timmar", "false": "arbetslast inte definierad"},
        "profit_distributed": {"true": "vinstutdelning förra året", "false": "ingen vinstutdelning förra året"},
        "owner_company_share": {"lte": "annat bolag äger högst {n} %", "lt": "annat bolag äger under {n} %", "gt": "annat bolag äger över {n} %", "gte": "annat bolag äger minst {n} %"},
        "paid_staff": {"lt": "färre än {n} avlönade", "lte": "högst {n} avlönade", "gt": "fler än {n} avlönade", "gte": "minst {n} avlönade", "eq": "{n} avlönade"},
        "de_minimis_eur": {"lt": "stöd av mindre betydelse på 3 år under {n} EUR", "lte": "stöd av mindre betydelse på 3 år högst {n} EUR"},
        "fulltime_in_company": {"true": "grundaren jobbar heltid i bolaget", "false": "grundaren jobbar inte heltid i bolaget"},
        "founder_employed_elsewhere": {"true": "grundaren har heltidsjobb på annat håll", "false": "inget heltidsjobb utanför bolaget"},
        "lost_half_capital": {"true": "mer än halva aktiekapitalet förbrukat", "false": "inte mer än halva aktiekapitalet förbrukat"},
        "work_started": {"true": "projektarbetet har redan börjat", "false": "projektet inte påbörjat före ansökan"},
        "on_market": {"true": "produkten redan på marknaden", "false": "produkten inte på marknaden än"},
        "prior_grants": {"excludes": "inget tidigare {list}", "contains": "tidigare {list}"},
        "active_grants": {"excludes": "inget pågående {list}", "contains": "ett pågående {list}"},
        "affiliation": {"eq": "{list}", "in": "{list}", "neq": "inte {list}", "not_in": "inte {list}"},
        "personal_data": {"eq": "data: {list}", "in": "data: {list}", "neq": "data inte {list}", "not_in": "data inte {list}"},
    },
    "fi": {
        "country": {"eq": "{country_in}", "neq": "ei {country_in}", "in": "maa: {list}", "not_in": "ei maa: {list}"},
        "residence_country": {"eq": "perustajat asuvat {country_in}", "neq": "perustajat eivät asu {country_in}", "in": "perustajat asuvat: {list}", "not_in": "perustajat eivät asu: {list}"},
        "legal_form": {"eq": "{form}", "neq": "ei {form}", "in": "{list}", "not_in": "ei {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "alle {n} vuotta vanha", "lte": "enintään {n} vuotta vanha", "gt": "yli {n} vuotta vanha", "gte": "vähintään {n} vuotta vanha", "eq": "{n} vuotta vanha"},
        "employees": {"lt": "alle {n} työntekijää", "lte": "enintään {n} työntekijää", "gt": "yli {n} työntekijää", "gte": "vähintään {n} työntekijää", "eq": "{n} työntekijää"},
        "revenue_msek": {"lt": "liikevaihto alle {n} MSEK", "lte": "liikevaihto enintään {n} MSEK", "gt": "liikevaihto yli {n} MSEK", "gte": "liikevaihto vähintään {n} MSEK"},
        "balance_msek": {"lt": "taseen loppusumma alle {n} MSEK", "lte": "taseen loppusumma enintään {n} MSEK", "gt": "taseen loppusumma yli {n} MSEK", "gte": "taseen loppusumma vähintään {n} MSEK"},
        "revenue_meur": {"lt": "liikevaihto alle {n} MEUR", "lte": "liikevaihto enintään {n} MEUR", "gt": "liikevaihto yli {n} MEUR", "gte": "liikevaihto vähintään {n} MEUR"},
        "balance_meur": {"lt": "taseen loppusumma alle {n} MEUR", "lte": "taseen loppusumma enintään {n} MEUR", "gt": "taseen loppusumma yli {n} MEUR", "gte": "taseen loppusumma vähintään {n} MEUR"},
        "funding_raised_usd": {"lt": "kerätty rahoitus alle {money}", "lte": "kerätty rahoitus enintään {money}", "gt": "kerätty rahoitus yli {money}", "gte": "kerätty rahoitus vähintään {money}"},
        "stage": {"eq": "vaihe: {stage}", "in": "vaihe: {list}", "neq": "muu vaihe kuin {stage}", "not_in": "muu vaihe kuin {list}"},
        "vc_backed": {"true": "sijoittaja mukana", "false": "ei institutionaalista sijoittajaa"},
        "stack": {"contains": "käyttää palvelua {vendor}"},
        "sector": {"contains": "toimiala: {sector}"},
        "has_vat": {"true": "ALV-rekisterissä", "false": "ei ALV-rekisterissä"},
        "has_employment": {"true": "työsuhteessa oleva projektipäällikkö allokaation jälkeen", "false": "ei työsuhteessa olevaa projektipäällikköä"},
        "has_work_email": {"true": "sähköposti omassa verkkotunnuksessa", "false": "ei sähköpostia omassa verkkotunnuksessa"},
        "has_website": {"true": "julkinen verkkosivusto", "false": "ei julkista verkkosivustoa"},
        "has_developer": {"true": "kehittäjä tiimissä", "false": "ei kehittäjää tiimissä"},
        "workload_defined": {"true": "työkuorma määritelty: koodi, yksi järjestelmä, GPU-tunnit", "false": "työkuormaa ei ole määritelty"},
        "profit_distributed": {"true": "osinkoa jaettu viime vuonna", "false": "ei osinkoa viime vuonna"},
        "owner_company_share": {"lte": "toinen yritys omistaa enintään {n} %", "lt": "toinen yritys omistaa alle {n} %", "gt": "toinen yritys omistaa yli {n} %", "gte": "toinen yritys omistaa vähintään {n} %"},
        "paid_staff": {"lt": "alle {n} palkattua", "lte": "enintään {n} palkattua", "gt": "yli {n} palkattua", "gte": "vähintään {n} palkattua", "eq": "{n} palkattua"},
        "de_minimis_eur": {"lt": "de minimis -tukea 3 vuodessa alle {n} EUR", "lte": "de minimis -tukea 3 vuodessa enintään {n} EUR"},
        "fulltime_in_company": {"true": "perustaja työskentelee yrityksessä kokoaikaisesti", "false": "perustaja ei työskentele yrityksessä kokoaikaisesti"},
        "founder_employed_elsewhere": {"true": "perustajalla kokoaikatyö muualla", "false": "ei kokoaikatyötä yrityksen ulkopuolella"},
        "lost_half_capital": {"true": "yli puolet osakepääomasta menetetty", "false": "ei menetetty yli puolta osakepääomasta"},
        "work_started": {"true": "hankkeen työ jo aloitettu", "false": "hanketta ei aloitettu ennen hakemusta"},
        "on_market": {"true": "tuote jo markkinoilla", "false": "tuote ei vielä markkinoilla"},
        "prior_grants": {"excludes": "ei aiempaa rahoitusta: {list}", "contains": "aiempi rahoitus: {list}"},
        "active_grants": {"excludes": "ei käynnissä olevaa rahoitusta: {list}", "contains": "käynnissä oleva rahoitus: {list}"},
        "affiliation": {"eq": "{list}", "in": "{list}", "neq": "ei {list}", "not_in": "ei {list}"},
        "personal_data": {"eq": "aineisto: {list}", "in": "aineisto: {list}", "neq": "aineisto ei {list}", "not_in": "aineisto ei {list}"},
    },
    "no": {
        "country": {"eq": "i {country}", "neq": "ikke i {country}", "in": "i {list}", "not_in": "ikke i {list}"},
        "residence_country": {"eq": "gründerne bor i {country}", "neq": "gründerne bor ikke i {country}", "in": "gründerne bor i {list}", "not_in": "gründerne bor ikke i {list}"},
        "legal_form": {"eq": "{form}", "neq": "ikke {form}", "in": "{list}", "not_in": "ikke {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "yngre enn {n} år", "lte": "høyst {n} år", "gt": "eldre enn {n} år", "gte": "minst {n} år", "eq": "{n} år"},
        "employees": {"lt": "færre enn {n} ansatte", "lte": "høyst {n} ansatte", "gt": "flere enn {n} ansatte", "gte": "minst {n} ansatte", "eq": "{n} ansatte"},
        "revenue_msek": {"lt": "omsetning under {n} MSEK", "lte": "omsetning høyst {n} MSEK", "gt": "omsetning over {n} MSEK", "gte": "omsetning minst {n} MSEK"},
        "balance_msek": {"lt": "balansesum under {n} MSEK", "lte": "balansesum høyst {n} MSEK", "gt": "balansesum over {n} MSEK", "gte": "balansesum minst {n} MSEK"},
        "revenue_meur": {"lt": "omsetning under {n} MEUR", "lte": "omsetning høyst {n} MEUR", "gt": "omsetning over {n} MEUR", "gte": "omsetning minst {n} MEUR"},
        "balance_meur": {"lt": "balansesum under {n} MEUR", "lte": "balansesum høyst {n} MEUR", "gt": "balansesum over {n} MEUR", "gte": "balansesum minst {n} MEUR"},
        "funding_raised_usd": {"lt": "hentet under {money}", "lte": "hentet høyst {money}", "gt": "hentet over {money}", "gte": "hentet minst {money}"},
        "stage": {"eq": "fase: {stage}", "in": "fase: {list}", "neq": "annen fase enn {stage}", "not_in": "annen fase enn {list}"},
        "vc_backed": {"true": "har en investor", "false": "ingen institusjonell investor"},
        "stack": {"contains": "bruker {vendor}"},
        "sector": {"contains": "jobber innen {sector}"},
        "has_vat": {"true": "MVA-registrert", "false": "ikke MVA-registrert"},
        "has_employment": {"true": "ansatt prosjektleder etter tildelingen", "false": "ingen ansatt prosjektleder"},
        "has_work_email": {"true": "e-post på eget domene", "false": "ingen e-post på eget domene"},
        "has_website": {"true": "et offentlig nettsted", "false": "ikke noe offentlig nettsted"},
        "has_developer": {"true": "en utvikler i teamet", "false": "ingen utvikler i teamet"},
        "workload_defined": {"true": "arbeidslast definert: kode, ett system, GPU-timer", "false": "arbeidslast ikke definert"},
        "profit_distributed": {"true": "utbytte utbetalt i fjor", "false": "ikke noe utbytte i fjor"},
        "owner_company_share": {"lte": "et annet selskap eier høyst {n} %", "lt": "et annet selskap eier under {n} %", "gt": "et annet selskap eier over {n} %", "gte": "et annet selskap eier minst {n} %"},
        "paid_staff": {"lt": "færre enn {n} lønnede", "lte": "høyst {n} lønnede", "gt": "flere enn {n} lønnede", "gte": "minst {n} lønnede", "eq": "{n} lønnede"},
        "de_minimis_eur": {"lt": "bagatellmessig støtte på 3 år under {n} EUR", "lte": "bagatellmessig støtte på 3 år høyst {n} EUR"},
        "fulltime_in_company": {"true": "gründeren jobber heltid i selskapet", "false": "gründeren jobber ikke heltid i selskapet"},
        "founder_employed_elsewhere": {"true": "gründeren har heltidsjobb et annet sted", "false": "ingen heltidsjobb utenfor selskapet"},
        "lost_half_capital": {"true": "mer enn halve aksjekapitalen tapt", "false": "ikke tapt mer enn halve aksjekapitalen"},
        "work_started": {"true": "prosjektarbeidet har allerede startet", "false": "prosjektet ikke startet før søknaden"},
        "on_market": {"true": "produktet allerede på markedet", "false": "produktet ikke på markedet ennå"},
        "prior_grants": {"excludes": "ikke tidligere {list}", "contains": "tidligere {list}"},
        "active_grants": {"excludes": "ikke løpende {list}", "contains": "et løpende {list}"},
        "affiliation": {"eq": "{list}", "in": "{list}", "neq": "ikke {list}", "not_in": "ikke {list}"},
        "personal_data": {"eq": "data: {list}", "in": "data: {list}", "neq": "data ikke {list}", "not_in": "data ikke {list}"},
    },
    "da": {
        "country": {"eq": "i {country}", "neq": "ikke i {country}", "in": "i {list}", "not_in": "ikke i {list}"},
        "residence_country": {"eq": "stifterne bor i {country}", "neq": "stifterne bor ikke i {country}", "in": "stifterne bor i {list}", "not_in": "stifterne bor ikke i {list}"},
        "legal_form": {"eq": "{form}", "neq": "ikke {form}", "in": "{list}", "not_in": "ikke {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "yngre end {n} år", "lte": "højst {n} år", "gt": "ældre end {n} år", "gte": "mindst {n} år", "eq": "{n} år"},
        "employees": {"lt": "færre end {n} ansatte", "lte": "højst {n} ansatte", "gt": "flere end {n} ansatte", "gte": "mindst {n} ansatte", "eq": "{n} ansatte"},
        "revenue_msek": {"lt": "omsætning under {n} MSEK", "lte": "omsætning højst {n} MSEK", "gt": "omsætning over {n} MSEK", "gte": "omsætning mindst {n} MSEK"},
        "balance_msek": {"lt": "balancesum under {n} MSEK", "lte": "balancesum højst {n} MSEK", "gt": "balancesum over {n} MSEK", "gte": "balancesum mindst {n} MSEK"},
        "revenue_meur": {"lt": "omsætning under {n} MEUR", "lte": "omsætning højst {n} MEUR", "gt": "omsætning over {n} MEUR", "gte": "omsætning mindst {n} MEUR"},
        "balance_meur": {"lt": "balancesum under {n} MEUR", "lte": "balancesum højst {n} MEUR", "gt": "balancesum over {n} MEUR", "gte": "balancesum mindst {n} MEUR"},
        "funding_raised_usd": {"lt": "rejst under {money}", "lte": "rejst højst {money}", "gt": "rejst over {money}", "gte": "rejst mindst {money}"},
        "stage": {"eq": "fase: {stage}", "in": "fase: {list}", "neq": "anden fase end {stage}", "not_in": "anden fase end {list}"},
        "vc_backed": {"true": "har en investor", "false": "ingen institutionel investor"},
        "stack": {"contains": "bruger {vendor}"},
        "sector": {"contains": "arbejder inden for {sector}"},
        "has_vat": {"true": "momsregistreret", "false": "ikke momsregistreret"},
        "has_employment": {"true": "ansat projektleder efter tildelingen", "false": "ingen ansat projektleder"},
        "has_work_email": {"true": "e-mail på eget domæne", "false": "ingen e-mail på eget domæne"},
        "has_website": {"true": "et offentligt websted", "false": "intet offentligt websted"},
        "has_developer": {"true": "en udvikler på holdet", "false": "ingen udvikler på holdet"},
        "workload_defined": {"true": "arbejdsbyrde defineret: kode, ét system, GPU-timer", "false": "arbejdsbyrde ikke defineret"},
        "profit_distributed": {"true": "udbytte udbetalt sidste år", "false": "intet udbytte sidste år"},
        "owner_company_share": {"lte": "en anden virksomhed ejer højst {n} %", "lt": "en anden virksomhed ejer under {n} %", "gt": "en anden virksomhed ejer over {n} %", "gte": "en anden virksomhed ejer mindst {n} %"},
        "paid_staff": {"lt": "færre end {n} lønnede", "lte": "højst {n} lønnede", "gt": "flere end {n} lønnede", "gte": "mindst {n} lønnede", "eq": "{n} lønnede"},
        "de_minimis_eur": {"lt": "de minimis-støtte på 3 år under {n} EUR", "lte": "de minimis-støtte på 3 år højst {n} EUR"},
        "fulltime_in_company": {"true": "stifteren arbejder fuld tid i virksomheden", "false": "stifteren arbejder ikke fuld tid i virksomheden"},
        "founder_employed_elsewhere": {"true": "stifteren har fuldtidsjob et andet sted", "false": "intet fuldtidsjob uden for virksomheden"},
        "lost_half_capital": {"true": "mere end halvdelen af selskabskapitalen tabt", "false": "ikke tabt mere end halvdelen af selskabskapitalen"},
        "work_started": {"true": "projektarbejdet er allerede i gang", "false": "projektet ikke startet før ansøgningen"},
        "on_market": {"true": "produktet allerede på markedet", "false": "produktet ikke på markedet endnu"},
        "prior_grants": {"excludes": "ikke tidligere {list}", "contains": "tidligere {list}"},
        "active_grants": {"excludes": "ikke igangværende {list}", "contains": "et igangværende {list}"},
        "affiliation": {"eq": "{list}", "in": "{list}", "neq": "ikke {list}", "not_in": "ikke {list}"},
        "personal_data": {"eq": "data: {list}", "in": "data: {list}", "neq": "data ikke {list}", "not_in": "data ikke {list}"},
    },
}

# One question per field, the thing the founder is asked when the field is unknown.
# {vendor} and {sector} are filled for contains rules.
QUESTIONS: dict[str, dict[str, str]] = {
    "en": {
        "country": "In which country is the company registered, or where will it be?",
        "residence_country": "In which country are the founders based?",
        "confirmed": "{confirmation_question}",
        "legal_form": "What is the legal form: a company, sole trader, non-profit, university, public sector, or no company yet?",
        "age_years": "How old is the company, in years?",
        "employees": "How many employees?",
        "revenue_msek": "Net revenue last fiscal year, in MSEK?",
        "balance_msek": "Balance sheet total, in MSEK?",
        "revenue_meur": "Turnover last fiscal year, in MEUR?",
        "balance_meur": "Balance sheet total, in MEUR?",
        "funding_raised_usd": "How much funding has the company raised, in USD?",
        "stage": "What stage: idea, pre-seed, seed, series A, or later?",
        "vc_backed": "Is there an institutional investor on the cap table?",
        "stack": "Do you use {vendor}?",
        "sector": "Does the company work in {sector}?",
        "has_vat": "Does the company have a VAT number?",
        "has_employment": "Is the project lead employed until at least three months after the allocation ends?",
        "has_work_email": "Is there a contact email on your own domain?",
        "has_website": "Does the company have a public website?",
        "has_developer": "Does the team include at least one developer?",
        "workload_defined": "Can you name the code, the single system and the number of GPU hours?",
        "profit_distributed": "Did the company pay a dividend last fiscal year?",
        "owner_company_share": "Apart from venture funds, angels or universities holding 50% or less, does another company, group or public body own 25% or more of yours, and how much?",
        "paid_staff": "How many people does the company pay a salary to?",
        "de_minimis_eur": "How much de minimis aid has the company received in the last three years, in EUR?",
        "fulltime_in_company": "Will you work full-time in the company once the funded work starts?",
        "founder_employed_elsewhere": "Will you keep a full-time job outside the company while you build it?",
        "lost_half_capital": "Has the company lost more than half of its share capital through accumulated losses?",
        "work_started": "Has the project you would apply for, not the company's earlier work, already started?",
        "on_market": "Is the product already sold to customers?",
        "prior_grants": "Which public grants or loans has the company received before, if any?",
        "active_grants": "Is any public grant or project still running for the company, and from which funder?",
        "affiliation": "Are you a student, researcher or employee at a university right now?",
        "personal_data": "Can anyone, the data source included, link a record in your data back to a person?",
    },
    "sv": {
        "country": "I vilket land är bolaget registrerat, eller var ska det registreras?",
        "residence_country": "I vilket land bor grundarna?",
        "confirmed": "{confirmation_question}",
        "legal_form": "Vilken bolagsform: aktiebolag eller annat bolag, enskild firma, ideell förening, universitet, offentlig sektor, eller inget bolag än?",
        "age_years": "Hur gammalt är bolaget, i år?",
        "employees": "Hur många anställda?",
        "revenue_msek": "Nettoomsättning senaste räkenskapsåret, i MSEK?",
        "balance_msek": "Balansomslutning, i MSEK?",
        "revenue_meur": "Omsättning senaste räkenskapsåret, i MEUR?",
        "balance_meur": "Balansomslutning, i MEUR?",
        "funding_raised_usd": "Hur mycket kapital har bolaget tagit in, i USD?",
        "stage": "Vilken fas: idé, pre-seed, seed, serie A, eller senare?",
        "vc_backed": "Finns en institutionell investerare bland ägarna?",
        "stack": "Använder ni {vendor}?",
        "sector": "Är bolaget verksamt inom {sector}?",
        "has_vat": "Är bolaget momsregistrerat?",
        "has_employment": "Är projektledaren anställd minst tre månader efter att allokeringen tar slut?",
        "has_work_email": "Finns en kontaktadress på er egen domän?",
        "has_website": "Har bolaget en publik webbplats?",
        "has_developer": "Finns minst en utvecklare i teamet?",
        "workload_defined": "Kan ni namnge koden, det enda systemet och antalet GPU-timmar?",
        "profit_distributed": "Gjorde bolaget vinstutdelning senaste räkenskapsåret?",
        "owner_company_share": "Bortsett från riskkapitalfonder, affärsänglar eller lärosäten med högst 50 %, äger något annat bolag, en koncern eller en offentlig aktör 25 % eller mer av ert, och hur mycket?",
        "paid_staff": "Hur många personer betalar bolaget lön till?",
        "de_minimis_eur": "Hur mycket stöd av mindre betydelse (de minimis) har bolaget fått de senaste tre åren, i euro?",
        "fulltime_in_company": "Kommer du att jobba heltid i bolaget när det finansierade arbetet startar?",
        "founder_employed_elsewhere": "Kommer du att ha kvar ett heltidsjobb utanför bolaget medan du bygger det?",
        "lost_half_capital": "Har bolaget förbrukat mer än hälften av aktiekapitalet genom ackumulerade förluster?",
        "work_started": "Har projektet ni skulle söka för redan börjat, alltså inte bolagets tidigare arbete?",
        "on_market": "Säljs produkten redan till kunder?",
        "prior_grants": "Vilka offentliga bidrag eller lån har bolaget fått tidigare, om några?",
        "active_grants": "Har bolaget något offentligt bidrag eller projekt som fortfarande pågår, och från vilken finansiär?",
        "affiliation": "Är du student, forskare eller anställd vid ett universitet eller en högskola just nu?",
        "personal_data": "Kan någon, källan inräknad, koppla en post i era data till en person?",
    },
    "fi": {
        "country": "Missä maassa yhtiö on rekisteröity, tai mihin se rekisteröidään?",
        "residence_country": "Missä maassa perustajat asuvat?",
        "confirmed": "{confirmation_question}",
        "legal_form": "Mikä on yhtiömuoto: osakeyhtiö tai muu yhtiö, toiminimi, yhdistys, yliopisto, julkinen sektori, vai ei vielä yhtiötä?",
        "age_years": "Kuinka vanha yhtiö on, vuosina?",
        "employees": "Kuinka monta työntekijää?",
        "revenue_msek": "Liikevaihto viime tilikaudella, MSEK?",
        "balance_msek": "Taseen loppusumma, MSEK?",
        "revenue_meur": "Liikevaihto viime tilikaudella, MEUR?",
        "balance_meur": "Taseen loppusumma, MEUR?",
        "funding_raised_usd": "Kuinka paljon rahoitusta yhtiö on kerännyt, USD?",
        "stage": "Mikä vaihe: idea, pre-seed, seed, A-kierros, vai myöhempi?",
        "vc_backed": "Onko omistajissa institutionaalinen sijoittaja?",
        "stack": "Käytättekö palvelua {vendor}?",
        "sector": "Toimiiko yhtiö alalla {sector}?",
        "has_vat": "Onko yhtiö ALV-rekisterissä?",
        "has_employment": "Onko projektipäällikkö työsuhteessa vähintään kolme kuukautta allokaation päättymisen jälkeen?",
        "has_work_email": "Onko yhteyssähköposti omassa verkkotunnuksessanne?",
        "has_website": "Onko yhtiöllä julkinen verkkosivusto?",
        "has_developer": "Onko tiimissä vähintään yksi kehittäjä?",
        "workload_defined": "Osaatteko nimetä koodin, yhden järjestelmän ja GPU-tuntien määrän?",
        "profit_distributed": "Jakoiko yhtiö osinkoa viime tilikaudella?",
        "owner_company_share": "Pääomarahastoja, enkelisijoittajia ja yliopistoja (enintään 50 %) lukuun ottamatta, omistaako toinen yritys, konserni tai julkinen toimija vähintään 25 % yrityksestänne, ja kuinka paljon?",
        "paid_staff": "Kuinka monelle henkilölle yritys maksaa palkkaa?",
        "de_minimis_eur": "Kuinka paljon de minimis -tukea yritys on saanut viimeisen kolmen vuoden aikana, euroina?",
        "fulltime_in_company": "Työskenteletkö yrityksessä kokoaikaisesti, kun rahoitettu työ alkaa?",
        "founder_employed_elsewhere": "Jatkatko kokoaikatyössä yrityksen ulkopuolella, kun rakennat yritystä?",
        "lost_half_capital": "Onko yhtiö menettänyt kertyneillä tappioilla yli puolet osakepääomastaan?",
        "work_started": "Onko hanke, jolle haette rahoitusta, jo alkanut, yrityksen aiempaa työtä lukuun ottamatta?",
        "on_market": "Myydäänkö tuotetta jo asiakkaille?",
        "prior_grants": "Mitä julkisia avustuksia tai lainoja yritys on saanut aiemmin, jos mitään?",
        "active_grants": "Onko yrityksellä vielä käynnissä julkista avustusta tai hanketta, ja miltä rahoittajalta?",
        "affiliation": "Oletko tällä hetkellä opiskelija, tutkija tai työntekijä yliopistossa tai korkeakoulussa?",
        "personal_data": "Voiko kukaan, tietolähde mukaan lukien, yhdistää aineistonne tietueen henkilöön?",
    },
    "no": {
        "country": "I hvilket land er selskapet registrert, eller hvor skal det registreres?",
        "residence_country": "I hvilket land bor gründerne?",
        "confirmed": "{confirmation_question}",
        "legal_form": "Hvilken selskapsform: aksjeselskap eller annet selskap, enkeltpersonforetak, ideell organisasjon, universitet, offentlig sektor, eller ikke noe selskap ennå?",
        "age_years": "Hvor gammelt er selskapet, i år?",
        "employees": "Hvor mange ansatte?",
        "revenue_msek": "Omsetning siste regnskapsår, i MSEK?",
        "balance_msek": "Balansesum, i MSEK?",
        "revenue_meur": "Omsetning siste regnskapsår, i MEUR?",
        "balance_meur": "Balansesum, i MEUR?",
        "funding_raised_usd": "Hvor mye kapital har selskapet hentet, i USD?",
        "stage": "Hvilken fase: idé, pre-seed, seed, serie A, eller senere?",
        "vc_backed": "Er det en institusjonell investor på eiersiden?",
        "stack": "Bruker dere {vendor}?",
        "sector": "Jobber selskapet innen {sector}?",
        "has_vat": "Er selskapet MVA-registrert?",
        "has_employment": "Er prosjektlederen ansatt i minst tre måneder etter at tildelingen tar slutt?",
        "has_work_email": "Finnes det en kontaktadresse på deres eget domene?",
        "has_website": "Har selskapet et offentlig nettsted?",
        "has_developer": "Er det minst én utvikler i teamet?",
        "workload_defined": "Kan dere navngi koden, det ene systemet og antall GPU-timer?",
        "profit_distributed": "Betalte selskapet utbytte siste regnskapsår?",
        "owner_company_share": "Bortsett fra venturefond, engleinvestorer eller universiteter med høyst 50 %, eier et annet selskap, et konsern eller en offentlig aktør 25 % eller mer av deres, og hvor mye?",
        "paid_staff": "Hvor mange personer betaler selskapet lønn til?",
        "de_minimis_eur": "Hvor mye bagatellmessig støtte (de minimis) har selskapet fått de siste tre årene, i euro?",
        "fulltime_in_company": "Skal du jobbe heltid i selskapet når det finansierte arbeidet starter?",
        "founder_employed_elsewhere": "Skal du beholde en heltidsjobb utenfor selskapet mens du bygger det?",
        "lost_half_capital": "Har selskapet tapt mer enn halvparten av aksjekapitalen gjennom akkumulerte tap?",
        "work_started": "Har prosjektet dere vil søke for allerede startet, altså ikke selskapets tidligere arbeid?",
        "on_market": "Selges produktet allerede til kunder?",
        "prior_grants": "Hvilke offentlige tilskudd eller lån har selskapet fått tidligere, om noen?",
        "active_grants": "Har selskapet et offentlig tilskudd eller prosjekt som fortsatt løper, og fra hvilken finansiør?",
        "affiliation": "Er du student, forsker eller ansatt ved et universitet eller en høyskole nå?",
        "personal_data": "Kan noen, kilden medregnet, koble en post i dataene deres til en person?",
    },
    "da": {
        "country": "I hvilket land er selskabet registreret, eller hvor skal det registreres?",
        "residence_country": "I hvilket land bor stifterne?",
        "confirmed": "{confirmation_question}",
        "legal_form": "Hvilken selskabsform: ApS, A/S eller andet selskab, enkeltmandsvirksomhed, nonprofit, universitet, offentlig sektor, eller intet selskab endnu?",
        "age_years": "Hvor gammelt er selskabet, i år?",
        "employees": "Hvor mange ansatte?",
        "revenue_msek": "Omsætning sidste regnskabsår, i MSEK?",
        "balance_msek": "Balancesum, i MSEK?",
        "revenue_meur": "Omsætning sidste regnskabsår, i MEUR?",
        "balance_meur": "Balancesum, i MEUR?",
        "funding_raised_usd": "Hvor meget kapital har selskabet rejst, i USD?",
        "stage": "Hvilken fase: idé, pre-seed, seed, serie A, eller senere?",
        "vc_backed": "Er der en institutionel investor i ejerkredsen?",
        "stack": "Bruger I {vendor}?",
        "sector": "Arbejder selskabet inden for {sector}?",
        "has_vat": "Er selskabet momsregistreret?",
        "has_employment": "Er projektlederen ansat i mindst tre måneder efter, at tildelingen slutter?",
        "has_work_email": "Er der en kontaktadresse på jeres eget domæne?",
        "has_website": "Har selskabet et offentligt websted?",
        "has_developer": "Er der mindst én udvikler på holdet?",
        "workload_defined": "Kan I navngive koden, det ene system og antallet af GPU-timer?",
        "profit_distributed": "Udbetalte selskabet udbytte sidste regnskabsår?",
        "owner_company_share": "Bortset fra venturefonde, business angels eller universiteter med højst 50 %, ejer en anden virksomhed, en koncern eller en offentlig aktør 25 % eller mere af jeres, og hvor meget?",
        "paid_staff": "Hvor mange personer betaler virksomheden løn til?",
        "de_minimis_eur": "Hvor meget de minimis-støtte har virksomheden modtaget de seneste tre år, i euro?",
        "fulltime_in_company": "Skal du arbejde fuld tid i virksomheden, når det finansierede arbejde starter?",
        "founder_employed_elsewhere": "Beholder du et fuldtidsjob uden for virksomheden, mens du bygger den?",
        "lost_half_capital": "Har selskabet tabt mere end halvdelen af selskabskapitalen gennem akkumulerede underskud?",
        "work_started": "Er projektet, I vil søge til, allerede gået i gang, altså ikke virksomhedens tidligere arbejde?",
        "on_market": "Sælges produktet allerede til kunder?",
        "prior_grants": "Hvilke offentlige tilskud eller lån har virksomheden fået før, hvis nogen?",
        "active_grants": "Har virksomheden et offentligt tilskud eller projekt, der stadig løber, og fra hvilken bevillingsgiver?",
        "affiliation": "Er du studerende, forsker eller ansat ved et universitet lige nu?",
        "personal_data": "Kan nogen, kilden medregnet, koble en post i jeres data til en person?",
    },
}

# Fixed phrases used in the glyph and the output. {date} and {list} are filled in.
PHRASES: dict[str, dict[str, str]] = {
    "en": {
        "or": " or ",
        "group_sep": ", or ",
        "round_closes": "Round closes {date}",
        "closed_when_verified": "Closed when verified {date}; read the status page for the next round",
        "stale": "Last verified {date}, read the status page before quoting",
        "also": "Also: {list}",
        "also_needs": "also needs:",
        "before_apply": "Before you apply: {list}",
        "unclear": "Unclear: {list}",
    },
    "sv": {
        "or": " eller ",
        "group_sep": ", eller ",
        "round_closes": "Omgången stänger {date}",
        "closed_when_verified": "Stängd vid kontroll {date}; läs statussidan för nästa omgång",
        "stale": "Senast kontrollerad {date}, läs statussidan innan du citerar",
        "also": "Även: {list}",
        "also_needs": "kräver dessutom:",
        "before_apply": "Innan ni ansöker: {list}",
        "unclear": "Oklart: {list}",
    },
    "fi": {
        "or": " tai ",
        "group_sep": ", tai ",
        "round_closes": "Haku sulkeutuu {date}",
        "closed_when_verified": "Suljettu tarkistushetkellä {date}; katso seuraava haku tilasivulta",
        "stale": "Tarkistettu viimeksi {date}, lue tilasivu ennen lainaamista",
        "also": "Myös: {list}",
        "also_needs": "vaatii lisäksi:",
        "before_apply": "Ennen hakemista: {list}",
        "unclear": "Epäselvää: {list}",
    },
    "no": {
        "or": " eller ",
        "group_sep": ", eller ",
        "round_closes": "Runden stenger {date}",
        "closed_when_verified": "Stengt ved kontroll {date}; les statussiden for neste runde",
        "stale": "Sist kontrollert {date}, les statussiden før du siterer",
        "also": "Også: {list}",
        "also_needs": "krever i tillegg:",
        "before_apply": "Før dere søker: {list}",
        "unclear": "Uklart: {list}",
    },
    "da": {
        "or": " eller ",
        "group_sep": ", eller ",
        "round_closes": "Runden lukker {date}",
        "closed_when_verified": "Lukket ved kontrol {date}; læs statussiden for næste runde",
        "stale": "Sidst kontrolleret {date}, læs statussiden før du citerer",
        "also": "Også: {list}",
        "also_needs": "kræver desuden:",
        "before_apply": "Før I ansøger: {list}",
        "unclear": "Uklart: {list}",
    },
}


def pick_lang(lang: object) -> str:
    code = str(lang or "").strip().lower()[:2]
    return code if code in LANGS else DEFAULT_LANG


def format_number(value: object) -> str:
    """1000000 -> '1 000 000', 2.5 -> '2.5'. Spaces as thousands separator read the same in all five languages."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if float(value).is_integer():
        return f"{int(value):,}".replace(",", " ")
    return str(value)


def country_name(code: object, lang: str) -> str:
    code_str = str(code).upper()
    return COUNTRY_NAMES[lang].get(code_str, code_str)


def country_in_fi(code: object) -> str:
    code_str = str(code).upper()
    return COUNTRY_IN_FI.get(code_str, f"maassa {code_str}")


def confirmation(key: object, lang: str) -> tuple[str, str]:
    """Label and question for a confirmation key; an unknown key is shown as itself so the gap is visible, not hidden."""
    entry = CONFIRMATIONS.get(str(key))
    if entry is None:
        return (str(key), f"{key}?")
    return entry.get(lang) or entry[DEFAULT_LANG]


def value_name(field: str, value: object, lang: str) -> str:
    """The display form of one rule value in one language."""
    if field == "confirmed":
        return confirmation(value, lang)[0]
    if field in ("country", "residence_country"):
        return country_name(value, lang)
    if field == "legal_form":
        return LEGAL_FORM_NAMES[lang].get(str(value), str(value))
    if field == "stage":
        return STAGE_NAMES[lang].get(str(value), str(value))
    if field == "sector":
        return SECTOR_NAMES[lang].get(str(value), str(value))
    if field == "stack":
        return VENDOR_NAMES.get(str(value), str(value))
    if field == "funding_raised_usd":
        return f"{format_number(value)} USD"
    if field in ("prior_grants", "active_grants"):
        return GRANT_NAMES.get(str(value), str(value))
    if field == "affiliation":
        return AFFILIATION_NAMES[lang].get(str(value), str(value))
    if field == "personal_data":
        return PERSONAL_DATA_NAMES[lang].get(str(value), str(value))
    return format_number(value)


def join_values(field: str, values: list, lang: str) -> str:
    names = [value_name(field, v, lang) for v in values]
    if len(names) <= 1:
        return "".join(names)
    return ", ".join(names[:-1]) + PHRASES[lang]["or"] + names[-1]


def rule_label(rule: dict, lang: str) -> str:
    """The label for one rule {field, op, value} in one language. Describes exactly what compare() checks."""
    field, op, value = rule["field"], rule["op"], rule["value"]
    table = LABELS[lang].get(field) or LABELS[DEFAULT_LANG].get(field, {})
    if isinstance(value, bool):
        template = table.get("true" if value else "false")
        if op == "neq" and template is not None:
            template = table.get("false" if value else "true")
    else:
        template = table.get(op)
    if template is None:
        # No template: say the check in plain field/op/value terms rather than hide it.
        return f"{field} {op} {value}"
    fill = {
        "n": format_number(value),
        "money": value_name(field, value, lang) if field == "funding_raised_usd" else format_number(value),
        "country": value_name(field, value, lang) if not isinstance(value, list) else "",
        "country_in": country_in_fi(value) if not isinstance(value, list) else "",
        "form": value_name(field, value, lang) if not isinstance(value, list) else "",
        "stage": value_name(field, value, lang) if not isinstance(value, list) else "",
        "vendor": value_name(field, value, lang) if not isinstance(value, list) else "",
        "sector": value_name(field, value, lang) if not isinstance(value, list) else "",
        "confirmation": value_name(field, value, lang) if not isinstance(value, list) else "",
        "list": join_values(field, value, lang) if isinstance(value, list) else value_name(field, value, lang),
    }
    return template.format(**fill)


def rule_question(rule: dict, lang: str) -> str:
    """The question to ask when the rule's field is unknown."""
    field, value = rule["field"], rule["value"]
    template = QUESTIONS[lang].get(field) or QUESTIONS[DEFAULT_LANG].get(field, f"{field}?")
    fill = {
        "vendor": value_name(field, value, lang) if field == "stack" else "",
        "sector": value_name(field, value, lang) if field == "sector" else "",
        "confirmation_question": confirmation(value, lang)[1] if field == "confirmed" else "",
    }
    return template.format(**fill)


def group_label(members: list[dict], lang: str) -> str:
    return PHRASES[lang]["group_sep"].join(rule_label(member, lang) for member in members)


def screen_question(topic: str, lang: str) -> str:
    """The one question the first answer asks about a situation topic."""
    if topic in SCREEN_FIELD:
        field = SCREEN_FIELD[topic]
        return QUESTIONS[lang].get(field) or QUESTIONS[DEFAULT_LANG][field]
    return SCREEN_QUESTIONS[lang].get(topic) or SCREEN_QUESTIONS[DEFAULT_LANG][topic]


def screen_why(topic: str, lang: str) -> str:
    return SCREEN_WHY[lang].get(topic) or SCREEN_WHY[DEFAULT_LANG][topic]


def route_name(route: str, lang: str) -> str:
    return ROUTE_NAMES[lang].get(route) or ROUTE_NAMES[DEFAULT_LANG].get(route, route)


def phrase(key: str, lang: str, **fill: object) -> str:
    return PHRASES[lang][key].format(**fill)
