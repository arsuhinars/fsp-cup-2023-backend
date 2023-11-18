from fastapi import APIRouter

router = APIRouter(prefix="/match")


@router.post("/", tags=["match"])
def post_match(name: str,
               location: str,
               discipline: str,
               date_registration: str,
               date_start: str,
               date_end: str,
               date_award: str,
               status: str,
               judge_id: int):
    pass


@router.get("/", tags=["match"])
def get_match(match_id: int):
    pass


@router.put("/", tags=["match"])
def update_match(match_id: int,
                 name: str,
                 location: str,
                 discipline: str,
                 date_registration: str,
                 date_start: str,
                 date_end: str,
                 date_award: str,
                 status: str,
                 judge_id: int):
    pass


@router.delete("/", tags=["match"])
def delete_match(match_id: int):
    pass
