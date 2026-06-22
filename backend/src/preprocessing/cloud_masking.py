from __future__ import annotations


def build_cloud_mask(pixels: list[float], threshold: float = 0.7) -> list[int]:
    return [1 if pixel >= threshold else 0 for pixel in pixels]
