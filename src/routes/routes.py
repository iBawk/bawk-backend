from fastapi import APIRouter
from routes.user.userRoutes import userRoutes

routes = APIRouter()

routes.include_router(userRoutes, prefix='/user', tags=['Usuario'])
