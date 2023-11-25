import app.core.db as db
import app.repositories.match_repository as match_repo
from app.exceptions import EntityNotFoundException
from app.models.match import Match
from app.schemas.match_schema import MatchSchema, UpdateMatchSchema
from app.utils import map_model_to_orm


def create(dto: MatchSchema) -> MatchSchema:
    match = Match(**dto.model_dump())
    with db.create_session() as session:
        match = match_repo.save(session, match)
        return MatchSchema.model_validate(match)


def update(match_id: int, dto: UpdateMatchSchema) -> MatchSchema:
    with db.create_session() as session:
        match = match_repo.get_by_id(session, match_id)
        if match is None:
            raise EntityNotFoundException("Match not found")
        map_model_to_orm(dto, match)
        match_repo.save(session, match)

        return MatchSchema.model_validate(match)


def delete(match_id: int) -> None:
    with db.create_session() as session:
        match = match_repo.get_by_id(session, match_id)
        if match is None:
            raise EntityNotFoundException("Match not found")
        match_repo.delete(session, match)


def get_by_id(match_id: int) -> MatchSchema:
    with db.create_session() as session:
        match = match_repo.get_by_id(session, match_id)
        if match is None:
            raise EntityNotFoundException("Match not found")
        return MatchSchema.model_validate(match)
