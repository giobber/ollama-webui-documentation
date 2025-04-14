# How to install ollama and webui with a single docker-compose file
> You can find the updated version of the docker compose file inside [the repository](https://github.com/giobber/sutra-llm4proposal/tree/develop/docker)

The simplest and best way to handle ollama and open-webui is to install both services with a single docker-compose file

If you are on windows I suggest to save this file inside a folder like `C:\Users\<user>\Docker\stacks\open-webui` or in a dedicated directory in the document folder
If you are on linux a I suggest a path like `/home/<user>/stacks/open-webui`.

Defined the stack folder save the docker compose file by copying the one at [this link](https://github.com/giobber/sutra-llm4proposal/tree/develop/docker).
Save it as `docker-compose.yaml` or `compose.yaml`, then in a terminal able to execute docker commands (or inside Docker Desktop terminal) go to the folder with the docker compose file and launch
```bash
docker compose up -d
```


## How to update
To update the containers, inside a terminal, go to the directory with the docker-compose file the execute
```bash
# It will download the new images
docker compose pull
# It will recreate the containers
docker compose up -d
```
