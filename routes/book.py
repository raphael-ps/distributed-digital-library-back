from fastapi import APIRouter, HTTPException
from schemas.book import Book, BookOut, BookUpdate
from services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookOut])
def list_books():
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: str):
    book = book_service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookOut)
def create_book(book: Book):
    return book_service.create_book(book.dict())

@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: str, update_data: BookUpdate):
    updated = book_service.update_book(book_id, {k: v for k, v in update_data.dict().items() if v is not None})
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found or update failed")
    return updated

@router.delete("/{book_id}")
def delete_book(book_id: str):
    if not book_service.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"msg": "Book deleted successfully"}

@router.patch("/{book_id}", response_model=BookOut)
def patch_book(book_id: str, update_data: BookUpdate):
    updated = book_service.update_book(book_id, {k: v for k, v in update_data.dict().items() if v is not None})
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found or update failed")
    return updated

@router.post("/{book_id}/borrow", response_model=BookOut)
def borrow_book(book_id: str):
    updated = book_service.borrow_book(book_id)
    if not updated:
        raise HTTPException(status_code=400, detail="Book not available for borrowing")
    return updated
