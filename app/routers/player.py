from fastapi import APIRouter

router = APIRouter(prefix="/player", tags=["player"])


@router.post("/", description="team_id is defined by leader.team.id")
def post_player(gto_id: int,
                first_name: str,
                last_name: str,
                patronymic: str,
                birth_date: str,
                gender: str,
                nickname: str,
                country: str,
                city: str,
                citizenship: str,
                phone: str,
                email: str,
                rank: str,
                pd_accepted: bool):
    pass


@router.get("/")
def get_player(player_id: int):
    pass


@router.put("/")
def update_player(player_id: int,
                  gto_id: int,
                  first_name: str,
                  last_name: str,
                  patronymic: str,
                  birth_date: str,
                  gender: str,
                  nickname: str,
                  country: str,
                  city: str,
                  citizenship: str,
                  phone: str,
                  email: str,
                  rank: str,
                  accepted: bool):
    pass


@router.delete("/")
def delete_player(player_id: int):
    pass
