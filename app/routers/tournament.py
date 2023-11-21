from fastapi import APIRouter

router = APIRouter(prefix="/tournaments", tags=["tournament"])


@router.post("/")
def create_tournament(tournament: dict):
    pass


@router.post("/{tournament_id}/set")
def set_tournament_set(tournament_id: int, tournament_set: dict):
    pass


@router.get("/")
def get_all_tournaments():
    pass


@router.get("/{tournament_id}")
def get_tournament(tournament_id: int):
    pass


@router.get("/{tournament_id}/set")
def get_tournament_set(tournament_id: int):
    pass


@router.put("/{tournament_id}")
def update_tournament(tournament_id: int, tournament: dict):
    pass


@router.delete("/{tournament_id}")
def delete_tournament(tournament_id: int):
    pass
