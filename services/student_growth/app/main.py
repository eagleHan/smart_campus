from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("student-growth")


@app.get("/profiles/demo", tags=["student"])
def demo_profile() -> dict[str, object]:
    return {"student_id": "stu-demo-001", "name": "张三", "attendance_rate": 0.98}
