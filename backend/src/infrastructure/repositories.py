from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from fastapi import UploadFile

from ..domain.models import InterpolationJob, InterpolationResult, UploadedAsset


class FileRepository:
    def __init__(self, upload_root: Path, preview_root: Path) -> None:
        self.upload_root = upload_root
        self.preview_root = preview_root
        self.upload_root.mkdir(parents=True, exist_ok=True)
        self.preview_root.mkdir(parents=True, exist_ok=True)

    async def save_upload(self, file: UploadFile) -> UploadedAsset:
        file_path = self.upload_root / (file.filename or "unnamed-file")
        content = await file.read()
        file_path.write_bytes(content)
        return UploadedAsset(
            filename=file_path.name,
            content_type=file.content_type or "application/octet-stream",
            size_bytes=len(content),
            saved_path=file_path,
        )

    def list_uploads(self) -> list[UploadedAsset]:
        uploads: list[UploadedAsset] = []
        for path in sorted(self.upload_root.iterdir()):
            if not path.is_file():
                continue
            uploads.append(
                UploadedAsset(
                    filename=path.name,
                    content_type="application/octet-stream",
                    size_bytes=path.stat().st_size,
                    saved_path=path,
                    preview_image=self._preview_name_for(path),
                    uploaded_at=datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc),
                )
            )
        return uploads

    def _preview_name_for(self, path: Path) -> str | None:
        preview_name = f"{path.stem}_input_preview.png"
        preview_path = self.preview_root / preview_name
        return preview_name if preview_path.exists() else None


class JobRepository:
    def __init__(self) -> None:
        self._jobs: dict[str, InterpolationJob] = {}
        self._results: dict[str, InterpolationResult] = {}

    def save_job(self, job: InterpolationJob) -> None:
        self._jobs[job.job_id] = job

    def save_result(self, result: InterpolationResult) -> None:
        self._results[result.job_id] = result

    def list_results(self) -> list[InterpolationResult]:
        return list(self._results.values())
