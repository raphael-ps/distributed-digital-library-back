from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    description: str
    genre: str
    available: bool

class BookUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    genre: Optional[str] = None
    available: Optional[bool] = None