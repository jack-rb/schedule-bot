import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import engine, Base
from app.bot.bot import bot, dp
from app.services.schedule import ScheduleService

# Создаем таблицы при запуске
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запуск бота
    bot_task = asyncio.create_task(dp.start_polling())
    yield
    # Остановка бота
    bot_task.cancel()
    try:
        await bot_task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan, title="Schedule Bot API")

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создаем экземпляр сервиса расписания
schedule_service = ScheduleService()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница с веб-интерфейсом"""
    return HTMLResponse(content=open("static/index.html").read())

@app.get("/api/schedule")
async def get_schedule():
    """API для получения расписания"""
    try:
        schedule = await schedule_service.get_all_schedules()
        return {"success": True, "data": schedule}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/api/schedule/{group}")
async def get_schedule_by_group(group: str):
    """API для получения расписания по группе"""
    try:
        schedule = await schedule_service.get_schedule_by_group(group)
        return {"success": True, "data": schedule}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/health")
async def health_check():
    """Проверка здоровья приложения"""
    return {"status": "healthy", "message": "Schedule Bot is running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 