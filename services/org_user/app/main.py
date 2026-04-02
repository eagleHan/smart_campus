from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("org-user")


@app.get("/users/demo", tags=["user"])
def demo_user() -> dict[str, object]:
    return {"user_id": "usr-demo-001", "name": "系统管理员", "roles": ["platform-admin"]}
