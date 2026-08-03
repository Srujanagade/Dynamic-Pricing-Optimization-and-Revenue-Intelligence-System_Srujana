from database.connection import engine
from models.user_model import Base
from models.product_model import Product

Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")