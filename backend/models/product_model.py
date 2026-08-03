from sqlalchemy import Column, Integer, String, Float
from models.user_model import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    category = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)