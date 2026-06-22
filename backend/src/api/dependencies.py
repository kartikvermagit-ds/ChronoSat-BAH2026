from __future__ import annotations

from ..application.services import ChronoSatService
from ..config import settings
from ..data_ingestion.preview_generator import PreviewGenerator
from ..data_ingestion.satellite_reader import SatelliteDataReader
from ..infrastructure.repositories import FileRepository, JobRepository
from ..interpolation.service import InterpolationService
from ..metrics.service import MetricsService


def get_settings():
    return settings


_service = ChronoSatService(
    file_repository=FileRepository(settings.upload_root, settings.preview_root),
    job_repository=JobRepository(),
    satellite_reader=SatelliteDataReader(),
    preview_generator=PreviewGenerator(),
    metrics_service=MetricsService(),
    interpolation_service=InterpolationService(
        output_root=settings.preview_root,
        preview_generator=PreviewGenerator(),
    ),
)


def get_chronosat_service() -> ChronoSatService:
    return _service
