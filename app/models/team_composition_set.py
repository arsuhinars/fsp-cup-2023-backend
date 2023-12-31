from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class TeamCompositionSet(Base):
    __tablename__ = "team_composition_set"

    team_composition_id: Mapped[int] = mapped_column(
        ForeignKey("team_composition.id"), primary_key=True
    )
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
