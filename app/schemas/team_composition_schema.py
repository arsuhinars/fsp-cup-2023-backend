from pydantic import BaseModel, ConfigDict

from app.schemas.player_schema import PlayerSchema
from app.schemas.team_schema import TeamSchema


class TeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team: TeamSchema
    players: list[PlayerSchema]
