from app.schemas.tournament_request_schema import TournamentRequestSchema


def create_request(tournament_id: int, team_id: int) -> TournamentRequestSchema:
    ...


def get_tournament_requests(tournament_id: int) -> list[TournamentRequestSchema]:
    ...


def get_by_team_id(tournament_id: int, team_id: int) -> TournamentRequestSchema:
    ...


def accept_request(request_id: int) -> TournamentRequestSchema:
    ...


def decline_request(request_id: int) -> TournamentRequestSchema:
    ...
