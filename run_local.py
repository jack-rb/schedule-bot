#!/usr/bin/env python3
"""
Скрипт для локального запуска приложения
"""

import os
import uvicorn
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

if __name__ == "__main__":
    # Проверяем наличие токена бота
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token or bot_token == "your_bot_token_here":
        print("⚠️  ВНИМАНИЕ: Токен бота не настроен!")
        print("Создайте файл .env и добавьте в него:")
        print("BOT_TOKEN=ваш_токен_бота")
        print("\nПолучить токен можно у @BotFather в Telegram")
        print("\nПриложение запустится без бота...")
    
    # Запускаем приложение
    print("🚀 Запуск Schedule Bot...")
    print("📱 Веб-интерфейс: http://localhost:8000")
    print("🔧 API документация: http://localhost:8000/docs")
    print("🛑 Для остановки нажмите Ctrl+C")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 