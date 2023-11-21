from sqlalchemy.sql import select

from app.models.user import User, UserRole


def get_all_by_role(session, role: UserRole) -> list[User]:
    return session.query(User).filter(User.role == role).all()


def get_by_id(session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_by_email(session, email: str) -> User | None:
    result = session.execute(select(User).where(User.email == email).limit(1))
    return result.scalar_one_or_none()


def save(session, user: User) -> User:
    session.add(user)
    session.flush()
    session.commit()
    return user


def delete(session, user: User) -> None:
    session.delete(user)
    session.commit()
