from backend.src.postprocessing.consistency_checker import temporal_consistency_score


def test_temporal_consistency_score_is_bounded():
    score = temporal_consistency_score([[0.1, 0.2], [0.15, 0.25], [0.2, 0.3]])
    assert 0.0 <= score <= 1.0
