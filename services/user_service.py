from storage.storage import Storage

class UserService:

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    async def create(self):
        print('a')

    async def get(self):
        pass
