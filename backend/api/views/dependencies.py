from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Profile, User, Task

from ..routes import user_routes
from ..routes import task_routes
from ..routes import profile_routes


def raise_not_found(name: str, obj: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"{name} with {obj} not found"
    )


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> User:
    user = await user_routes.get_user(
        session=session, user_id=user_id
    )
    if user is not None:
        return user
    raise_not_found(User, user_id)


async def task_by_id(
    task_id: Annotated[int, Path],
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> Task:
    task = await task_routes.get_task(
        session=session, task_id=task_id
    )
    if task is not None:
        return task
    raise_not_found(Task, task_id)


async def profile_by_id(
    profile_id: Annotated[int, Path],
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> Profile:
    profile = await profile_routes.get_profile(
        session=session, profile_id=profile_id
    )
    if profile is not None:
        return profile
    raise_not_found(Profile, profile_id)
