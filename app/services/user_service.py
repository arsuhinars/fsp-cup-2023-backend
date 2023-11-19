from hashlib import md5
from http import HTTPStatus

from email_validator import EmailNotValidError, validate_email

from app.exceptions import ValidationException, EntityAlreadyExistsException
from app.models import User
import app.repositories.user_repository as user_repo
from app.schemas import UserCreateSchema, UserSchema, UserUpdateSchema
import app.core.db as db


def create(user: UserCreateSchema) -> UserSchema:
    with db.create_session() as session:
        try:
            user.email = validate_email(
                user.email, check_deliverability=False
            ).normalized
        except EmailNotValidError:
            raise ValidationException("Invalid email")

        if (user_repo.get_by_email(session, user.email)) is not None:
            raise EntityAlreadyExistsException("User with this email already exists")

        user_dump = user.model_dump()
        user_dump["password_hash"] = md5(user.password).hexdigest()
        del user_dump["password"]

        user = User(**user_dump)

        # user = User(
        #     password_hash=md5(user.password).hexdigest(),
        #     first_name=user.first_name,
        #     last_name=user.last_name,
        #     patronymic=user.patronymic,
        #     birth_date=user.birth_date,
        #     country=user.country,
        #     city=user.city,
        #     phone=user.phone,
        #     email=user.email,
        #     role=user.role
        # )

        return UserSchema.model_validate(user_repo.save(session, user))


def get_by_id(user_id: int):
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        return UserSchema.model_validate(user)


def get_by_email(email: str):
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            return None
        return UserSchema.model_validate(user)


def update(user_id: int, user: UserUpdateSchema):
    with db.create_session() as session:
        db_user = user_repo.get_by_id(session, user_id)
        if db_user is None:
            return {"status_code": HTTPStatus.NOT_FOUND, "detail": "User not found"}

        db_user.display_name = user.display_name
        db_user = user_repo.save(session, db_user)

        return UserSchema.model_validate(db_user)


def check_credentials(email: str, password: str) -> bool:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            return False

        return user.password_hash == md5(password).hexdigest()
