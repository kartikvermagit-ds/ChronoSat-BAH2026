from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


@dataclass(slots=True)
class GOESScene:
    frame_id: str
    captured_at: datetime
    band: str
    local_path: Path


def fetch_latest_goes_frames(output_dir: Path, count: int = 2) -> list[GOESScene]:
    output_dir.mkdir(parents=True, exist_ok=True)
    base_time = datetime.now(timezone.utc).replace(second=0, microsecond=0)
    scenes: list[GOESScene] = []
    for offset in range(count):
        captured_at = base_time - timedelta(minutes=10 * (count - offset))
        frame_id = f"goes19-{captured_at:%Y%m%dT%H%M}"
        scenes.append(
            GOESScene(
                frame_id=frame_id,
                captured_at=captured_at,
                band="C13",
                local_path=output_dir / f"{frame_id}.nc",
            )
        )
    return scenes
