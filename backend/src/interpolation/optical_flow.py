from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class FlowVector:
    dx: float
    dy: float


def estimate_optical_flow(start_pixels: list[float], end_pixels: list[float]) -> list[FlowVector]:
    return [
        FlowVector(dx=round(end - start, 4), dy=round((end - start) / 2, 4))
        for start, end in zip(start_pixels, end_pixels)
    ]
