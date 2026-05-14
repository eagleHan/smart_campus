"""Academic Core 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Academic Core 服务配置."""

    # 服务特定配置
    service_name: str = "academic-core"


# 全局配置实例
settings = Settings()
