from fastapi import APIRouter

import app.services.user_service as user_service
from app.models.user import UserRole
from app.schemas.user_create_schema import UserCreateSchema
from app.schemas.user_schema import UserSchema
from app.schemas.user_update_schema import UserUpdateSchema

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=UserSchema)
def create_user(user: UserCreateSchema):
    return user_service.create(user)


@router.get("/", response_model=list[UserSchema])
def get_all_user_by_role(role: UserRole):
    return user_service.get_all_by_role(role)


@router.get("/current", response_model=UserSchema)
def get_current_user():
    pass


@router.put("/", response_model=UserSchema)
def update_user(user: UserUpdateSchema):
    return user_service.update(user.id, user)


@router.put("/current")
def update_current_user(password: str, user: UserUpdateSchema):
    pass


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return user_service.delete(user_id)
