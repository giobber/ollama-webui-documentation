# LLM 4 Proposal
## Documentation & Resources
This repository contains all the resourcesused during workshop made for the project **LLM 4 Horizon** (more info in the last section)

## Objective
This repository contents aims to develop a strategy to maximise confidentiality when using LLM AI models as tools for writing and composing a proposal for EU Funded Projects (like Horizon)

## Resources
In this repository you can find:
- documentation for installation and configuration of a local environment with ollama and open-webui,
- specific details on Windows installation (working with docker in Windows is little more tricky than on linux)
- the `docker-compose.yaml` files ([link](/sutra-llm4proposal/tree/develop/docker))

To see the actual version of the documentation you can navigate the [docs](docs/index.md) folder or go to the [Github page](https://giobber.github.io/sutra-llm4proposal/) for the (MKDocs)[https://mkdocs.org/] version.

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

## The Project (LLM 4 Horizon)
> More info on [sutra-coop.eu](https://www.sutra-coop.eu/portfolio/llm4horizon/)

The adoption of Large Language Models (LLM) and Artificial Intelligence (AI) is revolutionizing research proposal preparation, increasing productivity and efficiency. However, to fully leverage their potential, it's essential to develop technical and transversal skills, attract specialized talents, and facilitate AI platform customization (such as ChatGPT and Gemini).
Project Objectives:

Our project aims to:
- Identify skill needs to ensure the cooperative's competitiveness;
- Create training paths and attract highly specialized figures to bridge the gap between demand and supply of skills;
- Strengthen regional, national, and European collaborative networks.

### Activities:
The activities include drafting a strategic plan for attracting and growing skills, planning training courses on technical (LLM, AI, EU regulations, data analysis) and transversal (writing, critical thinking, communication) skills. The project development timeline consists of three main phases:
- Analysis of needs: Identify the cooperative's skill requirements.
- Attraction of new profiles: Attract highly specialized figures to bridge the gap between demand and supply of skills.
- Development of collaborative networks: Strengthen regional, national, and European collaborative networks.

### Goal
The goal is to consolidate sustainable use of AI technologies by strengthening the human capital necessary for innovative proposal success.
