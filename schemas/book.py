from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    name: str
    description: str
    genre: str
    quantity: int
    available: bool

class BookUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    genre: Optional[str] = None
    quantity: Optional[int] = None
    available: Optional[bool] = None

class BookOut(Book):
    id: str