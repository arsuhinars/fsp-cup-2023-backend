import app.core.db as db
import app.repositories.user_repository as user_repo
from app.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
    InvalidFormatException,
)
from app.models.user import User
from app.schemas.user_create_schema import UserCreateSchema
from app.schemas.user_password_update_schema import UserPasswordUpdateSchema
from app.schemas.user_schema import UserRole, UserSchema
from app.schemas.user_update_schema import UserUpdateSchema
from app.services import password_service
from app.utils import map_model_to_orm


def create(dto: UserCreateSchema) -> UserSchema:
    user = User(**dto.model_dump(exclude=["password"]))

    if user.role != UserRole.JUDGE and user.judge_rank is not None:
        raise InvalidFormatException(
            'User without role "JUDGE" must not have "judge_rank"'
        )

    with db.create_session() as session:
        if user_repo.get_by_email(session, dto.email) is not None:
            raise EntityAlreadyExistsException("User with this email already exists")

        user.password_salt = password_service.generate_salt()
        user.password_hash = password_service.encode_password(
            dto.password, user.password_salt
        )

        user = user_repo.save(session, user)

        return UserSchema.model_validate(user)


def get_all(role: UserRole | None) -> list[UserSchema]:
    with db.create_session() as session:
        users = user_repo.get_all(session, role)
        return list(map(UserSchema.model_validate, users))


def get_by_id(user_id: int) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.model_validate(user)


def get_by_email(email: str) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.model_validate(user)


def update(user_id: int, dto: UserUpdateSchema) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")

        if dto.judge_rank is not None and user.role != UserRole.JUDGE:
            raise InvalidFormatException(
                'User without role "JUDGE" must not have "judge_rank"'
            )

        if (
            user.email != dto.email
            and user_repo.get_by_email(session, dto.email) is not None
        ):
            raise EntityAlreadyExistsException("User with this email already exists")

        map_model_to_orm(dto, user)
        user_repo.save(session, user)

        return UserSchema.model_validate(user)


def update_password(user_id: int, dto: UserPasswordUpdateSchema) -> None:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")

        user.password_salt = password_service.generate_salt()
        user.password_hash = password_service.encode_password(
            dto.new_password, user.password_salt
        )

        user_repo.save(session, user)


def delete(user_id: int) -> None:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        user_repo.delete(session, user)


def check_credentials(email: str, password: str) -> bool:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            return False

        return password_service.compare_passwords(
            password, user.password_salt, user.password_hash
        )
