from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import OrderBase, OrderCreate
from database import get_db
from models.order import Order as ModelOrder

router = APIRouter()

@router.post("/orders/", response_model=OrderBase)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = ModelOrder(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/orders/", response_model=list[OrderBase])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ModelOrder).offset(skip).limit(limit).all()
