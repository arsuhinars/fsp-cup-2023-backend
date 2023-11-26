import math
from collections import defaultdict

import app.core.db as db
import app.repositories.match_repository as match_repo
import app.repositories.tournament_repository as tournament_repo
from app.exceptions import EntityNotFoundException, InvalidFormatException
from app.models.match import Match
from app.models.tournament import Tournament
from app.models.tournament_set import TournamentSet
from app.repositories import user_repository as user_repo
from app.schemas.match_schema import MatchSchema
from app.schemas.team_composition_schema import TeamCompositionSchema
from app.schemas.tournament_schema import (
    TournamentCreateSchema,
    TournamentSchema,
    TournamentStartSchema,
    TournamentStateEnum,
    TournamentUpdateSchema,
)
from app.schemas.tournament_set_schema import TournamentSetSchema
from app.utils import map_model_to_orm


def create(dto: TournamentCreateSchema, main_judge_id: int) -> TournamentSchema:
    tournament = Tournament(**dto.model_dump())
    with db.create_session() as session:
        if user_repo.get_by_id(session, main_judge_id) is None:
            raise EntityNotFoundException("User was not found")

        tournament.main_judge_id = main_judge_id
        tournament = tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def get_all() -> list[TournamentSchema]:
    with db.create_session() as session:
        return list(
            map(TournamentSchema.model_validate, tournament_repo.get_all(session))
        )


def get_by_id(tournament_id: int) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")
        return TournamentSchema.model_validate(tournament)


def get_team_comps(tournament_id: int) -> list[TeamCompositionSchema]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        team_comps = tournament_repo.get_team_comps(session, tournament_id)

        return list(map(TeamCompositionSchema.model_validate, team_comps))


def get_all_matches(tournament_id: int) -> list[Match]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        return list(map(MatchSchema.model_validate, tournament.matches))


def get_results(tournament_id: int) -> list[TournamentSetSchema]:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.FINISHED:
            raise InvalidFormatException(
                "Can't get tournament results on current stage"
            )

        return list(map(TournamentSetSchema.model_validate, tournament.tournament_sets))


def update(tournament_id: int, dto: TournamentUpdateSchema) -> TournamentSchema:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        map_model_to_orm(dto, tournament)
        tournament_repo.save(session, tournament)

        return TournamentSchema.model_validate(tournament)


def update_match_winner(match_id: int, team_composition_winner_id: int) -> MatchSchema:
    with db.create_session() as session:
        match = match_repo.get_by_id(session, match_id)
        if match is None:
            raise EntityNotFoundException("Match was not found")

        if (
            team_composition_winner_id != match.team_composition_a_id
            and team_composition_winner_id != match.team_composition_b_id
        ):
            raise InvalidFormatException("Invalid team composition id")

        if match.part_number != tournament_repo.get_max_match_part(
            session, match.tournament_id
        ):
            raise InvalidFormatException("You can change winner only on latest matches")

        match.team_composition_winner_id = team_composition_winner_id
        match_repo.save(session, match)

        return MatchSchema.model_validate(match)


def delete(tournament_id: int) -> bool:
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.JUST_CREATED:
            raise InvalidFormatException("Can't delete tournament on current stage")

        tournament_repo.delete(session, tournament)
        return True


def start_registration(tournament_id: int):
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.JUST_CREATED:
            raise InvalidFormatException(
                "Tournament registration can be started only on JUST_CREATED state"
            )

        tournament.state = TournamentStateEnum.REGISTRATION_OPENED

        tournament_repo.save(session, tournament)
        return TournamentSchema.model_validate(tournament)


def close_registration(tournament_id: int):
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.REGISTRATION_OPENED:
            raise InvalidFormatException(
                "Tournament registration can be started only on REGISTRATION_OPENED state"
            )

        teams_counts = len(tournament.tournament_sets)
        if (
            teams_counts < 2
            or teams_counts > 32
            or 2 ** int(math.log2(teams_counts)) != teams_counts
        ):
            raise InvalidFormatException("Invalid teams count on tournament")

        tournament.state = TournamentStateEnum.REGISTRATION_CLOSED

        tournament_repo.save(session, tournament)
        return TournamentSchema.model_validate(tournament)


def start_tournament(tournament_id: int, dto: TournamentStartSchema):
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.REGISTRATION_CLOSED:
            raise InvalidFormatException(
                "Tournament can be started only on REGISTRATION_CLOSED tournament state"
            )

        sets: list[TournamentSet] = tournament.tournament_sets
        teams_comps_ids = set(map(lambda s: s.team_composition_id, sets))
        if teams_comps_ids != set(dto.team_compositions_ids):
            raise InvalidFormatException("Invalid team compositions ids")

        matches: list[Match] = []
        for i in range(0, len(dto.team_compositions_ids), 2):
            matches.append(
                Match(
                    team_composition_a_id=dto.team_compositions_ids[i],
                    team_composition_b_id=dto.team_compositions_ids[i + 1],
                    team_composition_winner_id=None,
                    tournament_id=tournament_id,
                    order_number=i // 2,
                    part_number=0,
                )
            )

        tournament.state = TournamentStateEnum.ONGOING

        session.add_all(matches)
        session.add(tournament)
        session.flush()
        session.commit()

        return TournamentSchema.model_validate(tournament)


def start_next_matches(tournament_id: int):
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.ONGOING:
            raise InvalidFormatException(
                "Creating next matches can be done only on ONGOING tournament state"
            )

        max_part_number = tournament_repo.get_max_match_part(session, tournament_id)
        if max_part_number is None:
            raise InvalidFormatException("There are no matches in tournament")

        latest_matches = match_repo.get_by_tournament_id_and_part_number(
            session, tournament_id, max_part_number
        )

        if len(latest_matches) < 2:
            raise InvalidFormatException("There are no team composition remained")

        next_matches: list[Match] = []
        for i in range(len(0, latest_matches, 2)):
            team_a_id = latest_matches[i].team_composition_winner_id
            team_b_id = latest_matches[i + 1].team_composition_winner_id
            if team_a_id is None or team_b_id is None:
                raise InvalidFormatException(
                    "Not all matches have team composition winner"
                )

            next_matches.append(
                Match(
                    team_composition_a_id=team_a_id,
                    team_composition_b_id=team_b_id,
                    team_composition_winner_id=None,
                    tournament_id=tournament_id,
                    order_number=latest_matches[i].order_number // 2,
                    part_number=max_part_number + 1,
                )
            )

        match_repo.save_all(session, next_matches)


def finish_tournament(tournament_id: int):
    with db.create_session() as session:
        tournament = tournament_repo.get_by_id(session, tournament_id)
        if tournament is None:
            raise EntityNotFoundException("Tournament was not found")

        if tournament.state != TournamentStateEnum.ONGOING:
            raise InvalidFormatException(
                "Tournament can be finished only on ONGOING state"
            )

        max_part_number = tournament_repo.get_max_match_part(session, tournament_id)
        if max_part_number + 1 != int(math.log2(len(tournament.tournament_sets))):
            raise InvalidFormatException("Only one match must remain in tournament")

        match_by_part: dict[int, list[Match]] = defaultdict(lambda: [])
        for m in tournament.matches:
            match_by_part[m.part_number].append(m)

        team_comps = tournament_repo.get_team_comps(session, tournament_id)
        result_by_team: dict[int, int] = dict()
        team_comps_ids = set(map(lambda t: t.id, team_comps))
        counter = 1
        for i in range(max_part_number, -1, -1):
            for m in match_by_part[m.part_number]:
                if m.team_composition_winner_id not in team_comps_ids:
                    continue

                result_by_team[m.team_composition_winner_id] = counter
                counter += 1
                team_comps_ids.remove(m.team_composition_winner_id)

        for id in team_comps_ids:
            result_by_team[id] = counter
            counter += 1

        for tournament_set in tournament.tournament_sets:
            tournament_set.result_place = result_by_team[
                tournament_set.team_composition_id
            ]

        tournament.state = TournamentStateEnum.FINISHED

        tournament_repo.save(session, tournament)
        return TournamentSchema.model_validate(tournament)
