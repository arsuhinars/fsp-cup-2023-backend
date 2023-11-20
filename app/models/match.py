from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.team import Team


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_a_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team_b_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    name: Mapped[str] = mapped_column(String(50))

    team_a: Team = relationship("Team")
    team_b: Team = relationship("Team")
