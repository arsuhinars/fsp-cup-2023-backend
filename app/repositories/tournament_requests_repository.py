from sqlalchemy.orm import Session

from app.models.tournament import Tournament
from app.models.tournament_request import TournamentRequest


def get_by_team_comp_id(
    session: Session, tournament_id: int, team_composition_id: int
) -> TournamentRequest | None:
    return (
        session.query(TournamentRequest)
        .where(
            TournamentRequest.tournament_id == tournament_id,
            TournamentRequest.team_composition_id == team_composition_id,
        )
        .first()
    )


def save(session: Session, tournament_request: TournamentRequest) -> TournamentRequest:
    session.add(tournament_request)
    session.flush()
    session.commit()
    return tournament_request


def get_by_tournament_id(
    session: Session, tournament_id: int
) -> list[TournamentRequest]:
    return (
        session.query(TournamentRequest)
        .filter(TournamentRequest.tournament_id == tournament_id)
        .all()
    )


def get_by_tournament_id_and_team_comp_id(
    session: Session, tournament_id: int, team_comp_id: int
) -> TournamentRequest | None:
    return (
        session.query(TournamentRequest)
        .filter(
            TournamentRequest.tournament_id == tournament_id,
            TournamentRequest.team_composition_id == team_comp_id,
        )
        .first()
    )


def get_by_id(session: Session, request_id: int) -> TournamentRequest | None:
    return session.query(TournamentRequest).get(request_id)


def get_by_tournament_id_and_captain_id(
    session: Session, tournament_id: int, captain_id: int
) -> TournamentRequest | None:
    # TODO: сделать через JOIN запрос

    return [
        tr
        for tr in session.get(Tournament, tournament_id).tournament_requests
        if tr.captain_id == captain_id
    ][0]
