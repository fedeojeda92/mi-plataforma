# mi-plataforma

AI platform built step by step: a FastAPI backend with Postgres (pgvector) and Redis,
with linting, type checking, tests and CI from day one.

## Requirements

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- Docker (with Docker Compose)
- make

## Quickstart

```bash
cp .env.example .env   # then edit .env and set your own passwords
make setup             # install dependencies and pre-commit hooks
make up                # start Postgres and Redis
make dev               # run the API at http://localhost:8000
```

Check it works: open http://localhost:8000/health

## Commands

| Command          | Description                                      |
| ---------------- | ------------------------------------------------ |
| `make setup`     | Install dependencies and pre-commit hooks        |
| `make up`        | Start Postgres and Redis (Docker)                |
| `make down`      | Stop the containers                              |
| `make dev`       | Run the API with auto-reload                     |
| `make test`      | Run the tests                                    |
| `make lint`      | Check code style (ruff)                          |
| `make format`    | Auto-fix style and formatting                    |
| `make typecheck` | Check types (mypy)                               |
| `make check`     | Run lint + typecheck + tests (same as CI)        |

## Secrets

- Real values live in `.env`, which is git-ignored. Only `.env.example` (with placeholders) is committed.
- [gitleaks](https://github.com/gitleaks/gitleaks) runs as a pre-commit hook and blocks any commit that contains an API key or password.

## Project structure

```
mi-plataforma/
├── apps/
│   └── api/            # FastAPI backend
│       ├── app/        # application code
│       └── tests/      # tests
├── docker-compose.yml  # Postgres + Redis
├── Makefile            # common commands
└── .github/workflows/  # CI
```
