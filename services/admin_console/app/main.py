from fastapi import FastAPI

from platform_core.catalog import SERVICE_CATALOG
from platform_core.service_factory import create_service_app

app: FastAPI = create_service_app("admin-console")


@app.get("/dashboard/services", tags=["admin"])
def dashboard_services() -> dict[str, list[dict[str, object]]]:
    services = []
    for code, item in SERVICE_CATALOG.items():
        if code in {"api-gateway", "admin-console"}:
            continue
        services.append(
            {
                "service_code": code,
                "service_name": item["service_name"],
                "domain": item["domain"],
                "backend": f"http://127.0.0.1:{item['backend_port']}",
                "frontend": item["frontend_path"],
                "summary": item["summary"],
            }
        )
    return {"services": services}


@app.get("/dashboard/menu", tags=["admin"])
def dashboard_menu() -> dict[str, list[dict[str, str]]]:
    return {
        "menu": [
            {"key": "tenant", "label": "租户与学校管理"},
            {"key": "identity", "label": "账号与权限"},
            {"key": "organization", "label": "组织与用户"},
            {"key": "integration", "label": "集成与开放接口"},
            {"key": "ops", "label": "服务运行与配置中心"},
        ]
    }
