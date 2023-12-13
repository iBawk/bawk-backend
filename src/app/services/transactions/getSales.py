from app.repositories.transactions.transactionsRepository import TransactionsRepository
from db.models import UserModel


class GetSalesService:
    def __init__(self, db):
        self.db = db
        self.transaction_repository = TransactionsRepository(db)

    def execute(self, user: UserModel):
        wallet_id = self.transaction_repository.getWalletId(user.id)
        show_sales = self.transaction_repository.findSalesFromUser(wallet_id.id)

        return show_sales
