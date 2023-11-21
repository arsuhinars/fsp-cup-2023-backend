from sqlalchemy.sql import select

from app.models.match import Match

def get_all(session) -> list[Match] | None:
    return session.query(Match).all()


def get_by_id(session, match_id: int) -> Match | None:
    return session.get(Match, match_id)


def save(session, match: Match) -> Match:
    session.add(match)
    session.flush()
    session.commit()
    return match


def delete(session, match: Match) -> None:
    session.delete(match)
    session.commit()