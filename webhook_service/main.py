from fastapi import FastAPI
from .routers import subscriptions

app = FastAPI(title="Webhook Delivery Service")

app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])

@app.get("/")
def root():
    return {"message": "Webhook Service Running"}