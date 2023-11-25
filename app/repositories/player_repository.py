from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.player import Player


def get_by_id(session: Session, player_id: int) -> Player | None:
    return session.get(Player, player_id)


def get_by_team_id(session: Session, team_id: int) -> list[Player]:
    q = select(Player).where(Player.team_id == team_id).order_by(Player.id)
    return session.execute(q).scalars().all()


def save(session: Session, player: Player) -> Player:
    session.add(player)
    session.flush()
    session.commit()
    return player


def soft_delete(session: Session, player: Player):
    player.deleted = True
    save(session, player)
