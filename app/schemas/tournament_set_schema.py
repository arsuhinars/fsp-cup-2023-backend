from pydantic import BaseModel

from app.schemas.team_composition_schema import ShortTeamCompositionSchema


class TournamentSetSchema(BaseModel):
    team_composition: ShortTeamCompositionSchema
    result_place: int
