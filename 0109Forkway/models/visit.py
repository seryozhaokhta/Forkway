# models/visit.py

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
import datetime


class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    worker_id = Column(Integer, ForeignKey('workers.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'),
                      nullable=False, unique=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    trade_point_id = Column(Integer, ForeignKey(
        'trade_points.id'), nullable=False)
