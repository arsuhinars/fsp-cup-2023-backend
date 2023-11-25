from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.tournament_request_schema import TournamentRequestSchema
from app.schemas.user_schema import UserSchema
from app.security import require_judge, require_team_captain
from app.services import tournament_requests_service

router = APIRouter(prefix="/tournaments", tags=["Tournament"])


@router.post(
    "/{tournament_id}/start_registartion", dependencies=[Depends(require_judge)]
)
def start_tournament_registration(tournament_id: int):
    ...


@router.post(
    "/{tournament_id}/close_registartion", dependencies=[Depends(require_judge)]
)
def close_tournament_registration(tournament_id: int):
    ...


@router.get("/{tournament_id}/requests", response_model=list[TournamentRequestSchema])
def get_tournament_requests(
    tournament_id: int,
    user: Annotated[UserSchema, Depends(require_judge)],
):
    return tournament_requests_service.get_by_tournament_id(tournament_id)


@router.get("/{tournament_id}/requests/my", response_model=TournamentRequestSchema)
def get_my_tournament_request(
    tournament_id: int,
    user: Annotated[UserSchema, Depends(require_team_captain)],
):
    return tournament_requests_service.get_by_captain_id(tournament_id, user.id)


@router.post("/{tournament_id}/requests", response_model=TournamentRequestSchema)
def create_tournament_request(
    user: Annotated[UserSchema, Depends(require_team_captain)]
):
    ...


@router.post("/requests/{request_id}/accept")
def accept_tournament_request(
    request_id: int, user: Annotated[UserSchema, Depends(require_judge)]
):
    ...


@router.post("/requests/{request_id}/decline")
def decline_tournament_request(
    request_id: int, user: Annotated[UserSchema, Depends(require_judge)]
):
    ...
