# 容器实例 Docker 功能

容器实例的 Docker 功能为开发者提供了在算力云环境中进行容器化开发的强大能力。
通过启用 Docker 功能，用户可以在容器实例内部创建、管理和运行 Docker 容器，
实现更灵活的开发环境配置和应用部署。

Docker 功能支持完整的容器生命周期管理，包括镜像拉取、容器创建、启动停止等基本操作，
同时提供存储挂载、GPU 加速、网络配置等高级功能。开发者可以利用这些功能构建复杂的
容器化应用，进行 AI 模型训练、算法开发和服务部署等工作。

此外，Docker 功能还支持镜像制作和管理，用户可以通过 docker build、save 等方式
创建和保存自定义镜像，并支持 Docker buildx 和 Compose 等高级工具，满足复杂场景下的
容器化开发需求。

## 启用 Docker 功能

在创建容器实例时启用 Docker 功能：

1. 登录 d.run 平台，进入 **算力云** -> **容器实例** ，点击 **创建** 按钮。
2. 在创建页面中找到 **高级配置** 选项，展开高级配置面板。
3. 在高级配置中勾选 **启用 Docker** 选项。
4. 完成其他配置后，点击 **确定** 创建实例。

!!! tip

    启用 Docker 功能的容器实例创建后，Docker 服务会自动启动，无需手动配置。

## 容器的基本操作

Docker 功能提供完整的容器生命周期管理能力，支持容器的创建、启动、停止、删除等基本操作。

### 创建和运行容器

使用 `docker run` 命令创建并启动容器：

```bash
# 基本语法
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# 运行一个简单的 Ubuntu 容器
docker run -it ubuntu:20.04 /bin/bash

# 后台运行容器
docker run -d --name my-app nginx:latest

# 指定端口映射
docker run -d -p 8080:80 --name web-server nginx:latest
```

| 参数 | 说明 |
|---|---|
| `-d` | 后台运行容器 |
| `-it` | 交互式运行，分配伪终端 |
| `--name` | 指定容器名称 |
| `-p` | 端口映射，格式为 `宿主机端口:容器端口` |
| `-v` | 挂载数据卷 |

### 管理容器

查看容器状态：

```bash
# 查看正在运行的容器
docker ps

# 查看所有容器（包括已停止的）
docker ps -a

# 查看容器详细信息
docker inspect container_name
```

启动和停止容器：

```bash
# 启动已停止的容器
docker start container_name

# 停止运行中的容器
docker stop container_name

# 重启容器
docker restart container_name
```

### 进入容器

进入正在运行的容器：

```bash
# 进入容器的交互式终端
docker exec -it container_name /bin/bash

# 执行单个命令
docker exec container_name ls -la /app
```

!!! tip

    建议使用 `docker exec` 而不是 `docker attach` 来进入容器，因为 `exec` 会创建新的进程，
    退出时不会影响容器的运行状态。

## 挂载存储

容器实例支持将文件存储和数据盘挂载到 Docker 容器中，实现数据的持久化和共享。

### 挂载文件存储

文件存储默认挂载在容器实例的 `/root/data` 目录下，可以将此目录挂载到 Docker 容器中：

```bash
# 挂载文件存储到容器
docker run -d -v /root/data:/data --name my-app ubuntu:20.04

# 挂载到指定目录
docker run -d -v /root/data:/workspace/data --name dev-env python:3.9

# 只读挂载
docker run -d -v /root/data:/data:ro --name readonly-app ubuntu:20.04
```

文件存储特点：

- 支持多个容器实例间共享数据
- 数据持久化，容器删除后数据仍然保留
- 免费提供 20GB 空间，支持弹性扩容

### 挂载数据盘

数据盘与容器实例生命周期绑定，提供高性能的本地存储：

```bash
# 挂载数据盘（假设数据盘挂载在 /mnt/disk）
docker run -d -v /mnt/disk:/app/data --name high-perf-app ubuntu:20.04

# 同时挂载文件存储和数据盘
docker run -d \
  -v /root/data:/shared \
  -v /mnt/disk:/local \
  --name multi-storage ubuntu:20.04
```

数据盘特点：

- 免费提供 50GB 空间，支持扩容至 200GB
- 高性能本地存储，适合临时数据和缓存
- 与容器实例生命周期绑定，实例删除时数据会丢失
- 不支持实例间数据共享

## 使用 GPU

容器实例的 Docker 功能支持将 GPU 资源挂载到容器中，为 AI 训练和推理提供硬件加速能力。

### 挂载 GPU

使用 `--gpus` 参数将 GPU 设备挂载到容器：

```bash
# 挂载所有 GPU
docker run --gpus all -it pytorch/pytorch:latest python

# 挂载指定数量的 GPU
docker run --gpus 2 -it tensorflow/tensorflow:latest-gpu python

# 挂载指定的 GPU
docker run --gpus device=0 -it nvidia/cuda:11.8-devel-ubuntu20.04
```

### 支持的 GPU

d.run 算力云支持多种 GPU 供应商：

- **Nvidia GPU** ：支持 CUDA 加速，兼容主流深度学习框架
- **沐曦 GPU** ：国产 GPU 解决方案，支持 AI 计算加速

## 网络配置

Docker 容器可以通过多种网络模式与宿主机和外部网络进行通信。

将容器端口映射到宿主机端口，实现外部访问：

```bash
# 映射单个端口
docker run -d -p 8080:80 --name web-app nginx:latest

# 映射多个端口
docker run -d \
  -p 8080:80 \
  -p 8443:443 \
  --name web-server nginx:latest

# 映射到指定 IP
docker run -d -p 127.0.0.1:8080:80 --name local-app nginx:latest

# 映射随机端口
docker run -d -P --name random-port nginx:latest
```

## 制作镜像

Docker 功能支持多种方式制作和保存自定义镜像，满足不同场景的需求。

### docker build

使用 Dockerfile 构建镜像是最常用的方式：

```bash
# 基本构建命令
docker build -t my-app:latest .

# 指定 Dockerfile 路径
docker build -f /path/to/Dockerfile -t my-app:v1.0 .
```

### docker save

将镜像导出为 tar 文件：

```bash
# 导出单个镜像
docker save -o my-image.tar my-app:latest
```

导出的镜像可以通过 `docker load` 命令导入：

```bash
# 导入镜像
docker load -i my-image.tar
```

## 高级功能

容器实例的 Docker 功能支持 buildx 和 Compose 等高级工具，满足复杂场景下的容器化开发需求。

### Docker buildx

Docker buildx 是 Docker 的扩展构建功能，支持多平台构建和高级构建特性。

#### 基本用法

```bash
# 查看 buildx 版本
docker buildx version

# 查看可用的构建器
docker buildx ls

# 创建新的构建器
docker buildx create --name mybuilder --use

# 启动构建器
docker buildx inspect --bootstrap
```

#### 多平台构建

```bash
# 构建多平台镜像
docker buildx build --platform linux/amd64,linux/arm64 -t my-app:latest .

# 构建并推送到仓库
docker buildx build --platform linux/amd64,linux/arm64 -t my-app:latest --push .

# 构建特定平台
docker buildx build --platform linux/amd64 -t my-app:amd64 .
```

### Docker Compose

Docker Compose 用于定义和运行多容器应用程序。

#### 安装和基本用法

```bash
# 检查 Compose 版本
docker compose version

# 启动服务
docker compose up -d

# 查看服务状态
docker compose ps

# 停止服务
docker compose down

# 查看日志
docker compose logs
```

## 访问镜像仓库

容器实例的 Docker 功能支持访问算力云镜像仓库以及其他公有和私有镜像仓库。

### 算力云镜像仓库

算力云提供内置的镜像仓库服务，用户可以存储和管理自定义镜像。

#### 访问仓库

以下是查看仓库地址的一个示例。
实际地址请参考平台提供的 **我的镜像** 中仓库信息。

```bash
REGISTRY_URL="harbor.d.run"

# 拉取镜像
docker pull ${REGISTRY_URL}/my-namespace/my-app:latest

# 推送镜像
docker push ${REGISTRY_URL}/my-namespace/my-app:latest
```

#### 认证配置

!!! note

    当前版本暂不支持自动注入用户名和密码，需要手动配置认证信息。

手动配置认证：

```bash
# 登录到算力云镜像仓库
docker login registry.d.run -u your-username

# 输入密码
Password: your-password

# 验证登录状态
docker info | grep -A 5 "Registry Mirrors"
```

## 故障排查

常见问题及解决方法：

- **容器启动失败**

    ```bash
    # 查看容器日志
    docker logs container_name
    
    # 查看容器详细信息
    docker inspect container_name
    ```

- **端口访问问题**

    ```bash
    # 检查端口映射
    docker port container_name
    
    # 检查防火墙设置
    netstat -tlnp | grep :8080
    ```

- **存储挂载问题**

    ```bash
    # 检查挂载点
    docker inspect container_name | grep -A 10 "Mounts"
    
    # 验证宿主机路径权限
    ls -la /root/data
    ```

- **GPU 不可用**

    ```bash
    # 检查 GPU 状态
    nvidia-smi
    
    # 验证容器内 GPU 访问
    docker exec container_name nvidia-smi
    ```

!!! warning "重要提醒"

    - 容器实例关机时，运行中的 Docker 容器会被停止
    - 重启容器实例后，需要手动重启 Docker 容器
    - 删除容器实例会同时删除所有 Docker 容器和未持久化的数据

!!! tip "最佳实践"

    - 使用 Docker Compose 管理复杂的多容器应用
    - 定期清理未使用的镜像和容器以节省存储空间
    - 为生产环境的容器配置健康检查和重启策略
    - 使用标准化的镜像命名和版本管理规范

通过合理使用容器实例的 Docker 功能，开发者可以构建灵活、高效的容器化开发和部署环境，
充分利用算力云平台的计算资源和存储能力。
