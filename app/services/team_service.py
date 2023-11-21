import app.core.db as db
from app.models.team import Team
import app.repositories.team_repository as team_repo
from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException
from app.schemas.team_create_schema import TeamCreateSchema
from app.schemas.team_schema import TeamSchema
from app.schemas.team_update_schema import TeamUpdateSchema
from app.utils import map_model_to_orm


def get_by_leader_id(leader_id: int) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_leader_id(session, leader_id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        return TeamSchema.model_validate(team)


def create(dto: TeamCreateSchema) -> TeamSchema:
    team = Team(**dto.model_dump())
    with db.create_session() as session:
        if team_repo.get_by_name(session, dto.name) is not None:
            raise EntityAlreadyExistsException("Team with this name already exists")
        return TeamSchema.model_validate(team_repo.save(session, team))


def get_all() -> list[TeamSchema]:
    with db.create_session() as session:
        teams = team_repo.get_all(session)
        return [TeamSchema.model_validate(team) for team in teams]


def get_by_id(team_id: int) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        return TeamSchema.model_validate(team)


def get_by_name(name: str) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_name(session, name)
        if team is None:
            raise EntityNotFoundException("Team not found")
        return TeamSchema.model_validate(team)


def update(team_id: int, dto: TeamUpdateSchema) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        
        if (
            team.name != dto.name
            and team_repo.get_by_name(session, dto.name) is not None
        ):
            raise EntityAlreadyExistsException(
                "Team with this name already exists"
            )
        map_model_to_orm(dto, team)
        team_repo.save(session, team)

        return TeamSchema.model_validate(team)


def delete(team_id: int) -> bool:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team not found")
        team_repo.delete(session, team)
        return True
