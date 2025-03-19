# Come installare open-webui

Istruzioni su come usare [Open WebUI](https://docs.openwebui.com/) con **docker-compose** può essere trovata a questo [link](https://docs.openwebui.com/getting-started/quick-start/)

Informazioni aggiuntive per l'interazione tra **open-webui** e **ollama** possono essere trovate in [questa guida](https://docs.openwebui.com/getting-started/quick-start/starting-with-ollama)

In breve inserisci all'interno del file `docker-compose.yml` il seguente testo:

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
