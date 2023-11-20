from datetime import date
from hashlib import md5

from typing_extensions import Annotated

from app.models.user import UserRole, User, JudgeRankEnum
from pydantic import BaseModel, Field


class UserCreateSchema(BaseModel):
    password: Annotated[str, Field(min_length=8, max_length=50, examples=["password"])]
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
    role: Annotated[UserRole, Field()]
    judge_rank: Annotated[JudgeRankEnum | None, Field(default=None)]

    def to_model(self) -> User:
        print('\nJR >>>', self.judge_rank, '<<<\n')
        return User(
            password_hash=md5(self.password.encode()).hexdigest(),
            first_name=self.first_name,
            last_name=self.last_name,
            patronymic=self.patronymic,
            birth_date=self.birth_date,
            country=self.country,
            city=self.city,
            phone=self.phone,
            email=self.email,
            role=self.role,
            judge_rank=self.judge_rank
        )
