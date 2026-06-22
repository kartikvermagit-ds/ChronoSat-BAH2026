from __future__ import annotations

from datetime import datetime, timezone


def build_demo_payload(satellite: str, generated_frames: int) -> dict[str, object]:
    return {
        "satellite": satellite,
        "generated_frames": generated_frames,
        "requested_at": datetime.now(timezone.utc).isoformat(),
    }


def chunk_values(values: list[float], size: int) -> list[list[float]]:
    return [values[index : index + size] for index in range(0, len(values), size)]
