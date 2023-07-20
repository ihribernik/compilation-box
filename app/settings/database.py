from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from app.utils.constants import DB_NAME


async def init():
    # Create Motor client
    try:
        client = AsyncIOMotorClient(
            "mongodb://root:root123@localhost:27017/?authMechanism=DEFAULT"
        )

        await init_beanie(
            database=client[DB_NAME],
            document_models=[
                "app.models.Employee",
                "app.models.Episode",
                "app.models.Movie",
                "app.models.Role",
                "app.models.Season",
                "app.models.TvShow",
                "app.models.User",
            ],
        )

    except ServerSelectionTimeoutError as exc:
        print(f"connection timeout... {exc=}")

    except Exception as exc1:
        print(f"Some randond {exc1}")
