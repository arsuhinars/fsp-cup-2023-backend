from pydantic import BaseModel, ConfigDict


class MatchSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team_a_id: int
    team_b_id: int
    team_winner_id: int


class MatchCreateSchema(BaseModel):
    id: int
    team_a_id: int
    team_b_id: int


class MatchUpdateSchema(BaseModel):
    id: int
    team_a_id: int
    team_b_id: int
    team_winner_id: int
