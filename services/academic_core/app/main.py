from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("academic-core")


@app.get("/plans/demo", tags=["academic"])
def demo_plan() -> dict[str, object]:
    return {"plan_id": "plan-demo-001", "grade": "高一", "name": "春季教学计划"}
