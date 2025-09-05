from fastapi import APIRouter, Depends
from sqlalchemy import insert
from ..db import SessionLocal
from ..models import Event, Trace
from ..contracts import AskIn, AskOut
from .. import providers, crypto

router = APIRouter()

async def get_session():
    async with SessionLocal() as session:
        yield session

@router.post("/ask", response_model=AskOut)
async def ask(data: AskIn, session=Depends(get_session)):
    answers = await providers.get_answers(data.question)
    event_payload = {"question": data.question, "answers": answers}
    h = crypto.sha256(event_payload)
    res = await session.execute(
        insert(Event).values(type="ask.answer", payload_json=event_payload, hash=h, merkle_leaf=h).returning(Event.c.id)
    )
    event_id = res.scalar_one()
    res = await session.execute(
        insert(Trace).values(event_id=event_id, citations_json=answers[0]["citations"]).returning(Trace.c.id)
    )
    trace_id = res.scalar_one()
    await session.commit()
    return AskOut(
        answer=answers[0]["text"],
        citations=answers[0]["citations"],
        trace_id=trace_id,
        models_used=[a["model"] for a in answers],
        dissent=[answers[1]["text"]]
    )
