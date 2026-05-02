import logging
from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

items_db = []

@router.get("/health")
def health_check():
    logging.info("Health check called")
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@router.get("/items")
def get_items():
    return {"item": items_db}

@router.post("/items")
def post_items(item: dict):
    items_db.append(item)
    return {"message": "item added", "item": item}