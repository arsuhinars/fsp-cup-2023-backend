from fastapi import APIRouter

router = APIRouter(prefix="/team_composition", tags=["team_composition"])


@router.post("/")
def post_team_composition(team_id: int):
    pass


@router.get("/")
def get_team_composition(team_composition_id: int):
    pass


@router.delete("/")
def delete_team_composition(team_composition_id: int):
    pass
