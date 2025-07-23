from itertools import product

from pydantic import BaseModel, Field

class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description='Цена должны быть больше 0')
    tags: list[str] = []
    market: Market

item_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"],
    "market": {
        "id": 1,
        "name": "Amazon"
    }
}

item = Product(**item_data)
print(item)

new_item = Product(
    name="Phone",
    price=499.99,
    tags=["electronics", "smartphone"],
    market=Market(id=1, name="Amazon"))