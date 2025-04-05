from fastapi import APIRouter

from app.api.routes import (
    anime,
    authentication,
    employee,
    episode,
    genre,
    role,
    studio,
    test,
)

api_router = APIRouter()

api_router.include_router(authentication.router)
api_router.include_router(anime.router)
api_router.include_router(employee.router)
api_router.include_router(episode.router)
api_router.include_router(genre.router)
api_router.include_router(role.router)
api_router.include_router(studio.router)
api_router.include_router(test.router)
