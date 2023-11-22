from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    leader_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(50))

    leader: Mapped[Optional["User"]] = relationship(back_populates="team")
    players: Mapped[list["Player"]] = relationship()
    team_compositions: Mapped[list["TeamComposition"]] = relationship()
