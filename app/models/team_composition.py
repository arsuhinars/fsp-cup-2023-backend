from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.match import Match


class TeamComposition(Base):
    __tablename__ = "team_composition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
<<<<<<<<< Temporary merge branch 1

    team: Mapped["Team"] = relationship(back_populates="team_compositions")
    team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship(back_populates="team_composition")
    tournament_sets: Mapped[list["TournamentSet"]] = relationship(back_populates="team_composition")
    matches: Mapped[list["Match"]] = relationship(
        primaryjoin="or_(TeamComposition.id == Match.team_composition_a_id, TeamComposition.id == Match.team_composition_b_id)")
    win_matches: Mapped[list["Match"]] = relationship(
        primaryjoin="TeamComposition.id == Match.team_composition_winner_id")
=========
    is_active: Mapped[bool] = mapped_column(default=True)
    
    team: Mapped["Team"] = relationship()
    team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship(
        back_populates="team_composition"
    )
>>>>>>>>> Temporary merge branch 2
