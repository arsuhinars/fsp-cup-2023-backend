from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from app.schemas.player_schema import ShortPlayerSchema
from app.schemas.team_schema import TeamSchema


class TournamentRequestStatus(StrEnum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"


class TournamentRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team: TeamSchema
    active_players: list[ShortPlayerSchema]
    status: TournamentRequestStatus
