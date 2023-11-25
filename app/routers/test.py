from typing import Annotated
from app.services.tests_service import run_all_tests
from fastapi import APIRouter, Depends

from app.exceptions import EntityNotFoundException
from app.schemas.team_schema import TeamCreateSchema, TeamSchema, TeamUpdateSchema
from app.schemas.user_schema import UserSchema
from app.security import authenticate, require_team_captain
from app.services import team_service


router = APIRouter(prefix="/tests", tags=["Test"])

@router.get("/run")
def run_test() -> bool:
    return run_all_tests() #БИМ БИМ БАМ БАМ