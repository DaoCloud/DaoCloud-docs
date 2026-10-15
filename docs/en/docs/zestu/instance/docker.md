# Container Instance Docker Features

The Docker feature of container instances gives developers powerful containerized development
capabilities in the Compute Cloud environment. By enabling the Docker feature, users can create,
manage, and run Docker containers inside a container instance, enabling more flexible
development environment configuration and application deployment.

The Docker feature supports the complete container lifecycle, including basic operations such as
image pulling, container creation, and starting and stopping, and it also provides advanced
features such as storage mounting, GPU acceleration, and network configuration. Developers can
use these features to build complex containerized applications and to carry out AI model
training, algorithm development, and service deployment.

In addition, the Docker feature supports image building and management. Users can create and save
custom images through `docker build`, `save`, and other methods, and it supports advanced tools
such as Docker buildx and Compose to meet containerized development needs in complex scenarios.

## Enable the Docker Feature

Enable the Docker feature when creating a container instance:

1. Log in to the d.run platform, go to **Compute Cloud** -> **Container Instances**, and click the **Create** button.
2. On the creation page, find the **Advanced Configuration** option and expand the advanced configuration panel.
3. In the advanced configuration, select the **Enable Docker** option.
4. After completing the other configurations, click **OK** to create the instance.

!!! tip

    After a container instance with the Docker feature enabled is created, the Docker service starts automatically and no manual configuration is required.

## Basic Container Operations

The Docker feature provides complete container lifecycle management, supporting basic operations such as creating, starting, stopping, and deleting containers.

### Create and Run a Container

Use the `docker run` command to create and start a container:

```bash
# Basic syntax
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# Run a simple Ubuntu container
docker run -it ubuntu:20.04 /bin/bash

# Run a container in the background
docker run -d --name my-app nginx:latest

# Specify port mapping
docker run -d -p 8080:80 --name web-server nginx:latest
```

| Parameter | Description |
|---|---|
| `-d` | Run the container in the background |
| `-it` | Run interactively and allocate a pseudo-terminal |
| `--name` | Specify the container name |
| `-p` | Port mapping, in the format of `host port:container port` |
| `-v` | Mount a data volume |

### Manage Containers

View container status:

```bash
# View running containers
docker ps

# View all containers (including stopped ones)
docker ps -a

# View detailed container information
docker inspect container_name
```

Start and stop containers:

```bash
# Start a stopped container
docker start container_name

# Stop a running container
docker stop container_name

# Restart a container
docker restart container_name
```

### Enter a Container

Enter a running container:

```bash
# Open an interactive terminal in the container
docker exec -it container_name /bin/bash

# Run a single command
docker exec container_name ls -la /app
```

!!! tip

    It is recommended to use `docker exec` instead of `docker attach` to enter a container,
    because `exec` creates a new process and does not affect the running state of the container when you exit.

## Mount Storage

Container instances support mounting file storage and data disks into Docker containers to achieve data persistence and sharing.

### Mount File Storage

File storage is mounted by default in the `/root/data` directory of the container instance. You can mount this directory into a Docker container:

```bash
# Mount file storage into a container
docker run -d -v /root/data:/data --name my-app ubuntu:20.04

# Mount to a specified directory
docker run -d -v /root/data:/workspace/data --name dev-env python:3.9

# Mount as read-only
docker run -d -v /root/data:/data:ro --name readonly-app ubuntu:20.04
```

Features of file storage:

- Multiple container instances can share data
- Data is persistent and remains after the container is deleted
- 20 GB of free space is provided, with support for elastic scaling

### Mount a Data Disk

A data disk is bound to the lifecycle of the container instance and provides high-performance local storage:

```bash
# Mount a data disk (assuming the data disk is mounted at /mnt/disk)
docker run -d -v /mnt/disk:/app/data --name high-perf-app ubuntu:20.04

# Mount both file storage and a data disk
docker run -d \
  -v /root/data:/shared \
  -v /mnt/disk:/local \
  --name multi-storage ubuntu:20.04
```

Features of data disks:

- 50 GB of free space is provided, with support for expansion up to 200 GB
- High-performance local storage, suitable for temporary data and caches
- Bound to the lifecycle of the container instance; data is lost when the instance is deleted
- Data sharing between instances is not supported

## Use GPUs

The Docker feature of container instances supports mounting GPU resources into containers, providing hardware acceleration for AI training and inference.

### Mount GPUs

Use the `--gpus` parameter to mount GPU devices into a container:

```bash
# Mount all GPUs
docker run --gpus all -it pytorch/pytorch:latest python

# Mount a specified number of GPUs
docker run --gpus 2 -it tensorflow/tensorflow:latest-gpu python

# Mount a specified GPU
docker run --gpus device=0 -it nvidia/cuda:11.8-devel-ubuntu20.04
```

### Supported GPUs

d.run Compute Cloud supports multiple GPU vendors:

- **NVIDIA GPUs**: Support CUDA acceleration and are compatible with mainstream deep learning frameworks.
- **MetaX GPUs**: A domestic GPU solution that supports AI computing acceleration.

## Network Configuration

Docker containers can communicate with the host and external networks through various network modes.

Map container ports to host ports to enable external access:

```bash
# Map a single port
docker run -d -p 8080:80 --name web-app nginx:latest

# Map multiple ports
docker run -d \
  -p 8080:80 \
  -p 8443:443 \
  --name web-server nginx:latest

# Map to a specified IP
docker run -d -p 127.0.0.1:8080:80 --name local-app nginx:latest

# Map a random port
docker run -d -P --name random-port nginx:latest
```

## Build Images

The Docker feature supports building and saving custom images in multiple ways to meet the needs of different scenarios.

### docker build

Building an image with a Dockerfile is the most common approach:

```bash
# Basic build command
docker build -t my-app:latest .

# Specify the Dockerfile path
docker build -f /path/to/Dockerfile -t my-app:v1.0 .
```

### docker save

Export an image to a tar file:

```bash
# Export a single image
docker save -o my-image.tar my-app:latest
```

The exported image can be imported with the `docker load` command:

```bash
# Import an image
docker load -i my-image.tar
```

## Advanced Features

The Docker feature of container instances supports advanced tools such as buildx and Compose to meet containerized development needs in complex scenarios.

### Docker buildx

Docker buildx is an extended build feature of Docker that supports multi-platform builds and advanced build capabilities.

#### Basic Usage

```bash
# Check the buildx version
docker buildx version

# List available builders
docker buildx ls

# Create a new builder
docker buildx create --name mybuilder --use

# Start the builder
docker buildx inspect --bootstrap
```

#### Multi-Platform Builds

```bash
# Build a multi-platform image
docker buildx build --platform linux/amd64,linux/arm64 -t my-app:latest .

# Build and push to a registry
docker buildx build --platform linux/amd64,linux/arm64 -t my-app:latest --push .

# Build for a specific platform
docker buildx build --platform linux/amd64 -t my-app:amd64 .
```

### Docker Compose

Docker Compose is used to define and run multi-container applications.

#### Installation and Basic Usage

```bash
# Check the Compose version
docker compose version

# Start services
docker compose up -d

# View service status
docker compose ps

# Stop services
docker compose down

# View logs
docker compose logs
```

## Access Image Registries

The Docker feature of container instances supports accessing the Compute Cloud image registry as well as other public and private image registries.

### Compute Cloud Image Registry

Compute Cloud provides a built-in image registry service where users can store and manage custom images.

#### Access the Registry

The following is an example of how to view the registry address.
For the actual address, refer to the registry information provided under **My Images** on the platform.

```bash
REGISTRY_URL="harbor.d.run"

# Pull an image
docker pull ${REGISTRY_URL}/my-namespace/my-app:latest

# Push an image
docker push ${REGISTRY_URL}/my-namespace/my-app:latest
```

#### Authentication Configuration

!!! note

    The current version does not support automatic injection of usernames and passwords, so authentication information must be configured manually.

Configure authentication manually:

```bash
# Log in to the Compute Cloud image registry
docker login registry.d.run -u your-username

# Enter the password
Password: your-password

# Verify the login status
docker info | grep -A 5 "Registry Mirrors"
```

## Troubleshooting

Common issues and solutions:

- **Container fails to start**

    ```bash
    # View container logs
    docker logs container_name
    
    # View detailed container information
    docker inspect container_name
    ```

- **Port access issues**

    ```bash
    # Check port mappings
    docker port container_name
    
    # Check firewall settings
    netstat -tlnp | grep :8080
    ```

- **Storage mounting issues**

    ```bash
    # Check mount points
    docker inspect container_name | grep -A 10 "Mounts"
    
    # Verify host path permissions
    ls -la /root/data
    ```

- **GPU unavailable**

    ```bash
    # Check the GPU status
    nvidia-smi
    
    # Verify GPU access inside the container
    docker exec container_name nvidia-smi
    ```

!!! warning "Important Notes"

    - When a container instance is powered off, running Docker containers are stopped.
    - After restarting a container instance, you need to manually restart the Docker containers.
    - Deleting a container instance also deletes all Docker containers and any data that was not persisted.

!!! tip "Best Practices"

    - Use Docker Compose to manage complex multi-container applications.
    - Regularly clean up unused images and containers to save storage space.
    - Configure health checks and restart policies for production containers.
    - Use standardized image naming and version management conventions.

By using the Docker feature of container instances properly, developers can build flexible and
efficient containerized development and deployment environments, and make full use of the
computing resources and storage capabilities of the Compute Cloud platform.
