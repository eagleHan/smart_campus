"""Oa Collaboration 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Oa Collaboration 服务配置."""

    # 服务特定配置
    service_name: str = "oa-collaboration"


# 全局配置实例
settings = Settings()
