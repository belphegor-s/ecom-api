from datetime import datetime
from typing import List
from pydantic import BaseModel

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int

class Order(BaseModel):
    timestamp: datetime
    items: List[OrderItem]
    totalAmount: float
    userAddress: UserAddress
