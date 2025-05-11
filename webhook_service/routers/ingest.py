from fastapi import APIRouter, HTTPException, Request
from uuid import UUID, uuid4
from ..database import SessionLocal
from .. import models, tasks

router = APIRouter()

@router.post("/ingest/{subscription_id}")
async def ingest(subscription_id: UUID, request: Request):
    db = SessionLocal()
    try:
        sub = db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()
        if not sub:
            raise HTTPException(status_code=404, detail="Subscription not found")
        payload = await request.json()
        webhook_id = str(uuid4())
        tasks.deliver_webhook.delay(str(subscription_id), webhook_id, payload, sub.target_url)
        return {"message": "Webhook queued", "webhook_id": webhook_id}
    finally:
        db.close()