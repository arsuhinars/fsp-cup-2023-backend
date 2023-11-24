import app.repositories.player_repository as player_repo
import app.repositories.team_repository as team_repo
from app.core import db
from app.exceptions import EntityNotFoundException
from app.models.player import Player
from app.models.team_composition import TeamComposition
from app.schemas.player_schema import (
    PlayerCreateSchema,
    PlayerSchema,
    PlayerUpdateSchema,
    ShortPlayerSchema,
)
from app.utils import map_model_to_orm


def create_in_team(team_id: int, dto: PlayerCreateSchema) -> PlayerSchema:
    player = Player(**dto.model_dump())
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team was not found")

        player.team = team
        player = player_repo.save(session, player)

        session.refresh(player)

        return PlayerSchema.model_validate(player.convert_to_dict())


def get_team_players(team_id: int) -> list[ShortPlayerSchema]:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team was not found")

        active_composition = team_repo.get_active_composition(session, team)
        players = map(
            lambda p: p.convert_to_dict(active_composition),
            team.players,
        )

        return list(map(PlayerSchema.model_validate, players))


def get_by_id(player_id: int) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player is None:
            raise EntityNotFoundException("Player was not found")

        active_composition = team_repo.get_active_composition(session, player.team)

        return PlayerSchema.model_validate(player.convert_to_dict(active_composition))


def is_in_team(player_id: int, team_id: int) -> bool:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player is None:
            raise EntityNotFoundException("Player was not found")

        return player.team_id == team_id


def update(player_id: int, dto: PlayerUpdateSchema) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player is None or player.deleted:
            raise EntityNotFoundException("Player was not found")

        active_composition = team_repo.get_active_composition(session, player.team)
        is_active_in_team = player.is_active_in_composition(active_composition)

        if dto.is_active_in_team and not is_active_in_team:
            if active_composition is None:
                active_composition = TeamComposition(team_id=player.team_id)
                session.add(active_composition)

            active_composition.players.add(player)
        elif not dto.is_active_in_team and is_active_in_team:
            active_composition.players.remove(player)

        map_model_to_orm(dto, player)
        player = player_repo.save(session, player)

        session.refresh(player)

        return PlayerSchema.model_validate(player.convert_to_dict(active_composition))


def delete(player_id: int) -> PlayerSchema:
    with db.create_session() as session:
        player = player_repo.get_by_id(session, player_id)
        if player is None or player.deleted:
            raise EntityNotFoundException("Player was not found")
        player_repo.soft_delete(session, player)
