from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class TournamentSet(Base):
    __tablename__ = "tournament_set"

    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id"), primary_key=True)
    tournament = relationship("tournament")
    team_composition_id: Mapped[int] = mapped_column(ForeignKey("team_composition.id"), primary_key=True)
    team_composition = relationship("team_composition")
    order_number: Mapped[int] = mapped_column(Integer)
    result_place: Mapped[int] = mapped_column(Integer)
