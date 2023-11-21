from typing import Annotated

from fastapi import APIRouter, Depends

import app.services.user_service as user_service
from app.models.user import User, UserRole
from app.schemas.user_create_schema import UserCreateSchema
from app.schemas.user_password_update_schema import UserPasswordUpdateSchema
from app.schemas.user_schema import UserSchema
from app.schemas.user_update_schema import UserUpdateSchema
from app.security import authenticate, require_admin

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=UserSchema, dependencies=[Depends(require_admin)])
def create_user(user: UserCreateSchema):
    return user_service.create(user)


@router.get("/", response_model=list[UserSchema], dependencies=[Depends(require_admin)])
def get_all_users(role: UserRole | None = None):
    return user_service.get_all(role)


@router.get("/current", response_model=UserSchema)
def get_current_user(user: Annotated[User, Depends(authenticate)]):
    return UserSchema.model_validate(user)


@router.put("/current", response_model=UserSchema)
def update_current_user(
    user_schema: UserUpdateSchema, user: Annotated[User, Depends(authenticate)]
):
    return user_service.update(user.id, user_schema)


@router.put("/current/password")
def update_current_user_password(
    user_schema: UserPasswordUpdateSchema, user: Annotated[User, Depends(authenticate)]
):
    return user_service.update_password(user.id, user_schema)


@router.get("/{id}", response_model=UserSchema, dependencies=[Depends(require_admin)])
def get_user_by_id(id: int):
    return user_service.get_by_id(id)


@router.put("/{id}", response_model=UserSchema, dependencies=[Depends(require_admin)])
def update_user_by_id(id: int, user: UserUpdateSchema):
    return user_service.update(id, user)


@router.delete("/{id}", dependencies=[Depends(require_admin)])
def delete_user(id: int):
    return user_service.delete(id)
