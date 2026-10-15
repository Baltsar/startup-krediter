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


def test_probe_returns_zero_on_malformed_http_response(monkeypatch: object) -> None:
    import http.client

    def boom(request: object, timeout: float) -> object:
        raise http.client.BadStatusLine("garbage")

    monkeypatch.setattr(check_links.urllib.request, "urlopen", boom)  # type: ignore[attr-defined]
    assert check_links.probe("https://example.org/") == 0


# --- body of a bot-blocked response -----------------------------------------


def test_classify_body_tells_empty_waf_not_found_and_page_apart() -> None:
    assert check_links.classify_body(None) == "unreachable"
    assert check_links.classify_body("") == "empty"
    assert check_links.classify_body("  \n\t ") == "empty"
    assert check_links.classify_body("<html><title>Just a moment...</title><div id='cf-browser-verification'>") == "waf"
    assert check_links.classify_body("<html><h1>Access Denied</h1>You don't have permission to access this page") == "waf"
    assert check_links.classify_body("<html><title>Pardon Our Interruption</title>") == "waf"
    assert check_links.classify_body("<html><title>Page not found | Innovasjon Norge</title>") == "not-found"
    assert check_links.classify_body("<html><h1>Sidan hittades inte</h1>") == "not-found"
    assert check_links.classify_body("<html><h1>Startup grant 1</h1><p>The grant can cover up to 100% of invoiced costs.</p>") == "page"


def test_check_fetches_the_body_only_for_bot_blocked_urls() -> None:
    records = [{"id": "a", "status_url": "https://example.org/blocked", "apply_url": "https://example.org/fine"}]
    fetched: list[str] = []

    def body(url: str) -> str | None:
        fetched.append(url)
        return "<html><title>Just a moment...</title>"

    results = check_links.check(records, lambda url: 403 if url.endswith("blocked") else 200, body)
    assert fetched == ["https://example.org/blocked"]
    assert [(r.status, r.body) for r in results] == [("blocks-bot", "waf"), ("ok", "")]
    assert check_links.exit_code(results) == 0


def test_check_without_a_body_fetcher_leaves_body_blank() -> None:
    records = [{"id": "a", "status_url": "https://example.org/blocked", "apply_url": "mailto:x@example.org"}]
    results = check_links.check(records, lambda url: 403)
    assert results[0].status == "blocks-bot"
    assert results[0].body == ""


def test_fetch_body_returns_the_body_of_an_http_error(monkeypatch: object) -> None:
    import io
    import urllib.error

    def refuse(request: object, timeout: float) -> object:
        raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, io.BytesIO(b"<html>Access Denied</html>"))  # type: ignore[attr-defined]

    monkeypatch.setattr(check_links.urllib.request, "urlopen", refuse)  # type: ignore[attr-defined]
    assert check_links.fetch_body("https://example.org/") == "<html>Access Denied</html>"


def test_fetch_body_returns_none_when_nothing_answers(monkeypatch: object) -> None:
    import urllib.error

    def drop(request: object, timeout: float) -> object:
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(check_links.urllib.request, "urlopen", drop)  # type: ignore[attr-defined]
    monkeypatch.setattr(check_links, "fetch_body_curl", lambda url: None)  # type: ignore[attr-defined]
    assert check_links.fetch_body("https://example.org/") is None
