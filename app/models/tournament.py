from datetime import date

from sqlalchemy import Date, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.schemas.tournament_schema import TournamentStateEnum


class Tournament(Base):
    __tablename__ = "tournament"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(50))
    discipline: Mapped[str] = mapped_column(String(50))
    date_registration: Mapped[date] = mapped_column(Date)
    date_begin: Mapped[date] = mapped_column(Date)
    date_end: Mapped[date] = mapped_column(Date)
    date_awards: Mapped[date] = mapped_column(Date)
    main_judge_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    state: Mapped["TournamentStateEnum"] = mapped_column(
        Enum(TournamentStateEnum), default=TournamentStateEnum.JUST_CREATED)

    main_judge: Mapped["User"] = relationship(back_populates="judge_tournaments")
    # team_compositions: Mapped[list["TeamComposition"]] = relationship(
    #     secondary="tournament_set", back_populates="tournaments"
    #     )
    tournament_sets: Mapped[list["TournamentSet"]] = relationship(
        back_populates="tournament"
    )
