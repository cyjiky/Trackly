from typing import List, Union
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from ..schemas.user_dtos import UserCreate, UserUpdatePartial


async def get_users(
    session: AsyncSession,
) -> List[User]:
    stmt = select(User).order_by(User.id)
    res: Result = await session.execute(stmt)
    users = res.scalars().all()
    return list(users)


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> Union[User, None]:
    return await session.get(User, user_id)


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdatePartial,
    partial: bool = False,
) -> User:
    for n, val in user_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(user, n, val)
    await session.commit()
    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
