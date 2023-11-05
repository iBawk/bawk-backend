import datetime
import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from app.repositories.transactions.transactionsRepository import \
    TransactionsRepository
from app.repositories.user.userRepository import UserRepository
from app.schemas.transactions.TrasactionCreateSchema import \
    TransactionCreateSchema
from app.schemas.user.UserRegisterSchema import UserRegister
from app.services.user.createUser import CreateUserServiceV1
from db.models import TransactionsModel


class CreateTransactionsService:
    def __init__(self, db=Session):
        self.db = db
        self.create_user_service = CreateUserServiceV1(db)
        self.user_repository = UserRepository(db)
        self.transaction_repository = TransactionsRepository(db)
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, transaction: TransactionCreateSchema):
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

        user_existis = self.user_repository.get_user_by_email(transaction.email_buyer)
        if not user_existis:
            user_register_data = UserRegister(
            name=transaction.name_buyer,
            email=transaction.email_buyer,
            password=str(uuid.uuid4())
            )

            user = self.create_user_service.execute(credentials=user_register_data)
            
        buyer = self.user_repository.get_user_by_email(transaction.email_buyer)
        wallet = self.user_repository.get_wallet_by_user_id(buyer.id)
        product = self.product_repository.find_by_id(offer.product_id)

        newTransaction = self.transaction_repository.create(
            TransactionsModel(
                id=transaction_id,
                offer_id=transaction.offer_id,
                price=offer_price,
                situation=1,  # situação 1 APROVADA TRANSACAO
                transactionDate=datetime.datetime.now(),
                aproveDate=datetime.datetime.now(),
                refoundDate="",  # CAMPO VAZIO, POIS NAO FOI REEMBOLSADA
                buyer_id=buyer.id,
                wallet_id=wallet,
                product_id=product.id,
                paymentMethod=transaction.paymentMethod,  # ID DE PAGAMENTO
            )
        )

        return newTransaction
