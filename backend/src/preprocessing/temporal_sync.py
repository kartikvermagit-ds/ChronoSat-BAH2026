from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class TimeAlignment:
    reference_time: datetime
    target_time: datetime
    delta_seconds: int


def synchronize_timestamps(reference_time: datetime, target_time: datetime) -> TimeAlignment:
    return TimeAlignment(
        reference_time=reference_time,
        target_time=target_time,
        delta_seconds=int((target_time - reference_time).total_seconds()),
    )
