from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ..data_ingestion.preview_generator import PreviewGenerator


@dataclass(slots=True)
class InterpolationArtifact:
    output_array: np.ndarray
    saved_frame_path: Path
    preview_path: Path


class MockRIFEEngine:
    def interpolate(self, first_frame: np.ndarray, second_frame: np.ndarray) -> np.ndarray:
        left, right = self._align(first_frame, second_frame)
        return ((left + right) / 2.0).astype(np.float32)

    def _align(self, first_frame: np.ndarray, second_frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        target_shape = tuple(min(a, b) for a, b in zip(first_frame.shape, second_frame.shape))
        if len(target_shape) != 2:
            raise ValueError("Interpolation expects 2D frame arrays.")
        return (
            first_frame[: target_shape[0], : target_shape[1]],
            second_frame[: target_shape[0], : target_shape[1]],
        )


class InterpolationService:
    def __init__(self, output_root: Path, preview_generator: PreviewGenerator, engine: MockRIFEEngine | None = None) -> None:
        self.output_root = output_root
        self.preview_generator = preview_generator
        self.engine = engine or MockRIFEEngine()
        self.output_root.mkdir(parents=True, exist_ok=True)

    def generate_intermediate_frame(
        self,
        first_frame: np.ndarray,
        second_frame: np.ndarray,
        job_id: str,
        output_format: str,
    ) -> InterpolationArtifact:
        interpolated = self.engine.interpolate(first_frame, second_frame)
        frame_path = self.output_root / f"{job_id}_frame.{output_format}"
        preview_path = self.output_root / f"{job_id}_preview.png"
        self.preview_generator.save_preview(interpolated, frame_path)
        self.preview_generator.save_preview(interpolated, preview_path)
        return InterpolationArtifact(
            output_array=interpolated,
            saved_frame_path=frame_path,
            preview_path=preview_path,
        )
