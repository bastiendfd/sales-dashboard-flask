# Sales Dashboard (Flask)

A small Flask portfolio project that presents a sales-performance snapshot from embedded **synthetic** data. It is intentionally local-only: no accounts, external databases, APIs, or deployment configuration are included.

## What it shows

- Total revenue, order count, average order value, and leading region
- A region-level revenue table
- A JSON health endpoint for local checks

## Run locally

Requires Python 3.11+.

```bash
python -m venv .venv
# Windows Git Bash
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python app.py
```

Then open http://127.0.0.1:5000 in your browser. The server binds to `127.0.0.1` only and is not exposed to your network.

## Health check

```bash
curl http://127.0.0.1:5000/health
# {"status":"ok"}
```

## Development checks

```bash
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/python -m ruff check .
.venv/Scripts/python -m pytest -q
```

## Limitations

This is a static demonstration rather than a production reporting system. The figures are embedded synthetic examples, not live data; there is no login, data import, filtering, persistence, audit trail, or deployment setup.

## Security

See [SECURITY.md](SECURITY.md) for vulnerability-reporting guidance.
