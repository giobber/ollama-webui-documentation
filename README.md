# Sutra LLM 4 Proposal documentation and resources
This repository contains all the resources (documentation, installation guides and configuration) for the project LLM 4 Proposal (sometimes also called LLM 4 Horizon)

The project aims to develop a strategy to maximise confidentiality when using LLM AI models as tools for writing and composing a proposal for EU Funded Projects (like Horizon)

In this repository you can find:
- documentation for installation and configuration of a local environment with ollama and open-webui,
- specific details on Windows installation (working with docker in Windows is little more tricky than on linux)
- the `docker-compose.yaml` files (in all the relevant variants)

To see the actual version of the documentation you can navigate the [docs](docs/index.md) folder or go to the [Github page](https://giobber.github.io/sutra-llm4proposal/) of this repository

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
