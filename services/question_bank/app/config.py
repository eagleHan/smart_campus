"""Question Bank 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Question Bank 服务配置."""

    # 服务特定配置
    service_name: str = "question-bank"


# 全局配置实例
settings = Settings()
