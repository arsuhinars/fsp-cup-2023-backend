from datetime import date

from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.team_composition_set import TeamCompositionSet


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

    team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship(back_populates="tournaments")
