from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserCreate, User
from oauth2 import get_password_hash, decode_access_token
from fastapi.security import OAuth2PasswordBearer
from typing import Any
from sqlalchemy.orm import Session
from database import SessionLocal

router = APIRouter()

# Fake in‑memory store for registered users
fake_users_db = {}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=User)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_dict: dict[str, Any] = user.dict()
    user_dict["hashed_password"] = hashed_password
    user_dict["id"] = len(fake_users_db) + 1
    user_dict["loyalty_points"] = 0
    fake_users_db[user.username] = user_dict
    return user_dict

# Dependency to extract the token and get current user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    username = payload["sub"]
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user

@router.get("/me", response_model=User)
async def read_user_me(current_user: dict = Depends(get_current_user)):
    return current_user
