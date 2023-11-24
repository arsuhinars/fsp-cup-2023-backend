from sqlalchemy.orm import Session

from app.models.tournament import Tournament
from app.models.tournament_request import TournamentRequest


def get_all(session: Session) -> list[Tournament]:
    return session.query(Tournament).all()


def get_by_id(session: Session, tournament_id: int) -> Tournament | None:
    return session.get(Tournament, tournament_id)


def save(session: Session, tournament: Tournament) -> Tournament:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def delete(session: Session, tournament: Tournament) -> None:
    session.delete(tournament)
    session.commit()


def get_tournament_request_by_tournament_id_and_captain_id(
        session: Session,
        tournament_id: int,
        captain_id: int) -> TournamentRequest | None:
    return [tr for tr in session.get(Tournament, tournament_id).tournament_requests if tr.captain_id == captain_id][0]
