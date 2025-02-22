from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# --- User Schemas ---
class UserBase(BaseModel):
    username: str = Field(..., example="john_doe")
    email: EmailStr = Field(..., example="john@example.com")
    full_name: Optional[str] = Field(None, example="John Doe")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="secret123")

class User(UserBase):
    id: int
    loyalty_points: Optional[int] = Field(0, example=100)

    class Config:
        from_attributes = True

    class Config:
        orm_mode = True

# --- Menu Item Schemas ---
class Variation(BaseModel):
    name: str = Field(..., example="Large")
    price: float = Field(..., example=0.50)

class MenuItem(BaseModel):
    id: int
    name: str = Field(..., example="Cappuccino")
    category: str = Field(..., example="Beverages")
    sub_category: Optional[str] = Field(None, example="Hot Drinks")
    description: Optional[str] = Field(None, example="Freshly brewed cappuccino with frothy milk")
    tax: float = Field(..., example=0.10)
    packaging_charge: float = Field(..., example=0.50)
    SKU: str = Field(..., example="CAP123")
    product_cost: float = Field(..., example=3.00)
    variations: Optional[List[Variation]] = None

    class Config:
        orm_mode = True

# --- Order Schemas ---
class OrderItem(BaseModel):
    menu_item_id: int = Field(..., example=1)
    quantity: int = Field(..., example=2)
    unit_price: float = Field(..., example=3.50)
    variation: Optional[Variation] = None

class Order(BaseModel):
    id: int
    customer_id: int
    table_id: int
    items: List[OrderItem]
    total_price: float = Field(..., example=7.00)
    status: str = Field(..., example="pending")  # pending, confirmed, etc.
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

# --- Gamification Schemas ---
class GamificationRecord(BaseModel):
    id: int
    customer_id: int
    event_type: str = Field(..., example="order_placed")
    points: int = Field(..., example=10)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    description: Optional[str] = Field(None, example="Order over $20 bonus")

    class Config:
        orm_mode = True
