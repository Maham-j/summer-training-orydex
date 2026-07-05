from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "test-secret-key-for-ci"
    DATABASE_URL: str = "sqlite:///./test.db"
    
    model_config = {"env_file": ".env", "extra": "ignore"}

settings = Settings()