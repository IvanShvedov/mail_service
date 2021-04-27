from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response, JSONResponse

from services.user_service import UserService


class UserHandler(HTTPEndpoint):

    def __init__(self, *args):
        self.service = UserService()
        super().__init__(*args)

    async def get(self, request):
        await self.service.create()
        return JSONResponse(content={"msg":"hi"})

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass