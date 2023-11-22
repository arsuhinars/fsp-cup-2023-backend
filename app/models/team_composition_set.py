from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.player import Player
from app.models.team_composition import TeamComposition


class TeamCompositionSet(Base):
    __tablename__ = "team_composition_set"

    team_composition_id: Mapped[int] = mapped_column(
        ForeignKey("team_composition.id"), primary_key=True
    )
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)

    team_composition: Mapped["TeamComposition"] = relationship(
        back_populates="team_composition_sets", foreign_keys=[team_composition_id]
    )
    player: Mapped["Player"] = relationship(back_populates="team_composition_sets")
