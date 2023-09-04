# app/schemas/visit_schema.py

from pydantic import BaseModel
from datetime import datetime


class VisitBase(BaseModel):
    creation_date: datetime
    executor_id: int
    order_id: int
    author_id: int
    trade_point_id: int


class VisitCreate(VisitBase):
    pass


class Visit(VisitBase):
    id: int

    class Config:
        orm_mode = True
