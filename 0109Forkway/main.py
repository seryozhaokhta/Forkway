from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from routers import (
    customer_router,
    trade_point_router,
    order_router,
    visit_router,
    worker_router
)
from dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router.router, prefix="/customer", tags=["customer"])
app.include_router(trade_point_router.router, prefix="/trade_point", tags=["trade_point"])
app.include_router(order_router.router, prefix="/order", tags=["order"])
app.include_router(visit_router.router, prefix="/visit", tags=["visit"])
app.include_router(worker_router.router, prefix="/worker", tags=["worker"])
