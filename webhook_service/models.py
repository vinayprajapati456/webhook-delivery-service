from sqlalchemy import Column, String, DateTime, JSON, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

from .database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    target_url = Column(String, nullable=False)
    secret = Column(String, nullable=True)
    event_types = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class DeliveryLog(Base):
    __tablename__ = "delivery_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subscription_id = Column(UUID(as_uuid=True))
    webhook_id = Column(UUID(as_uuid=True))
    target_url = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    attempt = Column(Integer)
    status_code = Column(Integer)
    success = Column(Boolean)
    error_message = Column(String, nullable=True)