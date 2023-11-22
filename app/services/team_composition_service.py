import app.core.db as db
from app.models.team_composition import TeamComposition
import app.repositories.team_composition_repository as team_compo_repo
from app.schemas.team_composition_schema import TeamCompositionSchema


def create(team_comp: TeamCompositionSchema) -> int:
    with db.create_session as session:
        print('tc.id >>', team_comp.id)
        team_comp = team_compo_repo.save(session, TeamComposition(**team_comp.model_dump()))
        print('tc.id >>', team_comp.id)
        return team_comp.id
