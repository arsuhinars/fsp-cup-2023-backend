from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException
from app.models.tournament import Tournament
from app.schemas.tournament_create_schema import TournamentCreateSchema
from app.schemas.tournament_schema import TournamentSchema
import app.repositories.tournament_repository as tournament_repo
import app.core.db as db
from app.schemas.tournament_update_schema import TournamentUpdateSchema

def create(tournament: TournamentCreateSchema) -> TournamentSchema:
    tournament = TournamentCreateSchema.model_validate(tournament).to_Model()
    with db.create_session() as session:
        if tournament_repo.get_by_name(session, tournament.name) is not None:
            raise EntityAlreadyExistsException("Tournament with this name already exists")
        return TournamentSchema.from_model(tournament_repo.save(session, tournament))

def get_all() -> list[TournamentSchema]:
    with db.create_session() as session:
        tournaments = tournament_repo.get_all(session)
        return [TournamentSchema.from_model(tournament) for tournament in tournaments]
    
def get_by_id(tournament_id: int) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        return TournamentSchema.from_model(tournament)
    
def get_by_name(name: str) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_name(session, name)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        return TournamentSchema.from_model(tournament)

def update(tournament_id: int, tournament: TournamentUpdateSchema) -> TournamentSchema:
    TournamentUpdateSchema.model_validate(tournament)
    with db.create_session() as session:
        db_tournament = tournament_repo.get_by_id(session, tournament_id)
        if db_tournament is None:
            raise EntityNotFoundException("Tournament not found")
        db_tournament = tournament_repo.save(session, tournament.to_model(db_tournament))
        return TournamentSchema.from_model(db_tournament)
    
def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament not found")
        tournament_repo.delete(session, tournament)
        return True