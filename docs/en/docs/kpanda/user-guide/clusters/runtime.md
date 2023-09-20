# How to choose the container runtime

The container runtime is an important component in kubernetes to manage the life cycle of containers and container images. Kubernetes made containerd the default container runtime in version 1.19, and removed support for the Dockershim component in version 1.24.

Therefore, compared to the Docker runtime, we **recommend you to use the lightweight containerd as your container runtime**, because this has become the current mainstream runtime choice.

In addition, some operating system distribution vendors are not friendly enough for Docker runtime compatibility. The runtime support of different operating systems is as follows:

## Operating systems and supported runtimes

| Operating System | Supported containerd Versions | Supported Docker Versions |
|--------------|---------------|------------|
| CentOS | 1.5.5, 1.5.7, 1.5.8, 1.5.9, 1.5.10, 1.5.11, 1.5.12, 1.5.13, 1.6.0, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15 (default) | 18.09, 19.03, 20.10 (default) |
| RedHatOS | 1.5.5, 1.5.7, 1.5.8, 1.5.9, 1.5.10, 1.5.11, 1.5.12, 1.5.13, 1.6.0, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15 (default) | 18.09, 19.03, 20.10 (default) |
| KylinOS | 1.5.5, 1.5.7, 1.5.8, 1.5.9, 1.5.10, 1.5.11, 1.5.12, 1.5.13, 1.6.0, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15 (default) | 19.03 (Only supported by ARM architecture, Docker is not supported as a runtime under x86 architecture)|

!!! note

    In the offline installation mode, you need to prepare the runtime offline package of the relevant operating system in advance.
