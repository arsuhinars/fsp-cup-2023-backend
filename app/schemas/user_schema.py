from datetime import date

from typing_extensions import Annotated

from app.models.user import UserRole, User, JudgeRankEnum
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    first_name: Annotated[str, Field(max_length=50, examples=["Name"])]
    last_name: Annotated[str, Field(max_length=50, examples=["Lastname"])]
    patronymic: Annotated[str, Field(max_length=50, examples=["Patronymic"])]
    birth_date: Annotated[date, Field(examples=["2000-01-01"])]
    country: Annotated[str, Field(max_length=50, examples=["Country"])]
    city: Annotated[str, Field(max_length=50, examples=["City"])]
    phone: Annotated[str, Field(pattern=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
                                examples=["+7(999)999-99-99"])]
    email: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                                examples=["address@domain.com"])]
    role: UserRole
    judge_rank: Annotated[JudgeRankEnum | None, Field(default=None)]

    @staticmethod
    def from_model(user: User) -> "UserSchema":
        return UserSchema(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            patronymic=user.patronymic,
            birth_date=user.birth_date,
            country=user.country,
            city=user.city,
            phone=user.phone,
            email=user.email,
            role=user.role,
            judge_rank=user.judge_rank
        )
