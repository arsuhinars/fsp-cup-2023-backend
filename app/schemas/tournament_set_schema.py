from pydantic import BaseModel, ConfigDict

from app.schemas.team_composition_schema import ShortTeamCompositionSchema


class TournamentSetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    team_composition: ShortTeamCompositionSchema
    result_place: int
