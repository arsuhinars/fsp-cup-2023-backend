from app.schemas.match_create_schema import MatchCreateSchema
from app.schemas.match_schema import MatchUpdateSchema
from app.schemas.user_create_schema import UserCreateSchema
import match_service
import password_service
import player_service
import team_composition_service
import team_service
import tournament_service
import user_service

def init() -> bool:
    captain1 = user_service.create(UserSchema(
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

    admin = user_service.create(UserSchema(
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

    judge = user_service.create(UserSchema(
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

    captain2 = user_service.create(UserSchema(
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


    team1 = team_service.create(TeamCreateSchema(
        leader_id=captain1.id,
        name="Team1",
    ))

    team2 = team_service.create(TeamCreateSchema(
        leader_id=captain2.id,
        name="Team2",
    ))


    player1_team1 = player_service.create_in_team(PlayerCreateSchema(
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

    player2_team1 = player_service.create_in_team(PlayerCreateSchema(
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

    player1_team2 = player_service.create_in_team(PlayerCreateSchema(
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

    player2_team2 = player_service.create_in_team(PlayerCreateSchema(
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


    team_composition1_team1 = team_composition_service.create(TeamCompositionSchema(
        team=team1,
        players=[player1_team1, player2_team1],
    ))

    team_composition2_team1 = team_composition_service.create(TeamCompositionSchema(
        team=team1,
        players=[player1_team1, player2_team1],
    ))

    team_composition1_team2 = team_composition_service.create(TeamCompositionSchema(
        team=team2,
        players=[player1_team2, player2_team2],
    ))

    tournament1 = tournament_service.create(TournamentCreateSchema(
        name="Tournament1",
        location="Location1",
        discipline="Discipline1",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        main_judge_id=judge.id
        state="JUST_CREATED",
    ))

    tournament2 = tournament_service.create(TournamentCreateSchema(
        name="Tournament2",
        location="Location2",
        discipline="Discipline2",
        date_registration="2000-01-01",
        date_begin="2000-02-01",
        date_end="2000-03-01",
        date_awards="2000-04-01",
        main_judge_id=judge.id
        state="JUST_CREATED",
    ))


    match1 = match_service.create(MatchCreateSchema(
        team_a_id=team1.id,
        team_b_id=team2.id,
    ))

    match2 = match_service.create(MatchCreateSchema(
        team_a_id=team1.id,
        team_b_id=team2.id,
    ))