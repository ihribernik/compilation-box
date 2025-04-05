import asyncio
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

from app.core.config import settings
from app.core.logger import logger
from app.models import Anime, Employee, Episode, Genre, Studio, Role, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Conectando a Mongo...")
        logger.info("URL: %s", settings.MONGO_URL)
        logger.info("DB:%s", settings.MONGO_DB)

        app.db = AsyncIOMotorClient(settings.MONGO_URL)
        await init_beanie(
            database=app.db[settings.MONGO_DB],
            document_models=[
                Anime,
                Employee,
                Episode,
                Genre,
                Studio,
                Role,
                User,
            ],
        )
        logger.info("Startup complete")
        yield
        logger.info("Shutdown complete")

    except ServerSelectionTimeoutError as exc:
        logger.error("MSG: %s", exc)

    except Exception as exc1:
        logger.error("MSG: %s", exc1)
