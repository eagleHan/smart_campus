from fastapi import APIRouter, FastAPI

from .catalog import SERVICE_CATALOG


def create_service_app(service_code: str) -> FastAPI:
    metadata = SERVICE_CATALOG[service_code]
    app = FastAPI(
        title=metadata["service_name"],
        version="0.1.0",
        summary=metadata["summary"],
        openapi_tags=[{"name": tag} for tag in metadata["tags"]],
    )

    router = APIRouter()

    @router.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"service": service_code, "status": "ok"}

    @router.get("/meta", tags=["system"])
    def meta() -> dict:
        return metadata

    @router.get("/capabilities", tags=["system"])
    def capabilities() -> dict[str, object]:
        return {
            "service": service_code,
            "frontend_separated": bool(metadata["frontend_path"]),
            "frontend_path": metadata["frontend_path"],
            "backend_port": metadata["backend_port"],
            "domain": metadata["domain"],
        }

    app.include_router(router)
    return app
