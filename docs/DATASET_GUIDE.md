# Dataset Guide

Use `data/raw/` to store source imagery grouped by satellite. Place calibrated outputs in `data/processed/calibrated/` and interpolated products in `data/processed/interpolated/`.

Recommended starter conventions:

- Keep timestamps in UTC.
- Preserve the original file names from providers.
- Store sidecar metadata as JSON for reproducibility.
