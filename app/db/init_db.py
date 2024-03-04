from sqlalchemy import create_engine
from app.db.database import Base, DATABASE_URL
from app.models.table import Table
from app.models.user import User
from app.models.reservation import Reservation


engine = create_engine(DATABASE_URL)


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
