from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.player import Player
from app.models.team_composition_set import TeamCompositionSet
from app.repositories import team_composition_repository


def get_all(session: Session) -> list[Player]:
    q = select(Player).where(not Player.deleted)
    return session.execute(q).all()


def get_by_id(session: Session, player_id: int) -> Player | None:
    return session.get(Player, player_id)


def get_by_team_id(session: Session, team_id: int) -> list[Player]:
    q = select(Player).where(Player.team_id == team_id and not Player.deleted)
    return session.execute(q).all()


def is_active_in_team(session: Session, player_id: int, team_id: int) -> bool:
    composition = team_composition_repository.get_active_by_team_id(session, team_id)
    if composition is None:
        return False

    q = (
        select(TeamCompositionSet)
        .where(
            TeamCompositionSet.team_composition_id == composition.id
            and TeamCompositionSet.player_id == player_id
        )
        .exists()
    )

    return session.execute(select(q)).scalar_one()


def save(session: Session, player: Player) -> Player:
    session.add(player)
    session.flush()
    session.commit()
    return player


def soft_delete(session: Session, player: Player):
    player.deleted = True
    save(session, player)
