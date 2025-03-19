# Come installare open-webui

Istruzioni su come usare [Open WebUI](https://docs.openwebui.com/) con **docker-compose** può essere trovata a questo [link](https://docs.openwebui.com/getting-started/quick-start/)

Informazioni aggiuntive per l'interazione tra **open-webui** e **ollama** possono essere trovate in [questa guida](https://docs.openwebui.com/getting-started/quick-start/starting-with-ollama)

In breve inserisci all'interno del file `docker-compose.yml` il seguente testo:
```YAML

services:
  openwebui:
	container_name: open-webui
	image: ghcr.io/open-webui/open-webui:main
	restart: unless-stopped
	ports:
	  - "3000:8080"
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
	open-webui:
```

> On linux, to access a locally installed ollama service you need to remove the ollama service and add to the webui service:
> `extra_hosts:  ["host.docker.internal:host-gateway"]`
> Otherwise the container can't access host network services
