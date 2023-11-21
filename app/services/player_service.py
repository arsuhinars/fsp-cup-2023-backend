import app.core.db as db
from app.models.player import Player
import app.repositories.player_repository as player_repo
from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException
from app.schemas.player_schema import PlayerSchema
from app.schemas.player_create_schema import PlayerCreateSchema
from app.schemas.player_update_schema import PlayerUpdateSchema
from app.utils import map_model_to_orm


def create(dto: PlayerCreateSchema) -> PlayerSchema:
    player = Player(**dto.model_dump())
    with db.create_session() as session:
        if player_repo.get_by_gto(session, dto.gto_id) is not None:
            raise EntityAlreadyExistsException(
                "Player with this gto_id already exists"
                )
        if player_repo.get_by_nickname(session, dto.nickname) is not None:
            raise EntityAlreadyExistsException(
                "Player with this nickname already exists"
                )
        player = player_repo.save(session, player)
        return PlayerSchema.model_validate(player)
    

def update(player_id: int, dto: PlayerUpdateSchema) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player in None:
            raise EntityNotFoundException(
                "Player not found"
            )
        if (
            player.nickname != dto.nickname
            and player_repo.get_by_nickname(session, dto.nickname) is not None
        ):
            raise EntityAlreadyExistsException(
                "Player with this nickname already exists"
            )
        map_model_to_orm(dto, player)
        player_repo.save(session, player)

        return PlayerSchema.model_validate(player)
    

def delete():
    pass
    #TODO!!!!!

def get_all() -> list[PlayerSchema]:
    with db.create_session() as session:
        players = player_repo.get_all(session)
        return list(map(PlayerSchema.model_validate, players))
    
def get_by_id(player_id: int) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player is None:
            raise EntityNotFoundException("Player not found")
        return PlayerSchema.model_validate(player)
    

def get_by_nickname(nickname: str) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_nickname(session, nickname)
        if player is None:
            raise EntityNotFoundException(
                "Player with this nickname is not found"
                )
        return PlayerSchema.model_validate(player)


def get_by_gto(gto_id: int) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_gto(session, gto_id)
        if player is None:
            raise EntityNotFoundException(
                "Player with this gto id is not found"
                )
        return PlayerSchema.model_validate(player)
