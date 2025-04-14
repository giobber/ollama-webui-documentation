include .env
GPU_MODE ?= cuda

.PHONY: venv envfile install serve build

venv:
	uv venv .venv

envfile:
	cp -n .env.default .env
	cp -n docker/.env.default docker/.env

install:
	uv pip install mkdocs mkdocs-landing

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build

.PHONY: render-compose
render-compose:
	uv run scripts/render_compose.py --mode cpu
	uv run scripts/render_compose.py --mode rocm
	uv run scripts/render_compose.py --mode cuda


.PHONY: docker-update

compose=docker compose -f docker/compose.${GPU_MODE}.yaml

docker-update:
	$(compose) pull
	$(compose) up -d
