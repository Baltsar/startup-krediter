"""Tests for scripts/check_links.py with an injected prober. No network."""

from __future__ import annotations

import check_links


def test_classify_codes() -> None:
    assert check_links.classify(200) == "ok"
    assert check_links.classify(301) == "ok"
    assert check_links.classify(403) == "blocks-bot"
    assert check_links.classify(429) == "blocks-bot"
    assert check_links.classify(455) == "blocks-bot"
    assert check_links.classify(454) == "blocks-bot"
    assert check_links.classify(404) == "dead"
    assert check_links.classify(410) == "dead"
    assert check_links.classify(503) == "dead"
    assert check_links.classify(0) == "dead"


def test_check_skips_mailto_and_probes_each_url_once() -> None:
    records = [
        {"id": "a", "status_url": "https://example.org/a", "apply_url": "mailto:info@example.org"},
        {"id": "b", "status_url": "https://example.org/b", "apply_url": "https://example.org/b"},
        {"id": "c", "status_url": "https://example.org/c", "apply_url": "https://example.org/c/apply"},
    ]
    seen: list[str] = []

    def probe(url: str) -> int:
        seen.append(url)
        return 404 if url.endswith("/apply") else 200

    results = check_links.check(records, probe)
    assert seen == ["https://example.org/a", "https://example.org/b", "https://example.org/c", "https://example.org/c/apply"]
    assert [(r.status, r.code, r.id) for r in results] == [
        ("ok", 200, "a"),
        ("ok", 200, "b"),
        ("ok", 200, "c"),
        ("dead", 404, "c"),
    ]


def test_exit_code_is_one_only_for_dead_links() -> None:
    fine = [check_links.Result("ok", 200, "a", "https://x"), check_links.Result("blocks-bot", 403, "b", "https://y")]
    assert check_links.exit_code(fine) == 0
    dead = fine + [check_links.Result("dead", 404, "c", "https://z")]
    assert check_links.exit_code(dead) == 1


def test_probe_with_fallback_uses_secondary_only_when_primary_gets_no_response() -> None:
    calls: list[str] = []

    def primary(url: str) -> int:
        calls.append("primary")
        return 0

    def secondary(url: str) -> int:
        calls.append("secondary")
        return 200

    assert check_links.probe_with_fallback("https://x", primary, secondary) == 200
    assert calls == ["primary", "secondary"]
    calls.clear()
    assert check_links.probe_with_fallback("https://x", lambda url: 404, secondary) == 404
    assert calls == []
