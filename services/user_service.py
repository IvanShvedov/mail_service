from typing import Union

from storage.storage import Storage
from models.user import UserDTC

class UserService:

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    async def create(self, body):
        user = await self._parse_body(body)
        await self.storage.create(
            f"""
            INSERT INTO users (email, password) VALUES (
            '{user.email}',
            '{user.password}'
            )
            """
        )

    async def find_one(self, id: Union[int, str]):
        pass

    async def _parse_body(self, body) -> UserDTC:
        user = UserDTC()
        print(body)
        for k, v in body.items():
            setattr(user, k, v)
        return user

    async def _get_password_hash(self, password: str):
        pass
