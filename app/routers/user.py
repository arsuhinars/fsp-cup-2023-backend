from fastapi import APIRouter

from app.models.user import UserRole
from app.schemas.user_create_schema import UserCreateSchema
from app.schemas.user_update_schema import UserUpdateSchema
from app.schemas.user_schema import UserSchema
import app.services.user_service as user_service

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/",
             response_model=UserSchema)
def post_user(user: UserCreateSchema):
    return user_service.create(user)


@router.get("/all",
            response_model=list[UserSchema])
def get_all_user_by_role(role: UserRole):
    return user_service.get_all_by_role(role)


@router.put("/",
            response_model=UserSchema)
def update_user(user: UserUpdateSchema):
    return user_service.update(user.id, user)


@router.delete("/")
def delete_user(user_id: int):
    return user_service.delete(user_id)
