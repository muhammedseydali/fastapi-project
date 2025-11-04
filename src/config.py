from pydantic import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL : str

    model_config = SettingsConfigDict(
        envfile = '.env',
        extra = "ignore"
    )