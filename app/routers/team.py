from fastapi import APIRouter

router = APIRouter(prefix="/teams", tags=["team"])


@router.post("/")
def create_team(name: str):
    pass


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
