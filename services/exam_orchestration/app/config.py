"""Exam Orchestration 配置模块."""

from platform_core import BaseServiceSettings


class Settings(BaseServiceSettings):
    """Exam Orchestration 服务配置."""

    # 服务特定配置
    service_name: str = "exam-orchestration"


# 全局配置实例
settings = Settings()
