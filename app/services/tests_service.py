from app.schemas.match_create_schema import MatchCreateSchema
import match_service
import password_service
import player_service
import team_composition_service
import team_service
import tournament_service
import user_service


def create_match_test(dto: MatchCreateSchema) -> None:
    match = match_service.create()