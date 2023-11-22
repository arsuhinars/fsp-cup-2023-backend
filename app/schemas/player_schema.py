from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated


class PlayerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field()]
    gto_id: Annotated[int, Field(examples=["11111111111"])]
    team_id: Annotated[int | None, Field(default=None)]
    nickname: Annotated[str, Field(max_length=50, examples=["Nickname"])]
    first_name: Annotated[str, Field(max_length=50, examples=["Name"])]
    last_name: Annotated[str, Field(max_length=50, examples=["Lastname"])]
    patronymic: Annotated[str, Field(max_length=50, examples=["Patronymic"])]
    birth_date: Annotated[date, Field(examples=["2000-01-01"])]
    country: Annotated[str, Field(max_length=50, examples=["Country"])]
    city: Annotated[str, Field(max_length=50, examples=["City"])]
    phone: Annotated[str, Field(max_length=50, examples=["+7(999)999-99-99"])]
    email: EmailStr
    citizenship: Annotated[str, Field(max_length=50, examples=["Citizenship"])]
    rank: Annotated[str, Field(max_length=50, examples=["Rank"])]
    pd_accepted: bool
    is_active_in_team: bool
