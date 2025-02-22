from fastapi import APIRouter, Depends, HTTPException
from schemas import Order
from datetime import datetime
from typing import List
from database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

# For demonstration, using an in‑memory list.
fake_orders_db = []

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Order)
async def place_order(order: Order, db: Session = Depends(get_db)):
    # Calculate total price (this could be done in utils.py)
    total_price = sum(item.quantity * item.unit_price for item in order.items)
    order.total_price = total_price
    order.created_at = datetime.utcnow()
    # In production, insert order into the database via ORM.
    order.id = len(fake_orders_db) + 1
    fake_orders_db.append(order.dict())
    return order

@router.get("/", response_model=List[Order])
async def get_orders(db: Session = Depends(get_db)):
    return fake_orders_db
