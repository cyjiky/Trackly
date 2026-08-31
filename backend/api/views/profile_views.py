from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.models import db_helper

from ..routes import profile_routes as crud
from ..schemas.profile_dtos import *
from .dependencies import profile_by_id


router = APIRouter(tags=["Profiles"])


@router.post("/")
async def create_profile(
    profile_in: ProfileCreate,
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> Profile:
    return await crud.create_profile(
        session=session, 
        profile_in=profile_in
    )


@router.patch("/")
async def update_profile(
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
):
    return await crud.update_profile(
        session=session, 
        profile=profile
    )


@router.get("/{profile_id}/", response_model=Profile)
async def get_profile(
    profile: Profile = Depends(profile_by_id)
) -> Profile:
    return profile


@router.get("/", response_model=List[Profile])
async def get_all_profiles(
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> List[Profile]:
    return await crud.get_profiles(
        session=session
    )


@router.delete("/{profile_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(
        db_helper.scope_session_dependency
    ),
) -> None:
    await crud.delete_profile(
        session=session, 
        profile=profile
    )
