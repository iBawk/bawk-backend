import datetime
import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.transactions.transactionsRepository import TransactionsRepository
from app.repositories.user.userRepository import UserRepository
from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from app.schemas.transactions.TrasactionCreateSchema import TransactionCreateSchema
from app.services.user.createUser import CreateUserServiceV1
from app.schemas.user.UserRegisterSchema import UserRegister
from db.models import TransactionsModel


class CreateTransactionsService:
    def __init__(self, db=Session):
        self.db = db
        self.create_user_service = CreateUserServiceV1(db)
        self.user_repository = UserRepository(db)
        self.transaction_repository = TransactionsRepository(db)
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, transaction: TransactionCreateSchema, newUser: UserRegister):
        transaction_id = str(uuid.uuid4())
        id_existis = self.transaction_repository.find_by_id(transaction_id)
        if id_existis:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Houve um problema em gerar sua compra, tente novamente mais tarde.",
            )
        offer = self.offer_repository.find_by_id(transaction.offer_id)
        if not offer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A oferta referente ao produto não existe.",
            )
        offer_active = self.offer_repository.find_situation_by_id(transaction.offer_id)
        if offer_active != 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A oferta deste produto está inativa, entre em contato com o vendedor.",
            )

        offer_price = self.offer_repository.find_price_by_id(transaction.offer_id)

        new_user = self.user_repository.get_user_by_email(transaction.email_buyer)
        if not new_user:
            newUser.name = transaction.name_buyer
            newUser.email = transaction.email_buyer
            newUser.password = str(uuid.uuid4())
            self.create_user_service.execute(newUser)

        buyer_id = self.user_repository.get_user_by_email(transaction.email_buyer)
        wallet = self.user_repository.get_wallet_by_user_id(buyer_id)
        product_id = self.offer_repository.find_product_id_by_offer_id(
            transaction.offer_id
        )

        newTransaction = self.transaction_repository.create(
            TransactionsModel(
                id=transaction_id,
                offer_id=transaction.offer_id,
                price=offer_price,
                situation=1,  # situação 1 APROVADA TRANSACAO
                transactionDate=datetime.datetime.now(),
                aproveDate=datetime.datetime.now(),
                reimbursementDate=" ",  # CAMPO VAZIO, POIS NAO FOI REEMBOLSADA
                buyer_id=buyer_id,
                wallet_id=wallet,
                product_id=product_id,
                paymentMethod_id=transaction.paymentMethod_id,  # ID DE PAGAMENTO
            )
        )

        return newTransaction
