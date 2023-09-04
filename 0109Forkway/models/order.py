from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from .base import Base
import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    trade_point_id = Column(Integer, ForeignKey(
        'trade_points.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    status = Column(Enum('started', 'ended', 'in process',
                    'awaiting', 'canceled'), default='started')
    worker_id = Column(Integer, ForeignKey('workers.id'), nullable=True)
