"""平台核心配置管理模块.

提供统一的配置管理，支持从环境变量加载配置。
"""

from functools import lru_cache
from typing import List, Optional

from pydantic import Field, validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """数据库配置."""

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    host: str = "localhost"
    port: int = 5432
    user: str = "smartcampus"
    password: str = "smartcampus"
    db: str = "platform_db"

    @property
    def async_url(self) -> str:
        """异步数据库连接 URL."""
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

    @property
    def sync_url(self) -> str:
        """同步数据库连接 URL."""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class RedisSettings(BaseSettings):
    """Redis 配置."""

    model_config = SettingsConfigDict(env_prefix="REDIS_")

    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: Optional[str] = None

    @property
    def url(self) -> str:
        """Redis 连接 URL."""
        auth = f":{self.password}@" if self.password else ""
        return f"redis://{auth}{self.host}:{self.port}/{self.db}"


class RabbitMQSettings(BaseSettings):
    """RabbitMQ 配置."""

    model_config = SettingsConfigDict(env_prefix="RABBITMQ_")

    host: str = "localhost"
    port: int = 5672
    user: str = "guest"
    password: str = "guest"

    @property
    def url(self) -> str:
        """RabbitMQ 连接 URL."""
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/"


class JWTSettings(BaseSettings):
    """JWT 认证配置."""

    model_config = SettingsConfigDict(env_prefix="JWT_")

    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7


class SecuritySettings(BaseSettings):
    """安全配置."""

    model_config = SettingsConfigDict(env_prefix="")

    bcrypt_rounds: int = Field(default=12, alias="BCRYPT_ROUNDS")
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        alias="CORS_ORIGINS"
    )

    @validator("cors_origins", pre=True)
    def parse_cors_origins(cls, v):
        """解析 CORS 来源列表."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


class BaseServiceSettings(BaseSettings):
    """服务基础配置.

    所有微服务应继承此配置类。
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # 应用环境: dev, test, staging, production
    app_env: str = Field(default="dev", alias="APP_ENV")

    # 服务端口
    service_port: int = Field(default=8000, alias="SERVICE_PORT")

    # 调试模式
    debug: bool = False

    # 子配置
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    rabbitmq: RabbitMQSettings = Field(default_factory=RabbitMQSettings)
    jwt: JWTSettings = Field(default_factory=JWTSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)

    @validator("debug", pre=True, always=True)
    def set_debug(cls, v, values):
        """根据环境自动设置调试模式."""
        if v is not None:
            return v
        app_env = values.get("app_env", "dev")
        return app_env in ("dev", "development", "test")

    @property
    def is_development(self) -> bool:
        """是否为开发环境."""
        return self.app_env in ("dev", "development")

    @property
    def is_testing(self) -> bool:
        """是否为测试环境."""
        return self.app_env == "test"

    @property
    def is_production(self) -> bool:
        """是否为生产环境."""
        return self.app_env in ("prod", "production")


@lru_cache()
def get_settings(settings_class: type = BaseServiceSettings) -> BaseServiceSettings:
    """获取配置实例（单例模式）.

    Args:
        settings_class: 配置类，默认为 BaseServiceSettings

    Returns:
        配置实例
    """
    return settings_class()
