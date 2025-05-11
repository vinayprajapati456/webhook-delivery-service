# webhook_service/celery_app.py

from celery import Celery

app = Celery(
    'webhook_service',
    broker='redis://redis:6379/0',  # Or your actual broker URL
    backend='redis://redis:6379/0'  # Optional: for storing results
)

app.autodiscover_tasks(['webhook_service'])
