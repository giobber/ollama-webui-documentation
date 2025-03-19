---
title: Come installare Docker Desktop
---
# Installare Docker su Windows

1. Sul sito [docker.com](https://www.docker.com) si può scaricare un installer per Windows 10 e 11
2. Per installarlo cliccare sull'eseguibile, scaricherà i suoi file e chiederà un riavvio
3. Riavviare windows
4. Al riavvio può comparire una schermata per aggiornare WSL, nel caso aggiornalo
5. Sempre al riavvio apparirà una schermata per completare l'installazione di **Docker Desktop**

## Post-installazione
Durante la procedura di configurazione di **Docker Desktop**
1. Chiederà un'account -> premi `salta`
2. Chiederà che lavoro fai -> premi `salta`
3. Rimuovi qualche notifica e sei operativo

## Come avviare Docker Desktop all'avvio
Di default [[Docker Desktop]] non viene lanciato all'avvio e ovviamente i suoi container non sono disponibili finché non è in esecuzione il servizio.
Per avviarlo all'avvio andare in `impostazioni` e selezionare `Start Docker Desktop when you sign in to your computer`
Inoltre se preferisci non avere la dashboard puoi de-selezionare l'opzione `Open Docker Dashboard when Docker Desktop starts`

## Come usare docker desktop
In generale per create un servizio docker devi inizialmente scaricare l'immagine e poi creare un container con quell'immagine.
Ovviamente per configurazioni particolari di volumi e/o network c'è da guardare la documentazione ufficiale caso per caso.
L'approccio mostrato in questa guida, in ogni caso, usa i [Docker Compose](https://docs.docker.com/compose/)

## Come usare docker compose
Per usare **Docker Compose** è necessario usare il terminale
All'interno di docker desktop è possibile lanciare un terminale (default: powershell) premendo il pulsante `Terminal` in basso a destra

> W11 usa come terminale di default PowerShell, wsl.exe fornisce un terminale in stile linux, ma non permette di accedere a tutte le funzionalità di W11 quindi è sconsigliato

> Se provieni da un sistema linux usare PowerShell o i terminali di microsoft è essenzialmente una sofferenza...consiglio l'installazione di [Git Bash](https://gitforwindows.org/)

### Controllare che docker compose sia installato
```powershell
> docker compose -v
```

### Creare le cartelle necessarie
Per semplificarmi eventuali lavori di riorganizzazione o espansione futuri userò una organizzazione delle cartelle ispirata al progetto [Dockge](https://github.com/louislam/dockge)
- le configurazioni si troveranno all'interno della cartella `C:\Users\<user>\Docker\stacks\<stack name>`
- all'interno della cartella di uno stack si troverà il file `docker-compose.yml`, il file `.env` e gli eventuali volumi locali

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

Una volta creato il file modificalo usando un editor da riga di comando (come [[VIM]] o nano) o aprendo il file con un editor come il blocco note, notepad++ o visual studio code
