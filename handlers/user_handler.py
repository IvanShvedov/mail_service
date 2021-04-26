from starlette.endpoints import HTTPEndpoint

from services.service import Service

class UserHandler(HTTPEndpoint):

    __slots__ = ['service']

    def __init__(self, *args):
        super().__init__(*args)

    async def get(self, request):
        self.service.create()

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass