from datetime import date

from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated

from app.schemas.player_schema import GenderEnum


class PlayerUpdateSchema(BaseModel):
    gto_id: int
    nickname: Annotated[str, Field(max_length=50, examples=["Nickname"])]
    first_name: Annotated[str, Field(max_length=50, examples=["Name"])]
    last_name: Annotated[str, Field(max_length=50, examples=["Lastname"])]
    patronymic: Annotated[str, Field(max_length=50, examples=["Patronymic"])]
    birth_date: Annotated[date, Field(examples=["2000-01-01"])]
    gender: GenderEnum
    country: Annotated[str, Field(max_length=50, examples=["Country"])]
    city: Annotated[str, Field(max_length=50, examples=["City"])]
    phone: Annotated[str, Field(max_length=50, examples=["+7(999)999-99-99"])]
    email: EmailStr
    citizenship: Annotated[str, Field(max_length=50, examples=["Citizenship"])]
    rank: Annotated[str, Field(max_length=50, examples=["Rank"])]
    pd_accepted: bool
    is_active_in_team: bool
