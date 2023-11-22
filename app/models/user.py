from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import config
from app.core.db import Base
from app.schemas.user_schema import JudgeRankEnum, UserRole


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password_hash: Mapped[bytes] = mapped_column(
        LargeBinary(config.PASSWORD_HASH_LENGTH)
    )
    password_salt: Mapped[bytes] = mapped_column(
        LargeBinary(config.PASSWORD_SALT_LENGTH)
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    patronymic: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date] = mapped_column(Date)
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole))

    judge_rank: Mapped[JudgeRankEnum | None] = mapped_column(Enum(JudgeRankEnum))

    team: Mapped["Team"] = relationship()

    __table_args__ = (
        UniqueConstraint("email"),
        Index("idx_email", "email", unique=True),
    )
