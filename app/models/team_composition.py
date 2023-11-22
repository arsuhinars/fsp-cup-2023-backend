from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class TeamComposition(Base):
    __tablename__ = "team_composition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    is_active: Mapped[bool] = mapped_column(default=True)

    team: Mapped["Team"] = relationship(back_populates="team_compositions")
    # team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship()
    # tournament_sets: Mapped[list["TournamentSet"]] = relationship()
    matches_a: Mapped[list["Match"]] = relationship(
        foreign_keys="Match.team_composition_a_id"
    )
    matches_b: Mapped[list["Match"]] = relationship(
        foreign_keys="Match.team_composition_b_id"
    )
    win_matches: Mapped[list["Match"]] = relationship(
        foreign_keys="Match.team_composition_winner_id"
    )
    tournaments: Mapped[list["Tournament"]] = relationship(
        secondary="tournament_set",
        back_populates="team_compositions",
    )
    players: Mapped[list["Player"]] = relationship(
        secondary="team_composition_set",
        back_populates="team_compositions"
    )
