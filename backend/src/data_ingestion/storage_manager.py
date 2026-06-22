from __future__ import annotations

from pathlib import Path


class StorageManager:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def satellite_dir(self, satellite: str) -> Path:
        path = self.root / satellite
        path.mkdir(parents=True, exist_ok=True)
        return path

    def processed_dir(self, stage: str) -> Path:
        path = self.root / "processed" / stage
        path.mkdir(parents=True, exist_ok=True)
        return path
