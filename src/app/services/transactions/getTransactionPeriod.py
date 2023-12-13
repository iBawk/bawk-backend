from datetime import datetime, timedelta

from fastapi.encoders import jsonable_encoder

from app.repositories.products.productRepository import ProductRepository
from app.repositories.transactions.transactionsRepository import \
    TransactionsRepository
from db.models import UserModel


class GetTransactionPeriodService:
    def __init__(self, db):
        self.db = db
        self.transaction_repository = TransactionsRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, user: UserModel):
        data_now = datetime.now()
        data_inicio = data_now - timedelta(days=7)

        transacoes_periodo = self.transaction_repository.findSellsSevenDaysAgo(
            data_inicio, data_now
        )
        
        totalValues = 0
        data_dict = {}

        # Criar um dicionário com todas as datas dos últimos sete dias
        date_range = [data_now - timedelta(days=x) for x in range(6, -1, -1)] 
        date_range_str = [date.strftime("%d/%m/%Y") for date in date_range]

        for date_str in date_range_str:
            data_dict[date_str] = 0

        for transaction in transacoes_periodo:
            totalValues += transaction.price

            product = self.product_repository.find_by_id(transaction.product_id)

            if product.owner_id == user.id:
                date = transaction.aproveDate

                date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

                formatted_date = date_obj.strftime("%d/%m/%Y")

                if formatted_date in data_dict:
                    data_dict[formatted_date] += transaction.price

        data = [{"date": date, "value": value} for date, value in data_dict.items()]

        return {
            "totalValue": totalValues,
            "data": jsonable_encoder(data),
        }
