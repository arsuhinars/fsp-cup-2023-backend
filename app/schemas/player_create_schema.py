from datetime import date

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from app.models.player import Player

class PlayerCreateSchema(BaseModel):
    id: int
    gto_id: int
    nickname: Annotated[str, Field(max_length=50, examples=["Nickname"])]
    first_name: Annotated[str, Field(max_length=50, examples=["Name"])]
    last_name: Annotated[str, Field(max_length=50, examples=["Lastname"])]
    patronymic: Annotated[str, Field(max_length=50, examples=["Patronymic"])]
    birth_date: Annotated[date, Field(examples=["2000-01-01"])]
    country: Annotated[str, Field(max_length=50, examples=["Country"])]
    city: Annotated[str, Field(max_length=50, examples=["City"])]
    phone: Annotated[str, Field(max_length=50, examples=["+7(999)999-99-99"])]
    email: Annotated[
        str,
        Field(
            pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            examples=["address@domain.com"],
        ),
    ]
    citizenship: Annotated[str, Field(max_length=50, examples=["Citizenship"])]
    rank: Annotated[str, Field(max_length=50, examples=["Rank"])]
    pd_accepted: Annotated[bool, Field()]
    deleted: Annotated[bool, Field()]
