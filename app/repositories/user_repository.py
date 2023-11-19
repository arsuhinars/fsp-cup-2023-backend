from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models import User


def get_by_id(session_factory, user_id: int) -> User | None:
    session: Session
    with session_factory() as session:
        return session.get(User, user_id)


def get_by_email(session_factory, email: str) -> User | None:
    session: Session
    with session_factory() as session:
        result = session.execute(
            select(User).where(User.email == email).limit(1)
        )
        return result.scalar_one_or_none()


def save(session_factory, user: User) -> User:
    session: Session
    with session_factory() as session:
        session.add(user)
        session.flush()
        session.commit()
        return user
