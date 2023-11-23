from sqlalchemy.orm import Session

from app.models.tournament import Tournament


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
