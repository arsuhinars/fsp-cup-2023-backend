from typing import Iterable

from sqlalchemy.sql import select

from app.models.tournament_set import TournamentSet


def get_all(session) -> list[TournamentSet]:
    return session.query(TournamentSet).all()


def get_by_id(session, tournament_id: int, team_composition_id: int) -> list[TournamentSet]:
    return session.select(TournamentSet).where(
        TournamentSet.tournament_id == tournament_id,
        TournamentSet.team_composition_id == team_composition_id
    )


def save(session, tournament: TournamentSet) -> TournamentSet:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def save_all(session, tournaments: Iterable[TournamentSet]) -> Iterable[TournamentSet]:
    session.add_all(tournaments)
    session.flush()
    session.commit()
    return tournaments


def delete(session, tournament: TournamentSet) -> None:
    session.delete(tournament)
    session.commit()
