from fastapi import APIRouter
from models.user import *
from models.book import *
from config.database import *
from schema.schemas import *
from bson import ObjectId
import bcrypt

router = APIRouter()

@router.get("/users")
async def get_users() -> list:
    users = list_serial_users(collection_name.find())
    return users

@router.post("/user")
async def post_user(user : User):
    user_dict = dict(user)
    user_dict["password"] = bcrypt.hashpw(user_dict["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    collection_name.insert_one(user_dict)

@router.put("/user")
async def put_user(id: str, user: User):
    user_dict = dict(user)
    user_dict["password"] = bcrypt.hashpw(user_dict["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": user_dict})

@router.get("/books")
async def get_books():
    books = list_serial_books(book_collection.find())
    return books

@router.post("/book")
async def post_book(book : Book):
    book_collection.insert_one(dict(book))

@router.patch("/book")
async def update_book(id : str, book: BookUpdate):
    updated_book = {k: v for k, v in dict(book).items() if v is not None}

    result = book_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": updated_book},
        return_document=True
    )

    return individual_serial_book(result)