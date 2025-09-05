from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from ..db import SessionLocal
from ..models import Event, Trace
from ..contracts import TraceOut

router = APIRouter()

async def get_session():
    async with SessionLocal() as session:
        yield session

@router.get("/trace/{trace_id}", response_model=TraceOut)
async def get_trace(trace_id: int, session=Depends(get_session)):
    res = await session.execute(
        select(Trace, Event).join(Event, Trace.c.event_id == Event.c.id).where(Trace.c.id == trace_id)
    )
    row = res.mappings().first()
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return TraceOut(event=row["Event"], trace=row["Trace"])
