from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.table import TableCreate, Table
from app.operations.op_table import (
    create_table,
    get_table,
    get_tables,
    update_table,
    delete_table,
)
from app.db.database import get_db

router = APIRouter()


@router.post("/", response_model=Table, status_code=status.HTTP_201_CREATED)
def create_table_endpoint(table: TableCreate, db: Session = Depends(get_db)):
    return create_table(db=db, table=table)


@router.get("/", response_model=List[Table])
def read_tables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tables = get_tables(db, skip=skip, limit=limit)
    return tables


@router.get("/{table_id}", response_model=Table)
def read_table(table_id: int, db: Session = Depends(get_db)):
    db_table = get_table(db, table_id=table_id)
    if db_table is None:
        raise HTTPException(status_code=404, detail="Table not found")
    return db_table


@router.put("/{table_id}", response_model=Table)
def update_table_endpoint(table_id: int, table: TableCreate, db: Session = Depends(get_db)):
    return update_table(db=db, table_id=table_id, table=table)


@router.delete("/{table_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_table_endpoint(table_id: int, db: Session = Depends(get_db)):
    delete_table(db, table_id)
    return {"ok": True}
