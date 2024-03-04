from sqlalchemy.orm import Session
from app.models.reservation import Reservation as ReservationModel
from app.schemas.reservation import ReservationCreate


def create_reservation(db: Session, reservation: ReservationCreate, user_id: int) -> ReservationModel:
    db_reservation = ReservationModel(**reservation.dict(), user_id=user_id)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservation(db: Session, reservation_id: int) -> ReservationModel:
    return db.query(ReservationModel).filter(ReservationModel.id == reservation_id).first()


def get_reservations(db: Session, skip: int = 0, limit: int = 100) -> list[ReservationModel]:
    return db.query(ReservationModel).offset(skip).limit(limit).all()


def update_reservation(db: Session, reservation_id: int, reservation: ReservationCreate) -> ReservationModel:
    db_reservation = db.query(ReservationModel).filter(ReservationModel.id == reservation_id).first()
    if db_reservation:
        for var, value in vars(reservation).items():
            setattr(db_reservation, var, value) if value else None
        db.commit()
        db.refresh(db_reservation)
    return db_reservation


def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(ReservationModel).filter(ReservationModel.id == reservation_id).first()
    if db_reservation:
        db.delete(db_reservation)
        db.commit()
