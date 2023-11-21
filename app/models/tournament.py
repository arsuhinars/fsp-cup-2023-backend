from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Tournament(Base):
    __tablename__ = "tournament"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(50))
    discipline: Mapped[str] = mapped_column(String(50))
    date_registration: Mapped[date] = mapped_column(Date)
    date_start: Mapped[date] = mapped_column(Date)
    date_end: Mapped[date] = mapped_column(Date)
    date_award: Mapped[date] = mapped_column(Date)
    state: Mapped[str] = mapped_column(String(50))
    main_judge_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    tournament_sets: Mapped[list["TournamentSet"]] = relationship(back_populates="tournament")
