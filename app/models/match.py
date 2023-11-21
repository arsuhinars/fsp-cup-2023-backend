from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_a_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team_b_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team_winner_id: Mapped[int] = mapped_column(ForeignKey("team.id"))

    team_a: Mapped["Team"] = relationship(foreign_keys=[team_a_id])
    team_b: Mapped["Team"] = relationship(foreign_keys=[team_b_id])
    team_winner: Mapped["Team"] = relationship(foreign_keys=[team_winner_id])
