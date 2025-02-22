# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")  # Using Argon2 as the default hashing algo

# def hash(password: str):
#     return pwd_context.hash(password)

# def verify(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

def calculate_total_price(order_items: list) -> float:
    return sum(item['quantity'] * item['unit_price'] for item in order_items)

 