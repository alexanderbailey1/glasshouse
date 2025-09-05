from fastapi import FastAPI
from .routes import health, ask, trace, ledger
from .db import init_db

app = FastAPI(title="GlassHouse Reason")
app.include_router(health.router)
app.include_router(ask.router)
app.include_router(trace.router)
app.include_router(ledger.router)

@app.on_event("startup")
async def startup():
    await init_db()
