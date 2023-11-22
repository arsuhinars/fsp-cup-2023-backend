from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated


class TeamCompositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int | None, Field(examples=[None], default=None)]
    team_id: Annotated[int, Field(examples=[1])]
    is_active: Annotated[bool, Field(examples=[True])]
