from app.models.team_composition import TeamComposition
from fastapi import APIRouter

from app.schemas.team_composition_schema import TeamCompositionSchema
from app.services import team_composition_service


router = APIRouter(tags=["team_composition"])


@router.get("teams/composition/{team_composition_id}/players")  # TODO add prefix slash
def get_team_composition_players(team_composition_id: int):
    pass


@router.post("/team_comp")
def create_team_comp(team_id: int) -> int:
    return team_composition_service.create(team_id)
