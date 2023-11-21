from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.models.tournament import Tournament


class TournamentCreateSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    location: Annotated[str, Field(max_length=50, examples=["Location"])]
    discipline: Annotated[str, Field(max_length=50, examples=["Discipline"])]
    date_registration: Annotated[date, Field(examples=["2000-01-01"])]
    date_start: Annotated[date, Field(examples=["2000-01-01"])]
    state: Annotated[str, Field(max_length=50, examples=["State"])]
