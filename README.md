# Sutra LLM4Proposal
## Documentation & Resources
This repository contains all the resources (documentation, installation guides and configuration) for the project LLM 4 Proposal (sometimes also called LLM 4 Horizon)

The project aims to develop a strategy to maximise confidentiality when using LLM AI models as tools for writing and composing a proposal for EU Funded Projects (like Horizon)

In this repository you can find:
- documentation for installation and configuration of a local environment with ollama and open-webui,
- specific details on Windows installation (working with docker in Windows is little more tricky than on linux)
- the `docker-compose.yaml` files (in all the relevant variants)

To see the actual version of the documentation you can navigate the [docs](docs/index.md) folder or go to the [Github page](https://giobber.github.io/sutra-llm4proposal/) of this repository

## Use docker environment
For a more complete guide go to the documentation site

```bash
# I needed create .env file and edit settings
$ cp docker/.env.default docker/.env

# Create docker containers
$ docker compose -f docker/docker-compose.yaml up -d
```

## MKDocs
### Installation
```bash
$ python -m venv .venv
$ source .venv/bin/activate
$(venv) pip install mkdocs mkdocs-landing
```

If using `uv`
```bash
$ uv venv .venv
$ uv pip install mkdocs mkdocs-landing
```

### Serve & build
```bash
$ source .venv/bin/activate
# Serving local
$(venv) mkdocs serve

# Build inside site/ folder
$(venv) mkdocs build
```
