"""Marking Engine 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Marking Engine 服务配置."""

    # 服务特定配置
    service_name: str = "marking-engine"


# 全局配置实例
settings = Settings()
