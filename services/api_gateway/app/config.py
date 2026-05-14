"""Api Gateway 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Api Gateway 服务配置."""

    # 服务特定配置
    service_name: str = "api-gateway"


# 全局配置实例
settings = Settings()
