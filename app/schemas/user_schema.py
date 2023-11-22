from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated


class JudgeRankEnum(StrEnum):
    MATCH_JUDGE = "MATCH_JUDGE"
    MAIN_TOURNAMENT_JUDGE = "MAIN_TOURNAMENT_JUDGE"
    TOURNAMENT_SECRETARY = "TOURNAMENT_SECRETARY"


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    JUDGE = "JUDGE"
    TEAM_CAPTAIN = "TEAM_CAPTAIN"


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: Annotated[str, Field(max_length=50, examples=["Name"])]
    last_name: Annotated[str, Field(max_length=50, examples=["Lastname"])]
    patronymic: Annotated[str, Field(max_length=50, examples=["Patronymic"])]
    birth_date: Annotated[date, Field(examples=["2000-01-01"])]
    country: Annotated[str, Field(max_length=50, examples=["Country"])]
    city: Annotated[str, Field(max_length=50, examples=["City"])]
    phone: Annotated[str, Field(max_length=50, examples=["+7(999)999-99-99"])]
    email: EmailStr
    role: UserRole
    judge_rank: Annotated[JudgeRankEnum | None, Field(default=None)]
