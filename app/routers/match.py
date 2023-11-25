from fastapi import APIRouter
from app.services import match_service
router = APIRouter(tags=["Match"])


@router.post("/tournament/{tournament_id}/matches")
def set_tournament_match(tournament_id: int, match: dict):
    return match_service.create(tournament_id, match)


@router.post("/tournament/{tournament_id}/matches/generate-next")
def set_tournament_match_next(tournament_id: int):
    return match_service.create(tournament_id)


@router.get("/tournament/{tournament_id}/matches")
def get_tournament_match(tournament_id: int):
    return match_service.get_by_id(tournament_id)


@router.get("/matches/{match_id}")
def get_match(match_id: int):
    return match_service.get_by_id(match_id)


@router.put("/matches/{match_id}")
def update_match(match_id: int, match: dict):
    return match_service.update(match_id, match)


@router.delete("/matches/{match_id}")
def delete_match(match_id: int):
    return match_service.delete(match_id)
