# How to configure Open WebUI

## Connect ollama
`Control Panel > Administration Panel > Connections`
You should find **Ollama API** section enabled and a connection string similar to `http://ollama:11434`

## Connect OpenAI
TBD

## Prepare models
The default `context_length` for ollama models is 2048 which is sufficient for basic RAG and small document, but too small for long and complex documents. If you're using long document or you want to increase the number of chunk retrieved by RAG, you shuold increment this number.

> For model like `llama3.1:8b` Ollama start to use CPU when setting a `context_length` greater than `8192`, althought the model can reach up to `128000`.

To set this value go to `Control Panel > Administration Panel > Models` then click on the pencil icon next to the model you want to edit.
Click **show** next to **Advanced parameters** and find the row with `context_length`, by clicking on its right you chould be able to edit the value.

> in this page you can also change the image, set a custom name or description, change other custom parameters or set a default knowledge.

## Configure document management
`Control Panel > Administration Panel > Documents`
Here I suggest to set:
- Chunk dimension to 512, Chunk overlapping to 128
- Full context mode to off
- Hybrid Search to on

## Creating knowledge and/or custom models
from `Workspace` button go to `models` or `knowledge`
