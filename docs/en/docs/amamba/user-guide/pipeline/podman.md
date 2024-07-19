---
MTPE: windsonsea
Date: 2024-07-16
---

# Build Multi-Architecture Images through Jenkins Pipeline

In Jenkins, Podman is used as the tool for building images instead of Docker, primarily because Podman does not require mounting docker.sock and supports rootless mode, allowing it to run without root privileges, thus enhancing security.

In Jenkinsfile, you can directly use Docker or Podman commands; in most cases, they are the same. Currently, Podman has replaced Docker (alias docker=podman), so executing Docker commands will actually invoke Podman.

## Prerequisites

Similar to Docker, Docker supports multi-platform builds, provided the host machine supports multi-platform builds using QEMU to emulate other platform environments. Before building multi-architecture images, you need to configure the following:

### Configure binfmt_misc Module

Configure the `binfmt_misc` module (**mandatory**). `binfmt_misc` is a module in the Linux kernel that allows the kernel to recognize and execute binary files of a specified format. Since the `binfmt_misc` module requires high privileges, **root permissions** are needed to operate it. Therefore, you must **manually execute the following commands on all host machines running the Agent**:

```shell
find /proc/sys/fs/binfmt_misc -type f -name 'qemu-*' -exec sh -c 'echo -1 > {}'
wget -O qemu-binfmt-conf.sh https://raw.githubusercontent.com/qemu/qemu/master/scripts/qemu-binfmt-conf.sh && chmod +x qemu-binfmt-conf.sh && ./qemu-binfmt-conf.sh --qemu-suffix "-static" --qemu-path "/usr/bin"
```

### Install QEMU Binary Files

The base images provided in the workbench (`base`, `go`, `nodejs`, `python`, `maven`) already include QEMU binaries, so no additional steps are needed.

If your Agent image is not one of the aforementioned base images, you can add QEMU binaries in one of the following ways:

1. Add QEMU installation commands in the Dockerfile

    ```dockerfile
    # Add the following commands to the Dockerfile; choose the appropriate QEMU binary based on your target platform, e.g., for an arm64 target image
    FROM --platform=linux/amd64 multiarch/qemu-user-static:aarch64 as qemu
    COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
    ```

2. Directly add QEMU binaries to your Agent image using the following script

    ```shell
    arch="aarch64"
    version="v7.2.0-1"
    wget -O qemu-${arch}-static https://github.com/multiarch/qemu-user-static/releases/download/${version}/qemu-${arch}-static && chmod +x qemu-${arch}-static && mv qemu-${arch}-static /usr/bin 
    ```

For more information on QEMU and binfmt_misc, refer to:

- [Kernel Support for miscellaneous Binary Formats (binfmt_misc)](https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html)
- [QEMU User Emulation](https://wiki.debian.org/QemuUserEmulation)

## Build Multi-Platform Images

Podman is compatible with Dockerfile syntax but does not support the `--platform` parameter in Dockerfile (i.e., it does not support cross-compilation). Instead, it uses QEMU to emulate other platform environments, which means the build process will be slower than Docker.

Podman does not support directly building images for multiple platforms in one go using `--platform`. Instead, you need to build images for multiple platforms separately and then use Podman’s `manifest` command to merge them. However, Podman supports adding images to a manifest conveniently by using the manifest parameter in the build command.

Using Dao-2048 image as an example, the Dockerfile is as follows:

```dockerfile
FROM nginx # Ensure the base image supports multiple platforms if building multi-platform images
COPY . /usr/share/nginx/html
EXPOSE 80
CMD sed -i "s/ContainerID: /ContainerID: "$(hostname)"/g" /usr/share/nginx/html/index.html && nginx -g "daemon off;"
```

### Specify Manifest Parameter When Building Image

Run the following commands in sequence:

```shell
target=release.daocloud.io/demo/dao-2048:v1  # (1)!
platform=linux/amd64,linux/arm64 # (2)!
docker build -f Dockerfile --platform=$platform --manifest release.daocloud.io/demo/dao-2048:v1 . # (3)!
docker login xxx # (4)!
docker manifest push --all $target # (5)!
```

1. The final image name
2. Platforms to be built
3. Build multi-architecture image
4. Log in to the container registry
5. Push the image

The final built image will contain images for both amd64 and arm64 platforms:

![Dual-Platform Image](../../images/podman-build-mutil-arch.png)

Of course, if you directly use Docker commands in Jenkinsfile, which do not support the manifest parameter, you can achieve the same result by building images separately. The steps are as follows:

1. Build images for different platforms

    ```shell
    docker build -t release.daocloud.io/demo/dao-2048-amd -f Dockerfile . --platform=linux/amd64
    docker build -t release.daocloud.io/demo/dao-2048-arm -f Dockerfile . --platform=linux/arm64
    ```

2. Use podman manifest create to create a manifest image

    ```shell
    docker manifest create release.daocloud.io/demo/dao-2048:v1
    ```

3. Use podman manifest add to add images for different platforms to the manifest image

    ```shell
    docker manifest add release.daocloud.io/demo/dao-2048:v1 release.daocloud.io/demo/dao-2048-amd
    docker manifest add release.daocloud.io/demo/dao-2048:v1 release.daocloud.io/demo/dao-2048-arm
    ```

4. Use podman manifest push to push the manifest image to the container registry

    ```shell
    podman manifest push --all release.daocloud.io/demo/dao-2048:v1
    ```

## Jenkinsfile Example

```groovy
pipeline {
  agent {
    node {
      label 'base'
    }
  }
  stages {
    stage('clone') {
      agent none
      steps {
        container('base') {
          git(branch: 'master', credentialsId: 'zxw-gitlab', url: 'https://gitlab.daocloud.cn/ndx/dao-2048.git')
        }
      }
    }
    stage('build & push') {
      agent none
      steps {
        container('base') {
          sh '''
          pwd
          ls -a

          target=release.daocloud.io/demo/dao-2048:v1
          platform=linux/amd64,linux/arm64
          docker build -f Dockerfile --platform=$platform --manifest release.daocloud.io/demo/dao-2048:v1 .
          docker manifest push --all $target
          '''
        }
      }
    }
  }
}
```
