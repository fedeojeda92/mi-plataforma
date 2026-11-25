from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
        env_ignore_empty=True,
    )

    app_name: str = "mi-plataforma"
    app_env: Literal["local", "test", "staging", "prod"] = "local"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/plataforma"
    redis_url: str = "redis://localhost:6379/0"
    anthropic_api_key: SecretStr | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
