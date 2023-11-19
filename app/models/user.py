from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date

from app.core.db import Base


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    JUDGE = "JUDGE"
    TEAM_CAPTAIN = "TEAM_CAPTAIN"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    patronymic: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[Date] = mapped_column(Date)
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    role: Mapped[UserRole]
