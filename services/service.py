from abc import abstractmethod, ABC


class Service(ABC):
    
    @abstractmethod
    async def create(self):
        pass