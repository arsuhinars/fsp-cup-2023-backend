from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class TournamentStateEnum(StrEnum):
    JUST_CREATED = "JUST_CREATED"
    REGISTRATION_OPENED = "REGISTRATION_OPENED"
    REGISTRATION_CLOSED = "REGISTRATION_CLOSED"
    ONGOING = "ONGOING"
    FINISHED = "FINISHED"


class TournamentCreateSchema(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    location: Annotated[str, Field(max_length=50)]
    discipline: Annotated[str, Field(max_length=50)]
    date_registration: date
    date_begin: date
    date_end: date
    date_awards: date


class TournamentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: Annotated[str, Field(max_length=50)]
    location: Annotated[str, Field(max_length=50)]
    discipline: Annotated[str, Field(max_length=50)]
    date_registration: date
    date_begin: date
    date_end: date
    date_awards: date

    main_judge_id: int
    state: TournamentStateEnum


class TournamentUpdateSchema(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=50)]
    location: Annotated[str, Field(max_length=50)]
    discipline: Annotated[str, Field(max_length=50)]
    date_registration: date
    date_begin: date
    date_end: date
    date_awards: date
    main_judge_id: int
