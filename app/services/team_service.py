import app.core.db as db
import app.repositories.team_repository as team_repo
import app.repositories.user_repository as user_repo
from app.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
    ValidationException,
)
from app.models.team import Team
from app.schemas.team_create_schema import TeamCreateSchema
from app.schemas.team_schema import TeamSchema
from app.schemas.team_update_schema import TeamUpdateSchema
from app.schemas.user_schema import UserRole
from app.utils import map_model_to_orm


def create(dto: TeamCreateSchema, leader_id: int) -> TeamSchema:
    team = Team(**dto.model_dump())
    with db.create_session() as session:
        user = user_repo.get_by_id(session, leader_id)
        if user is None:
            raise EntityNotFoundException("User was not found")

        if user.role != UserRole.TEAM_CAPTAIN:
            raise ValidationException("User must be team captain to create new team")

        if user.team is not None:
            raise EntityAlreadyExistsException("User already has team")

        team.leader_id = user.id

        return TeamSchema.model_validate(team_repo.save(session, team))


def get_all() -> list[TeamSchema]:
    with db.create_session() as session:
        teams = team_repo.get_all(session)
        return list(map(TeamSchema.model_validate, teams))


def get_by_id(team_id: int) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team was not found")
        return TeamSchema.model_validate(team)


def get_by_leader_id(leader_id: int) -> TeamSchema:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, leader_id)
        if user is None:
            raise EntityNotFoundException("User was not found")

        if user.team is None:
            raise EntityNotFoundException("Team was not found")

        return TeamSchema.model_validate(user.team)


def update(team_id: int, dto: TeamUpdateSchema) -> TeamSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team was not found")

        map_model_to_orm(dto, team)
        team_repo.save(session, team)

        return TeamSchema.model_validate(team)
