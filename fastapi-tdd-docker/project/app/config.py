# project/app/config.py
import logging
from functools import lru_cache
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()

# BaseSettings also automatically reads from environment variables for these config settings. 
# In other words, environment: str = "dev" is equivalent to environment: str = os.getenv("ENVIRONMENT", "dev").