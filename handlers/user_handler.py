from starlette.endpoints import HTTPEndpoint

from services.service import Service

class UserHandler(HTTPEndpoint):

    def __init__(self, *args, **kwargs):
        # self.service = 
        print(args)
        super().__init__(*args, **kwargs)

    async def get(self, request):
        self.service.create()

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass