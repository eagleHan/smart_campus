from fastapi import FastAPI

from platform_core.catalog import SERVICE_CATALOG
from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("api-gateway")


@app.get("/routes", tags=["gateway"])
def routes() -> dict[str, list[dict[str, object]]]:
    registry = []
    for item in SERVICE_CATALOG.values():
        if item["service_code"] == "api-gateway":
            continue
        registry.append(
            {
                "service_code": item["service_code"],
                "target": f"http://127.0.0.1:{item['backend_port']}",
                "frontend_path": item["frontend_path"],
            }
        )
    return {"routes": registry}
