from starlette.endpoints import HTTPEndpoint


class UserHandler(HTTPEndpoint):


    def __init__(self, service):
        self.service = service

    async def get(self, request):
        pass

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass