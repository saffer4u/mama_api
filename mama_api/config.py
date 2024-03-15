from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = "dev"
    # model_config = SettingsConfigDict(env_file=".env")


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_file="DEV_")


class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_file="PROD_")


class TestConfig(GlobalConfig):
    DATABASE_URL: Optional[str] = "salite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    model_config = SettingsConfigDict(env_file="TEST_")


@lru_cache
def get_config(env_state: str):
    configs = {
        "dev": DevConfig,
        "prod": ProdConfig,
        "test": TestConfig,
    }
    return configs[env_state]


config = get_config(BaseConfig().ENV_STATE)
