from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import db
from app.core.settings import settings
from app.exceptions import EntityAlreadyExistsException
from app.routers.match import router as match_router
from app.routers.player import router as player_router
from app.routers.status import router as status_router
from app.routers.team import router as team_router
from app.routers.team_composition import router as team_composition_router
from app.routers.tournament import router as tournament_router
from app.routers.user import router as user_router
from app.services import user_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()

    if settings.initial_user_schema is not None:
        try:
            user_service.create(settings.initial_user_schema)
        except EntityAlreadyExistsException:
            print("Initial user already exist. Skipping.")

    yield

    db.release()


def create_app():
    app = FastAPI(redoc_url=None, title="FSP Cup 2023", lifespan=lifespan)

    app.include_router(status_router)
    app.include_router(user_router)
    app.include_router(player_router)
    app.include_router(match_router)
    app.include_router(tournament_router)
    app.include_router(team_router)
    app.include_router(team_composition_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
