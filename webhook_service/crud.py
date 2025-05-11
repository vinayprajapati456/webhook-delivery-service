from sqlalchemy.orm import Session
from . import models, schemas

def create_subscription(db: Session, sub: schemas.SubscriptionCreate):
    db_sub = models.Subscription(
        target_url=sub.target_url,
        secret=sub.secret,
        event_types=sub.event_types
    )
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub

def get_subscriptions(db: Session):
    return db.query(models.Subscription).all()

def get_subscription(db: Session, sub_id):
    return db.query(models.Subscription).filter(models.Subscription.id == sub_id).first()

def delete_subscription(db: Session, sub_id):
    sub = get_subscription(db, sub_id)
    if sub:
        db.delete(sub)
        db.commit()
        return True
    return False