from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true

from app.models.team_composition import TeamComposition


def get_by_id(session: Session, team_comp_id: int) -> TeamComposition | None:
    return session.get(TeamComposition, team_comp_id)


def get_all(session: Session) -> list[TeamComposition]:
    return session.query(TeamComposition).all()


def get_active_by_team_id(session: Session, team_id: int) -> TeamComposition | None:
    return (
        session.query(TeamComposition)
        .filter(TeamComposition.is_active == true())
        .filter(TeamComposition.team_id == team_id)
        .first()
    )


def save(session: Session, team_comp: TeamComposition) -> TeamComposition:
    session.add(team_comp)
    session.flush()
    session.commit()
    return team_comp
