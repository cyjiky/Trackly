from typing import List
from sqlalchemy import String, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base 

from .mixins import UserRelationMixin

class Task(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = 'tasks'

    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )

    