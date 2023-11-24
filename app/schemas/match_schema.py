from pydantic import BaseModel, ConfigDict

from app.schemas.team_composition_schema import ShortTeamCompositionSchema


class MatchSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team_composition_a: ShortTeamCompositionSchema
    team_composition_b: ShortTeamCompositionSchema
    team_composition_winner_id: int | None
    order_number: int
    part_number: int


class UpdateMatchSchema(BaseModel):
    team_composition_winner_id: int
