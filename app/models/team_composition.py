from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class TeamComposition(Base):
    __tablename__ = "team_composition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    is_active: Mapped[bool] = mapped_column(default=True)
    
    team: Mapped["Team"] = relationship()
    team_composition_sets: Mapped[list["TeamCompositionSet"]] = relationship(
        back_populates="team_composition"
    )
