from datetime import date

from typing_extensions import Annotated

from pydantic import BaseModel, Field

from app.models.team import Team


class TeamSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]

    @staticmethod
    def from_model(team: Team) -> "TeamSchema":
        return TeamSchema(
            id=team.id,
            name=team.name
        )