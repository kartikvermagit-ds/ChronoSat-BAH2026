import pytest

fastapi = pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from backend.src.api.dependencies import get_chronosat_service
from backend.src.data_ingestion.preview_generator import PreviewGenerator
from backend.src.data_ingestion.satellite_reader import SatelliteDataReader
from backend.src.main import app
from backend.src.application.services import ChronoSatService
from backend.src.infrastructure.repositories import FileRepository, JobRepository
from backend.src.interpolation.service import InterpolationService
from backend.src.metrics.service import MetricsService


@pytest.fixture
def client(tmp_path):
    service = ChronoSatService(
        file_repository=FileRepository(tmp_path / "uploads", tmp_path / "previews"),
        job_repository=JobRepository(),
        satellite_reader=SatelliteDataReader(),
        preview_generator=PreviewGenerator(),
        metrics_service=MetricsService(),
        interpolation_service=InterpolationService(
            output_root=tmp_path / "previews",
            preview_generator=PreviewGenerator(),
        ),
    )
    app.dependency_overrides[get_chronosat_service] = lambda: service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_healthcheck(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_upload_and_list_files(client):
    response = client.post(
        "/upload",
        files=[
            ("files", ("sample.nc", b"netcdf-content", "application/x-netcdf")),
            ("files", ("sample.h5", b"hdf5-content", "application/x-hdf5")),
        ],
    )
    assert response.status_code == 201
    assert len(response.json()["files"]) == 2
    assert response.json()["files"][0]["preview_image"] is not None

    list_response = client.get("/files")
    assert list_response.status_code == 200
    assert [item["filename"] for item in list_response.json()["files"]] == [
        "sample.h5",
        "sample.nc",
    ]


def test_upload_rejects_invalid_extension(client):
    response = client.post(
        "/upload",
        files=[("files", ("bad.txt", b"not-allowed", "text/plain"))],
    )
    assert response.status_code == 400


def test_interpolate_and_results(client):
    client.post(
        "/upload",
        files=[("files", ("scene.nc", b"netcdf-content", "application/x-netcdf"))],
    )

    response = client.post(
        "/interpolate",
        json={"source_files": ["scene.nc", "scene2.nc"], "output_format": "png", "satellite_source": "insat-3ds"},
    )
    assert response.status_code == 404
    client.post(
        "/upload",
        files=[("files", ("scene2.nc", b"another-netcdf-content", "application/x-netcdf"))],
    )
    response = client.post(
        "/interpolate",
        json={"source_files": ["scene.nc", "scene2.nc"], "output_format": "png", "satellite_source": "insat-3ds"},
    )
    assert response.status_code == 202
    body = response.json()
    assert body["status"] == "completed"
    assert body["source_files"] == ["scene.nc", "scene2.nc"]
    assert set(body["metrics"].keys()) == {"mse", "psnr", "ssim"}
    assert len(body["preview_images"]) == 1

    results_response = client.get("/results")
    assert results_response.status_code == 200
    assert len(results_response.json()["results"]) == 1
