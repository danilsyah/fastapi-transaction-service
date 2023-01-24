from fastapi.exceptions import HTTPException

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.api_models import BaseResponseModel
from app.api_models.transaction_item_model import TransactionItemModel
from app.models.transaction import Transaction
from app.models.transaction_item import TransactionItem
from app.utils.db import db_engine

class GetTransactionItemListResponseModel(BaseResponseModel):
    data: list = []
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'id': 1,
                        'user_id': 1,
                        'product_id': 1,
                        'product_name': 'My Product',
                        'price': 100,
                        'qty': 1,
                        'total': 400,
                        'created_at': '2023-01-15 08:22',
                        'modified_at': '2023-01-15 08:52',
                    }
                ],
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def get_transaction_item_list(transaction_id: int):
    with Session(db_engine) as session:
        transaction_item_list = session.query(
            TransactionItem
        ).filter(
            TransactionItem.transaction_id == transaction_id
        ).order_by(
            sa.desc(TransactionItem.id)
        ).all()
        
        result = []
        
        for transaction_item in transaction_item_list:
            result.append(
                TransactionItemModel(
                    id=transaction_item.id,
                    product_id=transaction_item.product_id,
                    product_name=transaction_item.product_name,
                    price=transaction_item.price,
                    qty=transaction_item.qty,
                    total=transaction_item.total,
                    created_at=transaction_item.created_at,
                    modified_at=transaction_item.modified_at
                )
            )
        
        return GetTransactionItemListResponseModel(
            data=result
        )