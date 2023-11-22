from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.team import Team
from app.models.team_composition import TeamComposition


def get_all(session: Session) -> list[Team]:
    return session.query(Team).all()


def get_by_id(session: Session, team_id: int) -> Team | None:
    return session.get(Team, team_id)


def has_active_composition(session: Session, team_id: int) -> bool:
    q = (
        select(TeamComposition)
        .where(TeamComposition.team_id == team_id and TeamComposition.is_active)
        .exists()
    )

    return session.execute(select(q)).scalar_one()


def save(session: Session, team: Team) -> Team:
    session.add(team)
    session.flush()
    session.commit()
    return team
