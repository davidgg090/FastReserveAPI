from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from app.db.database import Base


class Table(Base):
    """
    Table model for representing table data.

    Args:
        id (int): The ID of the table.
        capacity (int): The capacity of the table.
        location (str): The location of the table.

    Attributes:
        reservations (List[Reservation]): The reservations associated with the table.

    """

    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    capacity = Column(Integer)
    location = Column(String)

    reservations = relationship("Reservation", back_populates="table")

    @validates('capacity')
    def validate_capacity(self, key, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("La capacidad debe ser un entero positivo")
        return capacity
