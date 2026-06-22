from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api.middleware import register_middleware
from .api.routes import router
from .config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Satellite frame interpolation starter API for BAH 2026.",
    )
    register_middleware(app)
    app.include_router(router)
    settings.preview_root.mkdir(parents=True, exist_ok=True)
    app.mount("/artifacts", StaticFiles(directory=settings.preview_root), name="artifacts")
    return app


app = create_app()
