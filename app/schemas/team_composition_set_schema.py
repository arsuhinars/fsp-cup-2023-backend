from datetime import date

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

class TeamCompositionSetSchema(BaseModel):
    team_composition_id: int
    player_id: int
    