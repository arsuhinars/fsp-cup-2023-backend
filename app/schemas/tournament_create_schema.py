from datetime import date

from typing_extensions import Annotated

from app.models.tournament import Tournament
from pydantic import BaseModel, Field


class TournamentCreateSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    location: Annotated[str, Field(max_length=50, examples=["Location"])]
    discipline: Annotated[str, Field(max_length=50, examples=["Discipline"])]
    date_registration: Annotated[date, Field(examples=["2000-01-01"])]
    date_start: Annotated[date, Field(examples=["2000-01-01"])]
    state: Annotated[str, Field(max_length=50, examples=["State"])]

def to_model(self) -> Tournament:
    return Tournament(
        id=self.id,
        name=self.name,
        location=self.location,
        discipline=self.discipline,
        date_registration=self.date_registration,
        date_start=self.date_start,
        state=self.state
    )