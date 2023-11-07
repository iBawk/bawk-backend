from app.repositories.products.productRepository import ProductRepository
from fastapi import HTTPException, status
from app.repositories.transactions.transactionsRepository import TransactionsRepository
from utils.pageNumberCalc import calculate_number_of_pages
from db.models import UserModel


class FindProductByTransaction:
    def __init__(self, db):
        self.db = db
        self.transaction_repository = TransactionsRepository
        self.product_repository = ProductRepository(db)

    def execute(self, user: UserModel):
        transactions = self.transaction_repository.findTransactionsAproveFromUser(
            buyer_id=user.id
        )

        for transaction in transactions:
            product = self.product_repository.find_by_id(transaction.product_id)
            transaction.product = product

        json = {"offers": transactions}

        return json
