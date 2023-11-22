from datetime import date

from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated


class PlayerCreateSchema(BaseModel):
    gto_id: int
    nickname: Annotated[str, Field(max_length=50, examples=["nickname"])]
    first_name: Annotated[str, Field(max_length=50, examples=["First name"])]
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
