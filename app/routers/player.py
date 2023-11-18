from fastapi import APIRouter

router = APIRouter(prefix="/player")


@router.post("/", tags=["player"])
def post_player(gto_id: int,
                team_id: int,
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


@router.get("/", tags=["player"])
def get_player(player_id: int):
    pass


@router.put("/", tags=["player"])
def update_player(player_id: int,
                  team_id: int,
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


@router.delete("/", tags=["player"])
def delete_player(player_id: int):
    pass
