from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_composition_a_id: Mapped[int] = mapped_column(
        ForeignKey("team_composition.id")
    )
    team_composition_b_id: Mapped[int] = mapped_column(
        ForeignKey("team_composition.id")
    )
    team_composition_winner_id: Mapped[int | None] = mapped_column(
        ForeignKey("team_composition.id")
    )
    order_number: Mapped[int]
    part_number: Mapped[int]

    team_composition_a: Mapped[list["TeamComposition"]] = relationship(
        foreign_keys=[team_composition_a_id], back_populates="matches_a"
    )
    team_composition_b: Mapped[list["TeamComposition"]] = relationship(
        foreign_keys=[team_composition_b_id], back_populates="matches_b"
    )
    team_composition_winner: Mapped["TeamComposition | None"] = relationship(
        foreign_keys=[team_composition_winner_id], back_populates="win_matches"
    )
