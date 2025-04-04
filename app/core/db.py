from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from app.core.logger import logger
from app.core.config import settings


async def init():
    # Create Motor client
    try:
        client = AsyncIOMotorClient(settings.MONGO_URL)

        await init_beanie(
            database=client[settings.MONGO_DB],
            document_models=[
                "app.models.Anime",
                "app.models.Employee",
                "app.models.Episode",
                "app.models.Genre",
                "app.models.Studio",
                "app.models.Role",
                "app.models.User",
            ],
        )

    except ServerSelectionTimeoutError as exc:
        logger.error("MSG: %s", exc)

    except Exception as exc1:
        logger.error("MSG: %s", exc1)
