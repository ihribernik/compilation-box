from fastapi import FastAPI
from .routers import authentication, movies, shows

app = FastAPI()

app.include_router(authentication.router)
app.include_router(movies.router)
app.include_router(shows.router)
