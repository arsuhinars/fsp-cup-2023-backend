from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    JUDGE = "JUDGE"
    TEAM_CAPTAIN = "TEAM_CAPTAIN"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[UserRole]
