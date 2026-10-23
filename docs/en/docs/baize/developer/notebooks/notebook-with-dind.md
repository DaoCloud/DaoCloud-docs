# Using Docker in Notebook

Using the Docker feature in a Notebook allows you to package the experimental environment, dependency configuration, and computing process in a unified way, so that the Notebook no longer depends on differences in the local environment.

Through Docker, a Notebook can maintain consistent runtime behavior across different nodes and platforms. This makes it easier to reproduce experimental results, share the analysis process, and better align with the production environment. It is especially suitable for scenarios such as data analysis, machine learning, and model validation.

This article briefly explains how to enable, verify, and use the Docker feature in a Notebook instance, and also lists some advanced Docker features and common troubleshooting cases.

## Enable Docker

### Prerequisites

Refer to [Managing Helm Applications](../../../kpanda/user-guide/helm/helm-app.md) to install the required plugins.

### Enable the Docker Feature

1. Log in to the **AI Lab** platform, enter the Notebook interface, and click the **Create** button.

    !!! tip "Update an Existing Instance"

        To enable Docker in an existing instance, first click the **┇** button on the right of the instance, and then choose **Update**.

2. Fill in the basic information on the Notebook creation page, and then click **Next**.

3. Complete the resource configuration, and then click **Next**.

4. In the advanced configuration, select the **Enable Docker** option, and then click **OK**.

5. After the Notebook is created, return to the Notebook list page.

    <!-- ![baize-agent](../../images/notebook-with-dind2.png) -->

6. When the Notebook instance status changes from **Pending** to **Running**, it means the instance has started successfully. If it stays in **Pending**, refresh the page.

7. At this point, the icon in the **Open** column on the right of the instance is black and clickable. Click this icon to enter the corresponding Notebook instance.

### Verify Whether the Docker Feature Is Available

In the terminal environment of the Notebook, you can verify whether the Docker environment has been enabled successfully by running the following commands.

```bash
# View the running containers
docker ps

# View all containers (including stopped ones)
docker ps -a

# View the details of a specified container (replace <container_name> with the actual container name or ID)
docker inspect <container_name>
```

If the commands run normally and return Docker container list information (even if the list is empty), it means the Docker service has started properly.

If you are prompted that the Docker command does not exist or that the Docker daemon cannot be connected, confirm that [Docker has been correctly enabled](#enable-docker).

## Basic Container Management

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

The commonly used parameters are described as follows:

| Parameter | Description |
|------|------|
| `-d` | Run the container in the background |
| `-it` | Run interactively, allocating a pseudo-terminal |
| `--name` | Specify the container name |
| `-p` | Port mapping, in the format of host port:container port |
| `-v` | Mount a data volume |

### Manage Containers

View the container status:

```bash
# View the running containers
docker ps

# View all containers (including stopped ones)
docker ps -a

# View the container details
docker inspect <container_name>
```

Start and stop a container:

```bash
# Start a stopped container
docker start <container_name>

# Stop a running container
docker stop <container_name>

# Restart a container
docker restart <container_name>
```

### Access a Container

Enter a running container:

```bash
# Enter the interactive terminal of a container
docker exec -it <container_name> /bin/bash

# View all files in a container
docker exec <container_name> ls -la /app
```

!!! tip

    It is recommended to use `docker exec` instead of `docker attach` to enter a container, because `exec` creates a new process and exiting it does not affect the running status of the container.

## Mount Storage

A Notebook can mount a PVC or use a data space to achieve persistent data storage. Its mount path can be associated with Docker, thereby enabling data sharing between containers and persistent data storage.

```bash
# Mount to a specified directory
docker run -d -v /root/data:/workspace/data --name dev-env python:3.9
```

## Create Images

The Docker feature supports creating and saving custom images in various ways to meet the needs of different scenarios.

### docker build

Building an image with a Dockerfile is the most commonly used method:

```bash
# Basic build command
docker build -t my-app:latest .

# Specify the Dockerfile path
docker build -f /path/to/Dockerfile -t my-app:v1.0 .
```

### docker save

Export an image as a tar file:

```bash
# Export a single image
docker save -o my-image.tar my-app:latest
```

The exported image can be imported with the `docker load` command:

```bash
# Import an image
docker load -i my-image.tar
```

## Use GPU

After the Docker feature is enabled in a Notebook, you can mount GPU resources into a container to provide hardware acceleration for AI training and inference.

### Mount the GPU First

Use the `--gpus` parameter to mount a GPU into a container:

```bash
# Mount all GPUs
docker run --gpus all -it pytorch/pytorch:latest python

# Mount a specified number of GPUs
docker run --gpus 2 -it tensorflow/tensorflow:latest-gpu python

# Mount a specified GPU
docker run --gpus device=0 -it nvidia/cuda:11.8-devel-ubuntu20.04
```

### Which GPUs Are Supported

Notebook supports a variety of GPUs. For details, see [GPU Support Matrix](../../../kpanda/user-guide/gpu/gpu_matrix.md).

## Network Configuration

Docker containers can communicate with the host and external networks through various network modes.

### Port Mapping

Map a container port to a host port to enable external access:

```bash
# Map a single port
docker run -d -p 8080:80 --name web-app nginx:latest

# Map multiple ports
docker run -d \  -p 8080:80 \  -p 8443:443 \  --name web-server nginx:latest

# Map to a specified IP
docker run -d -p 127.0.0.1:8080:80 --name local-app nginx:latest

# Map a random port
docker run -d -P --name random-port nginx:latest
```

## Advanced Features

The Docker feature of Notebook supports advanced tools such as buildx and Compose to meet the containerized development needs in complex scenarios.

### Docker buildx

Docker buildx is an extended build feature of Docker that supports multi-platform builds and advanced build features.

#### Basic Usage

```bash
# View the buildx version
docker buildx version

# View the available builders
docker buildx ls

# Create a new builder
docker buildx create --name mybuilder --use

# Start the builder
docker buildx inspect --bootstrap
```

#### Multi-platform Build

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

# Start the services
docker compose up -d

# View the service status
docker compose ps

# Stop the services
docker compose down

# View the logs
docker compose logs
```

## Access the Image Registry

The Docker feature of Notebook supports accessing the image registry and other public and private image registries.

### Image Registry

This platform provides a built-in [image registry](../../../kangaroo/intro/index.md) service, where users can store and manage custom images.

#### Access the Registry

```bash
# View the registry address (example)
# For the actual address, refer to the repository information in **_My Images_** provided by the platform
REGISTRY_URL="harbor.io"

# Pull an image
docker pull ${REGISTRY_URL}/my-namespace/my-app:latest

# Push an image
docker push ${REGISTRY_URL}/my-namespace/my-app:latest
```

#### Authentication Configuration

!!! note

    The current version does not support automatically injecting the username and password. You need to configure the authentication information manually.

Configure authentication manually:

```bash
# Log in to the AI Lab image registry
docker login registry.io -u <your-username>

# Enter the password
Password: <your-password>

# Verify the login status
docker info | grep -A 5 "Registry Mirrors"
```

## Troubleshooting

Common issues and solutions:

- **Container fails to start**

    ```bash
    # View the container logs
    docker logs <container_name>

    # View the container details
    docker inspect <container_name>
    ```

- **Port access issues**

    ```bash
    # Check the port mapping
    docker port <container_name>

    # Check the firewall settings
    netstat -tlnp | grep :8080
    ```

- **GPU is unavailable**

    ```bash
    # Check the GPU status
    nvidia-smi

    # Verify GPU access inside the container
    docker exec <container_name> nvidia-smi
    ```

!!! warning "Important Notes"

    - When the Notebook is shut down, running Docker containers will be stopped.
    - After the Notebook is restarted, you need to manually restart the Docker containers.
    - Deleting the Notebook will also delete all Docker containers and any data that has not been persisted.

!!! tip "Best Practices"

    - Use Docker Compose to manage complex multi-container applications.
    - [Regularly clean up unused images and containers to save storage space](../../../kangaroo/space/reclaim.md)
    - [Configure health checks and restart policies for containers in the production environment](../../../kpanda/user-guide/workloads/pod-config/health-check.md)
    - [Use standardized image naming and version management specifications](https://docs.docker.com/reference/cli/docker/image/tag/)

By making reasonable use of the Docker feature of Notebook, developers can build a flexible and efficient containerized development and deployment environment,
fully utilizing the computing resources and storage capabilities of the AI Lab platform.
