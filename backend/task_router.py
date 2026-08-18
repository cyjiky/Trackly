from fastapi import APIRouter, Depends
from schemas import TaskCreate
from models import Task, Base
from sqlalchemy.orm import Session
from db import engine, session_local

task_router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db 
    finally:
        db.close()

@task_router.get("/")
def hello_world():
    return {"Hello": "World"}

@task_router.post('/task')
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@task_router.get('/task')
async def choose_task(db: Session = Depends(get_db)):
    return db.query(Task).all() 

@task_router.delete('/task')
async def del_task():
    pass 