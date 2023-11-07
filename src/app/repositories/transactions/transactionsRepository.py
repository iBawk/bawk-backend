from sqlalchemy.orm import Session

from db.models import TransactionsModel


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
