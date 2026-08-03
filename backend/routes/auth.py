from fastapi import APIRouter
from models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Temporary in-memory storage
users = []

@router.post("/register")
def register(user: User):
    users.append(user)
    return {
        "message": "User Registered Successfully",
        "user": user
    }

@router.post("/login")
def login(email: str, password: str):
    for user in users:
        if user.email == email and user.password == password:
            return {
                "message": "Login Successful"
            }

    return {
        "message": "Invalid Email or Password"
    }