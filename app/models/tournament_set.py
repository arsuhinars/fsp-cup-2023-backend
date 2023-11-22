from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class TournamentSet(Base):
    __tablename__ = "tournament_set"

    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id"), primary_key=True)
    team_composition_id: Mapped[int] = mapped_column(ForeignKey("team_composition.id"), primary_key=True)
    order_number: Mapped[int] = mapped_column(Integer)
    result_place: Mapped[Optional[int]] = mapped_column(Integer, default=None)

    tournament: Mapped["Tournament"] = relationship(back_populates="tournament_sets")
    team_composition: Mapped["TeamComposition"] = relationship(back_populates="tournament_sets")
