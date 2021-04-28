from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette import status

from services.user_service import UserService

# @TODO: jwt auth, get user_id from jwt
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
        return JSONResponse(content={"message": "new user was successful created"}, status_code=status.HTTP_201_CREATED)
        
    async def put(self, request):
        body = await request.json()
        await self.service.update(body=body, id=1)
        return JSONResponse(content={"message": "user was successful updated"}, status_code=status.HTTP_200_OK)

    async def delete(self, request):
        await self.service.delete(id=1)
        return JSONResponse(content={"message": "user was successful deleted"}, status_code=status.HTTP_200_OK)
