from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.products import router as product_router
from routes.auth import router as auth_router

app = FastAPI(
    title="PricePilot AI Backend",
    version="1.0.0"
)

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later change to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to PricePilot AI Backend"
    }

# Health Check API
@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

# Include Routes
app.include_router(product_router)
app.include_router(auth_router)