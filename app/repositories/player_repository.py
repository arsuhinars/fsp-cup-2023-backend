from sqlalchemy.orm import Session

from app.models.player import Player


def get_by_id(session: Session, player_id: int) -> Player | None:
    return session.get(Player, player_id)


def get_active_by_team_id(session: Session, team_id: int) -> list[Player]:
    # FIXME idk, что тут с типизацией, правда
    return session.query(Player) \
        .filter(Player.is_active) \
        .filter(Player.team_id == team_id) \
        .all()


def save(session: Session, player: Player) -> Player:
    session.add(player)
    session.flush()
    session.commit()
    return player


def soft_delete(session: Session, player: Player):
    player.deleted = True
    save(session, player)
