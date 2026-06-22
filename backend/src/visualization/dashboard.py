from __future__ import annotations


def build_dashboard_cards() -> list[dict[str, str]]:
    return [
        {"title": "Cadence Gap", "value": "10 min"},
        {"title": "Model", "value": "RIFE + Optical Flow"},
        {"title": "Primary Target", "value": "INSAT-3DS"},
    ]
