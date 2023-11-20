from fastapi import APIRouter

router = APIRouter(prefix="/game", tags=["game"])


@router.post("/")
def post_game(team_a_id: int,
              team_b_id: int,
              team_winner_id: int,
              match_part: str):
    pass


@router.get("/")
def get_game(game_id: int):
    pass


@router.put("/")
def update_game(game_id: int,
                team_a_id: int,
                team_b_id: int,
                team_winner_id: int,
                match_part: str):
    pass


@router.delete("/")
def delete_game(game_id: int):
    pass
