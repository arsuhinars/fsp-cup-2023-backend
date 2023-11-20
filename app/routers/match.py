from fastapi import APIRouter

router = APIRouter(prefix="/match", tags=["match"])


@router.post("/")
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


@router.get("/")
def get_match(match_id: int):
    pass


@router.put("/")
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


@router.delete("/")
def delete_match(match_id: int):
    pass
