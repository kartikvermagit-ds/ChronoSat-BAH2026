from pathlib import Path

from backend.src.data_ingestion.workflow import sample_processing_workflow


def main() -> None:
    sample_path = Path("data/uploads/sample.nc")
    preview_path = Path("data/previews/sample_preview.png")
    if not sample_path.exists():
        print("Add a sample .nc or .h5 file to data/uploads/sample.nc before running.")
        return
    report = sample_processing_workflow(sample_path, preview_path)
    print(report)


if __name__ == "__main__":
    main()
