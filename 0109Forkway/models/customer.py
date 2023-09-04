# models/customer.py

from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    phone_number = Column(String(255), index=True, nullable=False)
    trade_point_id = Column(Integer, ForeignKey('trade_points.id'), nullable=False)
