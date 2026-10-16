"""Tests for scripts/vinnova_api.py against recorded API responses. No network."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import vinnova_api

FIXTURES = Path(__file__).parent / "fixtures"
CALL = json.loads((FIXTURES / "vinnova_call.json").read_text(encoding="utf-8"))
ROUND = json.loads((FIXTURES / "vinnova_round.json").read_text(encoding="utf-8"))
CALL_ID = "2016-04714"
LATEST_DNR = "2025-04831"


def first(data: object) -> dict:
    return data[0] if isinstance(data, list) else data


def fake_fetch(url: str) -> dict:
    """Serve the recorded call and the recorded newest round; synthesize older rounds as closed."""
    if url == vinnova_api.CALL_URL.format(CALL_ID):
        return first(CALL)
    prefix = vinnova_api.ROUND_URL.format("")
    assert url.startswith(prefix), f"unexpected url {url}"
    dnr = url[len(prefix):]
    if dnr == LATEST_DNR:
        return first(ROUND)
    return {"Diarienummer": dnr, "Titel": f"Old round {dnr}", "Stangningsdatum": "2020-01-01T14:00:00", "LankLista": []}


def test_picks_round_closing_after_now() -> None:
    now = datetime(2026, 10, 15, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fake_fetch)
    assert found is not None
    assert found.dnr == LATEST_DNR
    assert found.closes == datetime(2027, 1, 12, 14, 0, tzinfo=ZoneInfo("Europe/Stockholm"))
    assert found.open_now is True
    assert "Innovativa Startups" in found.title
    assert found.apply_url is not None and found.apply_url.startswith("https://ansok.vinnova.se")


def test_returns_newest_when_all_closed() -> None:
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fake_fetch)
    assert found is not None
    assert found.dnr == LATEST_DNR


def test_returns_none_when_no_rounds() -> None:
    def empty_fetch(url: str) -> dict:
        return {"Diarienummer": CALL_ID, "AnsokningsomgangDnrLista": []}

    now = datetime(2026, 10, 15, tzinfo=timezone.utc)
    assert vinnova_api.open_round(CALL_ID, now, fetch=empty_fetch) is None


def test_skips_rounds_without_close_date() -> None:
    def fetch(url: str) -> dict:
        if url == vinnova_api.CALL_URL.format(CALL_ID):
            return {
                "Diarienummer": CALL_ID,
                "AnsokningsomgangDnrLista": [
                    {"DiarienummerAnsokningsomgang": "2019-00001"},
                    {"DiarienummerAnsokningsomgang": "2026-99999"},
                ],
            }
        if url.endswith("2026-99999"):
            return {"Diarienummer": "2026-99999", "Titel": "No close date yet", "LankLista": []}
        return {"Diarienummer": "2019-00001", "Titel": "Closed", "Stangningsdatum": "2019-06-01T14:00:00", "LankLista": []}

    now = datetime(2026, 10, 15, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fetch)
    assert found is not None
    assert found.dnr == "2019-00001"


def test_round_to_dict_is_json_ready() -> None:
    now = datetime(2026, 10, 15, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fake_fetch)
    assert found is not None
    payload = found.to_dict()
    assert payload["dnr"] == LATEST_DNR
    assert payload["closes"] == "2027-01-12T14:00:00+01:00"
    assert payload["opens"] == "2026-10-12T00:00:00+02:00"
    assert payload["open_now"] is True
    json.dumps(payload)


def test_round_announced_but_not_yet_open_is_not_open_now() -> None:
    now = datetime(2026, 10, 1, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fake_fetch)
    assert found is not None
    assert found.dnr == LATEST_DNR
    assert found.open_now is False


def test_newest_round_found_even_when_api_lists_newest_first() -> None:
    def fetch(url: str) -> dict:
        if url == vinnova_api.CALL_URL.format(CALL_ID):
            return {"Diarienummer": CALL_ID, "AnsokningsomgangDnrLista": [
                {"DiarienummerAnsokningsomgang": LATEST_DNR},
                {"DiarienummerAnsokningsomgang": "2016-04743"},
            ]}
        return fake_fetch(url)

    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    found = vinnova_api.open_round(CALL_ID, now, fetch=fetch)
    assert found is not None
    assert found.dnr == LATEST_DNR
