from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class InterpolatedFrame:
    frame_id: str
    timestep: float
    pixels: list[float]


def synthesize_with_rife(start_pixels: list[float], end_pixels: list[float], steps: int = 3) -> list[InterpolatedFrame]:
    if len(start_pixels) != len(end_pixels):
        raise ValueError("Anchor frames must have matching pixel counts.")

    frames: list[InterpolatedFrame] = []
    for index in range(1, steps + 1):
        timestep = index / (steps + 1)
        pixels = [
            round(start + ((end - start) * timestep), 4)
            for start, end in zip(start_pixels, end_pixels)
        ]
        frames.append(
            InterpolatedFrame(
                frame_id=f"interp-{index}",
                timestep=round(timestep, 3),
                pixels=pixels,
            )
        )
    return frames
