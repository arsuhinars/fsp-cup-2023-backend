from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.user import User
from app.schemas.user_schema import UserRole


def get_all(session: Session, role: UserRole | None) -> list[User]:
    q = select(User)
    if role is not None:
        q = q.filter(User.role == role)
    q = q.order_by(User.id)

    return list(session.execute(q).scalars())


def get_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_by_email(session: Session, email: str) -> User | None:
    q = select(User).where(User.email == email).limit(1)
    return session.execute(q).scalar_one_or_none()


def save(session: Session, user: User) -> User:
    session.add(user)
    session.flush()
    session.commit()
    return user


def delete(session: Session, user: User) -> None:
    session.delete(user)
    session.commit()
