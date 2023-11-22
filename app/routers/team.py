from fastapi import APIRouter

from app.schemas.team_create_schema import TeamCreateSchema
from app.schemas.team_schema import TeamSchema
from app.services import team_service

router = APIRouter(prefix="/teams", tags=["team"])


@router.post("/")
def create_team(team: TeamCreateSchema) -> TeamSchema:
    return team_service.create(team)


@router.get("/")
def get_all_teams():
    pass


@router.get("/my")
def get_my_teams():
    pass


@router.put("/{team_id}")
def update_team(team_id: int, team: dict):
    pass


@router.delete("/{team_id}")
def delete_team(team_id: int):
    pass
