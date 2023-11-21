from sqlalchemy.sql import select

from app.models.tournament import Tournament


def get_all(session) -> list[Tournament]:
    return session.query(Tournament).all()


def get_by_id(session, tournament_id: int) -> Tournament | None:
    return session.get(Tournament, tournament_id)


def get_by_name(session, name: str) -> Tournament | None:
    result = session.execute(select(Tournament).where(Tournament.name == name).limit(1))
    return result.scalar_one_or_none()


def save(session, tournament: Tournament) -> Tournament:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def delete(session, tournament: Tournament) -> None:
    session.delete(tournament)
    session.commit()
