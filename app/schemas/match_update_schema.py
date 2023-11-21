from datetime import date

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

class MatchUpdateSchema(BaseModel):
    id: int
    team_a_id: int
    team_b_id: int
    team_winner_id: int
    