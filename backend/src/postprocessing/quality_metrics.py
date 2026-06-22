from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class QualityMetrics:
    mae: float
    temporal_consistency: float
    flow_magnitude: float


def mean_absolute_error(reference: list[float], candidate: list[float]) -> float:
    if len(reference) != len(candidate):
        raise ValueError("MAE comparison requires equal length vectors.")
    mae = sum(abs(left - right) for left, right in zip(reference, candidate)) / max(len(reference), 1)
    return round(mae, 4)
