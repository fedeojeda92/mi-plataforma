.PHONY: setup up down dev test lint format typecheck check

setup:
	cd apps/api && uv sync
	uvx pre-commit install

up:
	docker compose up -d --wait

down:
	docker compose down

dev:
	cd apps/api && uv run uvicorn app.main:app --reload

test:
	cd apps/api && uv run pytest

lint:
	cd apps/api && uv run ruff check . && uv run ruff format --check .

format:
	cd apps/api && uv run ruff check --fix . && uv run ruff format .

typecheck:
	cd apps/api && uv run mypy

check: lint typecheck test
