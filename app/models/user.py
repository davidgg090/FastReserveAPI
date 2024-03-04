from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    """
    User model for representing user data.

    Args:
        id (int): The ID of the user.
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.
        is_active (bool): Indicates whether the user is active or not.

    Attributes:
        reservations (List[Reservation]): The reservations associated with the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    reservations = relationship("Reservation", back_populates="user")
