from fastapi import APIRouter

router = APIRouter(prefix="/teams", tags=["team"])


@router.post("/")
def post_team(name: str):
    pass


@router.get("/")
def get_team(team_id: int):
    pass


@router.put("/")
def update_team(team_id: int,
                name: str):
    pass


@router.delete("/")
def delete_team(team_id: int):
    pass
