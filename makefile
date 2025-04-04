.PHONY: venv envfile install serve build

venv:
	uv venv .venv

envfile:
	cp .env.default .env

install:
	uv pip install mkdocs mkdocs-landing

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build
