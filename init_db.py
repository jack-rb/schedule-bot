#!/usr/bin/env python3
"""
Скрипт для инициализации базы данных с тестовыми данными
"""

import asyncio
from app.core.database import engine, Base
from app.services.schedule import ScheduleService
from app.schemas.schedule import GroupCreate, ScheduleCreate

async def init_database():
    """Инициализация базы данных с тестовыми данными"""
    print("Создание таблиц...")
    
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    
    print("Добавление тестовых данных...")
    
    # Создаем группы
    groups_data = [
        {"name": "ИС-31", "description": "Информационные системы, 3 курс"},
        {"name": "ИС-41", "description": "Информационные системы, 4 курс"},
        {"name": "ПО-21", "description": "Программная инженерия, 2 курс"},
    ]
    
    created_groups = {}
    for group_data in groups_data:
        group = await ScheduleService.create_group(GroupCreate(**group_data))
        created_groups[group.name] = group.id
        print(f"Создана группа: {group.name}")
    
    # Создаем расписание для группы ИС-31
    is31_schedule = [
        # Понедельник
        {"group_id": created_groups["ИС-31"], "day_of_week": "Понедельник", "lesson_number": 1, 
         "subject": "Математический анализ", "teacher": "Иванов И.И.", "room": "301", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Понедельник", "lesson_number": 2, 
         "subject": "Программирование", "teacher": "Петров П.П.", "room": "404", 
         "time_start": "10:40", "time_end": "12:10"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Понедельник", "lesson_number": 3, 
         "subject": "Базы данных", "teacher": "Сидоров С.С.", "room": "505", 
         "time_start": "13:30", "time_end": "15:00"},
        
        # Вторник
        {"group_id": created_groups["ИС-31"], "day_of_week": "Вторник", "lesson_number": 1, 
         "subject": "Физика", "teacher": "Козлов К.К.", "room": "201", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Вторник", "lesson_number": 2, 
         "subject": "Английский язык", "teacher": "Смирнова А.А.", "room": "302", 
         "time_start": "10:40", "time_end": "12:10"},
        
        # Среда
        {"group_id": created_groups["ИС-31"], "day_of_week": "Среда", "lesson_number": 1, 
         "subject": "Веб-разработка", "teacher": "Новиков Н.Н.", "room": "404", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Среда", "lesson_number": 2, 
         "subject": "Алгоритмы и структуры данных", "teacher": "Морозов М.М.", "room": "505", 
         "time_start": "10:40", "time_end": "12:10"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Среда", "lesson_number": 3, 
         "subject": "Экономика", "teacher": "Волкова В.В.", "room": "301", 
         "time_start": "13:30", "time_end": "15:00"},
        
        # Четверг
        {"group_id": created_groups["ИС-31"], "day_of_week": "Четверг", "lesson_number": 1, 
         "subject": "Теория вероятностей", "teacher": "Иванов И.И.", "room": "201", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Четверг", "lesson_number": 2, 
         "subject": "Мобильная разработка", "teacher": "Петров П.П.", "room": "404", 
         "time_start": "10:40", "time_end": "12:10"},
        
        # Пятница
        {"group_id": created_groups["ИС-31"], "day_of_week": "Пятница", "lesson_number": 1, 
         "subject": "Информационная безопасность", "teacher": "Сидоров С.С.", "room": "505", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-31"], "day_of_week": "Пятница", "lesson_number": 2, 
         "subject": "Проектная работа", "teacher": "Новиков Н.Н.", "room": "404", 
         "time_start": "10:40", "time_end": "12:10"},
    ]
    
    # Создаем расписание для группы ИС-41
    is41_schedule = [
        # Понедельник
        {"group_id": created_groups["ИС-41"], "day_of_week": "Понедельник", "lesson_number": 1, 
         "subject": "Машинное обучение", "teacher": "Козлов К.К.", "room": "601", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-41"], "day_of_week": "Понедельник", "lesson_number": 2, 
         "subject": "Большие данные", "teacher": "Морозов М.М.", "room": "602", 
         "time_start": "10:40", "time_end": "12:10"},
        
        # Вторник
        {"group_id": created_groups["ИС-41"], "day_of_week": "Вторник", "lesson_number": 1, 
         "subject": "Архитектура ПО", "teacher": "Новиков Н.Н.", "room": "603", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ИС-41"], "day_of_week": "Вторник", "lesson_number": 2, 
         "subject": "DevOps практики", "teacher": "Петров П.П.", "room": "604", 
         "time_start": "10:40", "time_end": "12:10"},
        
        # Среда
        {"group_id": created_groups["ИС-41"], "day_of_week": "Среда", "lesson_number": 1, 
         "subject": "Дипломная работа", "teacher": "Иванов И.И.", "room": "605", 
         "time_start": "09:00", "time_end": "10:30"},
    ]
    
    # Создаем расписание для группы ПО-21
    po21_schedule = [
        # Понедельник
        {"group_id": created_groups["ПО-21"], "day_of_week": "Понедельник", "lesson_number": 1, 
         "subject": "Основы программирования", "teacher": "Смирнова А.А.", "room": "101", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ПО-21"], "day_of_week": "Понедельник", "lesson_number": 2, 
         "subject": "Математика", "teacher": "Волкова В.В.", "room": "102", 
         "time_start": "10:40", "time_end": "12:10"},
        
        # Вторник
        {"group_id": created_groups["ПО-21"], "day_of_week": "Вторник", "lesson_number": 1, 
         "subject": "Алгоритмы", "teacher": "Морозов М.М.", "room": "103", 
         "time_start": "09:00", "time_end": "10:30"},
        {"group_id": created_groups["ПО-21"], "day_of_week": "Вторник", "lesson_number": 2, 
         "subject": "Физика", "teacher": "Козлов К.К.", "room": "104", 
         "time_start": "10:40", "time_end": "12:10"},
    ]
    
    # Добавляем все расписания
    all_schedules = is31_schedule + is41_schedule + po21_schedule
    
    for schedule_data in all_schedules:
        schedule = await ScheduleService.create_schedule(ScheduleCreate(**schedule_data))
        print(f"Добавлено занятие: {schedule.subject} для группы {schedule.group_id}")
    
    print(f"\nБаза данных инициализирована!")
    print(f"Создано групп: {len(groups_data)}")
    print(f"Добавлено занятий: {len(all_schedules)}")

if __name__ == "__main__":
    asyncio.run(init_database()) 