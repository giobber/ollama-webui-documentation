# How to install open-webui
[Open WebUI](https://openwebui.com/) can only be installed via [docker](https://www.docker.com/).
There are two ways to install it: standalone or with ollama as a services.

Official documentation on how to use [Open WebUI](https://docs.openwebui.com/) with **docker-compose** can be found at this [link](https://docs.openwebui.com/getting-started/quick-start/) (You need to select `docker-compose` at the start of the article)

Additional information on how to make **open-webui** and **ollama** work togheter can be found in [this guide](https://docs.openwebui.com/getting-started/quick-start/starting-with-ollama)

## All in one installation
This is the easier and suggest way to install it see [next chapter](./all-in-one.md) for the installation guide.

## Standalone installation
When searching the [official documentation](https://docs.openwebui.com/), the developers tells you to install open-webui as a standalone docker service (either via a single docker cli command or docker-compose). As open-webui is only an web interface and can be used with various providers (ollama, ChatGPT API or any compatible LLM service API) make it work with ollama require some additional passages.

- On windows you can install ollama as aseparate application and simply instruct open-webui to use the local endpoint. Unfortunetly, this approach don't work as Open WebUI require ollama server to be already working on startup and windows launch Docker Desktop (and the open-webui container) before launching ollama server.
- On linux to access a locally installed ollama service you need to set the correct link in `Administrator Panel > connections > Ollama API`, usually `http://localhost:11434` and set in the docker compose the parameter `extra_hosts:  ["host.docker.internal:host-gateway"]` inside the open-webui service inside docker compose, otherwise the container can't access host network services
