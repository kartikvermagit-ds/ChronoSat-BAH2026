from __future__ import annotations

from datetime import datetime, timezone


def build_metadata(satellite: str, generated_frames: int, method: str) -> dict[str, object]:
    return {
        "satellite": satellite,
        "generated_frames": generated_frames,
        "method": method,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
