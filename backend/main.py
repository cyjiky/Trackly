from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Dict, List, Union, Optional, Annotated
from sqlalchemy.orm import Session

from models import Task, Base 
from db import engine, session_local
from schemas import TaskCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db 
    finally:
        db.close()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.post('/task')
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get('/task')
async def choose_task(db: Session = Depends(get_db)):
    return db.query(Task).all() 

@app.delete('/task')
async def del_task():
    pass 