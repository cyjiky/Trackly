from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base 

class Task(Base):
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text, default=None)