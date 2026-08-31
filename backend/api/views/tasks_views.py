from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.models import db_helper

from ..routes import task_routes as crud
from ..schemas.tasks_dtos import *
from .dependencies import task_by_id


router = APIRouter(tags=["Tasks"])


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> Task:
    return await crud.create_task(
        session=session, 
        task_in=task_in
    )


@router.get("/{task_id}/", response_model=Task)
async def get_task(
    task: Task = Depends(task_by_id)
) -> Task:
    return task


@router.get("/", response_model=List[Task])
async def get_all_tasks(
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> List[Task]:
    return await crud.get_tasks(
        session=session
    )


@router.patch("/")
async def update_task(
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> Task:
    return await crud.update_task(
        session=session, 
        task=task
    )


@router.delete("/{task_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> None:
    await crud.delete_task(
        session=session, 
        task=task
    )
