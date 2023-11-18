import asyncio
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker

from app.core.settings import settings


class Base(DeclarativeBase):
    ...


from app.models.user import User  # noqa: F401, E402

_engine: Engine = None
_session_factory: scoped_session[Session] = None


def initialize():
    global _engine, _session_factory

    _engine = create_engine(settings.db_url)
    _session_factory = scoped_session(
        sessionmaker(_engine, autoflush=False, expire_on_commit=True),
        lambda: asyncio.current_task(),
    )

    Base.metadata.create_all(_engine)


def release():
    _session_factory.close_all()
    _engine.dispose()


@contextmanager
def create_session():
    session = _session_factory()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
