from fastapi import APIRouter

router = APIRouter(prefix="/game")


@router.post("/", tags=["game"])
def post_game(team_a_id: int,
              team_b_id: int,
              team_winner_id: int,
              match_part: str):
    pass


@router.get("/", tags=["game"])
def get_game(game_id: int):
    pass


@router.put("/", tags=["game"])
def update_game(game_id: int,
                team_a_id: int,
                team_b_id: int,
                team_winner_id: int,
                match_part: str):
    pass


@router.delete("/", tags=["game"])
def delete_game(game_id: int):
    pass
