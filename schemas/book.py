from pydantic import BaseModel
from typing import Optional

class CoverImage(BaseModel):
    filename: str
    content_type: str
    data: str
    
class Book(BaseModel):
    titulo: str
    autor: str
    sinopse: str
    cover_image: CoverImage
    nota: float
    editora: str
    genero: list
    ano: str
    idade_sugerida: int
    quantity: int

class BookUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    sinopse: Optional[str] = None
    cover_image: Optional[CoverImage] = None
    nota: Optional[float] = None
    editora: Optional[str] = None
    genero: Optional[list] = None
    ano: Optional[str] = None
    idade_sugerida: Optional[int] = None
    quantity: Optional[int] = None

class BookOut(Book):
    id: str