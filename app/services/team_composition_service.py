import app.core.db as db
from app.models.team_composition import TeamComposition
import app.repositories.team_composition_repository as team_compo_repo


def create(team_comp: TeamComposition) -> int:
    with db.create_session as session:
        team_compo_repo.save(session, team_comp)
        return team_comp.id