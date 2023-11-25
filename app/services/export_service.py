from openpyexcel import Workbook

import app.core.db as db
import app.repositories.tournament_repository as tournament_repo
import openpyexcel as opx
from app.exceptions import EntityNotFoundException


def export_sheet_1_header(tournament_id: int) -> str:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")
    opx_file = opx.load_workbook("templates/template.xlsx")
    sheet = opx_file.active
    sheet["B1"].value = tournament.name
    sheet["B3"].value = tournament.location
    sheet["B7"].value = tournament.date_registration
    sheet["B8"].value = tournament.date_begin
    sheet["B9"].value = tournament.date_end
    sheet["B10"].value = tournament.date_awards
    sheet["B11"].value = tournament.discipline
    opx_file.save("templates/export.xlsx")
    return "export.xlsx"
