import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Настройки бота
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    
    # Настройки базы данных
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./schedule.db")
    
    # Настройки приложения
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    PORT: int = int(os.getenv("PORT", 8000))
    
    # Настройки Telegram Web App
    WEBAPP_URL: str = os.getenv("WEBAPP_URL", "")
    
    class Config:
        env_file = ".env"

settings = Settings()
