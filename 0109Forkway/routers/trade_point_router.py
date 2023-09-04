from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import trade_point
from schemas import TradePoint, TradePointCreate
from dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[TradePoint])
def read_trade_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trade_points = trade_point.get_multi(db, skip=skip, limit=limit)
    return trade_points

@router.post("/", response_model=TradePoint)
def create_trade_point(trade_point: TradePointCreate, db: Session = Depends(get_db)):
    return trade_point.create(db, obj_in=trade_point)

@router.get("/{trade_point_id}", response_model=TradePoint)
def read_trade_point(trade_point_id: int, db: Session = Depends(get_db)):
    db_trade_point = trade_point.get(db, trade_point_id)
    if db_trade_point is None:
        raise HTTPException(status_code=404, detail="TradePoint not found")
    return db_trade_point
