from datetime import date

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

class MatchCreateSchema(BaseModel):
    id: int
    team_a_id: int
    team_b_id: int