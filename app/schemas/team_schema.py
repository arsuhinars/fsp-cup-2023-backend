from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class TeamSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    leader_id: Annotated[int, Field(examples=[1])]
    leader_full_name: Annotated[str, Field(max_length=50)]
