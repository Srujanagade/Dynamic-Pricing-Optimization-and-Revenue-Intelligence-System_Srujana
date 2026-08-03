from fastapi import APIRouter
from database.session import SessionLocal
from models.product_model import Product
from models.product import ProductSchema

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Get All Products
@router.get("/")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products


# Add Product
@router.post("/")
def add_product(product: ProductSchema):
    db = SessionLocal()

    new_product = Product(
        product_name=product.product_name,
        category=product.category,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return {
        "message": "Product Added Successfully",
        "product": new_product
    }


# Update Product
@router.put("/{product_id}")
def update_product(product_id: int, updated_product: ProductSchema):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        product.product_name = updated_product.product_name
        product.category = updated_product.category
        product.price = updated_product.price
        product.stock = updated_product.stock

        db.commit()
        db.refresh(product)
        db.close()

        return {
            "message": "Product Updated Successfully",
            "product": product
        }

    db.close()

    return {
        "message": "Product Not Found"
    }


# Delete Product
@router.delete("/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        db.delete(product)
        db.commit()
        db.close()

        return {
            "message": "Product Deleted Successfully"
        }

    db.close()

    return {
        "message": "Product Not Found"
    }