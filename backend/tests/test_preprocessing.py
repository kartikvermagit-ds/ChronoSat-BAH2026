from backend.src.preprocessing.calibration import calibrate_frame


def test_calibration_applies_gain_and_bias():
    frame = calibrate_frame("f-1", [0.1, 0.2], gain=2.0, bias=0.1)
    assert frame.normalized_pixels == [0.3, 0.5]
