from models.user import users_collection
from utils.security import hash_password, verify_password, create_access_token
from bson.objectid import ObjectId

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def create_user(email: str, password: str):
    hashed_pw = hash_password(password)
    user = {"email": email, "password": hashed_pw}
    result = users_collection.insert_one(user)
    return str(result.inserted_id)

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        return None
    token = create_access_token({"sub": str(user["_id"])})
    return token
