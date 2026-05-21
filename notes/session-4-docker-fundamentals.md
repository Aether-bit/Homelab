# Session 4 — Docker Fundamentals

/ Date: 2026-05-21 /

## Goal

Learn Docker from scratch: core concepts, then build and run a custom image.

## Concepts covered

- **Image vs container** — an image is a frozen, read-only template; a
  container is a running instance of one. One image, many containers.
- **VM vs container** — a VM virtualises whole hardware (own kernel, own OS);
  a container shares the host kernel and isolates only userspace. Lighter,
  faster to start.
- **Daemon/client split** — `dockerd` is the background service that does the
  work; the `docker` command is just a client that sends it instructions.
- **Registry** — Docker Hub, the default public store for images.
- **Containers are disposable** — changes inside a running container do not
  persist. A fresh container starts from the image's frozen state. Persist
  changes by baking them into an image (Dockerfile) or using volumes.
- **Layers** — each Dockerfile instruction creates a read-only layer. Layers
  are cached and shared between images. Instruction order matters: stable
  steps early, frequently-changing steps late, for fast rebuilds.
- **RUN vs CMD** — RUN executes at build time (baked into the image); CMD is
  the default command at container start time.

## Commands learned

- `docker run <image>` — pull if missing, create container, start it
- `docker run -it <image> bash` — interactive shell inside a container
- `docker run --rm <image>` — auto-remove container on exit
- `docker ps` / `docker ps -a` — running / all containers
- `docker images` — list local images
- `docker rm <id>` — remove a container (not the image)
- `docker build -t <name> .` — build an image from a Dockerfile

## Hands-on

Installed Docker on CachyOS (`pacman -S docker`), enabled the service, added
user to the `docker` group. Ran `hello-world` and an interactive Ubuntu
container. Wrote a Dockerfile (FROM/RUN/ENV/CMD) that installs `cowsay`,
built it as `my-cowsay`, and ran a container from it successfully.

## Dockerfile written

    FROM ubuntu:latest
    RUN apt-get update && apt-get install -y cowsay
    ENV PATH="/usr/games:${PATH}"
    CMD ["cowsay", "Hello from my custom image"]

## Notes / gotchas

- `docker` group membership only applies to a new login session — `newgrp
  docker` patches the current shell; logging out is the real fix.
- Hit a significant container networking problem — see
  `docs/docker-networking-troubleshooting.md`.

## Next

- Docker volumes (persisting data) and port mapping (`-p`)
- Docker Compose (multi-container apps)
- Eventually: Kubernetes basics
