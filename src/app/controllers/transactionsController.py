from sqlalchemy.orm import Session

from app.services.transactions.createTransaction import CreateTransactionsService


class transactionsController:
    def __init__(self, db=Session):
        self.db = db
        self.create_transactions_service = CreateTransactionsService(db)

    def createTransaction(self, transaction):
        try:
            return self.create_transactions_service.execute(transaction)
        except Exception as e:
            print(e)
            raise e
