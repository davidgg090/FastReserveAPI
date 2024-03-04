from datetime import datetime
from pydantic import BaseModel


class ReservationBase(BaseModel):
    datetime: datetime
    num_people: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    """
        Reservation schema for representing reservation data.

        Args:
            id (int): The ID of the reservation.
            user_id (int): The ID of the user associated with the reservation.
            table_id (int, optional): The ID of the table associated with the reservation.

        Config:
            orm_mode (bool): Indicates whether the schema is used for ORM mode.
    """

    id: int
    user_id: int
    table_id: int | None = None

    class Config:
        orm_mode = True
