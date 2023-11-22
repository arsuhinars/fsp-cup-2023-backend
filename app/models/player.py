from datetime import date

from sqlalchemy import Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.schemas.player_create_schema import GenderEnum


class Player(Base):
    __tablename__ = "player"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    gto_id: Mapped[int] = mapped_column(Integer)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    nickname: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    patronymic: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date] = mapped_column(Date)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum))
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    citizenship: Mapped[str] = mapped_column(String(50))
    rank: Mapped[str] = mapped_column(String(50))
    pd_accepted: Mapped[bool] = mapped_column(default=False)
    deleted: Mapped[bool] = mapped_column(default=False)

    team: Mapped["Team"] = relationship(back_populates="players")
    team_compositions: Mapped[list["TeamComposition"]] = relationship(
        secondary="team_composition_set",
        back_populates="players",
    )

    def is_active_in_composition(self, team_composition: "TeamComposition | None"):
        return team_composition is not None and self in team_composition.players

    def as_dict(self, active_composition: "TeamComposition | None" = None):
        d = self.__dict__.copy()
        d["is_active_in_team"] = self.is_active_in_composition(active_composition)
        return d
