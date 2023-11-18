from fastapi import APIRouter

router = APIRouter(prefix="/team_composition")


@router.post("/", tags=["team_composition"])
def post_team_composition(team_id: int):
    pass


@router.get("/", tags=["team_composition"])
def get_team_composition(team_composition_id: int):
    pass


@router.delete("/", tags=["team_composition"])
def delete_team_composition(team_composition_id: int):
    pass
