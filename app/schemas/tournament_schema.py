from datetime import date

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from app.models.tournament import Tournament


class TournamentSchema(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    name: Annotated[str, Field(max_length=50, examples=["Team name"])]
    location: Annotated[str, Field(max_length=50, examples=["Location"])]
    discipline: Annotated[str, Field(max_length=50, examples=["Discipline"])]
    date_registration: Annotated[date, Field(examples=["2000-01-01"])]
    date_start: Annotated[date, Field(examples=["2000-01-01"])]
    date_end: Annotated[date, Field(examples=["2000-01-01"])]
    date_award: Annotated[date, Field(examples=["2000-01-01"])]
    state: Annotated[str, Field(max_length=50, examples=["State"])]

    @staticmethod
    def from_model(tournament: Tournament) -> "TournamentSchema":
        return TournamentSchema(
            id=tournament.id,
            name=tournament.name,
            location=tournament.location,
            discipline=tournament.discipline,
            date_registration=tournament.date_registration,
            date_start=tournament.date_start,
            date_end=tournament.date_end,
            date_award=tournament.date_award,
            state=tournament.state,
        )
