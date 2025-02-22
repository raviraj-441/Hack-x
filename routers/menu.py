from fastapi import APIRouter
from schemas import MenuItem
from typing import List

router = APIRouter()

fake_menu = [
    {
        "id": 1,
        "name": "Cappuccino",
        "category": "Beverages",
        "sub_category": "Hot Drinks",
        "description": "Freshly brewed cappuccino",
        "tax": 0.1,
        "packaging_charge": 0.5,
        "SKU": "CAP123",
        "product_cost": 3.0,
        "variations": [
            {"name": "Small", "price": 2.5},
            {"name": "Large", "price": 3.5}
        ]
    },
    {
        "id": 2,
        "name": "Sandwich",
        "category": "Food",
        "sub_category": "Snacks",
        "description": "Ham sandwich",
        "tax": 0.08,
        "packaging_charge": 0.3,
        "SKU": "SAN456",
        "product_cost": 4.0,
        "variations": None
    }
]

@router.get("/", response_model=List[MenuItem])
async def get_menu():
    return fake_menu
