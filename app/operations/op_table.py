from sqlalchemy.orm import Session
from app.models.table import Table as TableModel
from app.schemas.table import TableCreate


def create_table(db: Session, table: TableCreate) -> TableModel:
    db_table = TableModel(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def get_table(db: Session, table_id: int) -> TableModel:
    return db.query(TableModel).filter(TableModel.id == table_id).first()


def get_tables(db: Session, skip: int = 0, limit: int = 100) -> list[TableModel]:
    return db.query(TableModel).offset(skip).limit(limit).all()


def update_table(db: Session, table_id: int, table: TableCreate) -> TableModel:
    db_table = db.query(TableModel).filter(TableModel.id == table_id).first()
    if db_table:
        for var, value in vars(table).items():
            setattr(db_table, var, value) if value else None
        db.commit()
        db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_id: int):
    db_table = db.query(TableModel).filter(TableModel.id == table_id).first()
    if db_table:
        db.delete(db_table)
        db.commit()
