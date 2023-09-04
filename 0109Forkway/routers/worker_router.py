from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Worker as ModelWorker
from schemas import Worker as SchemaWorker, WorkerCreate as SchemaWorkerCreate
from database import get_db

router = APIRouter()

@router.post("/workers/", response_model=SchemaWorker)
def create_worker(worker: SchemaWorkerCreate, db: Session = Depends(get_db)):
    db_worker = ModelWorker(**worker.dict())
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker

# TODO: Add routes for reading, updating, and deleting a worker
