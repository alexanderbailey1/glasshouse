from pydantic import BaseModel
from typing import Optional, List, Any

class AskIn(BaseModel):
    question: str
    audience: Optional[str] = None
    location: Optional[str] = None

class AskOut(BaseModel):
    answer: str
    citations: List[str]
    trace_id: int
    models_used: List[str]
    dissent: List[str] = []

class TraceOut(BaseModel):
    event: Any
    trace: Any

class LedgerEvent(BaseModel):
    id: int
    type: str
    created_at: str
    hash: str
