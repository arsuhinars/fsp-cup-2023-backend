from typing import Annotated

from pydantic import AliasPath, BaseModel, ConfigDict, Field

from app.schemas.player_schema import PlayerSchema
from app.schemas.team_schema import TeamSchema


class TeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team: TeamSchema
    players: list[PlayerSchema]


class ShortTeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team_id: Annotated[int, Field(serialization_alias=AliasPath("team", "id"))]
    team_name: Annotated[str, Field(serialization_alias=AliasPath("team", "name"))]
