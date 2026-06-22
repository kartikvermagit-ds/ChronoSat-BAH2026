from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(slots=True)
class ValidationResult:
    is_valid: bool
    missing_files: list[str]
    warnings: list[str]


def validate_scene_files(paths: Iterable[Path]) -> ValidationResult:
    path_list = list(paths)
    missing = [str(path) for path in path_list if not path.exists()]
    warnings: list[str] = []
    if len(missing) == 0 and len(path_list) < 2:
        warnings.append("Interpolation performs best with at least two anchor frames.")
    return ValidationResult(is_valid=not missing, missing_files=missing, warnings=warnings)
