from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("oa-collaboration")


@app.get("/announcements/demo", tags=["oa"])
def demo_announcement() -> dict[str, object]:
    return {"notice_id": "notice-demo-001", "title": "清明假期值班安排", "level": "important"}
