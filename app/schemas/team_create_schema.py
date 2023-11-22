from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TeamCreateSchema(BaseModel):
    leader_id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Name"])]


