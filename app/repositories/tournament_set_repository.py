from sqlalchemy.orm import Session

from app.models.tournament_set import TournamentSet


def get_all(session: Session) -> list[TournamentSet]:
    return session.query(TournamentSet).all()


def get_by_id(
    session: Session, tournament_id: int, team_composition_id: int
) -> list[TournamentSet]:
    return (
        session.query(TournamentSet)
        .filter(
            TournamentSet.tournament_id == tournament_id,
            TournamentSet.team_composition_id == team_composition_id,
        )
        .all()
    )


def save(session: Session, tournament: TournamentSet) -> TournamentSet:
    session.add(tournament)
    session.flush()
    session.commit()
    return tournament


def delete(session: Session, tournament: TournamentSet) -> None:
    session.delete(tournament)
    session.commit()
