from typing import List
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Task
from ..schemas.tasks_dtos import TaskCreate, TaskUpdatePartial


async def get_task(
    session: AsyncSession,
    task_id: int,
) -> Task:
    return await session.get(Task, task_id)


async def create_task(
    session: AsyncSession,
    task_in: TaskCreate,
) -> Task:
    task = Task(**task_in.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def delete_task(
    session: AsyncSession,
    task: Task,
) -> None:
    await session.delete(task)
    await session.commit()


async def update_task(
    session: AsyncSession,
    task: Task,
    task_update: TaskUpdatePartial,
    partial: bool = False,
) -> Task:
    for n, val in task_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(task, n, val)
    await session.commit()
    return task


async def get_tasks(
    session: AsyncSession,
) -> List[Task]:
    stmt = select(Task).order_by(Task.id)
    res: Result = await session.execute(stmt)
    tasks = res.scalars().all()
    return list(tasks)
