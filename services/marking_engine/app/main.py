from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("marking-engine")


@app.get("/tasks/demo", tags=["marking"])
def demo_task() -> dict[str, object]:
    return {"task_id": "mark-demo-001", "status": "queued", "submission_count": 36}
