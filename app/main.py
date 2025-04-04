from fastapi import FastAPI

from app.routers import animes, authentication, shows
from app.core.db import init

app = FastAPI()

app.include_router(authentication.router)
app.include_router(animes.router)
app.include_router(shows.router)


@app.on_event("startup")
async def start_db():
    await init()
