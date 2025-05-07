from datetime import datetime, timedelta
from bson import ObjectId
from fastapi import HTTPException
from models.loan import loan_collection
from models.book import books_collection
from models.user import users_collection


def create_loan(book_id: str, user_id: str):
    book = books_collection.find_one({"_id": ObjectId(book_id)})
    
    loan = {
        "book_id": book_id,
        "user_id": user_id,
        "loan_date": datetime.utcnow(),
        "due_date": datetime.utcnow() + timedelta(days=7),
        "returned": False
    }
    result = loan_collection.insert_one(loan)
    loan["_id"] = str(result.inserted_id)
    return loan

def get_loan_by_id(loan_id: str):
    loan = loan_collection.find_one({"_id": ObjectId(loan_id)})
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    # Buscar o livro e o usuário
    book = books_collection.find_one({"_id": ObjectId(loan["book_id"])})
    user = users_collection.find_one({"_id": ObjectId(loan["user_id"])})

    if book:
        book["_id"] = str(book["_id"])
    if user:
        user["_id"] = str(user["_id"])

    return {
        "_id": str(loan["_id"]),
        "book": book,
        "user": user,
        "loan_date": loan["loan_date"],
        "due_date": loan["due_date"],
        "returned": loan["returned"]
    }

def get_loans():
    loans = []
    for loan in loan_collection.find():
        book = books_collection.find_one({"_id": ObjectId(loan["book_id"])})
        user = users_collection.find_one({"_id": ObjectId(loan["user_id"])})

        if book:
            book["_id"] = str(book["_id"])
        if user:
            user["_id"] = str(user["_id"])

        loans.append({
            "_id": str(loan["_id"]),
            "book": book,
            "user": user,
            "loan_date": loan["loan_date"],
            "due_date": loan["due_date"],
            "returned": loan["returned"]
        })
    return loans


def mark_as_returned(loan_id: str):
    result = loan_collection.update_one(
        {"_id": ObjectId(loan_id)},
        {"$set": {"returned": True}}
    )
    if result.matched_count == 0:
      raise HTTPException(status_code=404, detail="Loan not found")
    return {"message": "Loan marked as returned"}
