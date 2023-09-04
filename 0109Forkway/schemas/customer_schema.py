# app/schemas/customer_schema.py

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    trade_point_id: int


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
