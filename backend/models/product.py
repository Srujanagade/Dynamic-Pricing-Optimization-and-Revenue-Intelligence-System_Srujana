from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_name: str
    category: str
    price: float
    stock: int