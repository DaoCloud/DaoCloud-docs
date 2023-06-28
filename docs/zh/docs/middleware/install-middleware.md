---
hide:
  - toc
---

# 安装/升级数据服务

`数据服务`提供的各中间件需分别安装，您可以采用在线和离线两种安装方式，具体操作如下。

    !!! note

        中间件安装与升级的命令及操作方式相同。

1. 确保 `helm` 库已添加，如未添加，可执行以下操作：

    ```sh
    helm repo add mcamel-release https://release.daocloud.io/chartrepo/mcamel
    helm repo update mcamel-release
    ```

    !!! note

        以上操作仅用于在线操作，如果采用离线安装方式，可跳至第二步。

2. 从左侧导航栏点击`容器管理`，进入`集群列表`，点击准备安装服务网格的集群名称。

    ![集群列表](images/login01.jpg)

3. 在`集群概览`页面中点击`控制台`。

    ![控制台](images/login02.jpg)

4. 根据所安装的中间件，在控制台中逐行输入如下命令（请修改对应的 VERSION 版本号）：

#### 安装 MySQL

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-mysql mcamel-release/mcamel-mysql --version 0.6.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-mysql mcamel-release/mcamel-mysql --version 0.6.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail \
    --set mysql_five_image.registry=${localRegistry}   \
    --set phpmyadmin_image.registry=${localRegistry}  \
    --set mysql_eight_image.registry=${localRegistry}  \
    --set curl_image.registry=${localRegistry}
    ```

#### 安装 Redis

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-redis mcamel-release/mcamel-redis --version 0.7.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-redis mcamel-release/mcamel-redis --version 0.7.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail \
    --set redisCluster_image.registry=${localRegistry}    \
    --set exporter_image.registry=${localRegistry}
    ```

#### 安装 PostgreSQL

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-postgresql --create-namespace -n mcamel-system mcamel-	release/mcamel-postgresql --cleanup-on-fai
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-postgresql --create-namespace -n mcamel-system mcamel-	release/mcamel-postgresql --cleanup-on-fail \
    --set global.imageRegistry=release-ci.daocloud.io  \
    --set exporter_image.registry=${localRegistry}  \
    --set pgadmin_image.registry=${localRegistry}  \
    --set busybox_image.registry=${localRegistry}  \
    --set exporter_image.registry=${localRegistry}  \
    --set postgresql_image.registry=${localRegistry}  \
    --version 0.0.2-128-gb88dc45
    ```

#### 安装 RabbitMQ

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-rabbitmq mcamel-release/mcamel-rabbitmq --version 0.10.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-rabbitmq mcamel-release/mcamel-rabbitmq --version 0.10.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail \
    --set rabbitmq_image.registry=${localRegistry}
    ```

#### 安装 kafka

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-kafka mcamel-release/mcamel-kafka --version 0.5.0
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-kafka mcamel-release/mcamel-kafka --version 0.5.0 \
    --set zookeeper_image.registry=${localRegistry}    \
    --set manager_image.registry=${localRegistry}    \
    --set zooEntrance_image.registry=${localRegistry}  \
    --set curl_image.registry=${localRegistry}
    ```

#### 安装 Elasticsearch

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-elasticsearch mcamel-release/mcamel-elasticsearch --version 0.7.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-elasticsearch mcamel-release/mcamel-elasticsearch --version 0.7.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail \
    --set elasticsearch_image.registry=${localRegistry} \
    --set exporter_image.registry=${localRegistry} \
    --set kibana_image.registry=${localRegistry}
    ```

#### 安装 MinIO

=== "在线安装"

    ```sh
    helm upgrade --install mcamel-minio mcamel-release/mcamel-minio --version 0.5.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail
    ```

=== "离线安装"

    ```sh
    export localRegistry="xxx.xxx.xxx.xxx" # 本地仓库地址
    helm upgrade --install mcamel-minio mcamel-release/mcamel-minio --version 0.5.0 \
    --create-namespace -n mcamel-system --cleanup-on-fail \
    --set minio_image.registry=${localRegistry}
    ```

