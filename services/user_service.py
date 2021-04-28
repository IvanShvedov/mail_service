from typing import Any, Union, Dict

from storage.storage import Storage
from models.user import UserDTC

class UserService:

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    async def find_one(self, id: Union[int, str]):
        res = await self.storage.find_one(
            f"""
            SELECT * FROM users
            WHERE users.id={id}
            """
        )
        user = await self._parse_body(res)
        return user.to_dict()

    async def create(self, body: Dict[str, Any]):
        user = await self._parse_body(body)
        await self.storage.create(
            f"""
            INSERT INTO users (email, password) VALUES (
            '{user.email}',
            '{user.password}'
            )
            """
        )

    async def update(self, body: Dict[str, Any], id: int):
        user = await self._parse_body(body)
        await self.storage.update(
            f"""
            UPDATE users
            SET email='{user.email}', password='{user.password}'
            WHERE users.id = {id}
            """
        )

    async def delete(self, id: int):
        await self.storage.delete(
            f"""
            DELETE FROM users
            WHERE users.id={id}
            """
        )

    async def _parse_body(self, body) -> UserDTC:
        user = UserDTC()
        for k, v in body.items():
            setattr(user, k, v)
        return user

    async def _get_password_hash(self, password: str):
        pass
