import app.core.db as db
from app.models.team_composition import TeamComposition
import app.repositories.team_composition_repository as team_compo_repo
from app.schemas.team_composition_schema import TeamCompositionSchema


def create(team_id: int) -> int:
    with db.create_session() as session:
        team_comp = team_compo_repo.save(session, TeamComposition(team_id=team_id))
        return team_comp.id
