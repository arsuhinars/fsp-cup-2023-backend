from sqlalchemy.sql import select
import app.repositories.team_composition_set_repository as team_comp_set_repo
from app.models.player import Player

def get_all(session) -> list[Player]:
    return session.query(Player).all()
    

def get_by_id(session, player_id: int) -> Player | None:
    return session.get(Player, player_id)


def get_by_gto(session, gto_id: int) -> Player | None:
    return session.get(Player, gto_id)


def get_by_nickname(session, nickname: str) -> Player | None:
    result = session.execute(select(Player).where(Player.nickname == nickname).limit(1))
    return result.scalar_one_or_none()


def save(session, player: Player) -> Player:
    session.add(player)
    session.flush()
    session.commit()
    return player


def delete(session, player: Player):
    pass
    #TODO!!!!!