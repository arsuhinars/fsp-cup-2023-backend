from datetime import date

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

class MatchSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    team_a_id: Annotated[int, Field(examples=[1])]
    team_b_id: Annotated[int, Field(examples=[1])]
    team_winner_id: Annotated[int, Field(examples=[1])]