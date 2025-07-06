from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from app.core.database import SessionLocal
from app.models.schedule import Group, Schedule
from app.schemas.schedule import GroupCreate, ScheduleCreate

class ScheduleService:
    
    @staticmethod
    def get_db() -> Session:
        return SessionLocal()
    
    @staticmethod
    async def get_all_groups() -> List[Group]:
        """Получить все группы"""
        db = ScheduleService.get_db()
        try:
            result = db.execute(select(Group))
            return result.scalars().all()
        finally:
            db.close()
    
    @staticmethod
    async def get_all_schedules() -> List[Schedule]:
        """Получить все расписания с группами"""
        db = ScheduleService.get_db()
        try:
            result = db.execute(
                select(Schedule).join(Group).order_by(Group.name, Schedule.day_of_week, Schedule.lesson_number)
            )
            return result.scalars().all()
        finally:
            db.close()
    
    @staticmethod
    async def get_schedule_by_group(group_name: str) -> List[Schedule]:
        """Получить расписание по названию группы"""
        db = ScheduleService.get_db()
        try:
            result = db.execute(
                select(Schedule)
                .join(Group)
                .where(Group.name == group_name)
                .order_by(Schedule.day_of_week, Schedule.lesson_number)
            )
            return result.scalars().all()
        finally:
            db.close()
    
    @staticmethod
    async def create_group(group: GroupCreate) -> Group:
        """Создать новую группу"""
        db = ScheduleService.get_db()
        try:
            db_group = Group(**group.dict())
            db.add(db_group)
            db.commit()
            db.refresh(db_group)
            return db_group
        finally:
            db.close()
    
    @staticmethod
    async def create_schedule(schedule: ScheduleCreate) -> Schedule:
        """Создать новое расписание"""
        db = ScheduleService.get_db()
        try:
            db_schedule = Schedule(**schedule.dict())
            db.add(db_schedule)
            db.commit()
            db.refresh(db_schedule)
            return db_schedule
        finally:
            db.close()
    
    @staticmethod
    async def get_schedule_by_day_and_group(group_name: str, day_of_week: str) -> List[Schedule]:
        """Получить расписание по группе и дню недели"""
        db = ScheduleService.get_db()
        try:
            result = db.execute(
                select(Schedule)
                .join(Group)
                .where(Group.name == group_name, Schedule.day_of_week == day_of_week)
                .order_by(Schedule.lesson_number)
            )
            return result.scalars().all()
        finally:
            db.close() 