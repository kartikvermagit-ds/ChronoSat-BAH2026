from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str
    message: str


class UploadedFileResponse(BaseModel):
    filename: str
    content_type: str
    size_bytes: int
    saved_path: str
    preview_image: str | None = None
    uploaded_at: datetime


class UploadResponse(BaseModel):
    files: list[UploadedFileResponse]


class FileListResponse(BaseModel):
    files: list[UploadedFileResponse]


class InterpolationRequest(BaseModel):
    source_files: list[str] = Field(min_length=1)
    output_format: Literal["png", "jpg"] = "png"
    satellite_source: str | None = None


class MetricsReport(BaseModel):
    mse: float
    psnr: float
    ssim: float


class InterpolationResponse(BaseModel):
    job_id: str
    status: str
    source_files: list[str]
    output_frames: list[str]
    preview_images: list[str]
    metrics: MetricsReport
    satellite_source: str | None = None
    preview_url: str
    message: str
    created_at: datetime


class ResultsResponse(BaseModel):
    results: list[InterpolationResponse]
