from fastapi import APIRouter

router = APIRouter(tags=["Match"])


@router.post("/tournament/{tournament_id}/matches")
def set_tournament_match(tournament_id: int, match: dict):
    pass


@router.post("/tournament/{tournament_id}/matches/generate-next")
def set_tournament_match_next(tournament_id: int):
    pass


@router.get("/tournament/{tournament_id}/matches")
def get_tournament_match(tournament_id: int):
    pass


@router.get("/matches/{match_id}")
def get_match(match_id: int):
    pass


@router.put("/matches/{match_id}")
def update_match(match_id: int, match: dict):
    pass


@router.delete("/matches/{match_id}")
def delete_match(match_id: int):
    pass
