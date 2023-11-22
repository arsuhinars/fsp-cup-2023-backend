from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.team import Team
from app.models.team_composition import TeamComposition


def get_all(session: Session) -> list[Team]:
    return session.query(Team).all()


def get_by_id(session: Session, team_id: int) -> Team | None:
    return session.get(Team, team_id)


def get_active_composition(session: Session, team: Team) -> TeamComposition | None:
    q = select(TeamComposition).where(
        TeamComposition.is_active and TeamComposition.team_id == team.id
    )

    return session.execute(q).scalar_one_or_none()


def save(session: Session, team: Team) -> Team:
    session.add(team)
    session.flush()
    session.commit()
    return team
