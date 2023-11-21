from fastapi import APIRouter

router = APIRouter(tags=["player"])


@router.post("/teams/{team_id}/players")
def create_team_player(team_id: int, player: dict):
    pass


@router.get("/teams/{team_id}/players")
def get_team_players(team_id: int):
    pass


@router.get("/players/{player_id}")
def get_player(player_id: int):
    pass


@router.put("/players/{player_id}")
def update_player(player_id: int, player: dict):
    pass


@router.delete("/players/{player_id}")
def delete_player(player_id: int):
    pass
