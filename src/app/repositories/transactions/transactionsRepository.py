from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import TransactionsModel, WalletsModel


class TransactionsRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, transaction_id: str):
        return self.db.query(TransactionsModel).filter_by(id=transaction_id).first()

    def create(self, transaction: TransactionsModel):
        try:
            self.db.add(transaction)
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        except Exception as e:
            self.db.rollback()
            print(e)
            raise e

    def findTransactionsAproveFromUser(self, buyer_id: str):
        return (
            self.db.query(TransactionsModel)
            .filter(TransactionsModel.buyer_id == buyer_id)
            .filter(
                TransactionsModel.situation == 1
            )  # 3 é reembolsado, 1 é aprovado, 2 é aguardando pagamento
            .all()
        )

    def countProductsByTransactions(self, buyer_id: str):
        return (
            self.db.query(TransactionsModel)
            .filter_by(buyer_id=buyer_id)
            .filter(TransactionsModel.situation == 1)
            .count()
        )

    def AddBalance(self, wallet_id: str, walletNew: WalletsModel):
        try:
            wallet = self.db.query(WalletsModel).filter_by(id=wallet_id).first()

            if wallet:
                self.db.add(walletNew)
                self.db.commit()
                self.db.refresh(walletNew)

                return wallet

        except DatabaseError as e:
            print(e)
            raise e

    def find_value_by_wallet(self, wallet_id: str):
        return self.db.query(WalletsModel).filter_by(id=wallet_id).scalar()

    def findSellsSevenDaysAgo(self, data_inicio, data_fim):
        return (
            self.db.query(TransactionsModel)
            .filter(TransactionsModel.aproveDate >= data_inicio)
            .filter(TransactionsModel.aproveDate <= data_fim)
            .all()
        )