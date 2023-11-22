from sqlalchemy.sql import select

from app.models.team_composition_set import TeamComposition

def save(session, team_comp: TeamComposition) -> TeamComposition:
    session.add(team_comp)
    session.flush()
    session.commit()
    return team_comp