from __future__ import annotations

from .optical_flow import FlowVector


def blend_with_flow(start_pixels: list[float], end_pixels: list[float], flow: list[FlowVector], alpha: float) -> list[float]:
    blended: list[float] = []
    for start, end, vector in zip(start_pixels, end_pixels, flow):
        guided_target = end - (vector.dx * (1 - alpha) * 0.1)
        blended.append(round((start * (1 - alpha)) + (guided_target * alpha), 4))
    return blended
