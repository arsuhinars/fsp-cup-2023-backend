import app.repositories.tournament_repository as tournament_repo
import app.repositories.tournament_requests_repository as tournament_request_repo
from app.core import db
from app.exceptions import (
    EntityNotFoundException,
    InvalidFormatException,
    ValidationException,
)
from app.models.tournament import Tournament
from app.models.tournament_request import TournamentRequest
from app.models.tournament_set import TournamentSet
from app.schemas.tournament_request_schema import (
    TournamentRequestSchema,
    TournamentRequestStatus,
)


def create_request(tournament_id: int, team_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        # TODO: скопировать активную композицию команды и создать запрос от неё
        # Новая композиция при этом будет неактивной

        # TODO: создание только при статусе REGISTRATION_OPENED

        request = tournament_request_repo.save(
            session,
            TournamentRequest(
                tournament_id=tournament_id, team_composition_id=team_comp_id
            ),
        )
        return TournamentRequestSchema.model_validate(request)


def get_by_tournament_id(tournament_id: int) -> list[TournamentRequestSchema]:
    # TODO: только при статусе REGISTRATION_OPENED

    with db.create_session() as session:
        requests = tournament_request_repo.get_by_tournament_id(session, tournament_id)
        return list(map(TournamentRequestSchema.model_validate, requests))


def get_by_team_comp_id(
    tournament_id: int, team_comp_id: int
) -> TournamentRequestSchema:
    # TODO: только при статусе REGISTRATION_OPENED

    with db.create_session() as session:
        request = tournament_request_repo.get_by_tournament_id_and_team_comp_id(
            session, tournament_id, team_comp_id
        )
        return TournamentRequestSchema.model_validate(request)


def get_by_captain_id(tournament_id: int, captain_id: int) -> TournamentRequestSchema:
    # TODO: только при статусе REGISTRATION_OPENED

    with db.create_session() as session:
        request = tournament_request_repo.get_by_tournament_id_and_captain_id(
            session, tournament_id, captain_id
        )
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        return TournamentRequestSchema.model_validate(request)


def accept_request(request_id: int) -> TournamentRequestSchema:
    # TODO: только при статусе REGISTRATION_OPENED

    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        if request.status == TournamentRequestStatus.ACCEPTED:
            raise ValidationException("Can't accept request with status ACCEPTED")

        request.status = TournamentRequestStatus.ACCEPTED
        tournament: Tournament = request.tournament
        tournament.tournament_sets.append(
            TournamentSet(
                tournament_id=tournament.id,
                team_composition_id=request.team_composition_id,
            )
        )

        session.add(tournament)
        session.add(request)
        session.flush()
        session.commit()

        return TournamentRequestSchema.model_validate(request)


def decline_request(request_id: int) -> TournamentRequestSchema:
    # TODO: только при статусе REGISTRATION_OPENED

    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        match request.status:
            case TournamentRequestStatus.ACCEPTED:
                tournament_set = tournament_repo.get_set_by_team_comp_id(
                    session, request.tournament_id, request.team_composition_id
                )
                if tournament_set is not None:
                    session.delete(tournament_set)

            case TournamentRequestStatus.DECLINED:
                raise ValidationException("Can't accept request with status DECLINED")
            case TournamentRequestStatus.PENDING:
                ...
            case _:
                raise InvalidFormatException("Unknown TournamentRequest state")

        request.status = TournamentRequestStatus.DECLINED

        session.add(request)
        session.flush()
        session.commit()

        return TournamentRequestSchema.model_validate(request)
