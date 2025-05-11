from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
from uuid import UUID

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/status/{webhook_id}")
def get_status(webhook_id: UUID, db: Session = next(get_db())):
    logs = db.query(models.DeliveryLog).filter(models.DeliveryLog.webhook_id == webhook_id).all()
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found for webhook")
    return logs

@router.get("/subscriptions/{sub_id}/recent-deliveries")
def recent_logs(sub_id: UUID, db: Session = next(get_db())):
    logs = (
        db.query(models.DeliveryLog)
        .filter(models.DeliveryLog.subscription_id == sub_id)
        .order_by(models.DeliveryLog.timestamp.desc())
        .limit(20)
        .all()
    )
    return logs