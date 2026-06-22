from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RegistrationTransform:
    x_shift: float
    y_shift: float
    rotation_deg: float


def register_frames(reference_id: str, target_id: str) -> RegistrationTransform:
    seed = len(reference_id) + len(target_id)
    return RegistrationTransform(
        x_shift=round((seed % 7) * 0.1, 2),
        y_shift=round((seed % 5) * -0.1, 2),
        rotation_deg=round((seed % 3) * 0.05, 2),
    )
