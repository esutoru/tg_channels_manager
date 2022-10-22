from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
