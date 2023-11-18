from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import db
from app.routers.status import router as status_router
from app.routers.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()
    yield
    db.release()


def create_app():
    app = FastAPI(redoc_url=None, title="FSP Cup 2023", lifespan=lifespan)

    app.include_router(status_router)
    app.include_router(user_router)

    return app
