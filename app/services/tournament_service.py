import app.core.db as db
import app.repositories.tournament_repository as tournament_repo
from app.exceptions import EntityNotFoundException
from app.models.tournament import Tournament
from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_schema import (
    TournamentCreateSchema,
    TournamentSchema,
    TournamentUpdateSchema,
)
from app.utils import map_model_to_orm


def create(dto: TournamentCreateSchema, main_judge_id: int) -> TournamentSchema:
    tournament = Tournament(**dto.model_dump())
    with db.create_session() as session:
        # TODO

        return TournamentSchema.model_validate(
            tournament_repo.save(session, tournament)
        )


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
        # FIXME: возвращать схему, а не класс
        return tournament.team_compositions


def update(tournament_id: int, dto: TournamentUpdateSchema) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        # TODO: проверка статуса турнира

        map_model_to_orm(dto, tournament)
        tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")

        # TODO: проверка состояния

        tournament_repo.delete(session, tournament)
        return True
