from __future__ import annotations


def correct_atmospheric_haze(pixels: list[float], correction_strength: float = 0.02) -> list[float]:
    return [round(max(pixel - correction_strength, 0.0), 4) for pixel in pixels]
