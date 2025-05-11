import requests
import time
from .celery_app import app as celery_app
from .database import SessionLocal
from . import models, config

@celery_app.task(bind=True, max_retries=config.DELIVERY_RETRY_LIMIT)
def deliver_webhook(self, subscription_id, webhook_id, payload, target_url, attempt=1):
    db = SessionLocal()
    try:
        response = requests.post(target_url, json=payload, timeout=5)
        success = 200 <= response.status_code < 300
        models_log = models.DeliveryLog(
            subscription_id=subscription_id,
            webhook_id=webhook_id,
            target_url=target_url,
            attempt=attempt,
            status_code=response.status_code,
            success=success,
            error_message=None if success else response.text
        )
        db.add(models_log)
        db.commit()
        if not success:
            raise Exception(f"Failed with status {response.status_code}")
    except Exception as exc:
        wait = min(2 ** attempt * 5, 900)  # Exponential backoff (max 15 min)
        models_log = models.DeliveryLog(
            subscription_id=subscription_id,
            webhook_id=webhook_id,
            target_url=target_url,
            attempt=attempt,
            status_code=None,
            success=False,
            error_message=str(exc)
        )
        db.add(models_log)
        db.commit()
        try:
            self.retry(countdown=wait, kwargs={"attempt": attempt + 1})
        except self.MaxRetriesExceededError:
            print("Max retries exceeded.")
    finally:
        db.close()