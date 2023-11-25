import app.core.db as db
import app.repositories.tournament_repository as tournament_repo
from app.exceptions import EntityNotFoundException
from app.models.tournament import Tournament
from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_schema import (
    TournamentCreateSchema,
    TournamentSchema,
    TournamentStateEnum,
    TournamentUpdateSchema,
)
from app.utils import map_model_to_orm


def create(dto: TournamentCreateSchema, main_judge_id: int) -> TournamentSchema:
    tournament = Tournament(**dto.model_dump())
    with db.create_session() as session:
        tournament.main_judge_id = main_judge_id
        return TournamentSchema.model_validate(
            tournament_repo.save(session, tournament)
        )


def get_all() -> list[TournamentSchema]:
    with db.create_session() as session:
        return list(
            map(TournamentSchema.model_validate, tournament_repo.get_all(session))
        )


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
        return list(
            map(
                lambda ts: TeamCompositionSchema.model_validate(ts.team_composition),
                tournament.tournament_sets,
            )
        )


def update(tournament_id: int, dto: TournamentUpdateSchema) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        map_model_to_orm(dto, tournament)
        tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")

        if tournament.state != TournamentStateEnum.JUST_CREATED:
            raise Exception("Can't delete tournament on current stage")

        tournament_repo.delete(session, tournament)
        return True


def change_state(tournament_id: int, state: TournamentStateEnum) -> TournamentSchema:
    tournament = get_by_id(tournament_id)
    match tournament.state, state:
        case TournamentStateEnum.JUST_CREATED, TournamentStateEnum.REGISTRATION_OPENED:
            tournament.state = state
            return update(tournament_id, TournamentUpdateSchema(state=state))
        case TournamentStateEnum.REGISTRATION_OPENED, TournamentStateEnum.REGISTRATION_CLOSED:
            tournament.state = state
            return update(tournament_id, TournamentUpdateSchema(state=state))
        case TournamentStateEnum.REGISTRATION_CLOSED, TournamentStateEnum.ONGOING:
            tournament.state = state
            return update(tournament_id, TournamentUpdateSchema(state=state))
        case TournamentStateEnum.ONGOING, TournamentStateEnum.FINISHED:
            tournament.state = state
            return update(tournament_id, TournamentUpdateSchema(state=state))
        case _:
            raise Exception("Can't change state")
