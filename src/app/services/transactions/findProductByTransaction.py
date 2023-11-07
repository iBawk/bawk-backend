from app.repositories.products.productRepository import ProductRepository
from app.repositories.transactions.transactionsRepository import \
    TransactionsRepository
from db.models import UserModel


class FindProductByTransaction:
    def __init__(self, db):
        self.db = db
        self.transaction_repository = TransactionsRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, user: UserModel):
        transactions = self.transaction_repository.findTransactionsAproveFromUser(
            buyer_id=user.id
        )
        
        products = []

        for transaction in transactions:
            product = self.product_repository.find_by_id(transaction.product_id)
            products = products + [product]
            


        return products
