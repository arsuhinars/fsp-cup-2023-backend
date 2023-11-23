from sqlalchemy.orm import Session

from app.models.tournament_request import TournamentRequest


def get_by_team_id(
    session: Session, tournament_id: int, team_id: int
) -> TournamentRequest | None:
    ...


def save(session: Session, tournament_request: TournamentRequest):
    ...
