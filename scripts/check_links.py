#!/usr/bin/env python3
"""Probe every status_url and apply_url in data/programs.json. Standard library only.

    python3 scripts/check_links.py [path/to/programs.json]

Prints one line per URL: <status> <code> <id> <url>. Exit 1 when any link is
dead (connection failure, 404, 410, 5xx). A 401, 403, 429, 454 or 455 is reported as
blocks-bot and does not fail the run: those sites refuse automated clients and
were read in a browser when the record was verified. For a blocks-bot URL the
line also says what the GET body carried (body: empty, waf, not-found, page or
unreachable), so a page removed behind a WAF shows up as not-found instead of
hiding behind the 403. mailto: links are skipped.
"""

from __future__ import annotations

import http.client
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS_PATH = ROOT / "data" / "programs.json"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
TIMEOUT_SECONDS = 15
BOT_BLOCK_CODES = {401, 403, 429, 454, 455}
BODY_LIMIT_BYTES = 256 * 1024
# Phrases the common WAF and bot-challenge pages carry (Cloudflare, Akamai, Imperva, generic deny pages).
WAF_MARKERS = (
    "just a moment", "cf-browser-verification", "cf-chl", "challenge-platform", "attention required",
    "access denied", "pardon our interruption", "request blocked", "enable javascript and cookies",
    "incapsula", "imperva", "akamai", "captcha", "verify you are human", "bot detection",
)
# Not-found phrases in the languages of the sites the data covers, plus a bare 404.
NOT_FOUND_MARKERS = (
    "page not found", "not found", "sidan hittades inte", "sidan kunde inte hittas", "sidan finns inte",
    "siden finnes ikke", "siden ble ikke funnet", "siden blev ikke fundet", "sivua ei löytynyt", "síðan fannst ekki",
)


@dataclass(frozen=True)
class Result:
    status: str
    code: int
    id: str
    url: str
    body: str = ""


def classify(code: int) -> str:
    if code in BOT_BLOCK_CODES:
        return "blocks-bot"
    if 200 <= code < 400:
        return "ok"
    return "dead"


def probe(url: str) -> int:
    """HEAD first; fall back to GET when the server rejects HEAD. 0 means no HTTP response at all."""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                return int(response.status)
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 400):
                continue
            return int(exc.code)
        except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException):
            return 0
    return 0


def probe_curl(url: str) -> int:
    """Second opinion through curl. Some CDNs refuse Python's TLS client outright but answer curl."""
    if shutil.which("curl") is None:
        return 0
    done = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-time", str(TIMEOUT_SECONDS), "-A", USER_AGENT, url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        return int(done.stdout.strip() or "0")
    except ValueError:
        return 0


def classify_body(body: str | None) -> str:
    """What a bot-blocked response actually carried: nothing, a WAF challenge, a not-found page, or a real page."""
    if body is None:
        return "unreachable"
    if not body.strip():
        return "empty"
    lowered = body.lower()
    if any(marker in lowered for marker in WAF_MARKERS):
        return "waf"
    if any(marker in lowered for marker in NOT_FOUND_MARKERS) or re.search(r"\b404\b", lowered):
        return "not-found"
    return "page"


def fetch_body(url: str) -> str | None:
    """GET the page text, also for an error status: a 403 body tells a WAF page from a removed page. None when nothing answers."""
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return response.read(BODY_LIMIT_BYTES).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.read(BODY_LIMIT_BYTES).decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException):
        return fetch_body_curl(url)


def fetch_body_curl(url: str) -> str | None:
    """Second opinion through curl, as for probe_curl. None when curl is missing or gets no response."""
    if shutil.which("curl") is None:
        return None
    done = subprocess.run(
        ["curl", "-s", "-L", "--max-time", str(TIMEOUT_SECONDS), "-A", USER_AGENT, url],
        capture_output=True,
        text=True,
        errors="replace",
        check=False,
    )
    return done.stdout if done.returncode == 0 else None


def probe_with_fallback(url: str, primary: Callable[[str], int], secondary: Callable[[str], int]) -> int:
    """Use the secondary prober only when the primary got no HTTP response at all."""
    code = primary(url)
    return secondary(url) if code == 0 else code


def check(
    records: list[dict],
    prober: Callable[[str], int],
    body_fetcher: Callable[[str], str | None] | None = None,
) -> list[Result]:
    """Probe each distinct http(s) URL once, in record order, status_url before apply_url. Bot-blocked URLs also get their body read."""
    results: list[Result] = []
    seen: set[str] = set()
    for record in records:
        for key in ("status_url", "apply_url"):
            url = str(record.get(key) or "")
            if not url.startswith(("http://", "https://")) or url in seen:
                continue
            seen.add(url)
            code = prober(url)
            status = classify(code)
            body = classify_body(body_fetcher(url)) if status == "blocks-bot" and body_fetcher is not None else ""
            results.append(Result(status, code, str(record.get("id", "")), url, body))
    return results


def exit_code(results: list[Result]) -> int:
    return 1 if any(result.status == "dead" for result in results) else 0


def main(argv: list[str]) -> int:
    programs_path = Path(argv[1]) if len(argv) > 1 else PROGRAMS_PATH
    records = json.loads(programs_path.read_text(encoding="utf-8"))["programs"]
    results = check(records, lambda url: probe_with_fallback(url, probe, probe_curl), fetch_body)
    for result in results:
        suffix = f"  body: {result.body}" if result.body else ""
        print(f"{result.status:10} {result.code:3} {result.id:32} {result.url}{suffix}")
    dead = [result for result in results if result.status == "dead"]
    blocked = [result for result in results if result.status == "blocks-bot"]
    print(f"{len(results)} url(s): {len(results) - len(dead) - len(blocked)} ok, {len(blocked)} blocks-bot, {len(dead)} dead")
    return exit_code(results)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
