from fastapi import APIRouter

router = APIRouter(prefix="/status")


@router.get("/", tags=["status"])
def get_status():
    return "ok"
