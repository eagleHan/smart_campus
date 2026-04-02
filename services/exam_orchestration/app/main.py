from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("exam-orchestration")


@app.get("/exams/demo", tags=["exam"])
def demo_exam() -> dict[str, object]:
    return {"exam_id": "exam-demo-001", "name": "高一月考", "status": "draft"}
