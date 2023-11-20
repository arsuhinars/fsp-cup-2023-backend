from hashlib import md5

from app.exceptions import EntityAlreadyExistsException, EntityNotFoundException
from app.models.user import UserRole
import app.repositories.user_repository as user_repo
from app.schemas.user_create_schema import UserCreateSchema
from app.schemas.user_schema import UserSchema
from app.schemas.user_update_schema import UserUpdateSchema
import app.core.db as db


def create(user: UserCreateSchema) -> UserSchema:
    user = UserCreateSchema.model_validate(user).to_model()
    with db.create_session() as session:
        if user_repo.get_by_email(session, user.email) is not None:
            raise EntityAlreadyExistsException("User with this email already exists")
        return UserSchema.from_model(user_repo.save(session, user))


def get_all_by_role(role: UserRole) -> list[UserSchema]:
    with db.create_session() as session:
        users = user_repo.get_all_by_role(session, role)
        return [UserSchema.from_model(user) for user in users]


def get_by_id(user_id: int) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.from_model(user)


def get_by_email(email: str) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.from_model(user)


def update(user_id: int, user: UserUpdateSchema) -> UserSchema:
    UserUpdateSchema.model_validate(user)
    with db.create_session() as session:
        db_user = user_repo.get_by_id(session, user_id)
        if db_user is None:
            raise EntityNotFoundException("User not found")
        db_user = user_repo.save(session, user.to_model(db_user))
        return UserSchema.from_model(db_user)


def delete(user_id: int) -> bool:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        user_repo.delete(session, user)
        return True


def check_credentials(email: str, password: str) -> bool:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            return False

        return user.password_hash == md5(password.encode()).hexdigest()
