from sqlalchemy.orm import Session

from app.models.tournament import Tournament
from app.models.tournament_set import TournamentSet


def get_all(session: Session) -> list[Tournament]:
    return session.query(Tournament).all()


def get_by_id(session: Session, tournament_id: int) -> Tournament | None:
    return session.get(Tournament, tournament_id)


def get_set_by_team_comp_id(
    session: Session, tournament_id: int, team_composition_id: int
) -> TournamentSet | None:
    return session.get(TournamentSet, (tournament_id, team_composition_id))


def save(session: Session, tournament: Tournament) -> Tournament:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def delete(session: Session, tournament: Tournament) -> None:
    session.delete(tournament)
    session.commit()
