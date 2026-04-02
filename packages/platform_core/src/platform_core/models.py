from pydantic import BaseModel


class ServiceDescriptor(BaseModel):
    service_code: str
    service_name: str
    domain: str
    backend_port: int
    frontend_path: str | None
    tags: list[str]
    summary: str


class HealthPayload(BaseModel):
    service: str
    status: str = "ok"
