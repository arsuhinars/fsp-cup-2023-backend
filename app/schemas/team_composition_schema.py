from pydantic import BaseModel, Field
from typing_extensions import Annotated

class TeamCompositionSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    team_id: Annotated[int, Field(examples=[1])]