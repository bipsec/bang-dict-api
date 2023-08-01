from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DATABASE: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Add other configuration settings as needed

    class Config:
        env_file = ".env"  # Specify the path to your .env file


settings = Settings()
