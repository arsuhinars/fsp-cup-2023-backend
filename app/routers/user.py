from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.post("/", tags=["user"])
def post_user(password: str,
              first_name: str,
              last_name: str,
              patronymic: str,
              birth_date: str,
              country: str,
              city: str,
              phone: str,
              email: str,
              role: str,
              rank: str):
    pass


@router.get("/", tags=["user"])
def get_user(user_id: int):
    pass


@router.put("/", tags=["user"])
def update_user(user_id: int,
                password: str,
                first_name: str,
                last_name: str,
                patronymic: str,
                birth_date: str,
                country: str,
                city: str,
                phone: str,
                email: str,
                role: str,
                rank: str):
    pass


@router.delete("/", tags=["user"])
def delete_user(user_id: int):
    pass
