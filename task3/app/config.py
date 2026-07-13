from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "test-secret-key-for-ci"
    DATABASE_URL: str = "sqlite:///patients.db"
    
    class Config:
        env_file = ".env"

settings = Settings()