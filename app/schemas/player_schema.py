from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated


class GenderEnum(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class PlayerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    gto_id: str
    team_id: int | None = None
    nickname: Annotated[str, Field(max_length=50)]
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    gender: GenderEnum
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    citizenship: Annotated[str, Field(max_length=50)]
    rank: Annotated[str, Field(max_length=50)]
    pd_accepted: bool
    is_active_in_team: bool


class ShortPlayerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nickname: Annotated[str, Field(max_length=50)]
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    gender: GenderEnum


class PlayerCreateSchema(BaseModel):
    gto_id: str
    nickname: Annotated[str, Field(max_length=50)]
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    gender: GenderEnum
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    citizenship: Annotated[str, Field(max_length=50)]
    rank: Annotated[str, Field(max_length=50)]
    pd_accepted: bool


class PlayerUpdateSchema(BaseModel):
    gto_id: str
    nickname: Annotated[str, Field(max_length=50)]
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: date
    gender: GenderEnum
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    citizenship: Annotated[str, Field(max_length=50)]
    rank: Annotated[str, Field(max_length=50)]
    pd_accepted: bool
    is_active_in_team: bool
