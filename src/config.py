import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Configuration settings for the AI Hacker League Project Management System.
    Loads environment variables and provides default values.
    """
    PROJECT_NAME: str = "AI Hacker League Project Management System"
    PROJECT_VERSION: str = "1.0.0"
    
    GITHUB_CLI_PATH: str = os.getenv("GITHUB_CLI_PATH", "gh")
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./project_manager.db")

settings = Settings()
