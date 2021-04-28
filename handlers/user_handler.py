from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette import status

from services.user_service import UserService

class UserHandler(HTTPEndpoint):

    def __init__(self, *args):
        self.service = UserService()
        super().__init__(*args)

    async def get(self, request):
        user = await self.service.find_one()
        return JSONResponse(content={"user": user})

    async def post(self, request):
        body = await request.json()
        await self.service.create(body)
        return JSONResponse(content={"msg": "ok"}, status_code=status.HTTP_201_CREATED)
        

    async def put(self, request):
        pass

    async def delete(self, request):
        pass