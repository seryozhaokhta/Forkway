# models/worker.py

from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    phone_number = Column(String(255), unique=True, index=True, nullable=False)
    trade_point_id = Column(Integer, ForeignKey(
        'trade_points.id'), nullable=False)
