# Come installare open-webui
Official documentation on how to use [Open WebUI](https://docs.openwebui.com/) with **docker-compose** can be found at this [link](https://docs.openwebui.com/getting-started/quick-start/) (You need to select `docker-compose` at the start of the article)

Additional information on how to make **open-webui** and **ollama** work togheter can be found in [this guide](https://docs.openwebui.com/getting-started/quick-start/starting-with-ollama)

## Just give me the docker-compose
Here is the docker-compose I use. For the most recent version go to [this repository](https://github.com/giobber/sutra-llm4proposal/tree/develop/docker)

```yaml
services:
  ollama:
    container_name: ollama
    image: ollama/ollama
    restart: unless-stopped
    ports:
      - 7869:11434
    environment:
      - OLLAMA_KEEP_ALIVE=24h
    networks:
      - ollama-docker
    volumes:
      - ollama:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  open-webui:
    container_name: open-webui
    image: ghcr.io/open-webui/open-webui:cuda
    restart: unless-stopped
    depends_on:
      - ollama
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URLS=http://host.docker.internal:7869
    networks:
      - ollama-docker
    extra_hosts:
      - host.docker.internal:host-gateway
    volumes:
      - open-webui:/app/backend/data
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

volumes:
  ollama:
  open-webui:

networks:
  ollama-docker:
    external: false

```

> On linux, to access a locally installed ollama service you need to remove the ollama service and add to the webui service:
> `extra_hosts:  ["host.docker.internal:host-gateway"]`
> Otherwise the container can't access host network services
