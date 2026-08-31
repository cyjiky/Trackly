from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str 
    description: str | None
    user_id: int

class TaskCreate(TaskBase):
    pass 

class TaskUpdatePartial(TaskBase):
    titile: str | None 
    desctription: str | None 

class Task(TaskBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int 