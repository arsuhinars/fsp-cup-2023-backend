from fastapi import APIRouter

router = APIRouter(prefix="/team")


@router.post("/", tags=["team"])
def post_team(name: str):
    pass


@router.get("/", tags=["team"])
def get_team(team_id: int):
    pass


@router.put("/", tags=["team"])
def update_team(team_id: int,
                name: str):
    pass


@router.delete("/", tags=["team"])
def delete_team(team_id: int):
    pass
