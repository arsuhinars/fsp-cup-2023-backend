from sqlalchemy.sql import select

from app.models.team import Team

def get_all(session) -> list[Team]:
    return session.query(Team).all()

def get_by_id(session, team_id: int) -> Team | None:
    return session.get(Team, team_id)

def get_by_name(session, name: str) -> Team | None:
    result = session.execute(
        select(Team).where(Team.name == name).limit(1)
    )
    return result.scalar_one_or_none()

def get_by_leader_id(session, leader_id: int) -> Team | None:
    return session.get(Team, leader_id)

def save(session, team: Team) -> Team:
    session.add(team)
    session.flush()
    session.commit()
    return team

def delete(session, team: Team) -> None:
    session.delete(team)
    session.commit()