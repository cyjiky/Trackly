from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.models import db_helper

from ..routes import user_routes as crud
from ..schemas.user_dtos import *
from .dependencies import user_by_id


router = APIRouter(tags=["Users"])


@router.post("/")
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=User)
async def get_user(user: User = Depends(user_by_id)) -> User:
    return user


@router.get("/", response_model=List[User])
async def get_all_users(session: AsyncSession = Depends(db_helper.get_scoped_session)):
    return await crud.get_users(session=session)


@router.patch("/", response_model=User)
async def update_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
) -> User:
    return await crud.update_user(
        session=session,
        user=user,
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
) -> None:
    await crud.delete_user(session=session, user=user)
