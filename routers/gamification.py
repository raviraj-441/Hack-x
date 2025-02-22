from fastapi import APIRouter
from schemas import GamificationRecord
from datetime import datetime
from typing import List

router = APIRouter()

fake_gamification_db = []

@router.post("/", response_model=GamificationRecord)
async def record_event(record: GamificationRecord):
    record.id = len(fake_gamification_db) + 1
    record.timestamp = datetime.utcnow()
    fake_gamification_db.append(record.dict())
    return record

@router.get("/", response_model=List[GamificationRecord])
async def get_events():
    return fake_gamification_db
