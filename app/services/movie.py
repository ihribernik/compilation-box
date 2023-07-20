from motor.motor_asyncio import AsyncIOMotorClient

from app.services.database import BaseCrud


class MovieCrud(BaseCrud):
    def __init__(
        self, connection: AsyncIOMotorClient, db: str, collection: str
    ) -> None:
        self.connection = connection
        self.db = self.connection[db]
        self.collection = self.db[collection]

    async def add_movie(self):
        ...

    async def delete_movie(self) -> bool:
        row = await self.collection.find_one({})
        if row:
            result = await self.collection.delete_one({})
            if result.deleted_count > 0:
                return True
            else:
                return False
        return False

    async def get_movie(self):
        row = await self.collection.find_one()
        return row

    async def get_movies(self):
        rows = await self.collection.find()
        return rows

    async def update_movie(self):
        ...
