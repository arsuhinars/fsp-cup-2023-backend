from sqlalchemy.orm import Session

from app.models.team_composition import TeamComposition


def save(session: Session, team_comp: TeamComposition) -> TeamComposition:
    session.add(team_comp)
    session.flush()
    session.commit()
    return team_comp
