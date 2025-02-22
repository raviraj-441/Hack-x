from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from oauth2 import create_access_token, verify_password
from typing import Any

router = APIRouter()

# Fake in‑memory user for authentication demo
fake_users_db = {
    "john_doe": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "hashed_password": "$2b$12$KIXQjD9jYqMEvLCG6qNdeOlm47u2p2cKzV0GblF9uC0GZbE/z65bi",  # bcrypt hash of "secret"
        "disabled": False,
        "loyalty_points": 50
    }
}

def get_user_by_username(username: str) -> Any:
    return fake_users_db.get(username)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
