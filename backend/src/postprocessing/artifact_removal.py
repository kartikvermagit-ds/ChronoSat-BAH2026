from __future__ import annotations


def smooth_artifacts(pixels: list[float], weight: float = 0.15) -> list[float]:
    if len(pixels) < 3:
        return pixels
    smoothed = [pixels[0]]
    for left, center, right in zip(pixels, pixels[1:], pixels[2:]):
        adjusted = center * (1 - weight) + ((left + right) / 2) * weight
        smoothed.append(round(adjusted, 4))
    smoothed.append(pixels[-1])
    return smoothed
