import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from app.core.config import settings
from app.services.schedule import ScheduleService

# Инициализация бота
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📅 Открыть расписание",
            web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}")
        )]
    ])
    
    await message.answer(
        "👋 Привет! Я бот для просмотра расписания.\n\n"
        "Нажми кнопку ниже, чтобы открыть расписание:",
        reply_markup=keyboard
    )

@dp.message(Command("schedule"))
async def cmd_schedule(message: types.Message):
    """Обработчик команды /schedule"""
    try:
        # Получаем все группы
        groups = await ScheduleService.get_all_groups()
        
        if not groups:
            await message.answer("📝 Расписание пока не добавлено.")
            return
        
        # Создаем клавиатуру с группами
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=group.name, callback_data=f"group_{group.name}")]
            for group in groups
        ])
        
        await message.answer(
            "📚 Выберите группу для просмотра расписания:",
            reply_markup=keyboard
        )
        
    except Exception as e:
        await message.answer(f"❌ Ошибка при получении расписания: {str(e)}")

@dp.callback_query(lambda c: c.data.startswith('group_'))
async def process_group_selection(callback_query: types.CallbackQuery):
    """Обработчик выбора группы"""
    group_name = callback_query.data.replace('group_', '')
    
    try:
        # Получаем расписание для выбранной группы
        schedules = await ScheduleService.get_schedule_by_group(group_name)
        
        if not schedules:
            await callback_query.message.answer(f"📝 Расписание для группы {group_name} не найдено.")
            return
        
        # Формируем сообщение с расписанием
        schedule_text = f"📅 Расписание группы {group_name}:\n\n"
        
        current_day = ""
        for schedule in schedules:
            if schedule.day_of_week != current_day:
                current_day = schedule.day_of_week
                schedule_text += f"\n📆 {current_day}:\n"
            
            time_info = f" ({schedule.time_start}-{schedule.time_end})" if schedule.time_start else ""
            room_info = f" | 🏠 {schedule.room}" if schedule.room else ""
            teacher_info = f" | 👨‍🏫 {schedule.teacher}" if schedule.teacher else ""
            
            schedule_text += f"{schedule.lesson_number}. {schedule.subject}{time_info}{room_info}{teacher_info}\n"
        
        # Разбиваем на части, если сообщение слишком длинное
        if len(schedule_text) > 4096:
            parts = [schedule_text[i:i+4096] for i in range(0, len(schedule_text), 4096)]
            for part in parts:
                await callback_query.message.answer(part)
        else:
            await callback_query.message.answer(schedule_text)
            
    except Exception as e:
        await callback_query.message.answer(f"❌ Ошибка при получении расписания: {str(e)}")
    
    await callback_query.answer()

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    help_text = """
🤖 Доступные команды:

/start - Запустить бота
/schedule - Показать расписание по группам
/help - Показать эту справку

📱 Также вы можете использовать веб-интерфейс для удобного просмотра расписания.
    """
    await message.answer(help_text)

# Обработчик всех остальных сообщений
@dp.message()
async def echo_message(message: types.Message):
    """Обработчик всех остальных сообщений"""
    await message.answer(
        "🤖 Используйте команду /start для начала работы или /help для справки."
    )
