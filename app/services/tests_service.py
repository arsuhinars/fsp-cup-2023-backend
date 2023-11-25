from app.models.team_composition import TeamComposition
from app.schemas.match_schema import MatchSchema
from app.schemas.player_schema import PlayerCreateSchema
from app.schemas.team_schema import TeamCreateSchema
from app.schemas.tournament_schema import TournamentCreateSchema
from app.schemas.user_schema import UserCreateSchema, UserRole
from app.services import (
    match_service,
    player_service,
    team_composition_service,
    team_service,
    tournament_requests_service,
    tournament_service,
    user_service,
)

gv = {}


def init() -> bool:
    gv["admin"] = user_service.create(UserCreateSchema(
        first_name="Name2",
        last_name="Lastname2",
        patronymic="Patronymic2",
        birth_date="2000-01-01",
        country="Country2",
        city="City2",
        phone="+7(999)999-99-99",
        email="address2@domain.com",
        password="password",
        role="ADMIN",
    ))

    gv["judge"] = user_service.create(UserCreateSchema(
        first_name="Name3",
        last_name="Lastname3",
        patronymic="Patronymic3",
        birth_date="2000-01-01",
        country="Country3",
        city="City3",
        phone="+7(999)999-99-99",
        email="address3@domain.com",
        password="password",
        role="JUDGE",
    ))

    gv["captain1"] = user_service.create(UserCreateSchema(
        first_name="Name1",
        last_name="Lastname1",
        patronymic="Patronymic1",
        birth_date="2000-01-01",
        country="Country1",
        city="City1",
        phone="+7(999)999-99-99",
        email="address1@domain.com",
        password="password",
        role="TEAM_CAPTAIN",
    ))

    gv["captain2"] = user_service.create(UserCreateSchema(
        first_name="Name4",
        last_name="Lastname4",
        patronymic="Patronymic4",
        birth_date="2000-01-01",
        country="Country4",
        city="City4",
        phone="+7(999)999-99-99",
        email="address4@domain.com",
        password="password",
        role="TEAM_CAPTAIN",
    ))

    gv["team1"] = team_service.create(TeamCreateSchema(
        name="Team1",
    ), gv["captain1"].id)

    gv["team2"] = team_service.create(TeamCreateSchema(
        name="Team2",
    ), leader_id=gv["captain2"].id)

    gv["player1_team1"] = player_service.create_in_team(PlayerCreateSchema(
        gto_id="123",
        nickname="Player1",
        first_name="Name1",
        last_name="Lastname1",
        patronymic="Patronymic1",
        birth_date="2000-01-01",
        gender="MALE",
        country="Country1",
        city="City1",
        phone="+7(999)999-99-99",
        email="address1@domain.com",
        citizenship="Citizenship1",
        rank="Rank1",
        pd_accepted=True
    ), gv["team1"].id)

    gv["player2_team1"] = player_service.create_in_team(PlayerCreateSchema(
        gto_id="123",
        nickname="Player2",
        first_name="Name2",
        last_name="Lastname2",
        patronymic="Patronymic2",
        birth_date="2000-01-01",
        gender="MALE",
        country="Country2",
        city="City2",
        phone="+7(999)999-99-99",
        email="address2@domain.com",
        citizenship="Citizenship2",
        rank="Rank2",
        pd_accepted=True
    ), gv["team1"].id)

    gv["player1_team2"] = player_service.create_in_team(PlayerCreateSchema(
        gto_id="123",
        nickname="Player3",
        first_name="Name3",
        last_name="Lastname3",
        patronymic="Patronymic3",
        birth_date="2000-01-01",
        gender="MALE",
        country="Country3",
        city="City3",
        phone="+7(999)999-99-99",
        email="address3@domain.com",
        citizenship="Citizenship3",
        rank="Rank3",
        pd_accepted=True
    ), gv["team2"].id)

    gv["player2_team2"] = player_service.create_in_team(PlayerCreateSchema(
        gto_id="123",
        nickname="Player4",
        first_name="Name4",
        last_name="Lastname4",
        patronymic="Patronymic4",
        birth_date="2000-01-01",
        gender="MALE",
        country="Country4",
        city="City4",
        phone="+7(999)999-99-99",
        email="address4@domain.com",
        citizenship="Citizenship4",
        rank="Rank4",
        pd_accepted=True
    ), gv["team2"].id)


    gv["tournament1"] = tournament_service.create(TournamentCreateSchema(
        name="Tournament1",
        location="Location1",
        discipline="Discipline1",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        state="JUST_CREATED",
    ), gv["judge"].id)

    gv["tournament2"] = tournament_service.create(TournamentCreateSchema(
        name="Tournament2",
        location="Location2",
        discipline="Discipline2",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        state="JUST_CREATED",
    ), gv["judge"].id)

    player_service.set_active(gv["player1_team1"].id, True)
    player_service.set_active(gv["player2_team1"].id, False)
    gv["request1"] = tournament_requests_service.create_request(gv["tournament1"].id, gv["team1"].id)
    tournament_requests_service.accept_request(gv["request1"].id)
    player_service.set_active(gv["player1_team2"].id, True)
    player_service.set_active(gv["player2_team2"].id, True)
    gv["request2"] = tournament_requests_service.create_request(gv["tournament1"].id, gv["team2"].id)
    tournament_requests_service.accept_request(gv["request2"].id)

    player_service.set_active(gv["player1_team1"].id, True)
    player_service.set_active(gv["player2_team1"].id, True)
    gv["request3"] = tournament_requests_service.create_request(gv["tournament2"].id, gv["team1"].id)
    tournament_requests_service.accept_request(gv["request3"].id)
    player_service.set_active(gv["player1_team2"].id, True)
    player_service.set_active(gv["player2_team2"].id, False)
    gv["request4"] = tournament_requests_service.create_request(gv["tournament2"].id, gv["team2"].id)
    tournament_requests_service.accept_request(gv["request4"].id)

    gv["match1"] = match_service.create(MatchSchema(
        team_a_id=gv["team1.id"],
        team_b_id=gv["team2.id"],
    ))

    gv["match2"] = match_service.create(MatchSchema(
        team_a_id=gv["team1.id"],
        team_b_id=gv["team2.id"],
    ))

    return True


def player_test() -> bool:
    player1_create = player_service.create_in_team(gv["player1_team1"], gv["team1"].id)
    player2_create = player_service.create_in_team(gv["player1_team2"], gv["team2"].id)

    players1_get_all = player_service.get_team_players(gv["team1"].id)
    players2_get_all = player_service.get_team_players(gv["team2"].id)

    player1_get = player_service.get_by_id(gv["player1_create"].id)
    player2_get = player_service.get_by_id(gv["player2_create"].id)

    player1_is_in_team = player_service.is_in_team(gv["player1_create"].id, gv["team1"].id)
    player2_is_in_team = player_service.is_in_team(gv["player2_create"].id, gv["team2"].id)

    player1_delete = player_service.delete(gv["player1_create"].id)
    player2_delete = player_service.delete(gv["player2_create"].id)

    return True


def team_test() -> bool:
    team1_create = team_service.create(gv["team1"], gv["captain1"].id)
    team2_create = team_service.create(gv["team2"], gv["captain2"].id)

    get_all_teams = team_service.get_all()

    get_by_id_team1 = team_service.get_by_id(team1_create.id)
    get_by_id_team2 = team_service.get_by_id(team2_create.id)

    get_by_leader_id_team1 = team_service.get_by_leader_id(gv["captain1"].id)
    get_by_leader_id_team2 = team_service.get_by_leader_id(gv["captain2"].id)

    return True


def user_test() -> bool:
    captain1_create = user_service.create(gv["captain1"])
    captain2_create = user_service.create(gv["captain2"])

    admin_create = user_service.create(gv["admin"])

    judge_create = user_service.create(gv["judge"])

    get_all_admins = user_service.get_all(UserRole.ADMIN)
    get_all_captains = user_service.get_all(UserRole.TEAM_CAPTAIN)
    get_all_judges = user_service.get_all(UserRole.JUDGE)

    get_by_id_captain1 = user_service.get_by_id(captain1_create.id)
    get_by_id_captain2 = user_service.get_by_id(captain2_create.id)
    get_by_id_admin = user_service.get_by_id(admin_create.id)
    get_by_id_judge = user_service.get_by_id(judge_create.id)

    get_by_email_captain1 = user_service.get_by_email(gv["captain1"].email)
    get_by_email_captain2 = user_service.get_by_email(gv["captain2"].email)
    get_by_email_admin = user_service.get_by_email(gv["admin"].email)
    get_by_email_judge = user_service.get_by_email(gv["judge"].email)

    user_service.delete(gv["captain1_create"].id)
    user_service.delete(gv["captain2_create"].id)
    user_service.delete(gv["admin_create"].id)
    user_service.delete(gv["judge_create"].id)

    return True


def tournament_test() -> bool:
    tournament1_create = tournament_service.create(gv["tournament1"], gv["judge"].id)
    tournament2_create = tournament_service.create(gv["tournament2"], gv["judge"].id)

    get_all_tournaments = tournament_service.get_all()

    get_by_id_tournament1 = tournament_service.get_by_id(tournament1_create.id)
    get_by_id_tournament2 = tournament_service.get_by_id(tournament2_create.id)

    get_team_comps_tournament1 = tournament_service.get_team_comps(tournament1_create.id)
    get_team_comps_tournament2 = tournament_service.get_team_comps(tournament2_create.id)

    delete_tournament1 = tournament_service.delete(tournament1_create.id)
    delete_tournament2 = tournament_service.delete(tournament2_create.id)

    return True


def team_composition_test() -> bool:
    team_composition1_create = team_composition_service.create(gv["team_composition1_team1"])
    team_composition2_create = team_composition_service.create(gv["team_composition1_team2"])
    team_composition3_create = team_composition_service.create(gv["team_composition2_team1"])

    return True


def match_test() -> bool:
    match1_create = match_service.create(gv["match1"])
    match2_create = match_service.create(gv["match2"])

    get_by_id_match1 = match_service.get_by_id(match1_create.id)
    get_by_id_match2 = match_service.get_by_id(match2_create.id)

    match_service.delete(match1_create.id)
    match_service.delete(match2_create.id)

    return True


def tournament_requests_test() -> bool:
    request1_create = tournament_requests_service.create_request(gv["tournament1"].id, gv["team_composition1_team1"].id)
    request2_create = tournament_requests_service.create_request(gv["tournament1"].id, gv["team_composition1_team2"].id)
    request3_create = tournament_requests_service.create_request(gv["tournament2"].id, gv["team_composition2_team1"].id)
    request4_create = tournament_requests_service.create_request(gv["tournament2"].id, gv["team_composition1_team2"].id)

    get_tournament1_requests_by_tour_id = tournament_requests_service.get_by_tournament_id(gv["tournament1"].id)
    get_tournament2_requests_by_tour_id = tournament_requests_service.get_by_tournament_id(gv["tournament2"].id)

    get_by_team1_id_ = tournament_requests_service.get_by_team_comp_id(gv["tournament1"].id, gv["team1"].id)
    get_by_team2_id_ = tournament_requests_service.get_by_team_comp_id(gv["tournament1"].id, gv["team2"].id)
    get_by_team3_id_ = tournament_requests_service.get_by_team_comp_id(gv["tournament2"].id, gv["team1"].id)
    get_by_team4_id_ = tournament_requests_service.get_by_team_comp_id(gv["tournament2"].id, gv["team2"].id)

    accept_request1 = tournament_requests_service.accept_request(request1_create.id)
    accept_request2 = tournament_requests_service.accept_request(request2_create.id)
    accept_request3 = tournament_requests_service.accept_request(request3_create.id)
    accept_request4 = tournament_requests_service.accept_request(request4_create.id)

    decline_request1 = tournament_requests_service.decline_request(request1_create.id)
    decline_request2 = tournament_requests_service.decline_request(request2_create.id)
    decline_request3 = tournament_requests_service.decline_request(request3_create.id)
    decline_request4 = tournament_requests_service.decline_request(request4_create.id)

    return True


def run_all_tests() -> bool:
    init()
    player_test()
    team_test()
    user_test()
    tournament_test()
    team_composition_test()
    match_test()
    tournament_requests_test()

    return True
