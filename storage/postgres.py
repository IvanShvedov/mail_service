from databases import Database

from storage.storage import Storage


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

    async def find_one(self, command: str):
        res = await self._database.fetch_one(command)
        return res

    async def find(self, command: str):
        res = await self._database.fetch_all(command)
        return res

    async def create(self, command: str):
        res = await self._database.execute(command)
        return res

    async def update(self, command: str):
        res = await self._database.execute(command)
        return res

    async def delete(self, command: str):
        res = await self._database.execute(command)
        return res