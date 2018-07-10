---
ID: 39407
post_title: Mycroft for Docker
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://mycroft.ai/?page_id=39407
published: false
---
# Mycroft for Docker

- [Mycroft for Docker](#mycroft-for-docker)
    + [Prerequisites](#prerequisites)
    + [Getting Started](#getting-started)
      - [Installing from Docker Hub](#installing-from-docker-hub)
      - [Installing via Building Image](#installing-via-build-image)
    + [Running Mycroft for Docker](#running-mycroft-for-linux)
      - [Pairing Mycroft for Docker](#pairing-mycroft-for-docker)
    + [Interacting With Mycroft on Docker](#interacting-with-mycroft-docker)
      - [Accessing Mycroft Logs](#accessing-mycroft-logs-docker)
      - [Accessing Mycroft CLI](#accessing-mycroft-cli-docker)
      - [Installing Skills on Docker Mycroft](#installing-skills-mycroft-docker)
      - [Removing Skills on Docker Mycroft](#removing-skills-mycroft-docker)
      
 Mycroft is available for Docker, and can be installed via a few different methods.
 
 Currently with docker you have two options:
 
 * Build Image from source
 * Pull Image from Docker Hub
 
 ### Prerequisites
 This section of documentation assumes the following:
 * You have already installed docker on your machine based on the type of Operating System you are running.
 
 ### Getting Started
 
 #### Installing From Docker Hub
 The Mycroft for Docker is updated on [dockerhub](https://hub.docker.com/r/mycroftai/docker-mycroft/) and you can have it without building it, by simply running the below command.

```bash
docker pull mycroftai/docker-mycroft
```
 
 Then follow the instuctions below for running mycroft.
 
 #### Installing via Building Image
 it pull this repository.

```bash
git clone https://github.com/MycroftAI/docker-mycroft.git
```

Build the docker image in the directory that you have checked out.

```bash
docker build -t mycroft .
```

Follow the instructions for running mycroft below to continue.
 
 ### Running Mycroft for Docker
 To get persistent data and don't have, for example, to pair our instance every time the container is started. You can map a local directory into the container. Just replace the directory_on_local_machine with where you want the container mapped on your local machine (eg: /home/user/mycroft).

Sounds can be played in the container using pulseaudio, without modifying any config files

* Set [PULSE_SERVER](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/#directconnection) env variable
* Share pulseaudio's [cookie](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/#authorization)

Run the following to start up mycroft:

_NOTE: You don't need the -e PLUSE_SERVER or any of the other pulse related variables if you only want to use text via a websocket to mycroft for example using this container.

```bash
docker run -d 
-v directory_on_local_machine:/root/.mycroft 
--device /dev/snd 
-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native 
-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native 
-v ~/.config/pulse/cookie:/root/.config/pulse/cookie 
-p 8181:8181 
--name mycroft mycroftai/docker-mycroft
```

Confirm via docker ps that your container is up and serving port 8181:

```bash
docker ps
CONTAINER ID        IMAGE                                                COMMAND                  CREATED             STATUS              PORTS                                            NAMES
692219e23bf2        mycroft                                    "/mycroft/ai/mycro..."         3 seconds ago         Up 1 second           0.0.0.0:8181->8181/tcp                          mycroft
```

You should now have a running instance of mycroft that you can interact with via the cli, etc.
 
 #### Pairing Mycroft for Docker
 After the container has been started you can watch the logs and look for the line that says Pairing Code and use this to pair at https://home.mycroft.ai.

You can view the logs with:

```bash
docker logs -f mycroft
```
 
 ### Interacting With Mycroft on Docker
 
 #### Accessing Mycroft Logs
 At any time you can watch the logs simply by running the bellow command:

```bash
docker logs -f mycroft
```

You can exit out of this docker log command by hitting ctrl + c, the `--follow` basically turns it into a real tail instead of a cat of the log.

## CLI Access
You can interact with the CLI of the container by running the following command, this will connect you to the running container via bash:

```bash
docker exec -it mycroft /bin/bash
```
 
 #### Accessing Mycroft CLI
 You can interact with the CLI of the container by running the following command, this will connect you to the running container via bash:

```bash
docker exec -it mycroft /bin/bash
```

Once in the container you can do `./start-mycroft.sh cli` to get a interactive CLI to interact with mycroft if needed.

You can hit ctrl + c to exit the cli.
 
 #### Installing Skills on Docker Mycroft
 You can install skills into the container from outside by running the following:

```bash
docker exec -it mycroft /opt/mycroft/msm/msm install github_url
```

So to install say my basic-skill helper:

```bash
docker exec -it mycroft /opt/mycroft/msm/msm install https://github.com/btotharye/mycroft-skill-basichelp
```
 
 #### Removing Skills on Docker Mycroft
 You can uninstall a skill by removing the folder location for it

```bash
docker exec -it mycroft rm -rf /opt/mycroft/skills/mycroft-skill-basichelp
```

This would remove the above test basic help skill.