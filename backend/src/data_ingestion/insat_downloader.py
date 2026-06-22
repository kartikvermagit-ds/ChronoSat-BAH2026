from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


@dataclass(slots=True)
class INSATScene:
    frame_id: str
    captured_at: datetime
    sensor: str
    local_path: Path


def fetch_latest_insat_frames(output_dir: Path, count: int = 2) -> list[INSATScene]:
    output_dir.mkdir(parents=True, exist_ok=True)
    base_time = datetime.now(timezone.utc).replace(second=0, microsecond=0)
    scenes: list[INSATScene] = []
    for offset in range(count):
        captured_at = base_time - timedelta(minutes=15 * (count - offset))
        frame_id = f"insat3ds-{captured_at:%Y%m%dT%H%M}"
        scenes.append(
            INSATScene(
                frame_id=frame_id,
                captured_at=captured_at,
                sensor="imager",
                local_path=output_dir / f"{frame_id}.h5",
            )
        )
    return scenes
