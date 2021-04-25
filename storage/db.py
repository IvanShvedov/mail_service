from storage.storage import Storage
from databases import Database

class PostgresStorage(Storage):
    __slots__ = [
        'url',
        '_database'
        ]

    def __init__(
        self,
        host: str = '127.0.0.1',
        username: str = 'postgres',
        password: str = 'postgres',
        dbname: str = 'postgres',
        port: int = 5432
        ):
        # postgres://user:password@host:port/database?option=value
        self.url = f"postgres://{username}:{password}@{host}:{port}/{dbname}"

    async def connect(self):
        self._database = Database(url=self.url)
        await self._database.connect()

    async def find_one(self, *args, **kwargs):
        pass

    async def find(self, *args, **kwargs):
        pass

    async def create(self, *args, **kwargs):
        pass

    async def update(self, *args, **kwargs):
        pass

    async def delete(self, *args, **kwargs):
        pass