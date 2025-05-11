from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SubscriptionOut)
def create(sub: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.create_subscription(db, sub)

@router.get("/", response_model=list[schemas.SubscriptionOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_subscriptions(db)

@router.delete("/{sub_id}")
def delete(sub_id: UUID, db: Session = Depends(get_db)):
    success = crud.delete_subscription(db, sub_id)
    if not success:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"message": "Deleted"}