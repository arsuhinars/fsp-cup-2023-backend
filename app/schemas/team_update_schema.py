from datetime import date

from typing_extensions import Annotated

from app.models.team import Team
from pydantic import BaseModel, Field

class TeamUpdateSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    leader_id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Name"])]

def to_model(self, team: Team) -> Team:
    return Team(
        id = self.id,
        leader_id = self.leader_id,
        name = self.name
    )