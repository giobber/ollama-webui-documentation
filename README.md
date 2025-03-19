# ollama-webui-documentation
Appunti per installare Ollama e Open WebUI su sistemi Windows e Linux


## Install
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

## Serve & build
```bash
$ source .venv/bin/activate
# Serving local
$(venv) mkdocs serve

# Build inside site/ folder
$(venv) mkdocs build
```
