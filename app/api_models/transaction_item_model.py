from datetime import datetime
from pydantic import BaseModel

class TransactionItemModel(BaseModel):
    id: int
    product_id: int
    product_name: str
    price: int
    qty: int
    total: int
    created_at: datetime
    modified_at: datetime