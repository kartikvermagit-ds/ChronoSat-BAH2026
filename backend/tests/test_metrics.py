import numpy as np

from backend.src.metrics.service import MetricsService


def test_metrics_report_contains_expected_keys():
    service = MetricsService()
    first = np.array([[0, 1], [2, 3]], dtype=np.float32)
    second = np.array([[0, 1], [2, 4]], dtype=np.float32)

    report = service.generate_report(first, second)

    assert set(report.keys()) == {"mse", "psnr", "ssim"}


def test_metrics_are_perfect_for_identical_arrays():
    service = MetricsService()
    first = np.ones((4, 4), dtype=np.float32)
    second = np.ones((4, 4), dtype=np.float32)

    report = service.generate_report(first, second)

    assert report["mse"] == 0.0
    assert report["ssim"] == 1.0
