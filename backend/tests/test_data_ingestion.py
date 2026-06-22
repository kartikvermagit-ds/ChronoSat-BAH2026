from pathlib import Path

from backend.src.data_ingestion.goes_downloader import fetch_latest_goes_frames


def test_fetch_latest_goes_frames_returns_expected_count(tmp_path: Path):
    frames = fetch_latest_goes_frames(tmp_path, count=3)
    assert len(frames) == 3
    assert all(frame.local_path.parent == tmp_path for frame in frames)
