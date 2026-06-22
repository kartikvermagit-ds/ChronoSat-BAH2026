from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


class PreviewGenerator:
    def save_preview(self, array: np.ndarray, output_path: Path) -> Path:
        normalized = self._normalize(array)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(normalized, mode="L").save(output_path)
        return output_path

    def _normalize(self, array: np.ndarray) -> np.ndarray:
        data = np.asarray(array, dtype=np.float32)
        min_value = float(np.min(data))
        max_value = float(np.max(data))
        if max_value == min_value:
            return np.zeros_like(data, dtype=np.uint8)
        scaled = (data - min_value) / (max_value - min_value)
        return (scaled * 255).clip(0, 255).astype(np.uint8)
