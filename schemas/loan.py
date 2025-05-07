from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime, timedelta

class Emprestimo(BaseModel):
    book_id: str
    user_id: str
    loan_date: datetime = Field(default_factory=datetime.utcnow())
    due_date: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(days=7))
    returned: bool = False

