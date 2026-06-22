from pathlib import Path


def main() -> None:
    for path in [
        Path("data/raw/goes-19"),
        Path("data/raw/insat-3ds"),
        Path("data/raw/himawari-8"),
    ]:
        path.mkdir(parents=True, exist_ok=True)
    print("Dataset folders are ready.")


if __name__ == "__main__":
    main()
