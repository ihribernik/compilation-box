from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from app.utils.constants import DB_NAME, MONGO_URL
from app.utils.logger import logger


async def init():
    # Create Motor client
    try:
        client = AsyncIOMotorClient(MONGO_URL)

        await init_beanie(
            database=client[DB_NAME],
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
        logger.error(f"MSG: %s", exc)

    except Exception as exc1:
        logger.error(f"MSG: %s", exc1)
