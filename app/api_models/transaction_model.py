from datetime import datetime
from pydantic import BaseModel

class TransactionModel(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    modified_at: datetime
    status: int
    total: int