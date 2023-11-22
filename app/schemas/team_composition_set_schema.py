from pydantic import BaseModel, ConfigDict


class TeamCompositionSetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    team_composition_id: int
    player_id: int
    