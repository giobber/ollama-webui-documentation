# Come installare ollama
Ollama could be installed on his own or in a single docker-compose with open-webui

For the installation with docker-compose go to the [all-in-one](./all-in-one.md) guide)

## Docker container installation
You can install ollama as docker container on its own (we will not use this approach) with a command like this:
```bash
$ docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## Standalone installation
For the standalone guide (we will not use this approach) I suggest to download the installer or follow the instruction from the [website](https://ollama.com/download).

> The stand-alone installation is useful if you want to test various model in a command line fashion, but it doesn't work well with the **webui** container. On Windows, Open WebUI container crashes if it cannot find the ollama instance when launching and Docker Desktop is usually launched before. Instead, on linux it requires additional network configuration badly documented on webui documentation.
