from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TeamCreateSchema(BaseModel):
    name: Annotated[str, Field(max_length=50, examples=["Name"])]
