# Harbor 迁移指南

本文档将指导您将原始 Harbor 环境迁移至新的集群环境。此迁移案例模拟了一个复杂场景，原始 Harbor 使用 Localpath 存储，
新的环境使用 minio 对象存储，其中涉及到了 Harbor、PostgreSQL 和 Minio 的迁移过程。

## 环境准备

1. 原始 Harbor 环境：使用 Localpath 作为存储方式的 Harbor 容器环境。
2. 新集群环境：包含新的 PostgreSQL 和 Minio 存储环境。
3. 合理规划存储等资源
4. 待迁移 Harbor ：在迁移过程中，**将原始 Harbor 设置为只读模式**，确保数据的一致性和完整性。

## 步骤 1：迁移 PostgreSQL

在这一步骤中，我们将迁移原始 Harbor 所使用的 PostgreSQL 数据库至新的集群环境。

工具安装参见：[PostgreSQL 官网](https://www.postgresql.org/download/)

1. 使用 pg_dump 工具备份 Harbor 的 PostgreSQL 数据库：

    ```sh
    pg_dump --username=<原始数据库用户名> --host=<原始数据库主机> --port=<原始数据库端口> --format=plain --file=harbor_backup.sql <数据库名>
    ```

    请将尖括号中的参数替换为实际的值。例如，如果原始数据库用户名为 `postgres`，原始数据库主机为 `locahost`，端口为 `32332`，数据库名为 `core`，则命令应为：

    ```sh
    pg_dump --username=postgres --host=locahost --port=32332 --format=plain --file=harbor_backup.sql core
    ```

2. 将数据库备份文件 `harbor_backup.sql` 从原始 Harbor 环境传输到新的 PostgreSQL 环境。

3. 在新的 PostgreSQL 环境中恢复数据库：

    ```sh
    psql --host=<新数据库主机> --port=<新数据库端口> --username=<新数据库用户名> --dbname=<数据库名> --file=harbor_backup.sql
    ```

    请将尖括号中的参数替换为实际的值。例如，如果新数据库主机为 `locahost`，端口为 `32209`，新数据库用户名为 `postgres`，数据库名为 `core`，则命令应为：

    ```sh
    psql --host=locahost --port=32209 --username=postgres --dbname=core --file=harbor_backup.sql
    ```

完成以上步骤后，您已经成功将 Harbor 的 PostgreSQL 数据库迁移至新的集群环境。请确保在整个迁移过程中做好备份，并在迁移前做好充分的测试，以确保数据的安全性和业务的连续性。

## 步骤 2：迁移镜像数据至 Minio

在这一步骤中，我们将迁移原始 Harbor 存储的镜像数据至 Minio 存储系统。请按照以下步骤逐步进行：

1. 在新的集群环境中下载并安装 rclone 工具。rclone 是一个强大的命令行工具，可用于在不同对象存储之间进行数据同步和复制。
   您可以从 rclone 官方网站（https://rclone.org/）获取安装说明。

2. 配置 rclone，设置连接信息以连接到 Minio 存储。打开终端或命令提示符，并执行命令 `rclone config`，这将引导您完成配置过程。
   请根据提示，输入配置名称、Minio 存储类型以及访问密钥等信息。确保您已经正确设置了连接信息，并且可以成功连接到 Minio 存储桶。

3. 查看原始 Harbor 的 registry 服务所挂载的具体目录，这个目录存储着镜像文件。

4. 使用 rclone 进行数据迁移。在终端或命令提示符中执行以下命令

    ```sh
      rclone copy <原始Harbor镜像存储目录> <rclone配置名称>:<Minio存储桶名称>/harbor/images/
    ```

5. 请将尖括号中的参数替换为实际的值。例如，如果 rclone 配置名称为`minio`，Minio 存储桶名称为`harbor- images`，
   原始 Harbor 镜像存储目录为`/data/docker/registry/`，则命令应为：

    ```
    rclone copy /data/docker/registry/ minio:harbor-images/harbor/images/
    ```

!!! note

    数据迁移过程可能需要较长时间，具体耗时取决于镜像文件的大小和网络速度。请耐心等待数据迁移完成。

## 步骤 3：创建新的 Harbor 实例

在这一步中，我们将基于新的 PostgreSQL 和 Minio 环境创建一个全新的 Harbor 实例，并确保 Harbor 在新集群环境中正常运行。

1. 在新的集群环境中，使用新的 PostgreSQL 和 Minio 连接信息创建一个全新的 Harbor 实例。
   您可以使用镜像仓库组件进行[实例创建](https://docs.daocloud.io/kangaroo/managed/harbor/)，
   需要注意的是，创建时填写账号密码需要和原始环境中的保持一致，同时需要选择新环境中的数据库实例以及 minio 存储。
2. 确保新的 Harbor 实例已成功安装并配置。
3. 在新的 Harbor 实例中验证镜像数据是否已经成功迁移至 Minio 存储。
4. 确保新的 Harbor 实例在新集群环境中正常运行，并能够访问并提供镜像服务。
5. 测试新的 Harbor 实例，验证迁移的完整性和正确性。您可以尝试上传、下载镜像，并检查日志和事件等信息，确保 Harbor 正常工作。
6. 如果一切运行正常，恭喜！您已经成功完成了 Harbor 迁移至新的集群环境，并且现在的 Harbor 实例正常运行在 Minio 存储系统上。

请注意，在进行实际的迁移和创建新的 Harbor 实例之前，请确保做好充分的备份并在测试环境中测试迁移过程，以确保数据的安全性和业务的连续性。
