from models.book import Book

def individual_serial_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "password": user["password"],
        "created_at": user.get("created_at").isoformat() if user.get("created_at") else None,
        "active": user["active"]
    }

def individual_serial_book(book : Book) -> dict:
    return {
        "id": str(book.get("_id")),
        "name": book.get("name"),
        "description": book.get("description"),
        "genre": book.get("genre"),
        "available": book.get("available")
    }

def list_serial_books(books) -> list:
    return [individual_serial_book(book) for book in books]

def list_serial_users(users) -> list:
    return [individual_serial_user(user) for user in users]