from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import decode_access_token
from app.operations.op_user import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=400, detail="Invalid token payload")
    user = get_user_by_email(db, email=email)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user
