from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated

from app.models.team import Team


class TeamSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Annotated[int, Field(examples=[1])]
    leader_id: Annotated[int | None, Field(examples=[1], default=None)]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
