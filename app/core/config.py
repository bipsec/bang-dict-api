import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # Database
    DB_USER: str = os.getenv('POSTGRESQL_USER')
    DB_PASSWORD: str = os.getenv('POSTGRESQL_PASSWORD')
    DB_NAME: str = os.getenv('POSTGRESQL_DB')
    DB_HOST: str = os.getenv('POSTGRESQL_SERVER')
    DB_PORT: str = os.getenv('POSTGRESQL_PORT')
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # JWT
    JWT_SECRET: str = os.getenv('JWT_SECRET', 'JWT_PRIVATE_KEY')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('JWT_TOKEN_EXPIRE_MINUTES', 60)


def get_settings() -> Settings:
    return Settings()
