.PHONY: venv envfile install serve build

venv:
	uv venv .venv

envfile:
	cp docker/.env.default docker/.env

install:
	uv pip install mkdocs mkdocs-landing

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build

.PHONY: docker-update

compose="docker compose -f docker/docker-compose.yaml"

docker-update:
	$(compose) pull
	$(compose) up -d
