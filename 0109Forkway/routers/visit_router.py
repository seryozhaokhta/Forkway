from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import Visit, VisitCreate
from models import Visit as ModelVisit
from database import get_db

router = APIRouter()

@router.post("/visits/", response_model=Visit)
def create_visit(visit: VisitCreate, db: Session = Depends(get_db)):
    db_visit = ModelVisit(**visit.dict())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit
