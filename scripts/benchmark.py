from time import perf_counter

from backend.src.interpolation.rife_engine import synthesize_with_rife


def main() -> None:
    start = perf_counter()
    synthesize_with_rife([0.1] * 128, [0.6] * 128, steps=5)
    elapsed_ms = (perf_counter() - start) * 1000
    print(f"Starter benchmark finished in {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
