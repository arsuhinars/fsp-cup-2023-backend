from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_request_schema import TournamentRequestSchema
from app.schemas.tournament_schema import (
    TournamentCreateSchema,
    TournamentSchema,
    TournamentUpdateSchema,
)
from app.schemas.user_schema import UserSchema
from app.security import authenticate, require_judge, require_team_captain
from app.services import tournament_service
from app.services import tournament_requests_service

router = APIRouter(prefix="/tournaments", tags=["Tournament"])


@router.post("/", response_model=TournamentSchema)
def create_tournament(
        tournament: TournamentCreateSchema,
        user: Annotated[UserSchema, Depends(require_judge)],
) -> TournamentSchema:
    return tournament_service.create(tournament, user.id)


@router.get(
    "/", response_model=list[TournamentSchema], dependencies=[Depends(authenticate)]
)
def get_all_tournaments():
    return tournament_service.get_all()


@router.get(
    "/{tournament_id}",
    response_model=TournamentSchema,
    dependencies=[Depends(authenticate)],
)
def get_tournament_by_id(tournament_id: int):
    return tournament_service.get_by_id(tournament_id)


@router.put("/{tournament_id}")
def update_tournament(
        tournament_id: int,
        tournament: TournamentUpdateSchema,
        user: Annotated[UserSchema, Depends(require_judge)],
) -> TournamentSchema:
    # TODO проверка на судью
    return tournament_service.update(tournament_id, tournament)


@router.delete("/{tournament_id}")
def delete_tournament(tournament_id: int) -> bool:
    return tournament_service.delete(tournament_id)


@router.get(
    "/{tournament_id}/team_compositions",
    response_model=list[TeamCompositionSchema],
    dependencies=[Depends(authenticate)],
)
def get_tournament_team_compositions(tournament_id: int):
    return tournament_service.get_team_comps(tournament_id)


# @router.get("/{tournament_id}/requests", response_model=list[TournamentRequestSchema])
# def get_tournament_requests(
#         tournament_id: int,
#         user: Annotated[UserSchema, Depends(require_judge)],
# ):
#     return tournament_requests_service.get_by_tournament_id(tournament_id)
#
#
# @router.get("/{tournament_id}/requests/my", response_model=TournamentRequestSchema)
# def get_my_tournament_request(
#         tournament_id: int,
#         user: Annotated[UserSchema, Depends(require_team_captain)],
# ):
#     return tournament_requests_service.get_by_tournament_id(tournament_id)
#
#
# @router.post("/{tournament_id}/requests", response_model=TournamentRequestSchema)
# def create_tournament_request(
#         tournament_id: int,
#         user: Annotated[UserSchema, Depends(require_team_captain)]
# ):
#     return tournament_requests_service.create_request(tournament_id, user.team)
#
#
# @router.post("/requests/{request_id}/accept")
# def accept_tournament_request(
#         request_id: int,
#         user: Annotated[UserSchema, Depends(require_judge)]
# ):
#     return tournament_requests_service.accept_request(request_id)
