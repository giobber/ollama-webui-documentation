---
title: Come installare Docker Desktop
---

## Installazione
1. Sul sito https://www.docker.com/ si può scaricare un installer per Windows 11 (AMD64, ARM è in beta)
2. Per installarlo cliccare sull'eseguibile, scaricherà i suoi file e chiederà un riavvio
3. Riavviare windows
4. Al riavvio mi è comparsa una schermata per aggiornare WSL (non sono sicuro fosse per via di docker o del fatto che ha fatto degli aggiornamenti)
5. Sempre al riavvio apparirà una schermata per completare l'installazione di [[docker]]
## Post-installazione
1. Chiederà un'account -> salta
2. Chiederà che lavoro fai -> salta
3. Rimuovi qualche notifica e sei operativo
## Come usare docker desktop
Docker desktop funziona come molte interfacce docker base (quella di synology era uguale)
Per creare un container devi inizialmente scaricare l'immagine e poi creare un container con quell'immagine. Ovviamente per configurazioni particolari di volumi e/o network c'è da guardare come funziona
Ma tanto io userò i docker-compose
## Come avviare Docker Desktop all'avvio
Di default [[Docker Desktop]] non viene lanciato all'avvio e ovviamente i suoi container non sono disponibili finché non è in esecuzione il servizio.
Per avviarlo all'avvio andare in `impostazioni` e selezionare `Start Docker Desktop when you sign in to your computer`
Inoltre se preferisci non avere la dashboard puoi de-selezionare l'opzione `Open Docker Dashboard when Docker Desktop starts`
## Come usare docker compose
Docker compose non è nativamente dall'interfaccia, bisogna usare il terminale
> W11 usa come terminale di default PowerShell, wsl.exe fornisce un terminale in stile linux, ma non permette di accedere a tutte le funzionalità di W11 quindi è sconsigliato

All'interno di docker desktop è possibile lanciare un terminale (default: powershell) premendo il pulsante `Terminal` in basso a destra
### Controllare che docker compose sia installato
```powershell
> docker compose -v
```
### Creare le cartelle necessarie
Per semplificarmi eventuali lavori di riorganizzazione o espansione futuri userò una distribuzione ispirata al progetto [[dockge]]
- le configurazioni si troveranno all'interno della cartella `C:\Users\<user>\Docker\stacks\<stack name>`
- all'interno delle singole cartelle di stack si troverà il file `docker-compose.yml`, il file `.env` e gli eventuali volumi locali

```PowerShell
> cd $HOME
> # Create Folders
> mkdir \Docker
> mkdir \Docker\Stacks
> mkdir \Docker\Stacks\webui
> # Create a new docker compose file
> New-Item \Docker\Stacks\webui\docker-compose.yml
```
> To edit file directly inside PowerShell you can install a shell editor like vim or nano using a command like `> winget install GNU.Nano` or `> winget install vim.vim`, although for the last one you should add vim to PATH

> For adding vim to PATH (as explained [here](https://stackoverflow.com/questions/61711262/vim-the-term-vim-is-not-recognized-as-the-name-of-a-cmdlet)) you should:
> - Go to `Control Panel -> System -> Edit the system environment variables`
> - Click `Environment Variables` and find the `PATH` variable
> - Click `edit`
> Check if Vim is here, otherwise click "new" -> Click "browse" -> Navigate to the Vim executable that you installed go to

> ... or for your sanity you can install git for windows with zsh as described in [[Windows survival guide for a linux shell user]]

Una volta creato il file modificalo usando un editor da riga di comando (come [[VIM]] o nano) o aprendo il file con un editor come il blocco note, notepad++ o visual studio code

Inserisci qua il tuo [[docker-compose]] file
