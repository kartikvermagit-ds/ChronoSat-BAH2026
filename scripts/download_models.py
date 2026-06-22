from pathlib import Path


def main() -> None:
    model_root = Path("models/checkpoints")
    model_root.mkdir(parents=True, exist_ok=True)
    placeholder = model_root / "README.txt"
    placeholder.write_text(
        "Place downloaded RIFE and optical-flow checkpoints here.\n",
        encoding="utf-8",
    )
    print(f"Prepared model directory at {placeholder.parent}")


if __name__ == "__main__":
    main()
