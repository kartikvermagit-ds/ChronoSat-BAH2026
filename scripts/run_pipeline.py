from backend.src.interpolation.rife_engine import synthesize_with_rife
from backend.src.postprocessing.consistency_checker import temporal_consistency_score
from backend.src.utils.constants import DEFAULT_PIXEL_SERIES


def main() -> None:
    end_pixels = [value + 0.15 for value in DEFAULT_PIXEL_SERIES]
    generated = synthesize_with_rife(DEFAULT_PIXEL_SERIES, end_pixels, steps=3)
    score = temporal_consistency_score(
        [DEFAULT_PIXEL_SERIES, *[frame.pixels for frame in generated], end_pixels]
    )
    print(f"Generated {len(generated)} frames with consistency score {score}")


if __name__ == "__main__":
    main()
