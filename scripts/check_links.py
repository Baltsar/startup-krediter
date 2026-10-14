#!/usr/bin/env python3
"""Probe every status_url and apply_url in data/programs.json. Standard library only.

    python3 scripts/check_links.py [path/to/programs.json]

Prints one line per URL: <status> <code> <id> <url>. Exit 1 when any link is
dead (connection failure, 404, 410, 5xx). A 401, 403, 429, 454 or 455 is reported as
blocks-bot and does not fail the run: those sites refuse automated clients and
were read in a browser when the record was verified. mailto: links are skipped.
"""

from __future__ import annotations

import json
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


@dataclass(frozen=True)
class Result:
    status: str
    code: int
    id: str
    url: str


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
        except (urllib.error.URLError, TimeoutError, OSError):
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


def probe_with_fallback(url: str, primary: Callable[[str], int], secondary: Callable[[str], int]) -> int:
    """Use the secondary prober only when the primary got no HTTP response at all."""
    code = primary(url)
    return secondary(url) if code == 0 else code


def check(records: list[dict], prober: Callable[[str], int]) -> list[Result]:
    """Probe each distinct http(s) URL once, in record order, status_url before apply_url."""
    results: list[Result] = []
    seen: set[str] = set()
    for record in records:
        for key in ("status_url", "apply_url"):
            url = str(record.get(key) or "")
            if not url.startswith(("http://", "https://")) or url in seen:
                continue
            seen.add(url)
            code = prober(url)
            results.append(Result(classify(code), code, str(record.get("id", "")), url))
    return results


def exit_code(results: list[Result]) -> int:
    return 1 if any(result.status == "dead" for result in results) else 0


def main(argv: list[str]) -> int:
    programs_path = Path(argv[1]) if len(argv) > 1 else PROGRAMS_PATH
    records = json.loads(programs_path.read_text(encoding="utf-8"))["programs"]
    results = check(records, lambda url: probe_with_fallback(url, probe, probe_curl))
    for result in results:
        print(f"{result.status:10} {result.code:3} {result.id:32} {result.url}")
    dead = [result for result in results if result.status == "dead"]
    blocked = [result for result in results if result.status == "blocks-bot"]
    print(f"{len(results)} url(s): {len(results) - len(dead) - len(blocked)} ok, {len(blocked)} blocks-bot, {len(dead)} dead")
    return exit_code(results)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
