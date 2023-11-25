from app.models.team_composition import TeamComposition
import app.repositories.team_composition_repository as team_comp_repo
import app.core.db as db


def create(team_comp: TeamComposition) -> int:
    with db.create_session as session:
        team_comp_repo.save(session, team_comp)
        return team_comp.id
