from fastapi import FastAPI

from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("identity-access")


@app.get("/accounts/demo", tags=["identity"])
def demo_account() -> dict[str, object]:
    return {"account_id": "acc-demo-001", "username": "admin", "status": "active"}
