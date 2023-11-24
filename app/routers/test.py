from fastapi import APIRouter, Depends

import app.services.tests_service

router = APIRouter(prefix="/tests", tags=["Test"])

@router.get("/run")
def run_test() -> bool:
    return tests_service.run_all_tests() #БИМ БИМ БАМ БАМ