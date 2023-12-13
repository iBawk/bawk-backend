from app.repositories.products.productRepository import ProductRepository
from app.repositories.transactions.transactionsRepository import TransactionsRepository
from db.models import UserModel
import datetime
from db.models import TransactionsModel


class GetTransactionPeriodService:
    def __init__(self, db):
        self.db = db
        self.transaction_repository = TransactionsRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, user: UserModel):
        data_now = datetime.datetime.now()
        data_inicio = data_now - datetime.timedelta(days=7)

        transacoes_periodo = self.transaction_repository.get_transactions_in_period(
            user.id, data_inicio, data_now
        )

        return transacoes_periodo
