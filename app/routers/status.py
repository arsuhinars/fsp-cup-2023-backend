from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services import export_service

router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
def get_status():
    return "ok"


@router.get("/export")
def export() -> FileResponse:
    wb = export_service.export_sheet_1_header(1)
    return FileResponse("templates/export.xlsx", media_type='application/octet-stream', filename="export.xlsx")
