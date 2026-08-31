from typing import List
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Profile
from ..schemas.profile_dtos import ProfileCreate, ProfileUpdatePartial


async def get_profile(
    session: AsyncSession,
    profile_id: int,
) -> Profile:
    return await session.get(Profile, profile_id)


async def create_profile(
    session: AsyncSession,
    profile_in: ProfileCreate,
) -> Profile:
    profile = Profile(**profile_in.model_dump())
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile


async def delete_profile(
    session: AsyncSession,
    profile: Profile,
) -> None:
    await session.delete(profile)
    await session.commit()


async def update_profile(
    session: AsyncSession,
    profile: Profile,
    profile_update: ProfileUpdatePartial,
    partial: bool = False,
) -> Profile:
    for n, val in profile_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(profile, n, val)
    await session.commit()
    return profile


async def get_profiles(
    session: AsyncSession
) -> List[Profile]:
    stmt = select(Profile).order_by(Profile.id)
    res: Result = await session.execute(stmt)
    profiles = res.scalars().all()
    return list(profiles)
