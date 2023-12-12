from fastapi import APIRouter

from routes.offer.offerRoutes import offerRoutes
from routes.products.productsRoutes import productRoutes
from routes.transactions.transactionsRoutes import transactionsRoutes
from routes.user.userRoutes import userRoutes
from routes.wallets.walletsRoutes import walletsRoutes

routes = APIRouter()

routes.include_router(userRoutes, prefix="/user", tags=["Usuario"])
routes.include_router(productRoutes, prefix="/product", tags=["Produto"])
routes.include_router(offerRoutes, prefix="/offer", tags=["Oferta"])
routes.include_router(transactionsRoutes, prefix="/transaction", tags=["Transação"])
routes.include_router(walletsRoutes, prefix="/wallet", tags=["Carteira"])
