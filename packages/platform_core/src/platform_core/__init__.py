"""平台核心包.

提供智慧校园微服务平台的基础能力，包括服务目录、服务工厂、配置管理等。
"""

from .catalog import SERVICE_CATALOG
from .service_factory import create_service_app
from .settings import (
    BaseServiceSettings,
    DatabaseSettings,
    JWTSettings,
    RabbitMQSettings,
    RedisSettings,
    SecuritySettings,
    get_settings,
)

__all__ = [
    "SERVICE_CATALOG",
    "create_service_app",
    "BaseServiceSettings",
    "DatabaseSettings",
    "RedisSettings",
    "RabbitMQSettings",
    "JWTSettings",
    "SecuritySettings",
    "get_settings",
]
