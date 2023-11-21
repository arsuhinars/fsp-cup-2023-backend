from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.schemas.user_schema import JudgeRankEnum, UserRole


class UserCreateSchema(BaseModel):
    # FIXME: в пароль можно записать не ASCII символы
    # (возникнет ошибка, если попытаемся закодировать в base64 на фронте
    # для HTTP авторизации)
    password: Annotated[str, Field(min_length=8, max_length=50, examples=["password"])]
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
    role: UserRole

    judge_rank: Annotated[JudgeRankEnum | None, Field(default=None)]
