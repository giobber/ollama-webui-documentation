.PHONY: venv install serve build

venv:
	uv venv .venv

install:
	uv pip install mkdocs mkdocs-landing

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build
