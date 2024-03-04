from fastapi import APIRouter
from app.api.v1.endpoints import reservations, tables, users, auth

api_router = APIRouter()

api_router.include_router(reservations.router, prefix="/reservations", tags=["reservations"])
api_router.include_router(tables.router, prefix="/tables", tags=["tables"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

