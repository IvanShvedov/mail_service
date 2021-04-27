from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    async def find_one(self, *args, **kwargs):
        pass

    @abstractmethod
    async def find(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, *args, **kwargs):
        pass
