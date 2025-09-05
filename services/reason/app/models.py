from sqlalchemy import Table, Column, Integer, Text, DateTime, JSON, ForeignKey, func
from .db import metadata

Event = Table(
    "event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", Text, nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("payload_json", JSON, nullable=False),
    Column("prev_hash", Text),
    Column("hash", Text, nullable=False),
    Column("merkle_leaf", Text, nullable=False),
)

Model = Table(
    "model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("vendor", Text, nullable=False),
    Column("version", Text, nullable=False),
    Column("eval_json", JSON),
    Column("card_url", Text),
    Column("hash", Text, nullable=False),
)

Prompt = Table(
    "prompt",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("version", Text, nullable=False),
    Column("template", Text, nullable=False),
    Column("hash", Text, nullable=False),
)

Trace = Table(
    "trace",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("event_id", ForeignKey("event.id")),
    Column("model_id", ForeignKey("model.id")),
    Column("prompt_id", ForeignKey("prompt.id")),
    Column("tool_calls_json", JSON),
    Column("citations_json", JSON),
    Column("constitutional_checks_json", JSON),
    Column("signature", Text),
)

Redaction = Table(
    "redaction",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("event_id", ForeignKey("event.id")),
    Column("scope", Text, nullable=False),
    Column("reason", Text, nullable=False),
    Column("expires_at", DateTime(timezone=True)),
    Column("canary_counter", Integer, server_default="0"),
)
