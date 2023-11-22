from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    leader_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(50))

    leader: Mapped["User"] = relationship(back_populates="team")
    players: Mapped[list["Player"]] = relationship(back_populates="team")
    team_compositions: Mapped[list["TeamComposition"]] = relationship(back_populates="team")
    
