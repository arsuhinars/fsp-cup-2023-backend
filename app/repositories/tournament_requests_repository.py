from sqlalchemy.orm import Session
from sqlalchemy.sql import and_, select

from app.models.team_composition import TeamComposition
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
    q = (
        select(TournamentRequest)
        .where(
            TournamentRequest.tournament_id == tournament_id
            and TournamentRequest.team_composition_id == team_comp_id
        )
        .limit(1)
    )

    return session.execute(q).scalar_one_or_none()


def get_by_id(session: Session, request_id: int) -> TournamentRequest | None:
    return session.query(TournamentRequest).get(request_id)


def get_by_tournament_id_and_team_id(
    session: Session, tournament_id: int, team_id: int
) -> TournamentRequest | None:
    q = (
        select(TournamentRequest)
        .join(
            TeamComposition, TournamentRequest.team_composition_id == TeamComposition.id
        )
        .where(
            and_(
                TournamentRequest.tournament_id == tournament_id,
                TeamComposition.team_id == team_id,
            )
        )
        .limit(1)
    )

    return session.execute(q).scalar_one_or_none()
