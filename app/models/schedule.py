from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(Text, nullable=True)
    
    # Связь с расписанием
    schedules = relationship("Schedule", back_populates="group")

class Schedule(Base):
    __tablename__ = "schedules"
    
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    day_of_week = Column(String(20))  # Понедельник, Вторник, etc.
    lesson_number = Column(Integer)  # 1, 2, 3, etc.
    subject = Column(String(100))
    teacher = Column(String(100), nullable=True)
    room = Column(String(20), nullable=True)
    time_start = Column(String(10), nullable=True)  # 09:00
    time_end = Column(String(10), nullable=True)    # 10:30
    
    # Связь с группой
    group = relationship("Group", back_populates="schedules")
