from pydantic import BaseModel 

class TaskBase(BaseModel):
    title: str
    description: str | None = None 

class Task(TaskBase):
    id: int 

class TaskCreate(TaskBase):
    pass 