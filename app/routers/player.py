from fastapi import APIRouter

from app.schemas.player_create_schema import PlayerCreateSchema
from app.schemas.player_schema import PlayerSchema
from app.services import player_service

router = APIRouter(tags=["player"])


@router.post("/teams/{team_id}/players")
def create_team_player(team_id: int, player: PlayerCreateSchema) -> PlayerSchema:
    player.team_id = team_id
    return player_service.create(player)


@router.get("/teams/{team_id}/players")
def get_team_players(team_id: int):
    return player_service.get_all_in_team(team_id)


@router.get("/players/{player_id}")
def get_player(player_id: int):
    return player_service.get_by_id(player_id)


@router.put("/players/{player_id}")
def update_player(player_id: int, player: PlayerUpdateSchema):
    return player_service.update(player_id, player)


@router.delete("/players/{player_id}")
def delete_player(player_id: int):
    return player_service.delete(player_id)
