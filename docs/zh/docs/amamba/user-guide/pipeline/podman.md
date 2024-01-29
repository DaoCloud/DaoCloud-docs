## 通过流水线构建多架构镜像

在jenkins中，我们采用Podman来代替Docker作为构建镜像的工具，主要是因为Podman不需要挂载docker.sock，同时Podman支持rootless模式，可以在不需要root权限的情况下使用,安全性更高。

在JenkinsFile中，可以直接使用Docker命令或者Podman命令，他们大部分情况下是相同的。目前我们已经使用Podman代替了Docker（alias docker=podman），执行Docker命令时，实际上是调用Podman来执行的。

### 构建镜像

### 前提

与docker类似，docker支持多平台构建的前提是需要宿主机就支持多平台构建，利用QEMU来模拟其他平台的环境，因此如果需要构建多平台镜像，则jenkins所在的主机需要安装QEMU。

如果jenkins所在的主机是macos或者windows，则需要先启动虚拟机才可以使用podman:

```shell
podman machine init
podman machine start
```

## 构建多平台镜像

Podman兼容Dockerfile的语法，但是实际上并不支持Dockerfile中的--platform参数(不支持交叉编译)，采用的依旧是QEMU模拟其他平台的环境（仿真），因此构建速度也会比Docker慢。

podman 不支持直接通过 `--platform` 一次性打出多个平台的镜像, 需要打出多个平台的镜像后使用podman的`manifest`命令进行合并，不过支持在build命令中添加manifest参数便捷的添加镜像到manifest中，步骤如下：

以构建Dao-2048镜像为例，Dockerfile如下：
```dockerfile
FROM nginx # 如果需要构建多平台镜像，需要保证基础镜像支持多平台

COPY . /usr/share/nginx/html

EXPOSE 80

CMD sed -i "s/ContainerID: /ContainerID: "$(hostname)"/g" /usr/share/nginx/html/index.html && nginx -g "daemon off;"
```

##### 在构建镜像时指定manifest参数

步骤如下
```shell
> target=release.daocloud.io/demo/dao-2048:v1  # 最终镜像的名称
> platform=linux/amd64,linux/arm64 # 需要构建的平台
> docker build -f Dockerfile --platform=$platform  --manifest release.daocloud.io/demo/dao-2048:v1 . # 构建多架构镜像
> docker login xxx # 登录镜像仓库
> docker manifest push --all $target # 推送
```

最终构建出的镜像如下，包含了amd64和arm64两个平台的镜像:
![](../../images/podman-build-mutil-arch.png)

当然，如果直接在JenkinsFile中使用docker命令，不支持manifest参数，可以通过单独构建镜像的方式来实现,最终效果也是相同的，步骤如下：

1. 打出不同平台的镜像
```shell
docker build -t release.daocloud.io/demo/dao-2048-amd -f Dockerfile . --platform=linux/amd64

docker build -t release.daocloud.io/demo/dao-2048-arm -f Dockerfile . --platform=linux/arm64
```

2. 使用podman manifest create创建manifest镜像
```shell
docker manifest create release.daocloud.io/demo/dao-2048:v1
```

3. 使用podman manifest add将不同平台的镜像添加到manifest镜像中
```shell
docker manifest add release.daocloud.io/demo/dao-2048:v1 release.daocloud.io/demo/dao-2048-amd

docker manifest add release.daocloud.io/demo/dao-2048:v1 release.daocloud.io/demo/dao-2048-arm
```

4. 使用podman manifest push将manifest镜像推送到镜像仓库
```shell
podman manifest push --all release.daocloud.io/demo/dao-2048:v1 
```

### JenkinsFile示例
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
          sh '''pwd
ls -a

target=release.daocloud.io/demo/dao-2048:v1
platform=linux/amd64,linux/arm64
docker build -f Dockerfile --platform=$platform  --manifest release.daocloud.io/demo/dao-2048:v1 .
docker manifest push --all $target'''
        }

      }
    }

  }
}
```