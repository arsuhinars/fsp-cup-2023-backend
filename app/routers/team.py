from typing import Annotated

from fastapi import APIRouter, Depends

from app.exceptions import EntityNotFoundException
from app.models.user import User
from app.schemas.team_create_schema import TeamCreateSchema
from app.schemas.team_schema import TeamSchema
from app.schemas.team_update_schema import TeamUpdateSchema
from app.security import authenticate, require_team_captain
from app.services import team_service

router = APIRouter(prefix="/teams", tags=["Team"])


@router.post("/my", response_model=TeamSchema)
def create_my_team(
    team: TeamCreateSchema, user: Annotated[User, Depends(require_team_captain)]
) -> TeamSchema:
    return team_service.create(team, user.id)


@router.get("/", response_model=list[TeamSchema], dependencies=[Depends(authenticate)])
def get_all_teams():
    return team_service.get_all()


@router.get("/my", response_model=TeamSchema)
def get_my_team(user: Annotated[User, Depends(require_team_captain)]):
    return team_service.get_by_leader_id(user.id)


@router.get(
    "/{team_id}", response_model=TeamSchema, dependencies=[Depends(authenticate)]
)
def get_team_by_id(team_id: int):
    return team_service.get_by_id(team_id)


@router.put("/my", response_model=TeamSchema)
def update_my_team(
    schema: TeamUpdateSchema, user: Annotated[User, Depends(require_team_captain)]
):
    team = team_service.get_by_leader_id(user.id)
    if team is None:
        raise EntityNotFoundException("Team was not found")

    return team_service.update(team.id, schema)
