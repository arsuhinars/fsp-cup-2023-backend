from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TournamentStateEnum(StrEnum):
    JUST_CREATED = "JUST_CREATED"
    REGISTRATION_OPENED = "REGISTRATION_OPENED"
    REGISTRATION_CLOSED = "REGISTRATION_CLOSED"
    ONGOING = "ONGOING"
    FINISHED = "FINISHED"


class TournamentSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    location: Annotated[str, Field(max_length=50, examples=["Location"])]
    discipline: Annotated[str, Field(max_length=50, examples=["Discipline"])]
    date_registration: Annotated[date, Field(examples=["2000-01-01"])]
    date_begin: Annotated[date, Field(examples=["2000-02-01"])]
    date_end: Annotated[date, Field(examples=["2000-03-01"])]
    date_awards: Annotated[date, Field(examples=["2000-04-01"])]
    main_judge_id: Annotated[int, Field(example=1)]
    state: Annotated[TournamentStateEnum, Field(examples=["JUST_CREATED",
                                                          "REGISTRATION_OPENED",
                                                          "REGISTRATION_CLOSED",
                                                          "ONGOING",
                                                          "FINISHED"])]
