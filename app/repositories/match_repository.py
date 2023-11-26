from typing import Iterable

from sqlalchemy.orm import Session
from sqlalchemy.sql import and_, select

from app.models.match import Match


def get_all(session: Session) -> list[Match] | None:
    return session.query(Match).all()


def get_by_id(session: Session, match_id: int) -> Match | None:
    return session.get(Match, match_id)


def get_by_tournament_id_and_part_number(
    session: Session, tournament_id: int, part_number: int
) -> list[Match]:
    q = (
        select(Match)
        .where(
            and_(Match.tournament_id == tournament_id, Match.part_number == part_number)
        )
        .order_by(Match.order_number)
    )

    return session.execute(q).scalars().all()


def save(session: Session, match: Match) -> Match:
    session.add(match)
    session.flush()
    session.commit()
    return match


def save_all(session: Session, matches: Iterable[Match]):
    session.add_all(matches)
    session.flush()
    session.commit()


def delete(session: Session, match: Match) -> None:
    session.delete(match)
    session.commit()
