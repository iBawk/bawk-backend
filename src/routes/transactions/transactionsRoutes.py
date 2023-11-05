from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.transactionsController import transactionsController
from app.schemas.transactions.TrasactionCreateSchema import TransactionCreateSchema
from lib.depends import get_db_Session

transactionsRoutes = APIRouter()


@transactionsRoutes.post("", summary="Cria uma transação.")
def create(transaction: TransactionCreateSchema, db: Session = Depends(get_db_Session)):
    transactions_controller = transactionsController(db)

    try:
        return transactions_controller.createTransaction(transaction)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
