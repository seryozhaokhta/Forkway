
from typing import List
from pydantic import BaseModel

class WorkerBase(BaseModel):
    name: str
    phone_number: str
    trade_point_id: int

class WorkerCreate(WorkerBase):
    pass

class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True
