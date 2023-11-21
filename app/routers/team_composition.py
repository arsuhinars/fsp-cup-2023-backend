from fastapi import APIRouter

router = APIRouter(tags=["team_composition"])


@router.get("teams/composition/{team_composition_id}/players")
def get_team_composition_players(team_composition_id: int):
    pass
