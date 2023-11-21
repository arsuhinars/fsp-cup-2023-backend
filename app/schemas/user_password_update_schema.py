from typing import Annotated

from pydantic import BaseModel, Field


class UserPasswordUpdateSchema(BaseModel):
    new_password: Annotated[
        str, Field(min_length=8, max_length=50, examples=["password"])
    ]
