import app.repositories.team_repository as team_repo
import app.repositories.tournament_repository as tournament_repo
import app.repositories.tournament_requests_repository as tournament_request_repo
from app.core import db
from app.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
    InvalidFormatException,
    ValidationException,
)
from app.models.team_composition import TeamComposition
from app.models.tournament import Tournament
from app.models.tournament_request import TournamentRequest
from app.models.tournament_set import TournamentSet
from app.repositories import user_repository as user_repo
from app.schemas.tournament_request_schema import (
    TournamentRequestSchema,
    TournamentRequestStatus,
)
from app.schemas.tournament_schema import TournamentStateEnum


def create_request(tournament_id: int, team_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        team = team_repo.get_by_id(session, team_id)
        if team is None:
            raise EntityNotFoundException("Team was not found")

        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.REGISTRATION_OPENED:
            raise ValidationException("Tournament is not open for registration")

        active_comp = team_repo.get_active_composition(session, team)
        if active_comp is None:
            raise EntityNotFoundException("Team composition was not found")

        new_comp = TeamComposition(team_id=team_id, is_active=False)
        new_comp.players = set(active_comp.players)

        request = tournament_request_repo.get_by_tournament_id_and_team_id(
            session, tournament_id, team_id
        )
        if request is not None:
            match request.status:
                case TournamentRequestStatus.ACCEPTED | TournamentRequestStatus.PENDING:
                    raise EntityAlreadyExistsException(
                        "Unable to recreate tournament request, because there are already existing one"
                    )
                case TournamentRequestStatus.DECLINED:
                    request.status = TournamentRequestStatus.PENDING
        else:
            request = TournamentRequest(tournament_id=tournament_id)

        request.team_composition = new_comp
        request = tournament_request_repo.save(session, request)
        return TournamentRequestSchema.model_validate(request)


def get_by_tournament_id(tournament_id: int) -> list[TournamentRequestSchema]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        requests = tournament_request_repo.get_by_tournament_id(session, tournament_id)
        return list(map(TournamentRequestSchema.model_validate, requests))


def get_by_captain_id(tournament_id: int, captain_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        captain = user_repo.get_by_id(session, captain_id)
        if captain is None:
            raise EntityNotFoundException("User was not found")

        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        request = tournament_request_repo.get_by_tournament_id_and_team_id(
            session, tournament_id, captain.team.id
        )
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        return TournamentRequestSchema.model_validate(request)


def accept_request(request_id: int) -> TournamentRequestSchema:
    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        if request.tournament.state != TournamentStateEnum.REGISTRATION_OPENED:
            raise ValidationException("Tournament is not open for registration")

        if request.status == TournamentRequestStatus.ACCEPTED:
            raise ValidationException("Can't accept request with status ACCEPTED")

        request.status = TournamentRequestStatus.ACCEPTED

        tournament: Tournament = request.tournament
        if tournament.state != TournamentStateEnum.REGISTRATION_OPENED:
            raise ValidationException("Tournament is not open for registration")

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
    with db.create_session() as session:
        request = tournament_request_repo.get_by_id(session, request_id)
        if request is None:
            raise EntityNotFoundException("TournamentRequest was not found")

        if request.tournament.state != TournamentStateEnum.REGISTRATION_OPENED:
            raise ValidationException("Tournament is not open for registration")

        match request.status:
            case TournamentRequestStatus.ACCEPTED:
                tournament_set = tournament_repo.get_set_by_team_comp_id(
                    session, request.tournament_id, request.team_composition_id
                )
                if tournament_set is not None:
                    session.delete(tournament_set)

            case TournamentRequestStatus.DECLINED:
                raise ValidationException("Can't decline request with status DECLINED")
            case TournamentRequestStatus.PENDING:
                ...
            case _:
                raise InvalidFormatException("Unknown TournamentRequest state")

        request.status = TournamentRequestStatus.DECLINED

        session.add(request)
        session.flush()
        session.commit()

        return TournamentRequestSchema.model_validate(request)
