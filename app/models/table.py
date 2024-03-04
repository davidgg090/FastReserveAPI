from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
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
