from sqlalchemy.orm import Session

from app.services.transactions.createTransaction import CreateTransactionsService
from app.services.transactions.findProductByTransaction import FindProductByTransaction
from app.services.transactions.updateTransaction import UpdateTransactionService
from app.services.transactions.getTransactionPeriod import GetTransactionPeriodService
from db.models import UserModel
from app.services.transactions.getSales import GetSalesService


class transactionsController:
    def __init__(self, db=Session):
        self.db = db
        self.create_transactions_service = CreateTransactionsService(db)
        self.find_product_by_transaction = FindProductByTransaction(db)
        self.update_transactions_service = UpdateTransactionService(db)
        self.get_transactions_period_service = GetTransactionPeriodService(db)
        self.get_sales_service = GetSalesService(db)

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

    def update(self, transactions_id: str):
        try:
            return self.update_transactions_service.execute(transactions_id)
        except Exception as e:
            print(e)
            raise e

    def getPeriod(self, user: UserModel):
        try:
            return self.get_transactions_period_service.execute(user)
        except Exception as e:
            print(e)
            raise e

    def getSales(self, user: UserModel):
        try:
            return self.get_sales_service.execute(user)
        except Exception as e:
            print(e)
            raise e
