from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    """
        User schema for representing user data.

        Args:
            id (int): The ID of the user.
            is_active (bool): Indicates whether the user is active or not.

        Config:
            orm_mode (bool): Indicates whether the schema is used for ORM mode.
    """

    id: int
    is_active: bool

    class Config:
        orm_mode = True
