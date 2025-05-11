# ✅ Webhook Delivery Service - Backend Assignment (April 2025)

This project implements a complete webhook delivery backend using Python, FastAPI, PostgreSQL, Redis, and Celery. It is production-ready and containerized for easy deployment using Docker Compose.

---

## 🚀 Features Implemented

- ✅ Subscription CRUD APIs
- ✅ Webhook ingestion with event type filtering
- ✅ HMAC-SHA256 signature generation and verification (bonus)
- ✅ Asynchronous delivery using Celery
- ✅ Retry logic with exponential backoff (up to 5 retries)
- ✅ Delivery attempt logging (with attempt number, status code, error)
- ✅ Status and analytics APIs for delivery history
- ✅ Log cleanup job (retains only 72 hours of logs)
- ✅ Docker Compose setup for local development
- ✅ Celery Beat for scheduled tasks
- ✅ Auto-generated Swagger UI at `/docs`

---

## 🧱 Tech Stack

- FastAPI: for APIs
- **PostgreSQL: for data persistence
- Redis: as broker and caching layer
- Celery: for background task processing
- Docker Compose: for service orchestration

---

## 📦 How to Run (Locally with Docker)

### Prerequisites
- Docker Desktop (installed and running)
- VS Code (optional for editing)

### Steps

```bash
# Unzip the folder and navigate to it
cd webhook_delivery_service

# Build and run all services
docker-compose up --build
