from __future__ import annotations

from pathlib import Path

from .preview_generator import PreviewGenerator
from .satellite_reader import SatelliteDataReader


def sample_processing_workflow(file_path: Path, preview_output_path: Path) -> dict[str, object]:
    reader = SatelliteDataReader()
    preview_generator = PreviewGenerator()
    frame = reader.read(file_path)
    preview_path = preview_generator.save_preview(frame.array, preview_output_path)
    return {
        "filename": frame.filename,
        "file_type": frame.file_type,
        "band_name": frame.band_name,
        "shape": list(frame.array.shape),
        "preview_path": str(preview_path),
    }
