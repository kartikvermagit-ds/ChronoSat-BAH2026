from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class UploadedAsset:
    filename: str
    content_type: str
    size_bytes: int
    saved_path: Path
    preview_image: str | None = None
    uploaded_at: datetime = field(default_factory=utc_now)


@dataclass(slots=True)
class InterpolationJob:
    source_files: list[str]
    status: str = "queued"
    job_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=utc_now)


@dataclass(slots=True)
class InterpolationResult:
    job_id: str
    source_files: list[str]
    output_frames: list[str]
    preview_images: list[str]
    metrics: dict[str, float]
    preview_url: str
    satellite_source: str | None = None
    status: str = "completed"
    message: str = "Mock interpolation complete. RIFE integration will be added later."
    created_at: datetime = field(default_factory=utc_now)
