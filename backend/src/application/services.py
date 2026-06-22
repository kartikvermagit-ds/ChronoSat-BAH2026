from __future__ import annotations

from pathlib import Path

from fastapi import UploadFile
import numpy as np

from ..data_ingestion.preview_generator import PreviewGenerator
from ..data_ingestion.satellite_reader import SatelliteDataReader
from ..domain.models import InterpolationJob, InterpolationResult, UploadedAsset
from ..infrastructure.repositories import FileRepository, JobRepository
from ..interpolation.service import InterpolationService
from ..metrics.service import MetricsService


class ChronoSatService:
    allowed_extensions = {".nc", ".h5"}
    max_frame_side = 512

    def __init__(
        self,
        file_repository: FileRepository,
        job_repository: JobRepository,
        satellite_reader: SatelliteDataReader,
        preview_generator: PreviewGenerator,
        metrics_service: MetricsService,
        interpolation_service: InterpolationService,
    ) -> None:
        self.file_repository = file_repository
        self.job_repository = job_repository
        self.satellite_reader = satellite_reader
        self.preview_generator = preview_generator
        self.metrics_service = metrics_service
        self.interpolation_service = interpolation_service

    async def upload_files(self, files: list[UploadFile]) -> list[UploadedAsset]:
        uploaded_assets: list[UploadedAsset] = []
        for file in files:
            extension = Path(file.filename or "").suffix.lower()
            if extension not in self.allowed_extensions:
                raise ValueError(
                    f"Unsupported file '{file.filename}'. Only .nc and .h5 files are allowed."
                )
            asset = await self.file_repository.save_upload(file)
            frame = self.satellite_reader.read(asset.saved_path)
            frame.array = self._downsample_frame(frame.array)
            preview_name = f"{asset.saved_path.stem}_input_preview.png"
            preview_path = self.interpolation_service.output_root / preview_name
            self.preview_generator.save_preview(frame.array, preview_path)
            asset.preview_image = preview_name
            uploaded_assets.append(asset)
        return uploaded_assets

    def list_files(self) -> list[UploadedAsset]:
        return self.file_repository.list_uploads()

    def start_interpolation(
        self,
        source_files: list[str],
        output_format: str,
        satellite_source: str | None,
    ) -> InterpolationResult:
        uploaded_assets = self.file_repository.list_uploads()
        available_files = {asset.filename for asset in uploaded_assets}
        missing_files = [filename for filename in source_files if filename not in available_files]
        if missing_files:
            raise FileNotFoundError(
                f"Interpolation cannot start. Missing uploaded files: {', '.join(missing_files)}"
            )

        asset_index = {asset.filename: asset for asset in uploaded_assets}
        selected_paths = [asset_index[name].saved_path for name in source_files]
        frames = [self.satellite_reader.read(path) for path in selected_paths[:2]]
        if len(frames) < 2:
            raise ValueError("At least two uploaded files are required to start interpolation.")
        frames = [
            type(frame)(
                filename=frame.filename,
                file_path=frame.file_path,
                file_type=frame.file_type,
                band_name=frame.band_name,
                array=self._downsample_frame(frame.array),
            )
            for frame in frames
        ]

        job = InterpolationJob(source_files=source_files, status="running")
        artifact = self.interpolation_service.generate_intermediate_frame(
            frames[0].array,
            frames[1].array,
            job.job_id,
            output_format,
        )
        report = self.metrics_service.generate_report(frames[0].array, frames[1].array)
        result = InterpolationResult(
            job_id=job.job_id,
            source_files=source_files,
            output_frames=[artifact.saved_frame_path.name],
            preview_images=[artifact.preview_path.name],
            metrics=report,
            satellite_source=satellite_source,
            preview_url=f"/results/{job.job_id}",
        )
        job.status = "completed"
        self.job_repository.save_job(job)
        self.job_repository.save_result(result)
        return result

    def list_results(self) -> list[InterpolationResult]:
        return self.job_repository.list_results()

    def _downsample_frame(self, array: np.ndarray) -> np.ndarray:
        if array.ndim != 2:
            raise ValueError("ChronoSat prototype expects 2D arrays for interpolation.")
        height, width = array.shape
        max_dim = max(height, width)
        if max_dim <= self.max_frame_side:
            return array
        stride = max(1, int(np.ceil(max_dim / self.max_frame_side)))
        return array[::stride, ::stride].astype(np.float32)
