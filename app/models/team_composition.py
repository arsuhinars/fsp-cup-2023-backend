from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.match import Match
from app.models.team import Team
from app.models.team_composition_set import TeamCompositionSet


class TeamComposition(Base):
    __tablename__ = "team_composition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))

    team: Mapped["Team"] = relationship()
    team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship(
        back_populates="team_composition"
    )
