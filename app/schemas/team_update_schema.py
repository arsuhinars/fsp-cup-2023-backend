from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TeamUpdateSchema(BaseModel):
    name: Annotated[str, Field(max_length=50, examples=["Name"])]
