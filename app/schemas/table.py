from pydantic import BaseModel


class TableBase(BaseModel):
    capacity: int
    location: str


class TableCreate(TableBase):
    pass


class Table(TableBase):
    """
        Table schema for representing table data.

        Args:
            id (int): The ID of the table.

        Config:
            orm_mode (bool): Indicates whether the schema is used for ORM mode.
    """
    id: int

    class Config:
        orm_mode = True
