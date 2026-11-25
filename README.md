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
