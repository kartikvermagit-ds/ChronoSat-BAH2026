from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


@dataclass(slots=True)
class HimawariScene:
    frame_id: str
    captured_at: datetime
    resolution_km: float
    local_path: Path


def fetch_latest_himawari_frames(output_dir: Path, count: int = 2) -> list[HimawariScene]:
    output_dir.mkdir(parents=True, exist_ok=True)
    base_time = datetime.now(timezone.utc).replace(second=0, microsecond=0)
    scenes: list[HimawariScene] = []
    for offset in range(count):
        captured_at = base_time - timedelta(minutes=10 * (count - offset))
        frame_id = f"himawari8-{captured_at:%Y%m%dT%H%M}"
        scenes.append(
            HimawariScene(
                frame_id=frame_id,
                captured_at=captured_at,
                resolution_km=2.0,
                local_path=output_dir / f"{frame_id}.bz2",
            )
        )
    return scenes
