from typing import Annotated

from fastapi import APIRouter, Depends

from app.exceptions import EntityNotFoundException, ForbiddenException
from app.schemas.player_create_schema import PlayerCreateSchema
from app.schemas.player_schema import PlayerSchema
from app.schemas.player_update_schema import PlayerUpdateSchema
from app.schemas.user_schema import UserSchema
from app.security import authenticate, require_team_captain
from app.services import player_service, team_service

router = APIRouter(tags=["Player"])


@router.post("/teams/my/players")
def create_team_player(
    player: PlayerCreateSchema,
    user: Annotated[UserSchema, Depends(require_team_captain)],
) -> PlayerSchema:
    team = team_service.get_by_leader_id(user.id)
    if team is None:
        raise EntityNotFoundException("Team was not found")

    return player_service.create_in_team(team.id, player)


@router.get("/teams/{team_id}/players", dependencies=[Depends(authenticate)])
def get_team_players(team_id: int):
    return player_service.get_all_in_team(team_id)


@router.get("/players/{player_id}", dependencies=[Depends(authenticate)])
def get_player_by_id(player_id: int):
    return player_service.get_by_id(player_id)


@router.put("/players/{player_id}")
def update_player_by_id(
    player_id: int,
    player: PlayerUpdateSchema,
    user: Annotated[UserSchema, Depends(require_team_captain)],
):
    team = team_service.get_by_leader_id(user.id)
    if team is None:
        raise EntityNotFoundException("Team was not found")

    if not player_service.is_in_team(player_id, team.id):
        raise ForbiddenException("Player doesn't belong to your team")

    return player_service.update(player_id, player)


@router.delete("/players/{player_id}")
def delete_player_by_id(
    player_id: int, user: Annotated[UserSchema, Depends(require_team_captain)]
):
    team = team_service.get_by_leader_id(user.id)
    if team is None:
        raise EntityNotFoundException("Team was not found")

    if not player_service.is_in_team(player_id, team.id):
        raise ForbiddenException("Player doesn't belong to your team")

    return player_service.delete(player_id)
