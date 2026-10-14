from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base

from app.routes.auth import router as auth_router
from app.routes.menu import router as menu_router
from app.routes.orders import router as orders_router
from app.routes.payments import router as payments_router
from app.routes.recommendations import router as recommendation_router
from app.routes.admin import router as admin_router
from app.routes.websocket import router as websocket_router
from app.models.review import Review
from app.routes.review import router as review_router


# Import models
from app.models import user_model
from app.models.menu import Menu

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="CampusBite API",
    version="1.0.0"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth_router)
app.include_router(menu_router)
app.include_router(orders_router)
app.include_router(payments_router)
app.include_router(recommendation_router)
app.include_router(admin_router)
app.include_router(websocket_router)
app.include_router(review_router)

# Home route
@app.get("/")
def home():
    return {
        "message": "CampusBite Backend Running Successfully"
    }