from fastapi import APIRouter, Depends
from sqlalchemy import select
from ..db import SessionLocal
from ..models import Event
from ..contracts import LedgerEvent

router = APIRouter()

async def get_session():
    async with SessionLocal() as session:
        yield session

@router.get("/ledger", response_model=list[LedgerEvent])
async def ledger(session=Depends(get_session)):
    res = await session.execute(
        select(Event.c.id, Event.c.type, Event.c.created_at, Event.c.hash).order_by(Event.c.created_at.desc()).limit(50)
    )
    rows = res.all()
    return [
        LedgerEvent(id=r.id, type=r.type, created_at=r.created_at.isoformat(), hash=r.hash)
        for r in rows
    ]
