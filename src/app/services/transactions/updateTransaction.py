from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import datetime

from app.repositories.transactions.transactionsRepository import TransactionsRepository
from app.repositories.user.userRepository import UserRepository
from app.repositories.products.productRepository import ProductRepository
from app.repositories.offer.offerRepository import OfferRepository


class UpdateTransactionService:
    def __init__(self, db: Session):
        self.db = db
        self.transaction_repository = TransactionsRepository(db)
        self.user_repository = UserRepository(db)
        self.product_repository = ProductRepository(db)
        self.offer_repository = OfferRepository(db)

    def execute(self, transaction_id: str):
        transaction = self.transaction_repository.find_by_id(transaction_id)
        if not transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Não existe compra. Caiu no golpe kk",
            )
        if transaction.situation == 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Compra já foi reembolsada, aguarde. Caiu no golpe KK",
            )
        transaction.situation = 3
        transaction.refoundDate = datetime.datetime.now()

        offer = self.offer_repository.find_by_id(transaction.offer_id)
        product = self.product_repository.find_by_id(offer.product_id)
        saller = self.user_repository.get_user_by_id(product.owner_id)
        wallet = self.user_repository.get_wallet_by_user_id(saller.id)

        newBalance = wallet.amount_free - transaction.price
        wallet.amount_free = newBalance
        self.db.add(wallet)
        self.db.commit()
        self.db.refresh(wallet)

        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)

        return transaction.refoundDate
