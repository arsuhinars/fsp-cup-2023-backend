from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class MatchSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field(examples=[1])]
    team_a_id: Annotated[int, Field(examples=[1])]
    team_b_id: Annotated[int, Field(examples=[1])]
    team_winner_id: Annotated[int, Field(examples=[1])]