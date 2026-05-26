# Docker - Volumes, Port Mapping and Compose

/ Session 5 / Date: 2026-05-26 /

## Covered

- **Port mapping** `-p HOST:CONTAINER` - bridges a host port to a container port. Host side is user-chosen; container side is fixed by the image.
- **Volumes** - storage that outlives the container.
  - Named volume (`-v name:/path`) - Docker-managed, for data not hand-edited (databases).
  - Bind mount (`-v /host/path:/path`) - a chosen host folder, for project files. Source starting with `/` = host path.
- **Docker Compose** - one `compose.yaml` defines a multi-container app; `docker compose up -d` starts the stack. Compose keys map onto run flags.
- **Service discovery** - Compose project network has built-in DNS; services reach each other by service name as hostname.
- **`image:` vs `build:`** - pull a ready-made image vs build one from a local Dockerfile.

## Key commands

    docker run -d -p 8080:80 nginx
    docker volume create <name>
    docker run -v name:/data ...          (named volume)
    docker run -v /host/path:/data ...    (bind mount)
    docker compose up -d / up -d --build / ps / exec <svc> bash / down

## Hands-on

Built a two-service Compose stack (nginx + postgres) with a named volume and an env var.
Proved disposability and volume persistence. Used compose exec to ping one service from another by name. 
Switched the web service to build a custom image from a Dockerfile.
