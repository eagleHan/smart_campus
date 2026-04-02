from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("academic-master")


@app.get("/terms/current", tags=["academic"])
def current_term() -> dict[str, object]:
    return {"school_year": "2025-2026", "term": "2", "status": "active"}
