#!/usr/bin/env python3
"""Live round data for a Vinnova call from data.vinnova.se. Standard library only.

The open data API lists every application round of a call. This module finds
the round that is still open, or the newest closed one when none is open, so
the skill can quote a real closing date instead of a remembered one.

As a module:  open_round("2016-04714", datetime.now(timezone.utc))
As a script:  python3 scripts/vinnova_api.py 2016-04714
"""

from __future__ import annotations

import json
import sys
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone, tzinfo
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

CALL_URL = "https://data.vinnova.se/api/utlysningar/{}"
ROUND_URL = "https://data.vinnova.se/api/ansokningsomgangar/{}"
USER_AGENT = "opensverige-startup-krediter"
TIMEOUT_SECONDS = 30
try:
    STOCKHOLM: tzinfo = ZoneInfo("Europe/Stockholm")
except ZoneInfoNotFoundError:  # no tz database on this machine; dates then read as UTC, at most two hours off
    STOCKHOLM = timezone.utc


@dataclass(frozen=True)
class Round:
    dnr: str
    title: str
    closes: datetime
    opens: datetime | None
    apply_url: str | None
    open_now: bool

    def to_dict(self) -> dict:
        return {
            "dnr": self.dnr,
            "title": self.title,
            "closes": self.closes.isoformat(),
            "opens": self.opens.isoformat() if self.opens else None,
            "open_now": self.open_now,
            "apply_url": self.apply_url,
        }


def fetch_json(url: str) -> dict:
    """GET a Vinnova API url. The API wraps single objects in a one-item list."""
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        data = json.load(response)
    return data[0] if isinstance(data, list) else data


def parse_stamp(raw: str) -> datetime:
    """The API gives Swedish wall-clock time without a zone; read it as Europe/Stockholm."""
    stamp = datetime.fromisoformat(raw)
    return stamp if stamp.tzinfo else stamp.replace(tzinfo=STOCKHOLM)


def first_link(row: dict) -> str | None:
    for link in row.get("LankLista") or []:
        if link.get("URL"):
            return str(link["URL"])
    return None


def open_round(call_id: str, now: datetime, fetch: Callable[[str], dict] = fetch_json) -> Round | None:
    """The newest round that has not closed (open now, or announced), else the newest closed round, else None.

    Round numbers are YYYY-NNNNN, so sorting them descending walks from the
    newest regardless of the order the API lists them. Each round is one
    request; the loop stops at the first round that has not closed.
    """
    call = fetch(CALL_URL.format(call_id))
    ids = sorted((row["DiarienummerAnsokningsomgang"] for row in call.get("AnsokningsomgangDnrLista") or []), reverse=True)
    newest_closed: Round | None = None
    for dnr in ids:
        row = fetch(ROUND_URL.format(dnr))
        close = row.get("Stangningsdatum")
        if not close:
            continue
        closes = parse_stamp(close)
        opening = row.get("Oppningsdatum")
        opens = parse_stamp(opening) if opening else None
        found = Round(
            dnr=str(row.get("Diarienummer") or dnr),
            title=str(row.get("Titel") or ""),
            closes=closes,
            opens=opens,
            apply_url=first_link(row),
            open_now=(opens is None or opens <= now) and now <= closes,
        )
        if closes >= now:
            return found
        if newest_closed is None:
            newest_closed = found
    return newest_closed


def main(argv: list[str]) -> int:
    call_id = argv[1] if len(argv) > 1 else "2016-04714"
    found = open_round(call_id, datetime.now(timezone.utc))
    json.dump(found.to_dict() if found else None, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
