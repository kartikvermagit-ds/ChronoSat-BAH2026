from __future__ import annotations

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from ..application.services import ChronoSatService
from .dependencies import get_chronosat_service
from .schemas import (
    FileListResponse,
    HealthResponse,
    InterpolationRequest,
    InterpolationResponse,
    ResultsResponse,
    UploadResponse,
    UploadedFileResponse,
)

router = APIRouter()


def _to_uploaded_file_response(file_info) -> UploadedFileResponse:
    return UploadedFileResponse(
        filename=file_info.filename,
        content_type=file_info.content_type,
        size_bytes=file_info.size_bytes,
        saved_path=str(file_info.saved_path),
        preview_image=file_info.preview_image,
        uploaded_at=file_info.uploaded_at,
    )


def _to_interpolation_response(result) -> InterpolationResponse:
    return InterpolationResponse(
        job_id=result.job_id,
        status=result.status,
        source_files=result.source_files,
        output_frames=result.output_frames,
        preview_images=result.preview_images,
        metrics=result.metrics,
        satellite_source=result.satellite_source,
        preview_url=result.preview_url,
        message=result.message,
        created_at=result.created_at,
    )


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", message="ChronoSat backend is healthy.")


@router.post("/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_files(
    files: list[UploadFile] = File(...),
    service: ChronoSatService = Depends(get_chronosat_service),
) -> UploadResponse:
    try:
        uploaded = await service.upload_files(files)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error

    return UploadResponse(files=[_to_uploaded_file_response(item) for item in uploaded])


@router.get("/files", response_model=FileListResponse)
def list_files(
    service: ChronoSatService = Depends(get_chronosat_service),
) -> FileListResponse:
    files = service.list_files()
    return FileListResponse(files=[_to_uploaded_file_response(item) for item in files])


@router.post("/interpolate", response_model=InterpolationResponse, status_code=status.HTTP_202_ACCEPTED)
def start_interpolation(
    request: InterpolationRequest,
    service: ChronoSatService = Depends(get_chronosat_service),
) -> InterpolationResponse:
    try:
        result = service.start_interpolation(
            request.source_files,
            request.output_format,
            request.satellite_source,
        )
    except FileNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
    return _to_interpolation_response(result)


@router.get("/results", response_model=ResultsResponse)
def list_results(
    service: ChronoSatService = Depends(get_chronosat_service),
) -> ResultsResponse:
    results = service.list_results()
    return ResultsResponse(results=[_to_interpolation_response(item) for item in results])
