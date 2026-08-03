import pandas as pd
from database.session import SessionLocal
from models.product_model import Product

# Read the CSV file
df = pd.read_csv("datasets/products_dataset.csv")

# Create database session
db = SessionLocal()

for _, row in df.iterrows():
    product = Product(
        product_name=row["product_name"],
        category=row["category"],
        price=float(row["price"]),
        stock=int(row["stock"])
    )

    db.add(product)

db.commit()
db.close()

print("✅ Dataset Imported Successfully!")