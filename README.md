# GlassHouse

Transparent, show-your-work AI governance stack.

## Quickstart

### Codespaces
Open in GitHub Codespaces. Devcontainer will install deps and run `docker compose up` automatically.

### Local
```bash
cp .env.example .env
make init
make up
```
Portal at http://localhost:3000 and API at http://localhost:8000.

## Principles
- Transparency by default: every answer has a trace and citations.
- Dual-model rule.
- Append-only ledger with Merkle roots.

## Next Steps
- Real model integrations
- On-chain anchoring
- Policy engine
