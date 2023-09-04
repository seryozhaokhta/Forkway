# app/schemas/order_schema.py

from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    creation_date: datetime
    end_date: datetime
    trade_point_id: int
    customer_id: int
    status: str
    executor_id: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
