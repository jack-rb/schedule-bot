from pydantic import BaseModel
from typing import Optional, List

class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    
    class Config:
        from_attributes = True

class ScheduleBase(BaseModel):
    day_of_week: str
    lesson_number: int
    subject: str
    teacher: Optional[str] = None
    room: Optional[str] = None
    time_start: Optional[str] = None
    time_end: Optional[str] = None

class ScheduleCreate(ScheduleBase):
    group_id: int

class Schedule(ScheduleBase):
    id: int
    group_id: int
    group: Group
    
    class Config:
        from_attributes = True

class ScheduleResponse(BaseModel):
    success: bool
    data: Optional[List[Schedule]] = None
    error: Optional[str] = None 