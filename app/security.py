from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.exceptions import ForbiddenException, UnauthorizedException
from app.models.user import UserRole
from app.schemas.user_schema import UserSchema
from app.services import user_service

security = HTTPBasic()


def authenticate(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> UserSchema | None:
    email = credentials.username
    password = credentials.password

    if not user_service.check_credentials(email, password):
        raise UnauthorizedException("Invalid credentials were provided")

    return user_service.get_by_email(email)


class RequireRoles:
    def __init__(self, roles: list[UserRole]):
        self.__roles = roles

    def __call__(self, user: Annotated[UserSchema, Depends(authenticate)]):
        if user.role not in self.__roles:
            raise ForbiddenException("You don't have enough rights")
        return user


require_admin = RequireRoles([UserRole.ADMIN])
require_judge = RequireRoles([UserRole.JUDGE])
require_team_captain = RequireRoles([UserRole.TEAM_CAPTAIN])
