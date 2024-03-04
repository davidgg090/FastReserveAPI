from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.reservation import ReservationCreate, Reservation
from app.operations.op_reservation import (
    create_reservation,
    get_reservation,
    get_reservations,
    update_reservation,
    delete_reservation,
)
from app.db.database import get_db

router = APIRouter()


@router.post("/", response_model=Reservation, status_code=status.HTTP_201_CREATED)
def create_reservation_endpoint(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation(db=db, reservation=reservation)


@router.get("/", response_model=List[Reservation])
def read_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reservations = get_reservations(db, skip=skip, limit=limit)
    return reservations


@router.get("/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = get_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.put("/{reservation_id}", response_model=Reservation)
def update_reservation_endpoint(reservation_id: int, reservation: ReservationCreate, db: Session = Depends(get_db)):
    return update_reservation(db=db, reservation_id=reservation_id, reservation=reservation)


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation_endpoint(reservation_id: int, db: Session = Depends(get_db)):
    delete_reservation(db, reservation_id)
    return {"ok": True}
