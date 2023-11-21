from sqlalchemy.sql import select

from app.models.team_composition_set import TeamCompositionSet

def get_by_id(session, team_composition_id: int) -> TeamCompositionSet:
    return session.get(TeamCompositionSet, team_composition_id)