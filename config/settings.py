# external imports
from functools import lru_cache
from pathlib import Path

from pydantic import ConfigDict, SecretStr
from pydantic_settings import BaseSettings

# internal imports


class Settings(BaseSettings):
    """Base settings class for the application."""

    # Secret key for the application
    ANTHROPIC_API_KEY: SecretStr
    TAVILY_API_KEY: SecretStr

    # General settings
    APP_NAME: str = "Langgraph Template"

    # Data
    ROOT_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = ROOT_DIR / "data"

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        secrets_dir=None,
    )


@lru_cache
def get_settings() -> Settings:
    """Get the settings object."""
    return Settings()
