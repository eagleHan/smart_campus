from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("question-bank")


@app.get("/papers/demo", tags=["exam"])
def demo_paper() -> dict[str, object]:
    return {"paper_id": "paper-demo-001", "subject": "数学", "question_count": 18}
