from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.models.team import Team


class TeamCreateSchema(BaseModel):
    leader_id: Annotated[int | None, Field(examples=[None], default=None)]
    name: Annotated[str, Field(max_length=50, examples=["Name"])]


