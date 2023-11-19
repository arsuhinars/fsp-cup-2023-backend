from fastapi import APIRouter

from app.schemas import UserUpdateSchema, UserCreateSchema
from app.schemas.user_schema import UserSchema
import app.services.user_service as user_service

router = APIRouter(prefix="/user")


@router.post("/",
             response_model=UserCreateSchema,
             tags=["user"])
def post_user(user: UserCreateSchema):
    return user_service.create(user)


@router.get("/",
            response_model=UserSchema,
            tags=["user"])
def get_user(user_id: int):
    return UserSchema()


@router.put("/",
            response_model=UserUpdateSchema,
            tags=["user"])
def update_user(user: UserUpdateSchema):
    pass


@router.delete("/",
               tags=["user"])
def delete_user(user_id: int):
    pass
