from bson.objectid import ObjectId
from models.book import books_collection
from pymongo import ReturnDocument


def serialize_book(book) -> dict:
    return {
        "id": str(book["_id"]),
        "name": book["name"],
        "description": book["description"],
        "genre": book["genre"],
        "quantity": book["quantity"],
        "available": book["available"]
    }

def get_all_books():
    return [serialize_book(book) for book in books_collection.find()]

def get_book_by_id(book_id: str):
    book = books_collection.find_one({"_id": ObjectId(book_id)})
    return serialize_book(book) if book else None

def create_book(data: dict):
    result = books_collection.insert_one(data)
    return get_book_by_id(str(result.inserted_id))

def update_book(book_id: str, data: dict):
    books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": data})
    return get_book_by_id(book_id)

def delete_book(book_id: str):
    result = books_collection.delete_one({"_id": ObjectId(book_id)})
    return result.deleted_count > 0

def borrow_book(book_id: str):
    result = books_collection.find_one_and_update(
        {"_id": ObjectId(book_id), "quantity": {"$gt": 0}},
        {"$inc": {"quantity": -1}},
        return_document=ReturnDocument.AFTER
    )
    if result:
        # Se a nova quantidade for 0, marcamos como não disponível
        if result["quantity"] == 0:
            books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"available": False}})
        return serialize_book(result)
    return None
