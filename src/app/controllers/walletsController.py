from sqlalchemy.orm import Session

from app.services.transactions.createTransaction import CreateTransactionsService
from app.services.transactions.findProductByTransaction import FindProductByTransaction
from app.services.transactions.updateTransaction import UpdateTransactionService
from app.services.wallets.findAllVallues import FindAllValluesService
from db.models import UserModel


class walletsController:
    def __init__(self, db=Session):
        self.db = db
        self.find_all_vallues_user_service = FindAllValluesService(db)

    def findAllValues(self, user: UserModel):
        try:
            return self.find_all_vallues_user_service.execute(user)
        except Exception as e:
            print(e)
            raise e
