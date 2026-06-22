from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CalibratedFrame:
    frame_id: str
    gain: float
    bias: float
    normalized_pixels: list[float]


def calibrate_frame(frame_id: str, pixels: list[float], gain: float = 1.0, bias: float = 0.0) -> CalibratedFrame:
    normalized = [round((pixel * gain) + bias, 4) for pixel in pixels]
    return CalibratedFrame(frame_id=frame_id, gain=gain, bias=bias, normalized_pixels=normalized)
