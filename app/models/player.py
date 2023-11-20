from datetime import date
from enum import StrEnum

from sqlalchemy import ForeignKey, String, Integer, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class GenderEnum(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Player(Base):
    __tablename__ = "player"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    gto_id: Mapped[int] = mapped_column(Integer, unique=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team = relationship("Team", uselist=False)
    nickname: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    patronymic: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date] = mapped_column(Date)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum))
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    citizenship: Mapped[str] = mapped_column(String(50))
    rank: Mapped[str] = mapped_column(String(50))
    pd_accepted: Mapped[bool] = mapped_column(default=False)
