from fastapi import APIRouter

from routes.products.productsRoutes import productRoutes
from routes.user.userRoutes import userRoutes

routes = APIRouter()

routes.include_router(userRoutes, prefix="/user", tags=["Usuario"])
routes.include_router(productRoutes, prefix="/product", tags=["Produto"])
