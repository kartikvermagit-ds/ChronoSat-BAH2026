from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Settings:
    app_name: str = "ChronoSat"
    environment: str = os.getenv("CHRONOSAT_ENV", "development")
    data_root: Path = field(
        default_factory=lambda: Path(os.getenv("CHRONOSAT_DATA_ROOT", "data"))
    )
    output_root: Path = field(
        default_factory=lambda: Path(
            os.getenv("CHRONOSAT_OUTPUT_ROOT", "data/processed/interpolated")
        )
    )
    log_level: str = os.getenv("CHRONOSAT_LOG_LEVEL", "INFO")
    default_frame_gap_minutes: int = int(os.getenv("CHRONOSAT_FRAME_GAP_MINUTES", "10"))
    generated_frames: int = int(os.getenv("CHRONOSAT_GENERATED_FRAMES", "3"))
    upload_root: Path = field(
        default_factory=lambda: Path(os.getenv("CHRONOSAT_UPLOAD_ROOT", "data/uploads"))
    )
    preview_root: Path = field(
        default_factory=lambda: Path(os.getenv("CHRONOSAT_PREVIEW_ROOT", "data/previews"))
    )


settings = Settings()
