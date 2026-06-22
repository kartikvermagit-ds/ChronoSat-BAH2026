# Architecture

ChronoSat is split into a lightweight FastAPI backend and a Vite + React frontend.

## Flow

1. Data ingestion modules describe how satellite frames would be fetched.
2. Preprocessing normalizes pixels, masks clouds, and aligns timestamps.
3. Interpolation modules estimate flow and synthesize missing frames.
4. Postprocessing smooths artifacts and reports quality metrics.
5. Output utilities serialize results for APIs or downstream exports.
