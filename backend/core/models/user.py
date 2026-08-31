from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base 

if TYPE_CHECKING:
    from .task import Task
    from .profile import Profile

class User(Base):
    username: Mapped[str] = mapped_column(String(40), unique=True)
    user_email: Mapped[str] = mapped_column(unique=True)

    tasks: Mapped[List[Task]] = relationship(back_populates='user')
    profile: Mapped[List[Profile]] = relationship(back_populates='user')