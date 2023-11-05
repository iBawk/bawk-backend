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
