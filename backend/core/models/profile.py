from __future__ import annotations
from sqlalchemy import String 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base 
from .mixins import UserRelationMixin

class Profile(UserRelationMixin, Base):
    _user_id_unique: bool = True
    _user_back_populates = 'profile'

    first_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    second_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    bio: Mapped[str | None]