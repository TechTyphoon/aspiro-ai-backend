import os
from pydantic_settings import BaseSettings # <-- THIS LINE IS CHANGED
from dotenv import load_dotenv

# Load .env file variables
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "ASPIRO AI"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True

settings = Settings()
