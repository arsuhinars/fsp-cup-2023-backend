from fastapi import APIRouter, Depends

from app.schemas.match_schema import MatchSchema, UpdateMatchSchema
from app.schemas.tournament_schema import TournamentSchema, TournamentStartSchema
from app.security import authenticate, require_judge
from app.services import tournament_service

router = APIRouter(prefix="/tournaments", tags=["Tournament"])


@router.post(
    "/{tournament_id}/start",
    response_model=TournamentSchema,
    dependencies=[Depends(require_judge)],
)
def start_tournament(tournament_id: int, body: TournamentStartSchema):
    return tournament_service.start_tournament(tournament_id, body)


@router.get(
    "/{tournament_id}/matches",
    response_model=list[MatchSchema],
    dependencies=[Depends(authenticate)],
)
def get_all_tournament_matches(tournament_id: int):
    return tournament_service.get_all_matches(tournament_id)


@router.put(
    "/matches/{match_id}",
    response_model=MatchSchema,
    dependencies=[Depends(require_judge)],
)
def set_tournament_match_winner(match_id: int, match: UpdateMatchSchema):
    return tournament_service.update_match_winner(
        match_id, match.team_composition_winner_id
    )


@router.post("/{tournament_id}/matches/next", dependencies=[Depends(require_judge)])
def start_next_tournament_matches(tournament_id: int):
    tournament_service.start_next_matches(tournament_id)


@router.post("/{tournament_id}/finish", dependencies=[Depends(require_judge)])
def finish_tournament(tournament_id: int):
    return tournament_service.finish_tournament(tournament_id)
