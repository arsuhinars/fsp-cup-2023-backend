from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException
from app.models.team import Team
from app.schemas.team_create_schema import TeamCreateSchema
from app.schemas.team_schema import TeamSchema
import app.repositories.team_repository as team_repo
import app.core.db as db
from app.schemas.team_update_schema import TeamUpdateSchema


def get_my():
    pass
    #TODO !!!!!!!!!!!!!!!!!!!

def create(team: TeamCreateSchema) -> TeamSchema:
    team = TeamCreateSchema.model_validate(team).to_Model()
    with db.create_session() as session:
        if team_repo.get_by_name(session, team.name) is not None:
            raise EntityAlreadyExistsException("Team with this name already exists")
        return TeamSchema.from_model(team_repo.save(session, team))

def get_all() -> list[TeamSchema]:
    with db.create_session() as  session:
        teams = team_repo.get_all(session)
        return [TeamSchema.from_model(team) for team in teams]

def get_by_id(team_id: int) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        return TeamSchema.from_model(team)
    
def get_by_name(name: str) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_name(session, name)
        if team is None:
            raise EntityNotFoundException("Team not found")
        return TeamSchema.from_model(team)
    
def update(team_id: int, team: TeamUpdateSchema) -> TeamSchema:
    TeamUpdateSchema.model_validate(team)
    with db.create_session() as session:
        db_team = team_repo.get_by_id(session, team_id)
        if db_team is None:
            raise EntityNotFoundException("Team not found")
        db_team = team_repo.save(session, team.to_model(db_team))
        return TeamSchema.from_model(db_team)
    
def delete(team_id: int) -> bool:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        team_repo.delete(session,team)
        return True