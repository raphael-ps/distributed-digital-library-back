from fastapi import APIRouter
from services import loan_service

router = APIRouter()

@router.post("/loan/")
def create_loan(book_id: str, user_id: str):
    return loan_service.create_loan(book_id, user_id)

@router.get("/loans/")
def list_loans():
    return loan_service.get_loans()

@router.get("/loan/{loan_id}")
def get_loan(loan_id: str):
    return loan_service.get_loan_by_id(loan_id)

@router.put("/loan/{loan_id}/return")
def return_loan(loan_id: str):
    return loan_service.mark_as_returned(loan_id)
