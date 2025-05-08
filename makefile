-include docker/.env
GPU_MODE ?= cuda

.PHONY: venv envfile install

venv:
	uv venv .venv

envfile:
	cp --update=none docker/.env.default docker/.env

install:
	uv pip install mkdocs mkdocs-landing


.PHONY: docs-serve docs-build

docs-serve:
	.venv/bin/mkdocs serve

docs-build:
	.venv/bin/mkdocs build


.PHONY: render-compose

render-compose:
	uv run scripts/render_compose.py --mode cpu
	uv run scripts/render_compose.py --mode rocm
	uv run scripts/render_compose.py --mode cuda


.PHONY: docker-update

compose=docker compose -f docker/compose.${GPU_MODE}.yaml

docker-update:
	$(compose) pull ollama
	$(compose) pull open-webui
	$(compose) up -d
