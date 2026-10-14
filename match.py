#!/usr/bin/env python3
"""One door for a Sweden/Nordics builder. Profile JSON on stdin."""

import json
import sys
import urllib.request
from datetime import datetime, timezone

VINNOVA_CALL = "https://data.vinnova.se/api/utlysningar/2016-04714"
VINNOVA_ROUND = "https://data.vinnova.se/api/ansokningsomgangar/{}"
PLAYGROUND = "https://www.eurohpc-ju.europa.eu/playground-access-ai-factories_en"
PORTAL = "https://access.eurohpc-ju.europa.eu/"
FACTORY = "mailto:info@swedenaifactory.se"
ICE = "https://ice.ri.se/"
BLOG = "https://opensverige.se/blogg/startup-krediter-gpu-sverige"
TOR = "https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms+of+Reference+-+AIF+Access+Calls.pdf"
LUMI = "https://lumi-ai-factory.eu/pricing-and-eligibility/"
SIGMA = "https://www.sigma2.no/nb/ki-fabrikken"
CONSORTIUM = {"FI", "NO", "DK", "CZ", "EE", "PL"}


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "opensverige-startup-krediter"})
    with urllib.request.urlopen(req, timeout=30) as res:
        data = json.load(res)
    return data[0] if isinstance(data, list) else data


def open_round():
    call = get(VINNOVA_CALL)
    ids = [row["DiarienummerAnsokningsomgang"] for row in call.get("AnsokningsomgangDnrLista") or []]
    now = datetime.now(timezone.utc)
    latest = None
    for dnr in reversed(ids):
        row = get(VINNOVA_ROUND.format(dnr))
        close = row.get("Stangningsdatum")
        if not close:
            continue
        latest = row
        stamp = datetime.fromisoformat(close).replace(tzinfo=timezone.utc)
        if stamp >= now:
            return row
    return latest


def emit(door, why, missing, confidence, link, nxt, sources):
    json.dump(
        {
            "door": door,
            "why": why,
            "missing": missing,
            "confidence": confidence,
            "link": link,
            "next": nxt,
            "sources": sources,
        },
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")


def money(profile):
    try:
        row = open_round()
    except Exception as exc:
        emit(
            "Vinnova Innovativa Startups",
            "API:t svarade inte. Öppna programsidan innan du säger datum eller belopp.",
            [str(exc)],
            "låg",
            "https://www.vinnova.se/e/innovativa-startups/innovativa-startups-2026",
            "Du söker i Vinnovas e-tjänst.",
            [VINNOVA_CALL],
        )
        return
    title = row.get("Titel")
    close = (row.get("Stangningsdatum") or "")[:16].replace("T", " ")
    page = next((link.get("URL") for link in row.get("LankLista") or [] if link.get("URL")), None)
    page = page or "https://www.vinnova.se/e/innovativa-startups/innovativa-startups-2026"
    if profile.get("legal_form") != "ab":
        emit(
            title,
            "Omgången tar svenska aktiebolag. En förening eller ett oregistrerat projekt faller på formen.",
            ["aktiebolag", "högst 10 år", "högst 10 anställda", "omsättning eller balans högst 10 mkr", "ingen vinstutdelning"],
            "hög",
            page,
            f"Stänger {close}. Du söker inte den här omgången utan ett aktiebolag.",
            [VINNOVA_ROUND.format(row.get("Diarienummer"))],
        )
        return
    missing = []
    if not profile.get("has_org_number"):
        missing.append("organisationsnummer")
    emit(
        title,
        "Senaste öppna omgången på Vinnovas API. Bedömningen sitter på programsidan: potential, genomförbarhet, team.",
        missing,
        "hög" if not missing else "medel",
        page,
        f"Stänger {close}. Du fyller e-tjänsten och klarmarkerar.",
        [VINNOVA_ROUND.format(row.get("Diarienummer"))],
    )


def gpu(profile):
    form = profile.get("legal_form") or "unknown"
    sources = [TOR, "https://mimer-ai.eu/about/faq/"]
    if form in ("ideell_forening", "unknown"):
        emit(
            "Sweden AI Factory, be om call",
            "Playground är industri: bolag, SME eller startup, momsnummer, anställd projektledare, yrkesmejl, engelska. En ideell förening är inte den sökanden.",
            ["juridisk form är bekräftad", "organisationsnummer", "vad GPU:n ska köra, vilket system, hur många timmar"],
            "låg" if form == "unknown" else "hög",
            FACTORY,
            f"Du mejlar och ber dem peka call. Skicka inte Playground. Kan ni betala i väntan: {ICE}",
            sources,
        )
        return
    if form == "academia":
        emit(
            "EuroHPC AI for Science",
            "Akademi och offentlig sektor hör hemma här. Industriella användare utan EU-projekt hör hemma i Playground.",
            [],
            "medel",
            "https://www.eurohpc-ju.europa.eu/ai-factories/faqs-ai-factories_en",
            "Du söker i portalen. FAQ och hemsida anger olika timtak. Läs båda innan du citerar ett tal.",
            sources,
        )
        return
    missing = []
    if not profile.get("has_vat"):
        missing.append("momsnummer")
    if not profile.get("has_employment"):
        missing.append("anställd projektledare, minst 3 månader efter allokeringens slut")
    if not profile.get("has_work_email"):
        missing.append("yrkesmejl")
    if not profile.get("workload_defined"):
        missing.append("kod, ett system, GPU-timmar")
    emit(
        "EuroHPC Playground",
        "Första GPU-dörren för ett bolag. Behörighet och teknisk bedömning, sedan först till kvarn. Upp till 5 000 GPU-timmar, 1–3 månader, ett system.",
        missing,
        "hög" if not missing else "medel",
        PLAYGROUND,
        f"Du skapar konto på {PORTAL} och skickar formuläret. Sweden AI Factory kan läsa utkastet först: {FACTORY}",
        sources,
    )


def credits(profile):
    stack = [s.lower() for s in profile.get("stack") or []]
    if not stack:
        emit(
            "Vänta på stacken",
            "Krediter sitter hos leverantören. Utan stack blir svaret en lista, och listan blir gammal.",
            ["vilka tjänster ni redan kör"],
            "låg",
            BLOG,
            "Säg stacken. Hämta leverantörens sida innan du nämner ett belopp.",
            [BLOG],
        )
        return
    known = {
        "aws": ("AWS Activate Founders", "https://aws.amazon.com/startups/credits"),
        "cloudflare": ("Cloudflare for Startups", "https://www.cloudflare.com/startups/"),
        "neon": ("Neon Credits for Startups", "https://neon.com/startups"),
        "gcp": ("Google for Startups Cloud", "https://cloud.google.com/startup"),
        "google": ("Google for Startups Cloud", "https://cloud.google.com/startup"),
        "azure": ("Microsoft for Startups", "https://startups.microsoft.com"),
        "microsoft": ("Microsoft for Startups", "https://startups.microsoft.com"),
        "claude": ("Claude Startups", "https://claude.com/programs/startups"),
        "anthropic": ("Claude Startups", "https://claude.com/programs/startups"),
        "openai": ("OpenAI for Startups", "https://openai.com/startups/"),
        "chatgpt": ("OpenAI for Startups", "https://openai.com/startups/"),
    }
    for key, (door, link) in known.items():
        if key in stack:
            if key in ("openai", "chatgpt"):
                emit(
                    door,
                    "Sidan låser API-krediter bakom en partner-VC och en referral-kod. Inget belopp är publicerat. Ingen investerare betyder ingen sådan kod.",
                    ["partner-VC", "referral-kod"],
                    "medel",
                    link,
                    "Hämta sidan. Citera inte ett dollarbelopp som inte står där.",
                    [link],
                )
                return
            emit(
                door,
                "En leverantör. Öppna sidan och läs beloppet där. Partnerlås finns på flera av programmen.",
                [],
                "medel",
                link,
                "Du söker på deras sida. Citera inte ett dollarbelopp som inte står där idag.",
                [link],
            )
            return
    emit(
        "Leverantörens egen sida",
        "Stacken matchade inget program i den korta kartan.",
        stack,
        "låg",
        BLOG,
        "Hämta leverantörens startsida. Finns inget belopp där är beloppet okänt.",
        [BLOG],
    )


def matrix(profile):
    form = profile.get("legal_form") or "unknown"
    country = (profile.get("country") or "").upper()
    p_blocks, p_missing = playground_gates(profile)
    v_blocks, v_missing = vinnova_gates(profile)
    if p_blocks:
        p_walk, p_n, p_wall = "nej", len(p_blocks), ", ".join(p_blocks)
    elif p_missing:
        p_walk, p_n, p_wall = "osäker", len(p_missing), ", ".join(p_missing)
    else:
        p_walk, p_n, p_wall = "ja", 0, "inga"
    if v_blocks:
        v_walk, v_n, v_wall = "nej", len(v_blocks), ", ".join(v_blocks)
    elif v_missing:
        v_walk, v_n, v_wall = "osäker", len(v_missing), ", ".join(v_missing)
    else:
        v_walk, v_n, v_wall = "ja", 0, "inga"
    rows = [
        {
            "door": "Sweden AI Factory, fråga",
            "walk": "ja",
            "blockers": 0,
            "wall": "ingen för mejlet",
            "they_want": "att du ber dem peka call",
            "apply": "mejl, du skickar",
            "auto": "utkast",
        },
        {
            "door": "ICE Connect",
            "walk": "om du betalar",
            "blockers": 1,
            "wall": "faktura",
            "they_want": "ett konto och betalning",
            "apply": "webbshop",
            "auto": "nej",
        },
        {
            "door": "EuroHPC Playground",
            "walk": p_walk,
            "blockers": p_n,
            "wall": p_wall,
            "they_want": "industri, SME eller startup",
            "apply": "portal, inget skicka-API",
            "auto": "nej",
        },
        {
            "door": "EuroHPC Fast Lane",
            "walk": p_walk,
            "blockers": p_n,
            "wall": p_wall,
            "they_want": "samma industrikrav som Playground, rullande, ingen poängrunda",
            "apply": "portal, villkoren avsnitt 5.1.1, inget skicka-API",
            "auto": "nej",
        },
        {
            "door": "Almi",
            "walk": "osäker",
            "blockers": 1,
            "wall": "namngiven i beskrivningen, ingen kodad utlysning",
            "they_want": "att du hämtar Almis sida innan du nämner ett belopp",
            "apply": "ingen dörr i det här repot",
            "auto": "nej",
        },
        {
            "door": "Vinnova Innovativa Startups",
            "walk": v_walk,
            "blockers": v_n,
            "wall": v_wall,
            "they_want": "svenskt AB, högst 10 år, 10 anställda, 10 mkr",
            "apply": "e-tjänst, läs-API finns, skicka-API finns inte",
            "auto": "nej",
        },
        {
            "door": "EuroHPC AI for Science",
            "walk": "ja" if form == "academia" else "osäker" if form == "unknown" else "osäkert",
            "blockers": 0 if form == "academia" else 1,
            "wall": "ingen om du är akademi eller offentlig sektor" if form == "academia" else "vet inte om du är akademi" if form == "unknown" else "bolag utan EU-projekt hör hemma i Playground",
            "they_want": "forskning, offentlig sektor, eller industri i ett EU-projekt",
            "apply": "portal, inget skicka-API",
            "auto": "nej",
        },
        {
            "door": "RISE",
            "walk": "osäker",
            "blockers": 1,
            "wall": "ingen egen blankett. GPU-tid går via fabriken, faktura via ICE",
            "they_want": "att du tar fabriken eller betalar ICE",
            "apply": "ingen ansökan till RISE",
            "auto": "nej",
        },
        {
            "door": "LUMI nationellt",
            "walk": "osäker" if not country else "ja" if country in CONSORTIUM else "nej",
            "blockers": 0 if country in CONSORTIUM else 1,
            "wall": "land saknas" if not country else "konsortiumland" if country in CONSORTIUM else f"{country} tar EuroHPC, inte det nationella spåret",
            "they_want": "SME i ett konsortiumland. Finland kan dessutom söka Business Finland, tak 300 000 euro på tre år",
            "apply": "kontaktformulär, plus EuroHPC",
            "auto": "nej",
        },
        {
            "door": "KI-fabrikken",
            "walk": "osäker" if not country else "ja" if country == "NO" else "nej",
            "blockers": 0 if country == "NO" else 1,
            "wall": "land saknas" if not country else "kontakta Sigma2" if country == "NO" else "inte en norsk verksamhet",
            "they_want": "näringsliv och offentlig sektor i Norge, maskinen Olivia",
            "apply": "https://www.sigma2.no/nb/ki-fabrikken",
            "auto": "nej",
        },
        {
            "door": "NVIDIA Inception",
            "walk": "osäker",
            "blockers": 1,
            "wall": "bolag, sajt, utvecklare, under 10 år, yrkesmejl. Belopp inte publicerat",
            "they_want": "rabatt och partnerkrediter, inte EuroHPC-timmar",
            "apply": "https://www.nvidia.com/en-eu/startups/",
            "auto": "nej",
        },
        {
            "door": "Berget, ICE, Stormgrid",
            "walk": "om du betalar",
            "blockers": 1,
            "wall": "faktura",
            "they_want": "kunder, inte sökande",
            "apply": "ingen bidragssida",
            "auto": "nej",
        },
        {
            "door": "Hyperight, Agorify, HP, Bull, Consumeit, Aderian",
            "walk": "nej",
            "blockers": 1,
            "wall": "monter på Nordic AI Factory Summit 2026, inte en utlysning",
            "they_want": "besökare",
            "apply": "ingen",
            "auto": "nej",
        },
    ]
    json.dump({"legal_form": form, "rows": rows}, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def absent(profile, key):
    return key not in profile or profile.get(key) is None


def vinnova_gates(profile):
    blocks = []
    missing = []
    form = profile.get("legal_form") or "unknown"
    if form == "unknown":
        missing.append("juridisk form")
    elif form != "ab":
        blocks.append("kräver aktiebolag")
    if profile.get("country") not in (None, "SE"):
        blocks.append("sökanden är inte svensk")
    if absent(profile, "age_years"):
        missing.append("bolagets ålder")
    elif profile["age_years"] > 10:
        blocks.append("äldre än 10 år")
    if absent(profile, "employees"):
        missing.append("antal anställda")
    elif profile["employees"] > 10:
        blocks.append("fler än 10 anställda")
    rev = profile.get("revenue_msek")
    bal = profile.get("balance_msek")
    if rev is None and bal is None:
        missing.append("omsättning eller balans")
    elif rev is not None and bal is not None and rev > 10 and bal > 10:
        blocks.append("både omsättning och balans över 10 mkr")
    elif rev is not None and rev > 10 and bal is None:
        missing.append("balans, omsättningen är över 10 mkr")
    elif bal is not None and bal > 10 and rev is None:
        missing.append("omsättning, balansen är över 10 mkr")
    if absent(profile, "profit_distributed"):
        missing.append("vinstutdelning senaste året")
    elif profile["profit_distributed"]:
        blocks.append("vinstutdelning")
    return blocks, missing


def playground_gates(profile):
    form = profile.get("legal_form") or "unknown"
    if form == "unknown":
        return [], ["juridisk form"]
    if form != "ab":
        return ["kräver bolag, SME eller startup"], []
    missing = []
    if not profile.get("has_vat"):
        missing.append("momsnummer")
    if not profile.get("has_employment"):
        missing.append("anställd projektledare, minst 3 månader efter allokeringens slut")
    if not profile.get("has_work_email"):
        missing.append("yrkesmejl")
    if not profile.get("workload_defined"):
        missing.append("kod, ett system, GPU-timmar")
    return [], missing


SHORT = {
    "momsnummer": "moms",
    "anställd projektledare, minst 3 månader efter allokeringens slut": "anställning",
    "yrkesmejl": "yrkesmejl",
    "kod, ett system, GPU-timmar": "arbetsbeskrivning",
    "Playground kräver bolag": "Playground kräver bolag",
    "kräver aktiebolag": "aktiebolag",
    "kräver bolag, SME eller startup": "bolag",
}

LANG = "sv"

EN = (
    ("Finns ett anställningsavtal som gäller minst tre månader efter att GPU-tiden tar slut?", "Is there an employment contract that lasts at least three months after the GPU time ends?"),
    ("Har bolaget momsnummer?", "Does the company have a VAT number?"),
    ("Vilken adress på er egen domän ska stå som kontakt?", "Which address on your own domain is the contact?"),
    ("Vilken kod, vilket enda system, och hur många GPU-timmar?", "Which code, which single system, and how many GPU hours?"),
    ("Vilket land är bolaget registrerat i?", "Which country is the company registered in?"),
    ("Dörren beror på landet. Utan land blir ett nej en gissning.", "The door depends on the country. Without a country, a no is a guess."),
    ("GPU-tid betalar inte API-fakturan. Vinnova kan lotta två ansökningar som båda är starka.", "GPU time does not pay the API invoice. Vinnova can draw lots between two applications that are both strong."),
    ("Business Finland är finskt statligt stöd, tak 300 000 euro på tre år. Ett svenskt bolag tar EuroHPC, inte det här.", "Business Finland is Finnish state aid, capped at 300,000 euro over three years. A Swedish company takes EuroHPC, not this."),
    ("Är bolaget registrerat i Finland?", "Is the company registered in Finland?"),
    ("Är verksamheten norsk?", "Is the business Norwegian?"),
    ("Är bolaget ett danskt SME?", "Is the company a Danish SME?"),
    ("Är bolaget isländskt och ett SME?", "Is the company Icelandic and an SME?"),
    ("Våren stängde 17 februari 2026. Hösten stängde 25 augusti 2026 kl 12. Slutbesked väntas i mitten av december 2026.", "Spring closed 17 February 2026. Autumn closed 25 August 2026 at noon. A final answer is expected in mid-December 2026."),
    ("17 februari 2026 och 25 augusti 2026", "17 February 2026 and 25 August 2026"),
    ("Ansök i Rannís portal. Bara elektroniskt.", "Apply in the Rannís portal. Electronic only."),
    ("○  land", "○  country"),
    ("◐  land", "◐  country"),
    ("danskt SME", "Danish SME"),
    ("isländskt bolag", "Icelandic company"),
    ("finskt bolag", "Finnish company"),
    ("norsk verksamhet", "Norwegian business"),
    ("arbetsbeskrivning", "workload"),
    ("yrkesmejl", "work email"),
    ("anställning", "employment"),
    ("aktiebolag", "limited company"),
    ("personer", "people"),
    (" år", " years"),
    ("moms", "VAT"),
)


def localize(text):
    if LANG != "en":
        return text
    for src, dst in EN:
        text = text.replace(src, dst)
    return text


def glyph_block(state, door, gaps, unthought):
    head = {"stängd": "○", "osäker": "◐", "kan söka": "●", "fråga": "●"}.get(state, "○")
    lines = [f"{head}  {door}"]
    for gap in gaps:
        lines.append(f"○  {SHORT.get(gap, gap)}")
    if unthought:
        lines.append(f"→  {unthought}")
    return localize("\n".join(lines))


def picture(state, door, known, holes, ask, unthought, failed=None):
    head = {"stängd": "×", "osäker": "◐", "kan söka": "●", "fråga": "●"}.get(state, "○")
    lines = [f"{head}  {door}"]
    for label in known:
        lines.append(f"●  {label}")
    for label in failed or []:
        lines.append(f"×  {label}")
    for label in holes:
        lines.append(f"○  {label}")
    if ask:
        lines.append(f"?  {ask}")
    if unthought:
        lines.append(f"→  {unthought}")
    return localize("\n".join(lines))


def checks_for(known, holes, failed=None):
    rows = [{"label": label, "status": "uppfyllt"} for label in known]
    rows += [{"label": label, "status": "inte uppfyllt"} for label in (failed or [])]
    rows += [{"label": label, "status": "okänt"} for label in holes]
    return rows


GPU_SLOTS = (
    ("has_employment", "anställning", "Finns ett anställningsavtal som gäller minst tre månader efter att GPU-tiden tar slut?"),
    ("has_vat", "moms", "Har bolaget momsnummer?"),
    ("has_work_email", "yrkesmejl", "Vilken adress på er egen domän ska stå som kontakt?"),
    ("workload_defined", "arbetsbeskrivning", "Vilken kod, vilket enda system, och hur många GPU-timmar?"),
)


def slot_rows(profile, slots):
    known, holes, denied, ask = [], [], [], None
    for key, label, question in slots:
        if profile.get(key) is True:
            known.append(label)
        elif profile.get(key) is False:
            denied.append(label)
        else:
            holes.append(label)
            if ask is None:
                ask = question
    return known, holes, denied, ask


def facts(profile):
    known = []
    if profile.get("legal_form") == "ab":
        known.append("aktiebolag")
    if not absent(profile, "age_years"):
        known.append(f"{profile['age_years']} år")
    if not absent(profile, "employees"):
        known.append(f"{profile['employees']} personer")
    return known


def chance(profile):
    global LANG
    LANG = "en" if str(profile.get("lang") or "").lower() == "en" else "sv"
    need = profile.get("need") or "unsure"
    form = profile.get("legal_form") or "unknown"
    v_blocks, v_missing = vinnova_gates(profile)
    p_blocks, p_missing = playground_gates(profile)
    page = "https://www.vinnova.se/e/innovativa-startups/innovativa-startups-2026"

    if need in ("gpu", "money") and not (profile.get("country") or "").strip():
        json.dump(
            {
                "chance": "osäker",
                "glyph": picture("osäker", "land", [], ["land"], "Vilket land är bolaget registrerat i?", "Dörren beror på landet. Utan land blir ett nej en gissning."),
                "door": "land",
                "why": "Aktören avgörs av var bolaget sitter.",
                "missing": ["land"],
                "ask": "Vilket land är bolaget registrerat i?",
                "unthought": "Dörren beror på landet. Utan land blir ett nej en gissning.",
                "confidence": "låg",
                "link": BLOG,
                "next": "Säg landet. Säg aldrig att ansökan är skickad.",
                "sources": [BLOG],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    if need == "credits":
        credits(profile)
        return
    if need not in ("gpu", "money"):
        json.dump(
            {
                "chance": "osäker",
                "door": "Inget ännu",
                "why": "Chansen räknas mot en dörr. Pengar, GPU-timmar och krediter är tre olika dörrar.",
                "missing": ["need"],
                "unthought": "Formen stänger fler ansökningar än texten. Säg vilken dörr innan du skriver en pitch.",
                "confidence": "låg",
                "link": BLOG,
                "next": "Ett behov, en dörr.",
                "sources": [BLOG],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    if need == "gpu" and form == "ideell_forening":
        unthought = "Startup i den här kartan betyder bolag. Föreningen kan fråga fabriken. Den kan inte söka Playground."
        json.dump(
            {
                "chance": "fråga",
                "glyph": "○  Playground\n●  mejl till fabriken\n→  " + unthought,
                "door": "Sweden AI Factory, fråga",
                "why": "Playground är industri. Föreningen frågar fabriken vilken call som finns.",
                "missing": [],
                "unthought": unthought,
                "confidence": "hög",
                "link": FACTORY,
                "next": "Du mejlar. Säg aldrig att ansökan är skickad.",
                "sources": [page, TOR],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "gpu" and (profile.get("country") or "SE").upper() == "FI":
        finnish = profile.get("finnish_company")
        holes = [] if finnish is True else ["finskt bolag"]
        ask = None if finnish is True else "Är bolaget registrerat i Finland?"
        state = "kan söka" if finnish is True else "osäker"
        json.dump(
            {
                "chance": state,
                "glyph": picture(state, "LUMI", ["Finland"] if finnish is True else [], holes, ask, "Business Finland är finskt statligt stöd, tak 300 000 euro på tre år. Ett svenskt bolag tar EuroHPC, inte det här."),
                "door": "LUMI",
                "why": "Finland sitter i LUMI-konsortiet och har ett nationellt spår. RISE gör det inte.",
                "missing": holes,
                "ask": ask,
                "unthought": "Business Finland är finskt statligt stöd, tak 300 000 euro på tre år. Ett svenskt bolag tar EuroHPC, inte det här.",
                "confidence": "medel" if finnish is True else "låg",
                "link": LUMI,
                "next": "Du kontaktar LUMI. Säg aldrig att ansökan är skickad.",
                "sources": [LUMI],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "gpu" and (profile.get("country") or "SE").upper() == "NO":
        norwegian = profile.get("norwegian_company")
        holes = [] if norwegian is True else ["norsk verksamhet"]
        ask = None if norwegian is True else "Är verksamheten norsk?"
        state = "kan söka" if norwegian is True else "osäker"
        unthought = "Olivia är Norges maskin, hos Sigma2. RISE delar inte ut den tiden."
        json.dump(
            {
                "chance": state,
                "glyph": picture(state, "KI-fabrikken", ["Norge"] if norwegian is True else [], holes, ask, unthought),
                "door": "KI-fabrikken",
                "why": "Norges dörr på summiten är Sigma2, inte Sweden AI Factory.",
                "missing": holes,
                "ask": ask,
                "unthought": unthought,
                "confidence": "medel" if norwegian is True else "låg",
                "link": SIGMA,
                "next": "Du kontaktar Sigma2. Säg aldrig att ansökan är skickad.",
                "sources": [SIGMA],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "gpu" and (profile.get("country") or "SE").upper() == "DK":
        unthought = "Danmark sitter i LUMI-konsortiet. Ett nationellt bidragsnamn står inte på sidan. Gissa inte."
        json.dump(
            {
                "chance": "osäker",
                "glyph": picture("osäker", "LUMI", [], ["danskt SME"], "Är bolaget ett danskt SME?", unthought),
                "door": "LUMI",
                "why": "Danmark kan ta EuroHPC och LUMI:s nationella spår. Namnet på det nationella bidraget är okänt.",
                "missing": ["danskt SME"],
                "ask": "Är bolaget ett danskt SME?",
                "unthought": unthought,
                "confidence": "låg",
                "link": LUMI,
                "next": "Du kontaktar LUMI. Säg aldrig att ansökan är skickad.",
                "sources": [LUMI],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "gpu" and (profile.get("country") or "SE").upper() == "IS":
        unthought = "Island är en LUMI-antenn, inte ett konsortiumland. Ingen egen nationell GPU-pott på den sidan."
        json.dump(
            {
                "chance": "osäker",
                "glyph": picture("osäker", "Playground", [], ["isländskt bolag"], "Är bolaget isländskt och ett SME?", unthought),
                "door": "Playground",
                "why": "Island söker via EuroHPC. AI Iceland på summiten är inte en utlysning.",
                "missing": ["isländskt bolag"],
                "ask": "Är bolaget isländskt och ett SME?",
                "unthought": unthought,
                "confidence": "låg",
                "link": PLAYGROUND,
                "next": "Du söker i portalen. Säg aldrig att ansökan är skickad.",
                "sources": [LUMI, PLAYGROUND],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "gpu":
        door, link = "Playground", PLAYGROUND
        unthought = "GPU-tid betalar inte API-fakturan. Vinnova kan lotta två ansökningar som båda är starka."
        base = facts(profile)
        got, holes, denied, ask = slot_rows(profile, GPU_SLOTS)
        failed = denied or p_blocks
        if failed:
            state, confidence = "stängd", "hög"
            ask = None
        elif holes:
            state, confidence = "osäker", "låg"
        else:
            state, confidence = "kan söka", "medel"
        json.dump(
            {
                "chance": state,
                "glyph": picture(state, door, base + got, holes, ask, unthought, failed),
                "checks": checks_for(base + got, holes, failed),
                "door": door,
                "why": "Anställningen stänger Playground. Idén gör det inte.",
                "missing": holes,
                "ask": ask,
                "unthought": unthought,
                "confidence": confidence,
                "link": link,
                "next": "Du söker. Säg aldrig att ansökan är skickad.",
                "sources": [TOR],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "money" and (profile.get("country") or "SE").upper() == "NO":
        age = profile.get("age_years")
        form_ok = profile.get("legal_form") == "ab"
        if profile.get("legal_form") not in (None, "unknown", "ab"):
            state, holes, ask = "stängd", ["norskt AS"], None
        elif age is not None and age >= 5:
            state, holes, ask = "stängd", ["äldre än fem år"], None
        elif not form_ok:
            state, holes, ask = "osäker", ["norskt AS"], "Är bolaget ett norskt AS?"
        elif age is None:
            state, holes, ask = "osäker", ["yngre än fem år"], "Är bolaget yngre än fem år?"
        else:
            state, holes, ask = "kan söka", [], "Logga in på Innovasjon Norges Min side och starta Oppstartstilskudd 1."
        unthought = "Taket på sidan är 150 000 NOK. GPU-tid är KI-fabrikken, inte det här bidraget."
        json.dump(
            {
                "chance": state,
                "glyph": picture(state, "Oppstartstilskudd 1", facts(profile), holes, ask, unthought),
                "door": "Oppstartstilskudd 1",
                "why": "Innovasjon Norge tar ett norskt AS under fem år. Första steget är Min side.",
                "missing": holes,
                "ask": ask,
                "unthought": unthought,
                "confidence": "hög" if state == "stängd" else "medel" if state == "kan söka" else "låg",
                "link": "https://www.innovasjonnorge.no/en/tjeneste/oppstartstilskudd-1",
                "next": "Du loggar in och startar. Säg aldrig att ansökan är skickad.",
                "sources": ["https://www.innovasjonnorge.no/en/tjeneste/oppstartstilskudd-1"],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "money" and (profile.get("country") or "SE").upper() == "FI":
        age = profile.get("age_years")
        finnish = profile.get("finnish_company")
        if age is not None and age >= 5:
            state, holes, ask = "stängd", ["äldre än fem år"], None
        elif finnish is not True:
            state, holes, ask = "osäker", ["finskt bolag under fem år"], "Är bolaget finskt och yngre än fem år?"
        else:
            state, holes, ask = "kan söka", [], "Skicka ansökan i Business Finlands e-tjänst."
        unthought = "Beloppet står i e-tjänsten. GPU-tid är LUMI, och det nationella compute-spåret är statligt stöd."
        json.dump(
            {
                "chance": state,
                "glyph": picture(state, "Business Finland", [], holes, ask, unthought),
                "door": "Business Finland",
                "why": "Finlands pengadörr för unga bolag är Business Finland, inte Vinnova.",
                "missing": holes,
                "ask": ask,
                "unthought": unthought,
                "confidence": "hög" if state == "stängd" else "medel" if state == "kan söka" else "låg",
                "link": "https://www.businessfinland.fi/en/services/funding/",
                "next": "Du söker i deras e-tjänst. Säg aldrig att ansökan är skickad.",
                "sources": ["https://www.businessfinland.fi/en/services/funding/"],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "money" and (profile.get("country") or "SE").upper() == "DK":
        unthought = "Våren stängde 17 februari 2026. Hösten stängde 25 augusti 2026 kl 12. Slutbesked väntas i mitten av december 2026."
        json.dump(
            {
                "chance": "stängd",
                "glyph": picture("stängd", "Innofounder", [], ["17 februari 2026 och 25 augusti 2026"], None, unthought),
                "door": "Innofounder",
                "why": "Båda omgångarna 2026 är stängda. Skicka inte en ansökan mot ett passerat datum. Besked om hösten väntas i mitten av december.",
                "missing": ["17 februari 2026", "25 augusti 2026"],
                "ask": None,
                "unthought": unthought,
                "confidence": "hög",
                "link": "https://www.innovationsfonden.dk/en/p/innofounder",
                "next": "Vänta på nästa öppning. Säg aldrig att ansökan är skickad.",
                "sources": [
                    "https://www.innovationsfonden.dk/en/p/innofounder",
                    "https://innovationsfonden.dk/da/p/innofounder/innofounder-4",
                ],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    elif need == "money" and (profile.get("country") or "SE").upper() == "IS":
        unthought = "Sprout stängde 15 september 2026. Fræ är öppen året om, tak 2 miljoner ISK, bolag under fem år eller en person."
        json.dump(
            {
                "chance": "kan söka",
                "glyph": picture("kan söka", "Fræ", [], [], "Ansök i Rannís portal. Bara elektroniskt.", unthought),
                "door": "Fræ",
                "why": "Islands öppna dörr är Fræ hos Rannís. Sprout är stängd.",
                "missing": [],
                "ask": "Ansök i Rannís portal. Bara elektroniskt.",
                "unthought": unthought,
                "confidence": "medel",
                "link": "https://island.is/en/grants-plaza/grant/1-42",
                "next": "Du skickar i portalen. Säg aldrig att ansökan är skickad.",
                "sources": ["https://island.is/en/grants-plaza/grant/1-42", "https://island.is/en/grants-plaza/grant/1-46"],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
        return
    else:
        door, blocks, missing, link = "Vinnova Innovativa Startups", v_blocks, v_missing, page
        why = "Chansen är att få bli bedömd. Från 2026 lottas ansökningar som experterna tycker är höga och likvärdiga."
        unthought = "Vinnova ger kronor till att testa marknaden. Den ger inte GPU-timmarna."

    if blocks:
        state, confidence, gaps = "stängd", "hög", blocks
    elif missing:
        state, confidence, gaps = "osäker", "låg", missing
    else:
        state, confidence, gaps = "kan söka", "medel", []

    json.dump(
        {
            "chance": state,
            "glyph": glyph_block(state, door, gaps, unthought),
            "door": door,
            "why": why,
            "missing": gaps,
            "unthought": unthought,
            "confidence": confidence,
            "link": link,
            "next": "Du mejlar. Säg aldrig att ansökan är skickad." if link == FACTORY else "Du söker. Säg aldrig att ansökan är skickad.",
            "sources": [page, TOR],
        },
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")


def slot(profile, key, label):
    if key not in profile or profile.get(key) is None:
        return {"label": label, "ready": False, "value": None}
    value = profile.get(key)
    ready = value is not False and value != ""
    return {"label": label, "ready": ready, "value": value}


def actions(url, values, stop):
    steps = [{"do": "open", "url": url}]
    for key, value in (values or {}).items():
        if value:
            steps.append({"do": "fill", "field": key, "value": value})
    steps.append({"do": "stop", "before": stop})
    return steps


def door_packet(name, link, apply, fields):
    missing = [field["label"] for field in fields if not field["ready"]]
    return {
        "door": name,
        "link": link,
        "fill": "ja" if not missing else "nej",
        "submit": "nej",
        "why": apply,
        "missing": missing,
        "fields": fields,
    }


def packet(profile):
    playground = door_packet(
        "Playground",
        PLAYGROUND,
        "portal, inget skicka-API",
        [
            slot(profile, "legal_form", "aktiebolag"),
            slot(profile, "has_vat", "moms"),
            slot(profile, "has_employment", "anställning"),
            slot(profile, "has_work_email", "yrkesmejl"),
            slot(profile, "workload_defined", "arbetsbeskrivning"),
        ],
    )
    if playground["fields"][0]["value"] not in (None, "ab"):
        playground["fields"][0]["ready"] = False
        playground["fill"] = "nej"
        if "aktiebolag" not in playground["missing"]:
            playground["missing"].insert(0, "aktiebolag")
    playground["fill_url"] = "https://access.eurohpc-ju.europa.eu/auth/register"
    playground["gate"] = "Register to apply"
    playground["form"] = ["firstName", "lastName", "email", "password", "confirmPassword", "captcha"]
    playground["values"] = {
        "firstName": profile.get("first_name"),
        "lastName": profile.get("last_name"),
        "email": profile.get("work_email"),
    }
    playground["application_form"] = "nej"
    playground["captcha"] = "stopp"
    playground["assess"] = {
        "source": TOR,
        "questions": [
            "Behörighet: industri, SME eller startup i ett medlemsland eller associerat land.",
            "Projektledaren är anställd vid inlämning och minst tre månader efter allokeringens slut.",
            "Momsnummer, och PIC om det finns.",
            "Civilt syfte och förenligt med AI Act.",
            "Teknisk genomförbarhet på ett system.",
            "Alla obligatoriska fält i onlineformuläret.",
        ],
        "after": "Avsnitt 3.1: behörighet och teknisk förmåga. Avsnitt 5.1.1: först till kvarn tills resurserna tar slut. Samma villkor säger också att innovation avgör den sista tilldelningen i Playground. Välj inte.",
    }
    playground["actions"] = actions(playground["fill_url"], playground["values"], "Register")
    playground["actions_inloggad"] = [
        {"do": "open", "url": "https://access.eurohpc-ju.europa.eu/calls/60"},
    ]
    if profile.get("summary_en") or profile.get("summary_sv"):
        playground["actions_inloggad"].append(
            {
                "do": "fill",
                "field": "relevans",
                "value": profile.get("summary_en") or profile.get("summary_sv"),
            }
        )
    playground["actions_inloggad"].append({"do": "stop", "before": "submit"})
    vinnova = door_packet(
        "Vinnova Innovativa Startups",
        "https://www.vinnova.se/e/innovativa-startups/innovativa-startups-2026",
        "e-tjänst, läs-API finns, skicka-API finns inte",
        [
            slot(profile, "legal_form", "aktiebolag"),
            slot(profile, "has_org_number", "organisationsnummer"),
            slot(profile, "age_years", "ålder"),
            slot(profile, "employees", "anställda"),
            slot(profile, "revenue_msek", "omsättning"),
            slot(profile, "profit_distributed", "vinstutdelning"),
        ],
    )
    if vinnova["fields"][0]["value"] not in (None, "ab"):
        vinnova["fields"][0]["ready"] = False
    if profile.get("revenue_msek") is None and profile.get("balance_msek") is not None:
        vinnova["fields"][4]["value"] = profile["balance_msek"]
        vinnova["fields"][4]["ready"] = True
        vinnova["fields"][4]["label"] = "balans"
    if profile.get("profit_distributed") is False:
        vinnova["fields"][5]["ready"] = True
    if profile.get("profit_distributed") is True:
        vinnova["fields"][5]["ready"] = False
    if profile.get("age_years") is not None and profile["age_years"] > 10:
        vinnova["fields"][2]["ready"] = False
    if profile.get("employees") is not None and profile["employees"] > 10:
        vinnova["fields"][3]["ready"] = False
    vinnova["missing"] = [field["label"] for field in vinnova["fields"] if not field["ready"]]
    vinnova["fill"] = "ja" if not vinnova["missing"] else "nej"
    vinnova["fill_url"] = "https://etjanster.vinnova.se/public/login"
    vinnova["gate"] = "Logga in"
    vinnova["form"] = []
    vinnova["application_form"] = "nej"
    vinnova["after_login"] = {
        "projektsammanfattning på svenska": profile.get("summary_sv"),
        "projektsammanfattning på engelska": profile.get("summary_en"),
        "mål": profile.get("goals"),
        "start": profile.get("project_start"),
        "slut": profile.get("project_end"),
        "koordinator": profile.get("coordinator"),
        "projektledare": profile.get("project_leader"),
        "firmatecknare": profile.get("signatory"),
        "budget i hela kronor": profile.get("budget_sek"),
    }
    vinnova["assess"] = {
        "source": "https://www.vinnova.se/e/innovativa-startups/innovativa-startups-2026",
        "questions": [
            "På vilket sätt lösningen är mer innovativ än befintliga lösningar.",
            "På vilket sätt affärsidén kan skapa tillväxt i Sverige.",
            "På vilket sätt affärsidén har potential på en internationell marknad.",
            "På vilket sätt kunskapstillgångarna är unika och skyddsvärda.",
            "Att budget, plan och angreppssätt räcker till målet.",
            "Att det finns en plan för kommersialisering och finansiering efter projektet.",
            "Att behovet av Vinnovas finansiering är motiverat givet bolagets ekonomi.",
            "Hur konsult- och licenskostnader motiveras.",
            "Att bolaget kan genomföra projektet.",
            "Att grundarna har kontroll och driver bolaget.",
            "Att teamet är satt efter behovet, med en strategi för jämställd makt.",
        ],
        "after": "Svenska sidan: upp till 500 000 kr, beslut 23 mars 2027. Låg grad avslås. Mycket hög grad beviljas. Hög och likvärdig grad lottas. Engelsk sida: samma tak, och att full bedömningstext publiceras när utlysningen öppnar. Presentation mars 2026: poäng 0–5 och rangordning, öppning 1 september. Välj inte. Inga namngivna beviljanden för 2026-omgången före beslutsdagen.",
    }
    vinnova["actions"] = actions(vinnova["fill_url"], {}, "Skapa konto")
    vinnova["actions_inloggad"] = [
        {
            "do": "open",
            "url": "https://ansok.vinnova.se/utlysning/0382e83b-4c96-404d-bed1-08deab387617?opencall=true&lang=sv",
        }
    ]
    for field, value in vinnova["after_login"].items():
        if value:
            vinnova["actions_inloggad"].append({"do": "fill", "field": field, "value": value})
    vinnova["actions_inloggad"].append({"do": "stop", "before": "Klarmarkera ansökan"})
    nvidia = door_packet(
        "NVIDIA Inception",
        "https://www.nvidia.com/en-us/startups/faq/",
        "formulär, inget skicka-API",
        [
            slot(profile, "legal_form", "aktiebolag"),
            slot(profile, "age_years", "under 10 år"),
            slot(profile, "has_developer", "utvecklare"),
            slot(profile, "has_website", "sajt"),
            slot(profile, "has_work_email", "yrkesmejl"),
        ],
    )
    if profile.get("age_years") is not None and profile["age_years"] >= 10:
        nvidia["fields"][1]["ready"] = False
    nvidia["missing"] = [field["label"] for field in nvidia["fields"] if not field["ready"]]
    nvidia["fill"] = "ja" if not nvidia["missing"] else "nej"
    nvidia["fill_url"] = "https://programs.nvidia.com/phoenix/application"
    nvidia["gate"] = "Sign Up / Login"
    nvidia["form"] = ["businessEmail"]
    nvidia["values"] = {"businessEmail": profile.get("work_email")}
    nvidia["application_form"] = "nej"
    nvidia["assess"] = {
        "source": "https://programs.nvidia.com/phoenix/application",
        "questions": [
            "En utvecklare och en företagsledare, med varsitt yrkesmejl.",
            "Yrkesmejl på egen domän. Inte alias och inte gmail.",
            "Minst en utvecklare, en sajt, bolag, yngre än tio år.",
        ],
        "after": "Inget belopp på sidan. Sign Up / Login klickas inte.",
    }
    nvidia["actions"] = actions(nvidia["fill_url"], nvidia["values"], "Sign Up / Login")
    claude = door_packet(
        "Claude Startups",
        "https://claude.com/programs/startups",
        "Sidan tar inte emot nya ansökningar. Hämta den igen innan du säger att den är öppen.",
        [
            slot(profile, "age_years", "ålder"),
            slot(profile, "has_work_email", "yrkesmejl"),
            slot(profile, "has_website", "sajt"),
        ],
    )
    claude["fill"] = "nej"
    claude["gate"] = "kohorten är full"
    claude["form"] = []
    claude["application_form"] = "nej"
    claude["actions"] = [{"do": "open", "url": claude["link"]}, {"do": "stop", "before": "ansökan"}]
    facts = []
    if profile.get("legal_form") == "ab":
        facts.append("Vi är ett aktiebolag.")
    if profile.get("age_years") is not None:
        facts.append(f"Bolaget är {profile['age_years']} år.")
    if profile.get("employees") is not None:
        facts.append(f"Vi är {profile['employees']} personer.")
    draft = "\n".join(["Hej,", "", "Vi ber er peka vilken call som passar.", *facts])
    factory = {
        "door": "Sweden AI Factory",
        "link": FACTORY,
        "fill": "ja",
        "submit": "nej",
        "gate": "utkast",
        "application_form": "nej",
        "draft": draft,
        "actions": [
            {"do": "draft", "to": "info@swedenaifactory.se", "body": draft},
            {"do": "stop", "before": "skicka"},
        ],
    }
    json.dump(
        {
            "mcp": "nej",
            "host": {
                "claude": "browser, inte desktop-computer-use",
                "cursor": "cursor-ide-browser",
                "codex": "värdens browser",
            },
            "submit": "nej",
            "why": "Aktören har inget skicka-API. Paketet fylls i värdens browser. Inloggningen och sista klicket sitter hos den som äger kontot.",
            "doors": [playground, vinnova, nvidia, claude, factory],
        },
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")


def main():
    profile = json.load(sys.stdin)
    if profile.get("view") == "packet":
        packet(profile)
        return
    if profile.get("need") == "both":
        if not (profile.get("country") or "").strip():
            chance(dict(profile, need="gpu"))
            return
        import io
        from contextlib import redirect_stdout
        answers = []
        for need in ("gpu", "money"):
            buf = io.StringIO()
            with redirect_stdout(buf):
                chance(dict(profile, need=need))
            answers.append(json.loads(buf.getvalue()))
        json.dump({"answers": answers}, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return
    if profile.get("view") == "matrix":
        matrix(profile)
        return
    if profile.get("view") == "chance":
        chance(profile)
        return
    need = profile.get("need")
    if need == "money":
        money(profile)
    elif need == "gpu":
        gpu(profile)
    elif need == "credits":
        credits(profile)
    else:
        emit(
            "Inget ännu",
            "Säg om det är pengar, GPU-timmar eller cloud-krediter.",
            ["need"],
            "låg",
            BLOG,
            "Ett behov, en dörr.",
            [BLOG],
        )


if __name__ == "__main__":
    main()
