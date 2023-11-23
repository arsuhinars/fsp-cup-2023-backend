from app.core import db
from app.models.tournament_request import TournamentRequest
from app.schemas.tournament_request_schema import TournamentRequestSchema, TournamentRequestStatus
import app.repositories.tournament_requests_repository as tournament_request_repo


def create_request(tournament_id: int, team_comp_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        request = tournament_request_repo.save(session, TournamentRequest(
            tournament_id=tournament_id,
            team_composition_id=team_comp_id
        ))
        return TournamentRequestSchema.model_validate(request)


def get_tournament_requests(tournament_id: int) -> list[TournamentRequestSchema]:
    with db.create_session() as session:
        requests = tournament_request_repo.get_by_tournament_id(session, tournament_id)
        return [TournamentRequestSchema.model_validate(request) for request in requests]


def get_by_team_comp_id(tournament_id: int, team_comp_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        request = tournament_request_repo.get_by_tournament_id_and_team_comp_id(session, tournament_id, team_comp_id)
        return TournamentRequestSchema.model_validate(request)


def accept_request(request_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        request.status = TournamentRequestStatus.ACCEPTED
        request = tournament_request_repo.save(session, request)
        return TournamentRequestSchema.model_validate(request)


def decline_request(request_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        request.status = TournamentRequestStatus.DECLINED
        request = tournament_request_repo.save(session, request)
        return TournamentRequestSchema.model_validate(request)
