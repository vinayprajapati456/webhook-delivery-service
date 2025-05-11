import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
DELIVERY_RETRY_LIMIT = 5