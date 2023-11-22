import app.core.db as db
from app.models.team_composition import TeamComposition
from app.models.tournament import Tournament
import app.repositories.tournament_repository as tournament_repo
import app.repositories.tournament_set_repository as tournament_set_repo
from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException, InvalidFormatException
from app.models.tournament_set import TournamentSet
from app.schemas.tournament_create_schema import TournamentCreateSchema
from app.schemas.tournament_schema import TournamentSchema
from app.schemas.tournament_update_schema import TournamentUpdateSchema
from app.utils import map_model_to_orm


def create(dto: TournamentCreateSchema) -> TournamentSchema:
    tournament = Tournament(**dto.model_dump())
    with db.create_session() as session:
        if tournament_repo.get_by_name(session, dto.name) is not None:
            raise EntityAlreadyExistsException(
                "Tournament with this name already exists"
            )
        return TournamentSchema.model_validate(tournament_repo.save(session, tournament))


def set_team_comps(tournament_id: int, team_comp_ids: list[int]) -> list[int]:
    if len(team_comp_ids) != 32:
        raise InvalidFormatException("Invalid number of teams")
    with db.create_session() as session:
        return list(
            map(lambda ts: ts.id,
                tournament_set_repo.save_all(
                    session,
                    map(lambda order, team_comp_id: TournamentSet(tournament_id=tournament_id,
                                                                  team_composition_id=team_comp_id,
                                                                  order_number=order
                                                                  ),
                        enumerate(team_comp_ids)))))


def get_all() -> list[TournamentSchema]:
    with db.create_session() as session:
        tournaments = tournament_repo.get_all(session)
        return [TournamentSchema.model_validate(tournament) for tournament in tournaments]


def get_by_id(tournament_id: int) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        return TournamentSchema.model_validate(tournament)


def get_by_name(name: str) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_name(session, name)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        return TournamentSchema.model_validate(tournament)


def get_team_comps(tournament_id: int) -> list[TeamComposition]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        return tournament.team_compositions


def update(tournament_id: int, dto: TournamentUpdateSchema) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")

        map_model_to_orm(dto, tournament)
        tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        tournament_repo.delete(session, tournament)
        return True
