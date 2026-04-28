from sqlalchemy import String, SmallInteger, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id:       Mapped[str] = mapped_column(String(10), primary_key=True)
    name:     Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50),  nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="user", cascade="all, delete")


class Task(Base):
    __tablename__ = "tasks"

    id:               Mapped[str]           = mapped_column(String(10), primary_key=True)
    user_id:          Mapped[str]           = mapped_column(String(10), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    difficulty:       Mapped[int]           = mapped_column(SmallInteger, nullable=False)
    description:      Mapped[str]           = mapped_column(Text, nullable=False)
    additional_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status:           Mapped[str]           = mapped_column(String(20), nullable=False, default="active")

    user: Mapped["User"] = relationship("User", back_populates="tasks")