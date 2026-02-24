from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    PROJECT_NAME: str = "LeaseLens AI"
    DATABASE_URL: PostgresDsn = "postgresql+asyncpg://postgres:postgres@localhost:5432/leaselens"
    REDIS_URL: str = "redis://localhost:6379/0"

    # S3 / MinIO Settings
    S3_ENDPOINT: str = "http://localhost:9000"
    S3_ACCESS_KEY: str = "minioadmin"
    S3_SECRET_KEY: str = "minioadmin"
    AWS_S3_BUCKET: str = "leaselens-uploads"
    S3_USE_SSL: bool = False

    SECRET_KEY: str = "your-secret-key-here"
    OPENAI_API_KEY: str = "your-openai-key-here"


settings = Settings()
