from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserLogin
from services.auth_service import create_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate):
    if create_user(user.email, user.password):
        return {"msg": "User created"}
    raise HTTPException(status_code=400, detail="User creation failed")

@router.post("/login")
def login(user: UserLogin):
    token = authenticate_user(user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
