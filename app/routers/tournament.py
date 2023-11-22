from fastapi import APIRouter

from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_create_schema import TournamentCreateSchema
from app.schemas.tournament_schema import TournamentSchema
from app.schemas.tournament_update_schema import TournamentUpdateSchema
from app.services import tournament_service

router = APIRouter(prefix="/tournaments", tags=["tournament"])


@router.post("/")
def create_tournament(tournament: TournamentCreateSchema) -> TournamentSchema:
    return tournament_service.create(tournament)


@router.post("/{tournament_id}/set")
def set_tournament_set(tournament_id: int, team_ids: list[int]) -> list[int]:
    return tournament_service.set_team_comps(tournament_id, team_ids)


@router.get("/")
def get_all_tournaments():
    return tournament_service.get_all()


@router.get("/{tournament_id}")
def get_tournament(tournament_id: int):
    return tournament_service.get_by_id(tournament_id)


@router.get("/{tournament_id}/set")
def get_tournament_team_comps(tournament_id: int) -> list[TeamCompositionSchema]:
    return list(map(
        lambda team_comp: TeamCompositionSchema.model_validate(team_comp),
        tournament_service.get_team_comps(tournament_id)))


@router.put("/{tournament_id}")
def update_tournament(tournament_id: int, tournament: TournamentUpdateSchema) -> TournamentSchema:
    return tournament_service.update(tournament_id, tournament)


@router.delete("/{tournament_id}")
def delete_tournament(tournament_id: int) -> bool:
    return tournament_service.delete(tournament_id)
