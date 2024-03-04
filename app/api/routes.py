from fastapi import APIRouter
from app.api.v1.endpoints import reservations, tables

api_router = APIRouter()

api_router.include_router(reservations.router, prefix="/reservations", tags=["reservations"])
api_router.include_router(tables.router, prefix="/tables", tags=["tables"])