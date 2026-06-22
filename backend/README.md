# Backend

This backend exposes the Phase 1 FastAPI service for ChronoSat.

## Run locally

```bash
pip install -r backend/requirements.txt
uvicorn backend.src.main:app --reload
```

## Phase 1 endpoints

- `GET /health` health check
- `POST /upload` upload `.nc` and `.h5` satellite files
- `GET /files` list uploaded files
- `POST /interpolate` start a mock interpolation job
- `GET /results` list mock interpolation results
