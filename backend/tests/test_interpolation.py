from backend.src.interpolation.rife_engine import synthesize_with_rife


def test_rife_synthesizes_requested_steps():
    generated = synthesize_with_rife([0.0, 1.0], [1.0, 2.0], steps=2)
    assert [frame.timestep for frame in generated] == [0.333, 0.667]
