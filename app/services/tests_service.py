from app.schemas.match_create_schema import MatchCreateSchema
from app.schemas.match_schema import MatchUpdateSchema
from app.schemas.user_create_schema import UserCreateSchema
import match_service
import player_service
import team_composition_service
import team_service
import tournament_service
import user_service

global_vars = {}

def init() -> bool:
    global_vars["captain1"] = user_service.create(UserSchema(
        first_name="Name1",
        last_name="Lastname1",
        patronymic="Patronymic1",
        birth_date="2000-01-01",
        country="Country1",
        city="City1",
        phone="+7(999)999-99-99",
        email="address1@domain.com",
        password="password",
        role="Captain",
    ))

    global_vars["admin"] = user_service.create(UserSchema(
        first_name="Name2",
        last_name="Lastname2",
        patronymic="Patronymic2",
        birth_date="2000-01-01",
        country="Country2",
        city="City2",
        phone="+7(999)999-99-99",
        email="address2@domain.com",
        password="password",
        role="Admin",
    ))

    global_vars["judge"] = user_service.create(UserSchema(
        first_name="Name3",
        last_name="Lastname3",
        patronymic="Patronymic3",
        birth_date="2000-01-01",
        country="Country3",
        city="City3",
        phone="+7(999)999-99-99",
        email="address3@domain.com",
        password="password",
        role="Judge",
    ))

    global_vars["captain2"] = user_service.create(UserSchema(
        first_name="Name4",
        last_name="Lastname4",
        patronymic="Patronymic4",
        birth_date="2000-01-01",
        country="Country4",
        city="City4",
        phone="+7(999)999-99-99",
        email="address4@domain.com",
        password="password",
        role="Captain",
    ))


    global_vars["team1"] = team_service.create(TeamCreateSchema(
        leader_id=captain1.id,
        name="Team1",
    ))

    global_vars["team2"] = team_service.create(TeamCreateSchema(
        leader_id=captain2.id,
        name="Team2",
    ))


    global_vars["player1_team1"] = player_service.create_in_team(PlayerCreateSchema(
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
        pd_accepted=True,
        is_active_in_team=True,
    ))

    global_vars["player2_team1"] = player_service.create_in_team(PlayerCreateSchema(
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
        pd_accepted=True,
        is_active_in_team=True,
    ))

    global_vars["player1_team2"] = player_service.create_in_team(PlayerCreateSchema(
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
        pd_accepted=True,
        is_active_in_team=True,
    ))

    global_vars["player2_team2"] = player_service.create_in_team(PlayerCreateSchema(
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
        pd_accepted=True,
        is_active_in_team=True,
    ))


    global_vars["team_composition1_team1"] = team_composition_service.create(TeamCompositionSchema(
        team=team1,
        players=[player1_team1, player2_team1],
    ))

    global_vars["team_composition2_team1"] = team_composition_service.create(TeamCompositionSchema(
        team=team1,
        players=[player1_team1, player2_team1],
    ))

    global_vars["team_composition1_team2"] = team_composition_service.create(TeamCompositionSchema(
        team=team2,
        players=[player1_team2, player2_team2],
    ))

    global_vars["tournament1"] = tournament_service.create(TournamentCreateSchema(
        name="Tournament1",
        location="Location1",
        discipline="Discipline1",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        main_judge_id=judge.id,
        state="JUST_CREATED",
    ))

    global_vars["tournament2"] = tournament_service.create(TournamentCreateSchema(
        name="Tournament2",
        location="Location2",
        discipline="Discipline2",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        main_judge_id=judge.id,
        state="JUST_CREATED",
    ))


    global_vars["match1"] = match_service.create(MatchCreateSchema(
        team_a_id=team1.id,
        team_b_id=team2.id,
    ))

    global_vars["match2"] = match_service.create(MatchCreateSchema(
        team_a_id=team1.id,
        team_b_id=team2.id,
    ))

    return True


def player_test() -> bool:
    player1_create = player_service.create_in_team(team1.id, player1_team1) 
    player2_create = player_service.create_in_team(team2.id, player1_team2)

    players1_get_all = player_service.get_all_in_team(team1.id)
    players2_get_all = player_service.get_all_in_team(team2.id)

    player1_get = player_service.get_by_id(player1_create.id)
    player2_get = player_service.get_by_id(player2_create.id)

    player1_is_in_team = player_service.is_in_team(player1_create.id, team1.id)
    player2_is_in_team = player_service.is_in_team(player2_create.id, team2.id)

    player1_delete = player_service.delete(player1_create.id)
    player2_delete = player_service.delete(player2_create.id)

    return True


def team_test() -> bool:
    team1_create = team_service.create(team1, captain1.id)
    team2_create = team_service.create(team2, captain2.id)

    get_all_teams = team_service.get_all()

    get_by_id_team1 = team_service.get_by_id(team1_create.id)
    get_by_id_team2 = team_service.get_by_id(team2_create.id)

    get_by_leader_id_team1 = team_service.get_by_leader_id(captain1.id)
    get_by_leader_id_team2 = team_service.get_by_leader_id(captain2.id)

    return True


def user_test() -> bool:
    captain1_create = user_service.create(captain1)
    captain2_create = user_service.create(captain2)

    admin_create = user_service.create(admin)

    judge_create = user_service.create(judge)

    get_all_users = user_service.get_all()

    get_by_id_captain1 = user_service.get_by_id(captain1_create.id)
    get_by_id_captain2 = user_service.get_by_id(captain2_create.id)
    get_by_id_admin = user_service.get_by_id(admin_create.id)
    get_by_id_judge = user_service.get_by_id(judge_create.id)

    get_by_email_captain1 = user_service.get_by_email(captain1.email)
    get_by_email_captain2 = user_service.get_by_email(captain2.email)
    get_by_email_admin = user_service.get_by_email(admin.email)
    get_by_email_judge = user_service.get_by_email(judge.email)

    delete_captain1 = user_service.delete(captain1_create.id)
    delete_captain2 = user_service.delete(captain2_create.id)
    delete_admin = user_service.delete(admin_create.id)
    delete_judge = user_service.delete(judge_create.id)

    return True


def tournament_test() -> bool:
    tournament1_create = tournament_service.create(tournament1)
    tournament2_create = tournament_service.create(tournament2)

    get_all_tournaments = tournament_service.get_all()

    get_by_id_tournament1 = tournament_service.get_by_id(tournament1_create.id)
    get_by_id_tournament2 = tournament_service.get_by_id(tournament2_create.id)

    get_team_comps_tournament1 = tournament_service.get_team_comps(tournament1_create.id)
    get_team_comps_tournament2 = tournament_service.get_team_comps(tournament2_create.id)

    delete_tournament1 = tournament_service.delete(tournament1_create.id)
    delete_tournament2 = tournament_service.delete(tournament2_create.id)

    return True


def team_composition_test() -> bool:
    team_composition1_create = team_composition_service.create(team_composition1_team1)
    team_composition2_create = team_composition_service.create(team_composition1_team2)
    team_composition3_create = team_composition_service.create(team_composition2_team1)

    
    return True


def match_test() -> bool:
    match1_create = match_service.create(match1)
    match2_create = match_service.create(match2)

    get_by_id_match1 = match_service.get_by_id(match1_create.id)
    get_by_id_match2 = match_service.get_by_id(match2_create.id)

    delete_match1 = match_service.delete(match1_create.id)
    delete_match2 = match_service.delete(match2_create.id)

    return True


def tournament_requests_test() -> bool:
    request1_create = tournament_request_service.create_request(tournament1.id, team1.id)
    request2_create = tournament_request_service.create_request(tournament1.id, team2.id)
    request3_create = tournament_request_service.create_request(tournament2.id, team1.id)
    request4_create = tournament_request_service.create_request(tournament2.id, team2.id)

    get_tournament1_requests_by_tour_id = tournament_request_service.get_tournament_requests(tournament1.id)
    get_tournament2_requests_by_tour_id = tournament_request_service.get_tournament_requests(tournament2.id)

    get_by_team1_id_= tournament_request_service.get_by_team_id(tournament1.id, team1.id)
    get_by_team2_id_= tournament_request_service.get_by_team_id(tournament1.id, team2.id)
    get_by_team3_id_= tournament_request_service.get_by_team_id(tournament2.id, team1.id)
    get_by_team4_id_= tournament_request_service.get_by_team_id(tournament2.id, team2.id)

    accept_request1 = tournament_request_service.accept_request(request1_create.id)
    accept_request2 = tournament_request_service.accept_request(request2_create.id)
    accept_request3 = tournament_request_service.accept_request(request3_create.id)
    accept_request4 = tournament_request_service.accept_request(request4_create.id)

    decline_request1 = tournament_request_service.decline_request(request1_create.id)
    decline_request2 = tournament_request_service.decline_request(request2_create.id)
    decline_request3 = tournament_request_service.decline_request(request3_create.id)
    decline_request4 = tournament_request_service.decline_request(request4_create.id)

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

