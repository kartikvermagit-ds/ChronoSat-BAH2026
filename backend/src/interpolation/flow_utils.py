from __future__ import annotations

from .optical_flow import FlowVector


def flow_magnitude(flow: list[FlowVector]) -> float:
    if not flow:
        return 0.0
    total = sum(abs(vector.dx) + abs(vector.dy) for vector in flow)
    return round(total / len(flow), 4)
