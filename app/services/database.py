from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.constants import MONGO_MAX_CONNECTIONS, MONGO_MIN_CONNECTIONS, MONGO_URL


class Database:
    client: AsyncIOMotorClient | None = None


db = Database()


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect():
    """Connect to MONGO DB"""
    db.client = AsyncIOMotorClient(
        str(MONGO_URL),
        maxPoolSize=MONGO_MAX_CONNECTIONS,
        minPoolSize=MONGO_MIN_CONNECTIONS,
    )
    print(f"Connected to mongo at {MONGO_URL}")


async def close():
    """Close MongoDB Connection"""
    db.client.close()
    print("Closed connection with MongoDB")


class BaseCrud(ABC):
    @abstractmethod
    async def add_movie(self):
        pass

    @abstractmethod
    async def delete_movie(self) -> bool:
        pass

    @abstractmethod
    async def get_movie(self):
        pass

    @abstractmethod
    async def get_movies(self):
        pass

    @abstractmethod
    async def update_movie(self):
        pass
