from fastapi import APIRouter

from app.api.routes import animes, authentication

api_router = APIRouter()

api_router.include_router(authentication.router)
api_router.include_router(animes.router)
