from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.schemas.user_schema import JudgeRankEnum


class UserUpdateSchema(BaseModel):
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
    judge_rank: Annotated[JudgeRankEnum | None, Field(default=None)]