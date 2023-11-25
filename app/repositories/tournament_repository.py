from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import func

from app.models.match import Match
from app.models.team_composition import TeamComposition
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


def get_team_comps(session: Session, tournament_id: int) -> list[TeamComposition]:
    q = (
        select(TeamComposition)
        .join(TournamentSet, TournamentSet.team_composition_id == TeamComposition.id)
        .where(TournamentSet.tournament_id == tournament_id)
    )

    return session.execute(q).scalars().all()


def get_max_match_part(session: Session, tournament_id: int) -> int | None:
    q = select(func.max(Match.part_number)).where(Match.tournament_id == tournament_id)

    return session.execute(q).scalar_one_or_none()


def save(session: Session, tournament: Tournament) -> Tournament:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def delete(session: Session, tournament: Tournament) -> None:
    session.delete(tournament)
    session.commit()
