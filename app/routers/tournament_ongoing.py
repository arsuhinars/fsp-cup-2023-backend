from fastapi import APIRouter, Depends

from app.schemas.match_schema import MatchSchema, UpdateMatchSchema
from app.schemas.tournament_schema import TournamentStartSchema
from app.security import require_judge

router = APIRouter(prefix="/tournaments", tags=["Tournament"])


@router.post("/{tournament_id}/start", dependencies=[Depends(require_judge)])
def start_tournament(tournament_id: int, body: TournamentStartSchema):
    ...


@router.get("/{tournament_id}/matches", response_model=list[MatchSchema])
def get_all_tournament_matches(tournament_id: int):
    ...


@router.put(
    "/matches/{match_id}",
    response_model=MatchSchema,
    dependencies=[Depends(require_judge)],
)
def set_tournament_match_winner(match_id: int, match: UpdateMatchSchema):
    ...


@router.post("/{tournament_id}/matches/next", dependencies=[Depends(require_judge)])
def start_next_tournament_matches(tournament_id: int):
    ...


@router.post("/{tournament_id}/finish", dependencies=[Depends(require_judge)])
def finish_tournament(tournament_id: int):
    ...
