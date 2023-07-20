from fastapi import FastAPI
from app.routers import authentication, movies, shows
from app.settings.database import init

app = FastAPI()

app.include_router(authentication.router)
app.include_router(movies.router)
app.include_router(shows.router)


@app.on_event("startup")
async def start_db():
    await init()
