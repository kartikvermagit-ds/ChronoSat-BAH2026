from __future__ import annotations

import math

import numpy as np


class MetricsService:
    def mean_squared_error(self, first: np.ndarray, second: np.ndarray) -> float:
        left, right = self._prepare_arrays(first, second)
        return float(np.mean((left - right) ** 2))

    def peak_signal_to_noise_ratio(self, first: np.ndarray, second: np.ndarray) -> float:
        mse = self.mean_squared_error(first, second)
        if mse == 0:
            return float("inf")
        left, _ = self._prepare_arrays(first, second)
        max_pixel = float(np.max(left)) if np.max(left) > 0 else 1.0
        return float(20 * math.log10(max_pixel) - 10 * math.log10(mse))

    def structural_similarity_index(self, first: np.ndarray, second: np.ndarray) -> float:
        left, right = self._prepare_arrays(first, second)
        c1 = 0.01**2
        c2 = 0.03**2

        mu_left = float(np.mean(left))
        mu_right = float(np.mean(right))
        sigma_left = float(np.var(left))
        sigma_right = float(np.var(right))
        covariance = float(np.mean((left - mu_left) * (right - mu_right)))

        numerator = (2 * mu_left * mu_right + c1) * (2 * covariance + c2)
        denominator = (mu_left**2 + mu_right**2 + c1) * (sigma_left + sigma_right + c2)
        if denominator == 0:
            return 1.0
        return float(numerator / denominator)

    def generate_report(self, first: np.ndarray, second: np.ndarray) -> dict[str, float]:
        return {
            "mse": round(self.mean_squared_error(first, second), 6),
            "psnr": round(self.peak_signal_to_noise_ratio(first, second), 6),
            "ssim": round(self.structural_similarity_index(first, second), 6),
        }

    def _prepare_arrays(self, first: np.ndarray, second: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        left = np.asarray(first, dtype=np.float32)
        right = np.asarray(second, dtype=np.float32)
        target_shape = tuple(min(a, b) for a, b in zip(left.shape, right.shape))
        if len(target_shape) != 2:
            raise ValueError("MetricsService expects 2D numpy arrays.")
        left = left[: target_shape[0], : target_shape[1]]
        right = right[: target_shape[0], : target_shape[1]]
        return left, right
