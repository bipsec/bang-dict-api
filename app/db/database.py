from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings


class Database:
    def __init__(self):
        self.client = None
        self.database = None

    async def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URI)
        self.database = self.client[settings.MONGODB_DATABASE]

        # Create the database if it does not exist
        if settings.MONGODB_DATABASE not in await self.client.list_database_names():
            await self.client[settings.MONGODB_DATABASE].command("create", settings.MONGODB_DATABASE)

    async def disconnect(self):
        self.client.close()


database = Database()
