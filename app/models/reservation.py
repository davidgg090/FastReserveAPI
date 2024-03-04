from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import DateTime


class Reservation(Base):
    """
    Reservation model for representing reservation data.

    Args:
        id (int): The ID of the reservation.
        datetime (datetime): The date and time of the reservation.
        num_people (int): The number of people for the reservation.
        user_id (int): The ID of the user associated with the reservation.
        table_id (int, optional): The ID of the table associated with the reservation.

    Attributes:
        user (User): The user associated with the reservation.
        table (Table): The table associated with the reservation.
    """

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, index=True)
    num_people = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=True)

    user = relationship("User", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")
