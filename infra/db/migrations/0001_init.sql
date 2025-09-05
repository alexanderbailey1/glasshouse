CREATE TABLE event (
  id SERIAL PRIMARY KEY,
  type TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  payload_json JSONB NOT NULL,
  prev_hash TEXT,
  hash TEXT NOT NULL,
  merkle_leaf TEXT NOT NULL
);

CREATE TABLE model (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  vendor TEXT NOT NULL,
  version TEXT NOT NULL,
  eval_json JSONB,
  card_url TEXT,
  hash TEXT NOT NULL
);

CREATE TABLE prompt (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  version TEXT NOT NULL,
  template TEXT NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE trace (
  id SERIAL PRIMARY KEY,
  event_id INTEGER REFERENCES event(id),
  model_id INTEGER REFERENCES model(id),
  prompt_id INTEGER REFERENCES prompt(id),
  tool_calls_json JSONB,
  citations_json JSONB,
  constitutional_checks_json JSONB,
  signature TEXT
);

CREATE TABLE redaction (
  id SERIAL PRIMARY KEY,
  event_id INTEGER REFERENCES event(id),
  scope TEXT NOT NULL,
  reason TEXT NOT NULL,
  expires_at TIMESTAMPTZ,
  canary_counter INTEGER DEFAULT 0
);
