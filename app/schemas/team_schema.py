from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class TeamSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: Annotated[str, Field(max_length=50)]
    leader_id: int
    leader_full_name: Annotated[str, Field(max_length=50)]


class TeamCreateSchema(BaseModel):
    name: Annotated[str, Field(max_length=50)]


class TeamUpdateSchema(BaseModel):
    name: Annotated[str, Field(max_length=50)]
