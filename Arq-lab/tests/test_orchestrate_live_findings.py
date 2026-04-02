from __future__ import annotations

from tooling.orchestrate import _is_live_finding


def test_is_live_finding_keeps_active_history_only_findings() -> None:
    finding = {
        "detectionState": "ACTIVE",
        "presentOnHead": False,
        "presentInHistory": True,
        "detail": {
            "detectionState": "ACTIVE",
            "presentOnHead": False,
            "presentInHistory": True,
        },
    }

    assert _is_live_finding(finding) is True


def test_is_live_finding_drops_resolved_findings_even_if_exported() -> None:
    finding = {
        "detectionState": "RESOLVED",
        "resolvedAt": "2026-04-02T02:38:30Z",
        "detail": {
            "detectionState": "RESOLVED",
            "resolvedAt": "2026-04-02T02:38:30Z",
            "presentOnHead": False,
        },
    }

    assert _is_live_finding(finding) is False
