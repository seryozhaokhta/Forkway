# models/trade_point.py

from sqlalchemy import Column, Integer, String
from .base import Base


class TradePoint(Base):
    __tablename__ = "trade_points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
