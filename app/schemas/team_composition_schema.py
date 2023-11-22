from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated


class TeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field(examples=[1])]
    team_id: Annotated[int, Field(examples=[1])]