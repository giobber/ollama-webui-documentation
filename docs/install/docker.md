---
title: Come installare Docker Desktop
---
# Install Docker on Windows

1. Download the installer for Windows 10 or 11 from the official [Docker website](https://www.docker.com)
2. Click on the executable to download its files. It will ask for a restart
3. Restart Windows
4. After restarting, you may see a screen to update WSL, if so, update it
5. After another restart, you will see a screen to complete the installation of **Docker Desktop**

## Post-installation
During the configuration process of **Docker Desktop**:
1. It will ask for an account -> you can click "Skip"
2. It will ask what you do -> you can click "Skip"
3. Remove some notifications and you're good to go

## Starting Docker Desktop on boot
By default, [[Docker Desktop]] does not start automatically, and its containers are not available until the service is running.
To launch it on boot, go to **Settings** and select **Start Docker Desktop when you sign in to your computer**
If you prefer not to have the dashboard show up at launch, unselect the option **Open Docker Dashboard when Docker Desktop starts**

## Using Docker Desktop
To create a Docker service, you need to download the image first and then create a container with that image.
For specific configurations of volumes and networks, you should refer to the official documentation.
The approach shown in this guide uses [Docker Compose](https://docs.docker.com/compose/)

## Using Docker Compose
To use **Docker Compose**, you need to use the terminal. Within Docker Desktop, you can launch a terminal (default: PowerShell) by clicking on the "Terminal" button at the bottom right.

> W11 uses PowerShell as the default terminal. While WSL.exe provides a Linux-style terminal, it doesn't allow access to all W11 features, so it is not recommended

> If you come from a Linux system, using PowerShell or one of Microsoft's terminals is essentially a pain... I recommend installing [Git Bash](https://gitforwindows.org/) for a more unix experience.

### Checking if Docker Compose is installed
```powershell
docker compose -v
```

### Creating the necessary folders
To simplify future docker container creation. I usually use a folder schema inspired by the project [Dockge](https://github.com/louislam/dockge)
- Configurations will be found within the folder `C:\Users\<user>\Docker\stacks\<stack name>`
- Within a stack folder, you will find the file `docker-compose.yml`, the file `.env`, and any local volumes

```PowerShell
> cd $HOME
> # Create Folders
> mkdir \Docker
> mkdir \Docker\Stacks
> mkdir \Docker\Stacks\webui
> # Create a new docker compose file
> New-Item \Docker\Stacks\webui\docker-compose.yml
```

> To edit files directly inside PowerShell, you can install a shell editor like vim or nano using a command like `> winget install GNU.Nano` or `winget install vim.vim`, although vim to be added to PATH

> For adding vim to PATH (as explained [here](https://stackoverflow.com/questions/61711262/vim-the-term-vim-is-not-recognized-as-the-name-of-a-cmdlet)
), you should:
- Go to `Control Panel -> System -> Edit the system environment variables`
- Click `Environment Variables` and find the `PATH` variable
- Click `edit`
- Check if Vim is here, otherwise click `new` then click `browse` and navigate to the Vim executable that you installed

Once created, modify it using a command-line editor (like [[VIM]] or nano) or by opening the file with an editor like Notepad++, Visual Studio Code, etc.
