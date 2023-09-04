from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_customer, get_customer_by_phone, create_customer, get_customers
from schemas import CustomerCreate, Customer
from database import get_db

router = APIRouter()

@router.post("/customers/", response_model=Customer)
def create_customer_endpoint(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = get_customer_by_phone(db, phone=customer.phone)
    if db_customer:
        raise HTTPException(status_code=400, detail="Phone already registered")
    return create_customer(db=db, customer=customer)

@router.get("/customers/", response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = get_customers(db, skip=skip, limit=limit)
    return customers

@router.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer
