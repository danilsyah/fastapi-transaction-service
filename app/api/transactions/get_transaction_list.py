from fastapi.exceptions import HTTPException

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.api_models import BaseResponseModel
from app.api_models.transaction_model import TransactionModel
from app.models.transaction import Transaction
from app.utils.db import db_engine

class GetTransactionListResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'id': 1,
                        'user_id': 1,
                        'created_at': '2023-01-15 08:22',
                        'modified_at': '2023-01-15 08:52',
                        'status': 10,
                        'total': 400
                    }
                ],
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def get_transaction_list():
    with Session(db_engine) as session:
        transaction_list = session.query(
            Transaction
        ).order_by(
            sa.desc(Transaction.id)
        ).all()
        
        result = []
        
        for transaction in transaction_list:
            result.append(
                TransactionModel(
                    id=transaction.id,
                    user_id=transaction.user_id,
                    created_at=transaction.created_at,
                    modified_at=transaction.modified_at,
                    status=transaction.status,
                    total=transaction.total
                )
            )
        
        return GetTransactionListResponseModel(
            data=result
        )