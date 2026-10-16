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
    "new_to_aws_activate": {
        "en": ("new to AWS Activate credits, or asking for more than you received before", "Has the company received AWS Activate credits before, and if so, how much?"),
        "sv": ("ny i AWS Activate, eller ber om mer än ni fått tidigare", "Har bolaget fått AWS Activate-krediter tidigare, och i så fall hur mycket?"),
        "fi": ("uusi AWS Activate -hyvitysten hakija, tai pyytää enemmän kuin aiemmin", "Onko yhtiö saanut AWS Activate -hyvityksiä aiemmin, ja jos on, kuinka paljon?"),
        "no": ("ny i AWS Activate, eller ber om mer enn dere har fått før", "Har selskapet fått AWS Activate-kreditter før, og i så fall hvor mye?"),
        "da": ("ny i AWS Activate, eller beder om mere end I har fået før", "Har virksomheden fået AWS Activate-kreditter før, og i så fald hvor meget?"),
    },
    "need_owner": {
        "en": ("an established need owner committed to the project", "Do you have an established company or organisation committed as need owner in the project?"),
        "sv": ("en etablerad behovsägare som förbundit sig till projektet", "Har ni ett etablerat bolag eller en organisation som förbundit sig som behovsägare i projektet?"),
        "fi": ("vakiintunut tarpeen omistaja sitoutunut hankkeeseen", "Onko teillä vakiintunut yritys tai organisaatio sitoutuneena hankkeen tarpeen omistajaksi?"),
        "no": ("en etablert behovseier som har forpliktet seg til prosjektet", "Har dere et etablert selskap eller en organisasjon som har forpliktet seg som behovseier i prosjektet?"),
        "da": ("en etableret behovsejer, der har forpligtet sig til projektet", "Har I en etableret virksomhed eller organisation, der har forpligtet sig som behovsejer i projektet?"),
    },
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
    },
    "sv": {
        "country": {"eq": "i {country}", "neq": "inte i {country}", "in": "i {list}", "not_in": "inte i {list}"},
        "residence_country": {"eq": "grundarna bor i {country}", "neq": "grundarna bor inte i {country}", "in": "grundarna bor i {list}", "not_in": "grundarna bor inte i {list}"},
        "legal_form": {"eq": "{form}", "neq": "inte {form}", "in": "{list}", "not_in": "inte {list}"},
        "confirmed": {"contains": "{confirmation}"},
        "age_years": {"lt": "yngre än {n} år", "lte": "högst {n} år", "gt": "äldre än {n} år", "gte": "minst {n} år", "eq": "{n} år"},
        "employees": {"lt": "färre än {n} anställda", "lte": "högst {n} anställda", "gt": "fler än {n} anställda", "gte": "minst {n} anställda", "eq": "{n} anställda"},
        "revenue_msek": {"lt": "omsättning under {n} mkr", "lte": "omsättning högst {n} mkr", "gt": "omsättning över {n} mkr", "gte": "omsättning minst {n} mkr"},
        "balance_msek": {"lt": "balansomslutning under {n} mkr", "lte": "balansomslutning högst {n} mkr", "gt": "balansomslutning över {n} mkr", "gte": "balansomslutning minst {n} mkr"},
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
    },
    "sv": {
        "country": "I vilket land är bolaget registrerat, eller var ska det registreras?",
        "residence_country": "I vilket land bor grundarna?",
        "confirmed": "{confirmation_question}",
        "legal_form": "Vilken bolagsform: aktiebolag eller annat bolag, enskild firma, ideell förening, universitet, offentlig sektor, eller inget bolag än?",
        "age_years": "Hur gammalt är bolaget, i år?",
        "employees": "Hur många anställda?",
        "revenue_msek": "Nettoomsättning senaste räkenskapsåret, i mkr?",
        "balance_msek": "Balansomslutning, i mkr?",
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


def phrase(key: str, lang: str, **fill: object) -> str:
    return PHRASES[lang][key].format(**fill)
