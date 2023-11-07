from sqlalchemy.orm import Session

from app.services.transactions.createTransaction import CreateTransactionsService
from app.services.transactions.findProductByTransaction import FindProductByTransaction


class transactionsController:
    def __init__(self, db=Session):
        self.db = db
        self.create_transactions_service = CreateTransactionsService(db)
        self.find_product_by_transaction = FindProductByTransaction(db)

    def createTransaction(self, transaction):
        try:
            return self.create_transactions_service.execute(transaction)
        except Exception as e:
            print(e)
            raise e

    def getProducstByTransaction(self, user):
        try:
            return self.find_product_by_transaction.execute(user)
        except Exception as e:
            print(e)
            raise e