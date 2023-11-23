import app.core.db as db
import app.repositories.tournament_repository as tournament_repo
from app.exceptions import EntityNotFoundException
from app.models.tournament import Tournament
from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_request_schema import TournamentRequestSchema
from app.schemas.tournament_schema import (
    TournamentCreateSchema,
    TournamentSchema,
    TournamentUpdateSchema, TournamentStateEnum,
)
from app.utils import map_model_to_orm


def create(dto: TournamentCreateSchema, main_judge_id: int) -> TournamentSchema:
    tournament = Tournament(**dto.model_dump())
    with db.create_session() as session:
        tournament.main_judge_id = main_judge_id
        return TournamentSchema.model_validate(tournament_repo.save(session, tournament))


def get_all() -> list[TournamentSchema]:
    with db.create_session() as session:
        tournaments = tournament_repo.get_all(session)
        return list(map(TournamentSchema.model_validate, tournaments))


def get_by_id(tournament_id: int) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")
        return TournamentSchema.model_validate(tournament)


def get_team_comps(tournament_id: int) -> list[TeamCompositionSchema]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")
        return list(map(
            lambda ts: TeamCompositionSchema.model_validate(ts.team_composition),
            tournament.tournament_sets))


def get_tournament_requests_by_tournament_id(tournament_id) -> list[TournamentRequestSchema]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")
        return list(map(
            lambda tr: TournamentRequestSchema.model_validate(tr),
            tournament.tournament_requests
        ))


def update(tournament_id: int, dto: TournamentUpdateSchema) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state == TournamentStateEnum.JUST_CREATED \
                and dto.state != TournamentStateEnum.REGISTRATION_OPENED \
                or tournament.state == TournamentStateEnum.REGISTRATION_OPENED \
                and dto.state != TournamentStateEnum.REGISTRATION_CLOSED \
                or tournament.state == TournamentStateEnum.REGISTRATION_CLOSED \
                and dto.state != TournamentStateEnum.ONGOING \
                or tournament.state == TournamentStateEnum.ONGOING \
                and dto.state != TournamentStateEnum.FINISHED:
            raise Exception("Can't change tournament state")

        map_model_to_orm(dto, tournament)
        tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        if tournament.state not in (TournamentStateEnum.JUST_CREATED, TournamentStateEnum.FINISHED):
            raise Exception("Can't delete tournament on current stage")
        tournament_repo.delete(session, tournament)
        return True


def get_tournament_request_by_tournament_id_and_captain_id(
        tournament_id: int,
        captain_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        return TournamentRequestSchema.model_validate(
            tournament_repo.get_tournament_request_by_tournament_id_and_captain_id(
                session,
                tournament_id,
                captain_id))
