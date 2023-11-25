from pydantic import BaseModel, ConfigDict

from app.schemas.player_schema import ShortPlayerSchema
from app.schemas.team_schema import TeamSchema


class TeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team: TeamSchema
    players: list[ShortPlayerSchema]


class ShortTeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team_id: int
    team_name: str
