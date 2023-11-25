from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated

from app.schemas.team_schema import TeamSchema


class JudgeRankEnum(StrEnum):
    MATCH_JUDGE = "MATCH_JUDGE"
    MAIN_TOURNAMENT_JUDGE = "MAIN_TOURNAMENT_JUDGE"
    TOURNAMENT_SECRETARY = "TOURNAMENT_SECRETARY"


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    JUDGE = "JUDGE"
    TEAM_CAPTAIN = "TEAM_CAPTAIN"


PasswordField = Annotated[
    str,
    Field(
        min_length=8,
        max_length=50,
        pattern=r"^[ -9;-~]*$",
        examples=["password"],
    ),
]


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    role: UserRole
    judge_rank: JudgeRankEnum | None = None
    team: TeamSchema | None


class UserCreateSchema(BaseModel):
    password: PasswordField
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    role: UserRole

    judge_rank: JudgeRankEnum | None = None


class UserUpdateSchema(BaseModel):
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr

    judge_rank: JudgeRankEnum | None = None


class UserPasswordUpdateSchema(BaseModel):
    new_password: PasswordField
