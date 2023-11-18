from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import db
from app.routers.status import router as status_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()
    yield
    db.release()


def create_app():
    app = FastAPI(redoc_url=None, title="FSP Cup 2023", lifespan=lifespan)

    app.include_router(status_router)

    return app
