from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.models.tournament import Tournament


class TournamentUpdateSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    location: Annotated[str, Field(max_length=50, examples=["Location"])]
    discipline: Annotated[str, Field(max_length=50, examples=["Discipline"])]
    date_registration: Annotated[date, Field(examples=["2000-01-01"])]
    date_start: Annotated[date, Field(examples=["2000-01-01"])]
    date_end: Annotated[date, Field(examples=["2000-01-01"])]
    date_award: Annotated[date, Field(examples=["2000-01-01"])]
    state: Annotated[str, Field(max_length=50, examples=["State"])]


def to_model(self, tournament: Tournament) -> Tournament:
    return Tournament(
        id=self.id,
        name=self.name,
        location=self.location,
        discipline=self.discipline,
        date_registration=self.date_registration,
        date_start=self.date_start,
        date_end=self.date_end,
        date_award=self.date_award,
        state=self,
    )
