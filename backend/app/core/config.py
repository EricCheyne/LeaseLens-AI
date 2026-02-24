from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    PROJECT_NAME: str = "LeaseLens AI"
    DATABASE_URL: PostgresDsn = "postgresql+asyncpg://postgres:postgres@localhost:5432/leaselens"
    SECRET_KEY: str = "your-secret-key-here"
    AWS_S3_BUCKET: str = "leaselens-uploads"
    OPENAI_API_KEY: str = "your-openai-key-here"


settings = Settings()
