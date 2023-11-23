from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.schemas.tournament_request_schema import TournamentRequestStatus


class TournamentRequest(Base):
    __tablename__ = "tournament_requests"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id"))
    team_composition_id: Mapped[int] = mapped_column(ForeignKey("team_composition.id"))
    status: Mapped[TournamentRequestStatus] = mapped_column(default=TournamentRequestStatus.PENDING)

    team_composition: Mapped["TeamComposition"] = relationship(
        foreign_keys=[team_composition_id]
    )
    tournament: Mapped["Tournament"] = relationship(
        foreign_keys=[tournament_id]
    )

    @hybrid_property
    def active_players(self):
        return self.team_composition.players
