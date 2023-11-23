from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.models.tournament import Tournament
from app.schemas.tournament_schema import TournamentStateEnum


class TournamentUpdateSchema(BaseModel):
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

