"""Identity Access 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Identity Access 服务配置."""

    # 服务特定配置
    service_name: str = "identity-access"


# 全局配置实例
settings = Settings()
