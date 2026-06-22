from __future__ import annotations


def temporal_consistency_score(frames: list[list[float]]) -> float:
    if len(frames) < 2:
        return 1.0
    deltas = []
    for previous, current in zip(frames, frames[1:]):
        drift = sum(abs(now - before) for before, now in zip(previous, current))
        deltas.append(drift / max(len(current), 1))
    score = max(0.0, 1.0 - (sum(deltas) / len(deltas)))
    return round(score, 4)
