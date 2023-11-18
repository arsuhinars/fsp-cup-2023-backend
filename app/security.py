import secrets
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.exceptions import ForbiddenException, UnauthorizedException
from app.models.user import User, UserRole

security = HTTPBasic()


def authenticate(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> User | None:
    login = credentials.username.encode("utf-8")
    password = credentials.password.encode("utf-8")

    # TODO: поиск логина в БД, хеширование и сравнение с паролем,
    # возвращение объекта пользователя

    is_login_correct = secrets.compare_digest(login, b"admin")
    is_password_correct = secrets.compare_digest(password, b"12345678")

    if not (is_login_correct and is_password_correct):
        raise UnauthorizedException("Invalid credentials were provided")

    return User()


class RequireRoles:
    def __init__(self, roles: list[UserRole]):
        self.__roles = roles

    def __call__(self, user: Annotated[User, Depends(authenticate)]):
        if user.role not in self.__roles:
            raise ForbiddenException("You don't have enough rights")
