from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.operations.op_user import create_user, get_user
from app.db.database import get_db
from app.schemas.user import UserCreate, User

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user
